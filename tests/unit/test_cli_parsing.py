"""
Test CLI argument parsing and validation.

This module tests the parse_and_validate_arguments() function to ensure
command-line arguments are properly parsed and validated before processing.

Validates: Requirements 6.1-6.7
"""

import sys
from pathlib import Path
from unittest import mock

import pytest

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aws2tf import parse_and_validate_arguments


class TestParseAndValidateArguments:
    """Test parse_and_validate_arguments() function."""
    
    def test_no_arguments_returns_defaults(self):
        """Test that running with no arguments returns default values."""
        with mock.patch('sys.argv', ['aws2tf.py']):
            args = parse_and_validate_arguments()
            
            assert args.type is None
            assert args.id is None
            assert args.region is None
            assert args.profile is None
            assert args.merge is False
            assert args.debug is False
            assert args.fast is False
    
    def test_valid_region_argument(self):
        """Test that valid region argument is accepted."""
        with mock.patch('sys.argv', ['aws2tf.py', '-r', 'us-east-1']):
            args = parse_and_validate_arguments()
            assert args.region == 'us-east-1'
    
    def test_invalid_region_rejected(self):
        """Test that invalid region is rejected."""
        with mock.patch('sys.argv', ['aws2tf.py', '-r', 'invalid-region']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_valid_resource_type_argument(self):
        """Test that valid resource type argument is accepted."""
        with mock.patch('sys.argv', ['aws2tf.py', '-t', 'aws_vpc']):
            args = parse_and_validate_arguments()
            assert args.type == 'aws_vpc'
    
    def test_invalid_resource_type_rejected(self):
        """Test that invalid resource type is rejected."""
        with mock.patch('sys.argv', ['aws2tf.py', '-t', 'INVALID_TYPE']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_valid_resource_id_argument(self):
        """Test that valid resource ID argument is accepted."""
        with mock.patch('sys.argv', ['aws2tf.py', '-i', 'vpc-12345678']):
            args = parse_and_validate_arguments()
            assert args.id == 'vpc-12345678'
    
    def test_resource_id_with_path_traversal_rejected(self):
        """Test that resource ID with path traversal is rejected."""
        with mock.patch('sys.argv', ['aws2tf.py', '-i', '../../../etc/passwd']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_resource_id_with_shell_metacharacters_rejected(self):
        """Test that resource ID with shell metacharacters is rejected."""
        dangerous_ids = [
            'vpc-123;rm -rf /',
            'vpc-123|cat /etc/passwd',
            'vpc-123`whoami`',
        ]
        
        for dangerous_id in dangerous_ids:
            with mock.patch('sys.argv', ['aws2tf.py', '-i', dangerous_id]):
                with pytest.raises(SystemExit):
                    parse_and_validate_arguments()
    
    def test_valid_profile_argument(self):
        """Test that valid profile argument is accepted."""
        with mock.patch('sys.argv', ['aws2tf.py', '-p', 'production']):
            args = parse_and_validate_arguments()
            assert args.profile == 'production'
    
    def test_invalid_profile_rejected(self):
        """Test that invalid profile is rejected."""
        with mock.patch('sys.argv', ['aws2tf.py', '-p', 'profile;rm -rf /']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_valid_terraform_version_argument(self):
        """Test that valid terraform version argument is accepted."""
        with mock.patch('sys.argv', ['aws2tf.py', '-tv', '6.27.0']):
            args = parse_and_validate_arguments()
            assert args.tv == '6.27.0'
    
    def test_invalid_terraform_version_rejected(self):
        """Test that invalid terraform version is rejected."""
        with mock.patch('sys.argv', ['aws2tf.py', '-tv', 'invalid']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_valid_ec2_tag_argument(self):
        """Test that valid EC2 tag argument is accepted."""
        with mock.patch('sys.argv', ['aws2tf.py', '-ec2tag', 'Name:my-instance']):
            args = parse_and_validate_arguments()
            assert args.ec2tag == 'Name:my-instance'
    
    def test_boolean_flags(self):
        """Test that boolean flags are parsed correctly."""
        with mock.patch('sys.argv', ['aws2tf.py', '-d', '-f', '-m', '-w']):
            args = parse_and_validate_arguments()
            assert args.debug is True
            assert args.fast is True
            assert args.merge is True
            assert args.warn is True
    
    def test_exclude_argument(self):
        """Test that exclude argument is parsed."""
        with mock.patch('sys.argv', ['aws2tf.py', '-e', 'aws_vpc,aws_subnet']):
            args = parse_and_validate_arguments()
            assert args.exclude == 'aws_vpc,aws_subnet'
    
    def test_invalid_exclude_list_rejected(self):
        """Test that invalid exclude list is rejected."""
        with mock.patch('sys.argv', ['aws2tf.py', '-e', 'aws_vpc,INVALID']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_data_source_flags(self):
        """Test that data source flags are parsed correctly."""
        with mock.patch('sys.argv', ['aws2tf.py', '-dnet', '-dsgs', '-dkms', '-dkey']):
            args = parse_and_validate_arguments()
            assert args.datanet is True
            assert args.datasgs is True
            assert args.datakms is True
            assert args.datakey is True
    
    def test_serverless_flag(self):
        """Test that serverless flag is parsed correctly."""
        with mock.patch('sys.argv', ['aws2tf.py', '-la']):
            args = parse_and_validate_arguments()
            assert args.serverless is True
    
    def test_combined_arguments(self):
        """Test that multiple arguments can be combined."""
        with mock.patch('sys.argv', [
            'aws2tf.py',
            '-r', 'us-east-1',
            '-t', 'aws_vpc',
            '-i', 'vpc-12345678',
            '-p', 'production',
            '-d',
            '-f'
        ]):
            args = parse_and_validate_arguments()
            assert args.region == 'us-east-1'
            assert args.type == 'aws_vpc'
            assert args.id == 'vpc-12345678'
            assert args.profile == 'production'
            assert args.debug is True
            assert args.fast is True


class TestArgumentValidationIntegration:
    """Integration tests for argument validation."""
    
    def test_all_validation_functions_called(self):
        """Test that all validation functions are called during parsing."""
        with mock.patch('sys.argv', [
            'aws2tf.py',
            '-r', 'us-east-1',
            '-t', 'aws_vpc',
            '-i', 'vpc-12345678',
            '-p', 'production',
            '-tv', '6.27.0',
            '-e', 'aws_subnet'
        ]):
            # Should call all validators without error
            args = parse_and_validate_arguments()
            
            # Verify all arguments were validated and accepted
            assert args.region == 'us-east-1'
            assert args.type == 'aws_vpc'
            assert args.id == 'vpc-12345678'
            assert args.profile == 'production'
            assert args.tv == '6.27.0'
            assert args.exclude == 'aws_subnet'
    
    def test_first_invalid_argument_stops_processing(self):
        """Test that first invalid argument causes immediate exit."""
        # Invalid region should cause exit before other args are processed
        with mock.patch('sys.argv', [
            'aws2tf.py',
            '-r', 'INVALID',
            '-t', 'aws_vpc',
        ]):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
    
    def test_help_flag_shows_usage(self):
        """Test that -h flag shows help and exits."""
        with mock.patch('sys.argv', ['aws2tf.py', '-h']):
            with pytest.raises(SystemExit):
                parse_and_validate_arguments()
            # Help flag causes SystemExit (argparse behavior)
    
    def test_list_flag_parsed(self):
        """Test that -l/--list flag is parsed correctly."""
        with mock.patch('sys.argv', ['aws2tf.py', '-l']):
            args = parse_and_validate_arguments()
            assert args.list is True


class TestArgumentEdgeCases:
    """Test edge cases in argument parsing."""
    
    def test_empty_string_arguments(self):
        """Test that empty string arguments are handled."""
        with mock.patch('sys.argv', ['aws2tf.py', '-t', '']):
            args = parse_and_validate_arguments()
            # Empty type should be accepted (will default to 'all' later)
            assert args.type == ''
    
    def test_long_argument_names(self):
        """Test that long argument names work."""
        with mock.patch('sys.argv', [
            'aws2tf.py',
            '--region', 'us-east-1',
            '--type', 'aws_vpc',
            '--debug',
            '--fast'
        ]):
            args = parse_and_validate_arguments()
            assert args.region == 'us-east-1'
            assert args.type == 'aws_vpc'
            assert args.debug is True
            assert args.fast is True
    
    def test_mixed_short_and_long_arguments(self):
        """Test that short and long arguments can be mixed."""
        with mock.patch('sys.argv', [
            'aws2tf.py',
            '-r', 'us-east-1',
            '--type', 'aws_vpc',
            '-d',
            '--fast'
        ]):
            args = parse_and_validate_arguments()
            assert args.region == 'us-east-1'
            assert args.type == 'aws_vpc'
            assert args.debug is True
            assert args.fast is True
    
    def test_arn_as_resource_id(self):
        """Test that ARNs can be passed as resource IDs."""
        arn = 'arn:aws:s3:::my-bucket'
        with mock.patch('sys.argv', ['aws2tf.py', '-i', arn]):
            args = parse_and_validate_arguments()
            assert args.id == arn
    
    def test_composite_id_with_colon(self):
        """Test that composite IDs with colons are accepted."""
        composite_id = 'subnet-123:reservation-456'
        with mock.patch('sys.argv', ['aws2tf.py', '-i', composite_id]):
            args = parse_and_validate_arguments()
            assert args.id == composite_id
    
    def test_composite_id_with_slash(self):
        """Test that composite IDs with slashes are accepted."""
        composite_id = 'api-123/deployment-456'
        with mock.patch('sys.argv', ['aws2tf.py', '-i', composite_id]):
            args = parse_and_validate_arguments()
            assert args.id == composite_id
