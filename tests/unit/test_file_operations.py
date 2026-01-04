"""
Test file operations for security and correctness.

This module tests all file operation functions in common.py to ensure
they properly handle path traversal prevention, file permissions,
and secure file writing.

Validates: Requirements 5.1-5.6
"""

import os
import stat
import sys
from pathlib import Path

import pytest

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

from common import (
    safe_filename,
    safe_write_file,
    safe_write_sensitive_file,
    secure_terraform_files,
    get_file_permissions_info
)


class TestSafeFilename:
    """Test safe_filename() function for path traversal prevention."""
    
    def test_simple_filename_passes(self, tmp_path):
        """Test that simple filenames pass validation."""
        simple_names = [
            'test.txt',
            'myfile.tf',
            'import.json',
            'data_file.csv',
        ]
        
        for filename in simple_names:
            result = safe_filename(filename, base_dir=str(tmp_path))
            assert Path(result).name == filename
            assert str(tmp_path) in result
    
    def test_path_traversal_sanitized(self, tmp_path):
        """Test that path traversal attempts are sanitized."""
        # safe_filename uses os.path.basename() which strips directory components
        # So '../../../etc/passwd' becomes 'passwd'
        test_cases = [
            ('../../../etc/passwd', 'passwd'),
            ('../../aws/config', 'config'),
            ('../parent/file.txt', 'file.txt'),
        ]
        
        for malicious, expected_name in test_cases:
            result = safe_filename(malicious, base_dir=str(tmp_path))
            # Should strip path components and keep only filename
            assert Path(result).name == expected_name
            # Should be within base_dir
            assert str(tmp_path) in result
    
    def test_dangerous_characters_sanitized(self, tmp_path):
        """Test that dangerous characters are sanitized."""
        dangerous_names = [
            'file;rm -rf /',
            'file|cat /etc/passwd',
            'file`whoami`',
            'file$(whoami)',
            'file with spaces',
        ]
        
        for dangerous in dangerous_names:
            result = safe_filename(dangerous, base_dir=str(tmp_path))
            # Should be sanitized (special chars replaced with _)
            assert ';' not in result
            assert '|' not in result
            assert '`' not in result
            assert '$' not in result
    
    def test_hidden_files_prevented(self, tmp_path):
        """Test that hidden files (starting with .) are prevented."""
        hidden_names = [
            '.hidden',
            '.bashrc',
            '.ssh',
        ]
        
        for hidden in hidden_names:
            result = safe_filename(hidden, base_dir=str(tmp_path))
            # Should be prefixed with _ to prevent hidden files
            assert not Path(result).name.startswith('.')
    
    def test_terraform_lock_file_allowed(self, tmp_path):
        """Test that .terraform.lock.hcl is allowed (special case)."""
        result = safe_filename('.terraform.lock.hcl', base_dir=str(tmp_path))
        assert Path(result).name == '.terraform.lock.hcl'
    
    def test_resolved_path_within_base_dir(self, tmp_path):
        """Test that resolved path stays within base directory."""
        filename = 'test.txt'
        result = safe_filename(filename, base_dir=str(tmp_path))
        
        result_path = Path(result).resolve()
        base_path = Path(tmp_path).resolve()
        
        # Verify result is within base directory
        assert str(result_path).startswith(str(base_path))
    
    def test_default_base_dir_is_cwd(self):
        """Test that default base_dir is current working directory."""
        filename = 'test.txt'
        result = safe_filename(filename)
        
        # Should use current working directory
        assert os.getcwd() in result


