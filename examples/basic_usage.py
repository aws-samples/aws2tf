#!/usr/bin/env python3
"""
Basic usage examples for the Configuration Management System.
This file demonstrates common patterns and usage scenarios.
"""
import sys
import os

# Add the parent directory to Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from code.config import (
    ConfigurationManager,
    create_argument_parser,
    parse_and_update_config,
    create_test_config
)


def example_basic_configuration():
    """Example: Basic configuration setup and usage."""
    print("=== Basic Configuration Example ===")
    
    # Create a new configuration manager
    config = ConfigurationManager()
    
    # Set basic configuration
    config.aws.region = 'us-east-1'
    config.aws.profile = 'default'
    config.runtime.target_type = 'vpc'
    config.runtime.target_id = 'vpc-123456'
    config.debug.debug = True
    
    # Use configuration in your code
    print(f"Processing {config.runtime.target_type}: {config.runtime.target_id}")
    print(f"AWS Region: {config.aws.region}")
    print(f"Debug Mode: {config.is_debug_enabled()}")
    
    # Validate configuration
    errors = config.validate_all()
    if errors:
        print(f"Configuration errors: {errors}")
    else:
        print("Configuration is valid!")


def example_command_line_parsing():
    """Example: Parse configuration from command line arguments."""
    print("\n=== Command Line Parsing Example ===")
    
    # Simulate command line arguments
    test_args = [
        'aws2tf.py',
        '-t', 'vpc',
        '-i', 'vpc-123456',
        '-r', 'us-west-2',
        '-p', 'production',
        '--debug'
    ]
    
    # Parse arguments into configuration
    import sys
    original_argv = sys.argv
    try:
        sys.argv = test_args
        
        config = ConfigurationManager()
        args = parse_and_update_config(config)
        
        print(f"Parsed target type: {config.runtime.target_type}")
        print(f"Parsed target ID: {config.runtime.target_id}")
        print(f"Parsed region: {config.aws.region}")
        print(f"Parsed profile: {config.aws.profile}")
        print(f"Debug enabled: {config.debug.debug}")
        
    finally:
        sys.argv = original_argv


def example_resource_tracking():
    """Example: Track processed resources."""
    print("\n=== Resource Tracking Example ===")
    
    config = ConfigurationManager()
    
    # Track some resources
    resources = [
        'aws_vpc.vpc-123456',
        'aws_subnet.subnet-789012',
        'aws_security_group.sg-345678'
    ]
    
    for resource in resources:
        config.mark_resource_processed(resource)
        print(f"Marked as processed: {resource}")
    
    # Check if resources are processed
    for resource in resources:
        is_processed = config.is_resource_processed(resource)
        print(f"{resource}: {'✓' if is_processed else '✗'}")
    
    # Add VPCs to resource list
    config.resources.add_vpc_to_list('vpc-123456')
    config.resources.add_vpc_to_list('vpc-789012')
    
    vpc_list = config.resources.get_vpc_list()
    print(f"VPC list: {vpc_list}")


def example_processing_state():
    """Example: Manage processing state and tracking."""
    print("\n=== Processing State Example ===")
    
    config = ConfigurationManager()
    
    # Start processing
    config.start_processing()
    print("Processing started...")
    
    # Set tracking messages
    config.set_tracking_message("Discovering VPCs...")
    print(f"Status: {config.get_tracking_message()}")
    
    # Simulate some work
    import time
    time.sleep(0.1)
    
    config.set_tracking_message("Processing subnets...")
    print(f"Status: {config.get_tracking_message()}")
    
    # Set processing flags
    config.processing.set_processing_flag('vpc_discovery_complete', True)
    config.processing.set_processing_flag('subnet_processing_active', True)
    
    # Check processing flags
    vpc_done = config.processing.get_processing_flag('vpc_discovery_complete')
    subnet_active = config.processing.get_processing_flag('subnet_processing_active')
    
    print(f"VPC discovery complete: {vpc_done}")
    print(f"Subnet processing active: {subnet_active}")
    
    # Get elapsed time
    elapsed = config.get_processing_elapsed()
    print(f"Processing time: {elapsed:.3f} seconds")


