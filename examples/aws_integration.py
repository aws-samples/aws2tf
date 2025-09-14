#!/usr/bin/env python3
"""
AWS integration examples for the Configuration Management System.
This file demonstrates AWS credential setup and session management.
"""
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from code.config import (
    ConfigurationManager,
    configure_aws_credentials,
    validate_aws_credentials,
    print_credentials_info,
    create_test_config
)


def example_aws_credential_setup():
    """Example: Set up AWS credentials and session."""
    print("=== AWS Credential Setup Example ===")
    
    config = ConfigurationManager()
    
    # Set AWS configuration
    config.aws.region = 'us-east-1'
    config.aws.profile = 'default'
    
    print(f"Configuring AWS for region: {config.aws.region}")
    print(f"Using profile: {config.aws.profile}")
    
    # Configure AWS credentials (this will try to use real AWS credentials)
    try:
        success = configure_aws_credentials(config)
        if success:
            print("✓ AWS credentials configured successfully")
            print(f"Account ID: {config.aws.account_id}")
        else:
            print("✗ Failed to configure AWS credentials")
    except Exception as e:
        print(f"AWS credential error: {e}")
        print("This is expected if AWS credentials are not configured")


def example_aws_credential_validation():
    """Example: Validate AWS credentials."""
    print("\n=== AWS Credential Validation Example ===")
    
    config = ConfigurationManager()
    config.aws.region = 'us-west-2'
    config.aws.profile = 'default'
    
    # Try to validate credentials
    try:
        validation = validate_aws_credentials(config)
        
        print(f"Credentials valid: {validation['valid']}")
        print(f"Can make API calls: {validation['can_make_api_calls']}")
        
        if validation['error']:
            print(f"Error: {validation['error']}")
        
        if validation['account_id']:
            print(f"Account ID: {validation['account_id']}")
            
    except Exception as e:
        print(f"Validation error: {e}")


def example_mock_aws_credentials():
    """Example: Use mock AWS credentials for testing."""
    print("\n=== Mock AWS Credentials Example ===")
    
    # Mock boto3 session for demonstration
    with patch('boto3.Session') as mock_session:
        # Set up mock
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        # Mock STS client
        mock_sts = MagicMock()
        mock_session_instance.client.return_value = mock_sts
        mock_sts.get_caller_identity.return_value = {
            'Account': '123456789012',
            'Arn': 'arn:aws:iam::123456789012:user/testuser'
        }
        
        config = ConfigurationManager()
        config.aws.region = 'us-east-1'
        config.aws.profile = 'test'
        
        # Configure with mock
        success = configure_aws_credentials(config)
        print(f"Mock credential setup: {'✓' if success else '✗'}")
        print(f"Mock account ID: {config.aws.account_id}")
        
        # Validate with mock
        validation = validate_aws_credentials(config)
        print(f"Mock validation: {validation}")


def example_multiple_aws_profiles():
    """Example: Work with multiple AWS profiles."""
    print("\n=== Multiple AWS Profiles Example ===")
    
    profiles = ['default', 'production', 'development']
    
    for profile in profiles:
        print(f"\nTesting profile: {profile}")
        
        config = ConfigurationManager()
        config.aws.region = 'us-east-1'
        config.aws.profile = profile
        
        try:
            success = configure_aws_credentials(config)
            if success:
                print(f"  ✓ Profile {profile} configured")
                print(f"  Account ID: {config.aws.account_id}")
            else:
                print(f"  ✗ Profile {profile} failed")
        except Exception as e:
            print(f"  ✗ Profile {profile} error: {e}")


def example_aws_session_usage():
    """Example: Use AWS session from configuration."""
    print("\n=== AWS Session Usage Example ===")
    
    # Create test configuration with mock session
    with patch('boto3.Session') as mock_session:
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        # Mock EC2 client
        mock_ec2 = MagicMock()
        mock_session_instance.client.return_value = mock_ec2
        
        # Mock VPC response
        mock_ec2.describe_vpcs.return_value = {
            'Vpcs': [
                {
                    'VpcId': 'vpc-123456',
                    'State': 'available',
                    'CidrBlock': '10.0.0.0/16'
                }
            ]
        }
        
        config = ConfigurationManager()
        config.aws.region = 'us-east-1'
        configure_aws_credentials(config)
        
        # Use the session
        session = config.aws.get_session()
        ec2_client = session.client('ec2')
        
        # Make API call
        response = ec2_client.describe_vpcs()
        vpcs = response['Vpcs']
        
        print(f"Found {len(vpcs)} VPCs:")
        for vpc in vpcs:
            print(f"  VPC ID: {vpc['VpcId']}")
            print(f"  State: {vpc['State']}")
            print(f"  CIDR: {vpc['CidrBlock']}")