class TestSafeWriteFile:
    """Test safe_write_file() function."""
    
    def test_creates_file_with_correct_permissions(self, tmp_path):
        """Test that files are created with correct permissions."""
        filepath = tmp_path / "test.txt"
        content = "test content"
        
        safe_write_file(str(filepath), content, permissions=0o644)
        
        # Verify file exists
        assert filepath.exists()
        
        # Verify content
        assert filepath.read_text() == content
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(filepath)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o644
    
    def test_creates_file_with_custom_permissions(self, tmp_path):
        """Test that custom permissions are applied."""
        filepath = tmp_path / "test.txt"
        content = "test content"
        
        safe_write_file(str(filepath), content, permissions=0o600)
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(filepath)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o600
    
    def test_path_traversal_prevented(self, tmp_path):
        """Test that path traversal is prevented."""
        malicious_path = '../../../etc/passwd'
        content = "malicious content"
        
        with pytest.raises(ValueError):
            safe_write_file(malicious_path, content, base_dir=str(tmp_path))
    
    def test_subdirectory_handling(self, tmp_path):
        """Test that subdirectories are created correctly."""
        filepath = "imported/test.tf"
        content = "resource content"
        
        safe_write_file(filepath, content, base_dir=str(tmp_path))
        
        # Verify file exists in subdirectory
        full_path = tmp_path / "imported" / "test.tf"
        assert full_path.exists()
        assert full_path.read_text() == content
    
    def test_subdirectory_traversal_rejected(self, tmp_path):
        """Test that subdirectory with traversal is rejected."""
        malicious_path = "imported/../../etc/passwd"
        content = "malicious content"
        
        with pytest.raises(ValueError, match="Path traversal"):
            safe_write_file(malicious_path, content, base_dir=str(tmp_path))
    
    def test_binary_mode_works(self, tmp_path):
        """Test that binary mode works correctly."""
        filepath = tmp_path / "test.bin"
        content = b"binary content"
        
        safe_write_file(str(filepath), content, mode='wb')
        
        assert filepath.exists()
        assert filepath.read_bytes() == content
    
    def test_overwrites_existing_file(self, tmp_path):
        """Test that existing files are overwritten."""
        filepath = tmp_path / "test.txt"
        
        # Write initial content
        safe_write_file(str(filepath), "initial content")
        assert filepath.read_text() == "initial content"
        
        # Overwrite
        safe_write_file(str(filepath), "new content")
        assert filepath.read_text() == "new content"


class TestSafeWriteSensitiveFile:
    """Test safe_write_sensitive_file() function."""
    
    def test_creates_file_with_restricted_permissions(self, tmp_path):
        """Test that sensitive files get 0o600 permissions."""
        filepath = tmp_path / "sensitive.txt"
        content = "sensitive data"
        
        safe_write_sensitive_file(str(filepath), content)
        
        # Verify file exists
        assert filepath.exists()
        assert filepath.read_text() == content
        
        # Verify restricted permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(filepath)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o600
    
    def test_path_traversal_prevented(self, tmp_path):
        """Test that path traversal is prevented for sensitive files."""
        malicious_path = '../../../etc/shadow'
        content = "malicious content"
        
        with pytest.raises(ValueError):
            safe_write_sensitive_file(malicious_path, content, base_dir=str(tmp_path))


class TestSecureTerraformFiles:
    """Test secure_terraform_files() function."""
    
    def test_secures_terraform_state_files(self, tmp_path):
        """Test that terraform.tfstate gets 0o600 permissions."""
        # Create state file
        state_file = tmp_path / "terraform.tfstate"
        state_file.write_text('{"version": 4}')
        
        # Secure it
        secure_terraform_files(directory=str(tmp_path))
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(state_file)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o600
    
    def test_secures_terraform_state_backup(self, tmp_path):
        """Test that terraform.tfstate.backup gets 0o600 permissions."""
        # Create backup file
        backup_file = tmp_path / "terraform.tfstate.backup"
        backup_file.write_text('{"version": 4}')
        
        # Secure it
        secure_terraform_files(directory=str(tmp_path))
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(backup_file)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o600
    
    def test_secures_terraform_lock_file(self, tmp_path):
        """Test that .terraform.lock.hcl gets 0o644 permissions."""
        # Create lock file
        lock_file = tmp_path / ".terraform.lock.hcl"
        lock_file.write_text('# Lock file')
        
        # Secure it
        secure_terraform_files(directory=str(tmp_path))
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(lock_file)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o644
    
    def test_secures_tfvars_files(self, tmp_path):
        """Test that *.tfvars files get 0o600 permissions."""
        # Create tfvars files
        tfvars1 = tmp_path / "terraform.tfvars"
        tfvars1.write_text('variable = "value"')
        
        tfvars2 = tmp_path / "prod.tfvars"
        tfvars2.write_text('env = "prod"')
        
        # Secure them
        secure_terraform_files(directory=str(tmp_path))
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            for tfvars_file in [tfvars1, tfvars2]:
                file_stat = os.stat(tfvars_file)
                file_perms = stat.S_IMODE(file_stat.st_mode)
                assert file_perms == 0o600
    
    def test_secures_log_files(self, tmp_path):
        """Test that aws2tf.log gets 0o600 permissions."""
        # Create log file
        log_file = tmp_path / "aws2tf.log"
        log_file.write_text('Log content')
        
        # Secure it
        secure_terraform_files(directory=str(tmp_path))
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(log_file)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o600
    
    def test_handles_missing_files_gracefully(self, tmp_path):
        """Test that function handles missing files without error."""
        # Call on empty directory - should not raise error
        secure_terraform_files(directory=str(tmp_path))
        
        # No assertion needed - just verify it doesn't crash
    
    def test_handles_permission_errors_gracefully(self, tmp_path):
        """Test that permission errors are handled gracefully."""
        # Create a file
        test_file = tmp_path / "terraform.tfstate"
        test_file.write_text('{"version": 4}')
        
        # This should not raise an exception even if permissions fail
        secure_terraform_files(directory=str(tmp_path))