def example_configuration_categories():
    """Example: Work with different configuration categories."""
    print("\n=== Configuration Categories Example ===")
    
    config = ConfigurationManager()
    
    # AWS Configuration
    config.aws.region = 'eu-west-1'
    config.aws.account_id = '123456789012'
    print(f"AWS: {config.aws.region} (Account: {config.aws.account_id})")
    
    # Debug Configuration
    config.debug.debug = True
    config.debug.debug5 = False
    print(f"Debug: {config.debug.debug}, Verbose: {config.debug.debug5}")
    
    # Runtime Configuration
    config.runtime.target_type = 'subnet'
    config.runtime.cores = 4
    config.set_cores(8)  # Use helper method
    print(f"Runtime: {config.runtime.target_type}, Cores: {config.get_cores()}")
    
    # Setup paths
    config.setup_paths()
    print(f"Paths: {config.runtime.path1}")


def example_dependency_injection():
    """Example: Use dependency injection pattern."""
    print("\n=== Dependency Injection Example ===")
    
    def process_vpc(config: ConfigurationManager, vpc_id: str) -> bool:
        """Example function using dependency injection."""
        if config.debug.debug:
            print(f"Processing VPC {vpc_id} in region {config.aws.region}")
        
        # Mark as processed
        config.mark_resource_processed(f'aws_vpc.{vpc_id}')
        
        # Add to VPC list
        config.resources.add_vpc_to_list(vpc_id)
        
        return True
    
    def process_subnet(config: ConfigurationManager, subnet_id: str, vpc_id: str) -> bool:
        """Example function processing subnets."""
        if config.debug.debug:
            print(f"Processing subnet {subnet_id} in VPC {vpc_id}")
        
        # Check if VPC was processed
        if not config.is_resource_processed(f'aws_vpc.{vpc_id}'):
            print(f"Warning: VPC {vpc_id} not processed yet")
        
        config.mark_resource_processed(f'aws_subnet.{subnet_id}')
        return True
    
    # Create configuration
    config = create_test_config()
    config.debug.debug = True
    
    # Use functions with dependency injection
    process_vpc(config, 'vpc-123456')
    process_subnet(config, 'subnet-789012', 'vpc-123456')
    
    # Check results
    vpc_list = config.resources.get_vpc_list()
    print(f"Processed VPCs: {vpc_list}")


def example_error_handling():
    """Example: Handle configuration errors and validation."""
    print("\n=== Error Handling Example ===")
    
    config = ConfigurationManager()
    
    # Try with invalid configuration
    config.aws.region = ''  # Invalid empty region
    config.runtime.target_type = 'invalid_type'  # Invalid target type
    
    # Validate and handle errors
    errors = config.validate_all()
    if errors:
        print("Configuration validation errors:")
        for error in errors:
            print(f"  - {error}")
        
        # Fix the errors
        config.aws.region = 'us-east-1'
        config.runtime.target_type = 'vpc'
        
        # Validate again
        errors = config.validate_all()
        if not errors:
            print("Configuration fixed and validated successfully!")
    
    # Example of handling AWS credential errors
    try:
        from code.config import configure_aws_credentials
        success = configure_aws_credentials(config)
        if success:
            print("AWS credentials configured successfully")
        else:
            print("Failed to configure AWS credentials")
    except Exception as e:
        print(f"AWS credential error: {e}")


def main():
    """Run all examples."""
    print("Configuration Management System - Basic Usage Examples")
    print("=" * 60)
    
    examples = [
        example_basic_configuration,
        example_command_line_parsing,
        example_resource_tracking,
        example_processing_state,
        example_configuration_categories,
        example_dependency_injection,
        example_error_handling
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"Error in {example.__name__}: {e}")
    
    print("\n" + "=" * 60)
    print("All examples completed!")


if __name__ == '__main__':
    main()