def example_aws_error_handling():
    """Example: Handle AWS credential and API errors."""
    print("\n=== AWS Error Handling Example ===")
    
    def test_invalid_profile():
        """Test handling of invalid AWS profile."""
        print("Testing invalid profile...")
        
        config = ConfigurationManager()
        config.aws.region = 'us-east-1'
        config.aws.profile = 'nonexistent-profile'
        
        try:
            success = configure_aws_credentials(config)
            if not success:
                print("  ✓ Correctly handled invalid profile")
        except Exception as e:
            print(f"  ✓ Exception caught for invalid profile: {e}")
    
    def test_invalid_region():
        """Test handling of invalid AWS region."""
        print("Testing invalid region...")
        
        config = ConfigurationManager()
        config.aws.region = 'invalid-region'
        config.aws.profile = 'default'
        
        errors = config.validate_all()
        region_errors = [e for e in errors if 'region' in e.lower()]
        
        if region_errors:
            print(f"  ✓ Region validation caught: {region_errors[0]}")
        else:
            print("  ⚠ Region validation might need improvement")
    
    def test_network_error():
        """Test handling of network errors."""
        print("Testing network error simulation...")
        
        with patch('boto3.Session') as mock_session:
            # Simulate network error
            mock_session.side_effect = Exception("Network error")
            
            config = ConfigurationManager()
            config.aws.region = 'us-east-1'
            config.aws.profile = 'default'
            
            try:
                success = configure_aws_credentials(config)
                print(f"  ✓ Network error handled gracefully: {not success}")
            except Exception as e:
                print(f"  ✓ Network error caught: {e}")
    
    # Run error handling tests
    test_invalid_profile()
    test_invalid_region()
    test_network_error()


def example_aws_credential_info():
    """Example: Display AWS credential information."""
    print("\n=== AWS Credential Information Example ===")
    
    # Mock credentials for demonstration
    with patch('boto3.Session') as mock_session:
        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance
        
        mock_sts = MagicMock()
        mock_session_instance.client.return_value = mock_sts
        mock_sts.get_caller_identity.return_value = {
            'Account': '123456789012',
            'Arn': 'arn:aws:iam::123456789012:user/demo-user',
            'UserId': 'AIDACKCEVSQ6C2EXAMPLE'
        }
        
        config = ConfigurationManager()
        config.aws.region = 'us-east-1'
        config.aws.profile = 'demo'
        
        # Configure credentials
        configure_aws_credentials(config)
        
        # Print credential information
        print("AWS Credential Information:")
        print_credentials_info(config)


def example_aws_configuration_best_practices():
    """Example: Best practices for AWS configuration."""
    print("\n=== AWS Configuration Best Practices Example ===")
    
    def setup_production_config():
        """Set up configuration for production environment."""
        config = ConfigurationManager()
        
        # Use specific profile for production
        config.aws.profile = 'production'
        config.aws.region = 'us-east-1'
        
        # Validate before use
        errors = config.validate_all()
        if errors:
            raise ValueError(f"Configuration errors: {errors}")
        
        # Configure credentials
        success = configure_aws_credentials(config)
        if not success:
            raise RuntimeError("Failed to configure AWS credentials")
        
        # Validate credentials work
        validation = validate_aws_credentials(config)
        if not validation['valid']:
            raise RuntimeError(f"Invalid credentials: {validation['error']}")
        
        return config
    
    def setup_development_config():
        """Set up configuration for development environment."""
        config = ConfigurationManager()
        
        # Use default profile for development
        config.aws.profile = 'default'
        config.aws.region = 'us-west-2'  # Different region for dev
        
        # Enable debug mode
        config.debug.debug = True
        
        return config
    
    # Demonstrate environment-specific setup
    print("Production configuration setup:")
    try:
        prod_config = setup_production_config()
        print("  ✓ Production config ready")
    except Exception as e:
        print(f"  ✗ Production config failed: {e}")
    
    print("\nDevelopment configuration setup:")
    try:
        dev_config = setup_development_config()
        print("  ✓ Development config ready")
        print(f"  Debug mode: {dev_config.debug.debug}")
    except Exception as e:
        print(f"  ✗ Development config failed: {e}")


def main():
    """Run all AWS integration examples."""
    print("Configuration Management System - AWS Integration Examples")
    print("=" * 70)
    
    examples = [
        example_aws_credential_setup,
        example_aws_credential_validation,
        example_mock_aws_credentials,
        example_multiple_aws_profiles,
        example_aws_session_usage,
        example_aws_error_handling,
        example_aws_credential_info,
        example_aws_configuration_best_practices
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"Error in {example.__name__}: {e}")
    
    print("\n" + "=" * 70)
    print("All AWS integration examples completed!")
    print("\nNote: Some examples may show errors if AWS credentials are not configured.")
    print("This is expected behavior for demonstration purposes.")


if __name__ == '__main__':
    main()