class TestGetFilePermissionsInfo:
    """Test get_file_permissions_info() function."""
    
    def test_returns_dict_with_file_types(self):
        """Test that function returns dictionary with file type information."""
        info = get_file_permissions_info()
        
        assert isinstance(info, dict)
        assert 'terraform_files' in info
        assert 'state_files' in info
        assert 'variable_files' in info
        assert 'log_files' in info
        assert 'import_files' in info
    
    def test_each_entry_has_required_fields(self):
        """Test that each entry has description, pattern, permissions, reason."""
        info = get_file_permissions_info()
        
        for file_type, details in info.items():
            assert 'description' in details
            assert 'pattern' in details
            assert 'permissions' in details
            assert 'reason' in details
            
            # Verify types
            assert isinstance(details['description'], str)
            assert isinstance(details['pattern'], str)
            assert isinstance(details['permissions'], int)
            assert isinstance(details['reason'], str)
    
    def test_sensitive_files_have_restricted_permissions(self):
        """Test that sensitive files have 0o600 permissions."""
        info = get_file_permissions_info()
        
        # State files should be 0o600
        assert info['state_files']['permissions'] == 0o600
        
        # Variable files should be 0o600
        assert info['variable_files']['permissions'] == 0o600
        
        # Log files should be 0o600
        assert info['log_files']['permissions'] == 0o600
    
    def test_non_sensitive_files_have_normal_permissions(self):
        """Test that non-sensitive files have 0o644 permissions."""
        info = get_file_permissions_info()
        
        # Terraform files should be 0o644
        assert info['terraform_files']['permissions'] == 0o644
        
        # Import files should be 0o644
        assert info['import_files']['permissions'] == 0o644


class TestFileOperationsIntegration:
    """Integration tests for file operations."""
    
    def test_complete_workflow(self, tmp_path):
        """Test complete workflow: write file, secure it, verify permissions."""
        # Write a terraform state file
        state_file = tmp_path / "terraform.tfstate"
        state_content = '{"version": 4, "terraform_version": "1.0.0"}'
        
        safe_write_sensitive_file(str(state_file), state_content)
        
        # Verify it was created with correct permissions
        assert state_file.exists()
        assert state_file.read_text() == state_content
        
        if os.name != 'nt':  # Skip on Windows
            file_stat = os.stat(state_file)
            file_perms = stat.S_IMODE(file_stat.st_mode)
            assert file_perms == 0o600
    
    def test_multiple_files_in_workspace(self, tmp_path):
        """Test securing multiple files in a workspace."""
        # Create various files
        files = {
            'terraform.tfstate': ('{"version": 4}', 0o600),
            'terraform.tfstate.backup': ('{"version": 3}', 0o600),
            '.terraform.lock.hcl': ('# Lock', 0o644),
            'terraform.tfvars': ('var = "val"', 0o600),
            'aws2tf.log': ('Log entry', 0o600),
            'main.tf': ('resource "aws_vpc" {}', 0o644),  # Should not be changed
        }
        
        for filename, (content, _) in files.items():
            filepath = tmp_path / filename
            filepath.write_text(content)
        
        # Secure the workspace
        secure_terraform_files(directory=str(tmp_path))
        
        # Verify permissions (on Unix systems)
        if os.name != 'nt':  # Skip on Windows
            for filename, (_, expected_perms) in files.items():
                if filename == 'main.tf':
                    continue  # main.tf is not secured by secure_terraform_files
                
                filepath = tmp_path / filename
                file_stat = os.stat(filepath)
                file_perms = stat.S_IMODE(file_stat.st_mode)
                assert file_perms == expected_perms, f"{filename} should have {oct(expected_perms)}"
    
    def test_safe_operations_prevent_directory_escape(self, tmp_path):
        """Test that all safe operations prevent directory escape."""
        base_dir = tmp_path / "workspace"
        base_dir.mkdir()
        
        # safe_filename sanitizes by stripping path components
        result = safe_filename('../../../etc/passwd', base_dir=str(base_dir))
        assert 'passwd' in result
        assert str(base_dir) in result
        
        # safe_write_file with subdirectory traversal should be rejected
        with pytest.raises(ValueError):
            safe_write_file('imported/../../etc/passwd', "content", base_dir=str(base_dir))
        
        # safe_write_sensitive_file with subdirectory traversal should be rejected
        with pytest.raises(ValueError):
            safe_write_sensitive_file('imported/../../etc/passwd', "content", base_dir=str(base_dir))
