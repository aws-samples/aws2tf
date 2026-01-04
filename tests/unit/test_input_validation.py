"""
Test input validation functions for security.

This module tests all input validation functions in aws2tf.py to ensure
they properly reject malicious inputs and prevent security vulnerabilities
like path traversal, shell injection, and format string attacks.

Validates: Requirements 2.1-2.8
"""

import pytest
import sys
from pathlib import Path

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aws2tf import (
    validate_region,
    validate_profile,
    validate_resource_type,
    validate_resource_id,
    validate_ec2_tag,
    validate_terraform_version,
    validate_exclude_list
)


class TestValidateRegion:
    """Test validate_region() function."""
    
    def test_valid_regions_pass(self):
        """Test that valid AWS regions pass validation."""
        valid_regions = [
            'us-east-1',
            'us-east-2',
            'us-west-1',
            'us-west-2',
            'eu-west-1',
            'eu-west-2',
            'eu-west-3',
            'eu-central-1',
            'ap-southeast-1',
            'ap-southeast-2',
            'ap-northeast-1',
            'ap-south-1',
            'sa-east-1',
            'ca-central-1',
        ]
        
        for region in valid_regions:
            result = validate_region(region)
            assert result == region, f"Valid region {region} should pass"
    
    def test_invalid_format_raises_error(self):
        """Test that invalid region formats raise ValueError."""
        invalid_regions = [
            'invalid',
            'us_east_1',  # Underscores instead of hyphens
            'US-EAST-1',  # Uppercase
            'us-east',    # Missing number
            'east-1',     # Missing country code
            '1-east-1',   # Starts with number
            'us-east-1a', # Extra character
            '',           # Empty string
            'us-east-123', # Too many digits
        ]
        
        for region in invalid_regions:
            with pytest.raises(ValueError, match="Invalid AWS region format"):
                validate_region(region)
    
    def test_path_traversal_rejected(self):
        """Test that path traversal attempts are rejected."""
        malicious_inputs = [
            '../../../etc/passwd',
            '../../aws/config',
            '../us-east-1',
            'us-east-1/../../../etc',
        ]
        
        for malicious in malicious_inputs:
            with pytest.raises(ValueError):
                validate_region(malicious)
    
    def test_special_characters_rejected(self):
        """Test that special characters are rejected."""
        # Note: The regex only validates format, not all dangerous chars
        # These should fail format validation
        special_chars = [
            'us-east-1;rm',  # Semicolon breaks format
            'us-east-1|cat',  # Pipe breaks format
            'us-east-1 space',  # Space breaks format
            'US-EAST-1',  # Uppercase breaks format
        ]
        
        for special in special_chars:
            with pytest.raises(ValueError):
                validate_region(special)


class TestValidateProfile:
    """Test validate_profile() function."""
    
    def test_valid_profiles_pass(self):
        """Test that valid profile names pass validation."""
        valid_profiles = [
            'default',
            'production',
            'dev',
            'test-profile',
            'my_profile',
            'profile-123',
            'UPPERCASE',
            'MixedCase',
        ]
        
        for profile in valid_profiles:
            result = validate_profile(profile)
            assert result == profile
    
    def test_invalid_characters_rejected(self):
        """Test that profiles with invalid characters are rejected."""
        invalid_profiles = [
            'profile with spaces',
            'profile/slash',
            'profile\\backslash',
            'profile;semicolon',
            'profile|pipe',
            'profile`backtick',
            'profile$dollar',
            '../../../etc/passwd',
            '',  # Empty string
        ]
        
        for profile in invalid_profiles:
            with pytest.raises(ValueError, match="Invalid AWS profile name"):
                validate_profile(profile)


class TestValidateResourceType:
    """Test validate_resource_type() function."""
    
    def test_valid_resource_types_pass(self):
        """Test that valid terraform resource types pass validation."""
        valid_types = [
            'aws_vpc',
            'aws_subnet',
            'aws_s3_bucket',
            'aws_lambda_function',
            'aws_iam_role',
            'aws_ec2_instance',
            'aws_rds_cluster',
            'aws_dynamodb_table',
        ]
        
        for resource_type in valid_types:
            result = validate_resource_type(resource_type)
            assert result == resource_type
    
    def test_comma_separated_list_passes(self):
        """Test that comma-separated resource types pass validation."""
        resource_list = 'aws_vpc,aws_subnet,aws_s3_bucket'
        result = validate_resource_type(resource_list)
        assert result == resource_list
    
    def test_invalid_format_rejected(self):
        """Test that invalid resource type formats are rejected."""
        invalid_types = [
            'AWS_VPC',  # Uppercase
            'aws-vpc',  # Hyphens instead of underscores
            '123_vpc',  # Starts with number
            'aws vpc',  # Space
            'aws_vpc;rm -rf /',  # Shell injection
            '../../../etc/passwd',  # Path traversal
            '',  # Empty string
        ]
        
        for invalid_type in invalid_types:
            with pytest.raises(ValueError, match="Invalid resource type format"):
                validate_resource_type(invalid_type)
    
    def test_special_characters_rejected(self):
        """Test that resource types with special characters are rejected."""
        # Note: The regex validates format (lowercase, underscores)
        # These break the format validation
        special_chars = [
            'aws_vpc space',  # Space breaks format
            'AWS_VPC',  # Uppercase breaks format
            'aws-vpc',  # Hyphen breaks format
            '123_vpc',  # Starts with number
        ]
        
        for special in special_chars:
            with pytest.raises(ValueError):
                validate_resource_type(special)


