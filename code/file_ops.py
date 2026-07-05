"""File operations and security utilities for aws2tf."""

import os
import re
import glob
import context
import logging
from pathlib import Path

log = logging.getLogger('aws2tf')


# Security Fix #3: Path traversal prevention
def safe_filename(filename: str, base_dir: str = None) -> str:
    """
    Validate and sanitize filename to prevent path traversal attacks.
    
    Args:
        filename: The filename to validate
        base_dir: Optional base directory to restrict to (defaults to current working dir)
    
    Returns:
        Sanitized filename safe for use
        
    Raises:
        ValueError: If path traversal attempt detected
    """
    if base_dir is None:
        base_dir = os.getcwd()
    
    # Convert to Path objects for safe manipulation
    base_path = Path(base_dir).resolve()
    
    # Remove any path separators and resolve the path
    # This prevents ../../../etc/passwd type attacks
    safe_name = os.path.basename(filename)
    
    # Additional sanitization - remove dangerous characters
    # Keep alphanumeric, dash, underscore, dot
    safe_name = re.sub(r'[^\w\-\.]', '_', safe_name)
    
    # Prevent hidden files (starting with .)
    if safe_name.startswith('.') and safe_name != '.terraform.lock.hcl':
        safe_name = '_' + safe_name
    
    # Construct full path
    full_path = (base_path / safe_name).resolve()
    
    # Verify the resolved path is still within base_dir
    try:
        full_path.relative_to(base_path)
    except ValueError:
        raise ValueError(f"Path traversal attempt detected: {filename}")
    
    return str(full_path)


def safe_write_file(filename: str, content: str, mode: str = 'w', base_dir: str = None, permissions: int = 0o644) -> None:
    """
    Safely write content to a file with path validation and secure permissions.
    
    Args:
        filename: The filename to write to
        content: Content to write
        mode: File mode ('w' or 'wb')
        base_dir: Optional base directory to restrict to
        permissions: Unix file permissions (default: 0o644 = rw-r--r--)
                    Use 0o600 for sensitive files (rw-------)
    
    Security Features:
    - Path traversal prevention
    - Secure file permissions
    - Atomic write operation
    """
    # For files in subdirectories like 'imported/', handle specially
    if '/' in filename:
        # Split into directory and filename
        parts = filename.split('/')
        subdir = '/'.join(parts[:-1])
        fname = parts[-1]
        
        # Validate subdirectory doesn't contain traversal
        if '..' in subdir:
            raise ValueError(f"Path traversal attempt in directory: {subdir}")
        
        # Create subdirectory if it doesn't exist
        if base_dir:
            full_subdir = os.path.join(base_dir, subdir)
        else:
            full_subdir = subdir
            
        os.makedirs(full_subdir, mode=0o755, exist_ok=True)
        
        # Validate the filename part
        safe_fname = safe_filename(fname, full_subdir)
        safe_path = safe_fname
    else:
        # Simple filename, validate it
        safe_path = safe_filename(filename, base_dir)
    
    # Write the file with specified permissions
    if 'b' in mode:
        # Binary mode
        fd = os.open(safe_path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, permissions)
        with os.fdopen(fd, mode) as f:
            f.write(content)
    else:
        # Text mode - use os.open for atomic creation with permissions
        fd = os.open(safe_path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, permissions)
        with os.fdopen(fd, mode) as f:
            f.write(content)
    
    # Verify permissions were set correctly
    actual_perms = os.stat(safe_path).st_mode & 0o777
    if actual_perms != permissions:
        # Try to fix permissions
        os.chmod(safe_path, permissions)


def safe_write_sensitive_file(filename: str, content: str, mode: str = 'w', base_dir: str = None) -> None:
    """
    Write sensitive files (state, credentials, etc.) with restricted permissions.
    
    Uses 0o600 permissions (rw-------) - only owner can read/write.
    """
    safe_write_file(filename, content, mode, base_dir, permissions=0o600)


def secure_terraform_files(directory: str = '.') -> None:
    """
    Secure terraform state files and other sensitive files with appropriate permissions.
    
    Security Fix #7: Set restrictive permissions on sensitive files
    
    Files secured:
    - terraform.tfstate (0o600) - Contains sensitive data
    - terraform.tfstate.backup (0o600) - Contains sensitive data
    - .terraform.lock.hcl (0o644) - Lock file, less sensitive
    - *.tfvars (0o600) - May contain secrets
    - aws2tf.log (0o600) - May contain sensitive information
    
    Args:
        directory: Directory to secure files in (default: current directory)
    """
    sensitive_files = {
        'terraform.tfstate': 0o600,
        'terraform.tfstate.backup': 0o600,
        '.terraform.lock.hcl': 0o644,
        'aws2tf.log': 0o600,
    }
    
    # Secure specific files
    for filename, perms in sensitive_files.items():
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            try:
                os.chmod(filepath, perms)
                if context.debug:
                    log.debug(f"Secured {filename} with permissions {oct(perms)}")
            except Exception as e:
                log.warning(f"Could not set permissions on {filename}: {e}")
    
    # Secure all .tfvars files
    for tfvars_file in glob.glob(os.path.join(directory, '*.tfvars')):
        try:
            os.chmod(tfvars_file, 0o600)
            if context.debug:
                log.debug(f"Secured {os.path.basename(tfvars_file)} with permissions 0o600")
        except Exception as e:
            log.warning(f"Could not set permissions on {tfvars_file}: {e}")


def get_file_permissions_info() -> dict:
    """
    Get information about file permissions for security documentation.
    
    Returns:
        Dictionary with file types and their recommended permissions
    """
    return {
        'terraform_files': {
            'description': 'Terraform configuration files',
            'pattern': '*.tf',
            'permissions': 0o644,
            'reason': 'Configuration files, readable by group'
        },
        'state_files': {
            'description': 'Terraform state files (SENSITIVE)',
            'pattern': 'terraform.tfstate*',
            'permissions': 0o600,
            'reason': 'Contains secrets, credentials, and sensitive resource data'
        },
        'variable_files': {
            'description': 'Terraform variable files (POTENTIALLY SENSITIVE)',
            'pattern': '*.tfvars',
            'permissions': 0o600,
            'reason': 'May contain secrets and sensitive configuration'
        },
        'log_files': {
            'description': 'Application log files (POTENTIALLY SENSITIVE)',
            'pattern': '*.log',
            'permissions': 0o600,
            'reason': 'May contain AWS resource IDs, ARNs, and debugging information'
        },
        'import_files': {
            'description': 'Terraform import files',
            'pattern': 'import__*.tf',
            'permissions': 0o644,
            'reason': 'Import declarations, less sensitive'
        },
    }