class TestValidateResourceId:
    """Test validate_resource_id() function."""
    
    def test_valid_resource_ids_pass(self):
        """Test that valid AWS resource IDs pass validation."""
        valid_ids = [
            'vpc-12345678',
            'subnet-abcdef12',
            'i-1234567890abcdef0',
            'sg-0123456789abcdef0',
            'arn:aws:s3:::my-bucket',
            'arn:aws:lambda:us-east-1:123456789012:function:my-function',
            'my-bucket-name',
            'function-name_123',
            'role/my-role',
            'policy.name',
        ]
        
        for resource_id in valid_ids:
            result = validate_resource_id(resource_id)
            assert result == resource_id
    
    def test_path_traversal_rejected(self):
        """Test that path traversal attempts are rejected."""
        malicious_ids = [
            '../../../etc/passwd',
            '../../aws/config',
            'vpc-123/../../../etc',
            '..\\..\\windows\\system32',
        ]
        
        for malicious in malicious_ids:
            with pytest.raises(ValueError, match="Path traversal detected"):
                validate_resource_id(malicious)
    
    def test_shell_metacharacters_rejected(self):
        """Test that shell metacharacters are rejected."""
        dangerous_ids = [
            'vpc-123;rm -rf /',
            'vpc-123|cat /etc/passwd',
            'vpc-123&whoami',
            'vpc-123`whoami`',
            'vpc-123\nrm -rf /',
            'vpc-123\rmalicious',
        ]
        
        for dangerous in dangerous_ids:
            with pytest.raises(ValueError, match="Invalid character"):
                validate_resource_id(dangerous)
    
    def test_arns_with_special_chars_pass(self):
        """Test that ARNs with allowed special characters pass."""
        valid_arns = [
            'arn:aws:iam::123456789012:role/my-role',
            'arn:aws:s3:::my-bucket/path/to/object',
            'arn:aws:lambda:us-east-1:123456789012:function:my-function',
            'arn:aws:dynamodb:us-east-1:123456789012:table/my-table',
        ]
        
        for arn in valid_arns:
            result = validate_resource_id(arn)
            assert result == arn


class TestValidateEc2Tag:
    """Test validate_ec2_tag() function."""
    
    def test_valid_tags_pass(self):
        """Test that valid EC2 tags pass validation."""
        valid_tags = [
            ('Name', 'my-instance'),
            ('Environment', 'production'),
            ('Owner', 'team@example.com'),
            ('Cost-Center', '12345'),
            ('Project', 'web-app'),
        ]
        
        for expected_key, expected_value in valid_tags:
            tag_string = f"{expected_key}:{expected_value}"
            key, value = validate_ec2_tag(tag_string)
            assert key == expected_key
            assert value == expected_value
    
    def test_invalid_format_rejected(self):
        """Test that invalid tag formats are rejected."""
        invalid_tags = [
            'NoColon',  # Missing colon
            ':NoKey',   # Empty key
            'NoValue:', # Empty value
            '',         # Empty string
        ]
        
        for invalid_tag in invalid_tags:
            with pytest.raises(ValueError, match="Invalid tag format|cannot be empty"):
                validate_ec2_tag(invalid_tag)
    
    def test_empty_key_or_value_rejected(self):
        """Test that empty keys or values are rejected."""
        invalid_tags = [
            ':value',  # Empty key
            'key:',    # Empty value
        ]
        
        for invalid_tag in invalid_tags:
            with pytest.raises(ValueError, match="cannot be empty"):
                validate_ec2_tag(invalid_tag)
    
    def test_special_characters_in_tags(self):
        """Test that allowed special characters in tags pass."""
        valid_tags = [
            'Name:my-instance_123',
            'Email:user@example.com',
            'Path:/var/log/app',
            'Version:1.2.3',
            'Description:This is a test',
        ]
        
        for tag in valid_tags:
            key, value = validate_ec2_tag(tag)
            assert key is not None
            assert value is not None


class TestValidateTerraformVersion:
    """Test validate_terraform_version() function."""
    
    def test_valid_versions_pass(self):
        """Test that valid version strings pass validation."""
        valid_versions = [
            '6.27.0',
            '5.0.0',
            '1.0.0',
            '10.20.30',
            '0.1.0',
        ]
        
        for version in valid_versions:
            result = validate_terraform_version(version)
            assert result == version
    
    def test_invalid_format_rejected(self):
        """Test that invalid version formats are rejected."""
        invalid_versions = [
            '6.27',      # Missing patch
            '6',         # Only major
            'v6.27.0',   # Has 'v' prefix
            '6.27.0.1',  # Too many parts
            'latest',    # Not a version
            '6.27.x',    # Non-numeric
            '',          # Empty
        ]
        
        for version in invalid_versions:
            with pytest.raises(ValueError, match="Invalid version format"):
                validate_terraform_version(version)


class TestValidateExcludeList:
    """Test validate_exclude_list() function."""
    
    def test_empty_string_returns_empty_list(self):
        """Test that empty string returns empty list."""
        result = validate_exclude_list('')
        assert result == []
        
        result = validate_exclude_list(None)
        assert result == []
    
    def test_single_type_returns_list(self):
        """Test that single resource type returns list with one item."""
        result = validate_exclude_list('aws_vpc')
        assert result == ['aws_vpc']
    
    def test_comma_separated_list_parsed(self):
        """Test that comma-separated list is parsed correctly."""
        result = validate_exclude_list('aws_vpc,aws_subnet,aws_s3_bucket')
        assert len(result) == 3
        assert 'aws_vpc' in result
        assert 'aws_subnet' in result
        assert 'aws_s3_bucket' in result
    
    def test_whitespace_stripped(self):
        """Test that whitespace is stripped from types."""
        result = validate_exclude_list('aws_vpc, aws_subnet , aws_s3_bucket')
        assert result == ['aws_vpc', 'aws_subnet', 'aws_s3_bucket']
    
    def test_invalid_types_rejected(self):
        """Test that invalid resource types in list are rejected."""
        invalid_lists = [
            'aws_vpc,INVALID_TYPE',
            'aws_vpc,../../../etc/passwd',
            'aws_vpc,aws_subnet;rm -rf /',
        ]
        
        for invalid_list in invalid_lists:
            with pytest.raises(ValueError):
                validate_exclude_list(invalid_list)


class TestInputValidationIntegration:
    """Integration tests for input validation."""
    
    def test_all_validators_reject_path_traversal(self):
        """Test that all validators reject path traversal attempts."""
        path_traversal = '../../../etc/passwd'
        
        with pytest.raises(ValueError):
            validate_region(path_traversal)
        
        with pytest.raises(ValueError):
            validate_profile(path_traversal)
        
        with pytest.raises(ValueError):
            validate_resource_type(path_traversal)
        
        with pytest.raises(ValueError):
            validate_resource_id(path_traversal)
    
    def test_all_validators_reject_shell_injection(self):
        """Test that all validators reject shell injection attempts."""
        shell_injection = 'valid;rm -rf /'
        
        with pytest.raises(ValueError):
            validate_region(shell_injection)
        
        with pytest.raises(ValueError):
            validate_profile(shell_injection)
        
        with pytest.raises(ValueError):
            validate_resource_type(shell_injection)
        
        with pytest.raises(ValueError):
            validate_resource_id(shell_injection)
    
    def test_validators_handle_empty_strings(self):
        """Test that validators properly handle empty strings."""
        with pytest.raises(ValueError):
            validate_region('')
        
        with pytest.raises(ValueError):
            validate_profile('')
        
        with pytest.raises(ValueError):
            validate_resource_type('')
        
        # validate_exclude_list should return empty list for empty string
        result = validate_exclude_list('')
        assert result == []
    
    def test_validators_are_consistent(self):
        """Test that validators have consistent behavior."""
        # All should reject None (if passed as string)
        # All should reject path traversal
        # All should reject shell metacharacters
        
        dangerous_inputs = [
            '../../../etc/passwd',
            'input;rm -rf /',
            'input|cat /etc/passwd',
            'input`whoami`',
        ]
        
        validators = [
            validate_region,
            validate_profile,
            validate_resource_type,
            validate_resource_id,
        ]
        
        for dangerous in dangerous_inputs:
            for validator in validators:
                with pytest.raises(ValueError):
                    validator(dangerous)
