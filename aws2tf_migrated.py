#!/usr/bin/env python3
"""
aws2tf - Import AWS resources to Terraform

Migrated version using ConfigurationManager instead of global variables.
"""

import sys
import os
import datetime
import multiprocessing
from pathlib import Path

# Add the current directory to Python path for imports
sys.path.insert(0, '.')

# Import configuration system
from code.config import (
    ConfigurationManager,
    create_argument_parser,
    parse_and_update_config,
    validate_argument_combinations,
    configure_aws_credentials,
    validate_aws_credentials,
    print_credentials_info
)

# Import existing modules
import code.common_minimal as common

# Simple timed interrupt replacement to avoid globals dependency
class SimpleTimedInterrupt:
    def __init__(self, increment=20):
        self.increment = increment
        self.running = False
    
    def start(self):
        self.running = True
        if hasattr(self, 'config'):
            print(f"Started progress tracking (every {self.increment}s)")
    
    def stop(self):
        self.running = False
        print("Stopped progress tracking")

# Create a simple timed interrupt instance
class TimedInterruptModule:
    def __init__(self):
        self.timed_int = SimpleTimedInterrupt()

timed_interrupt = TimedInterruptModule()


def setup_multiprocessing(config: ConfigurationManager) -> None:
    """
    Set up multiprocessing configuration.
    
    Args:
        config: Configuration manager to update with core count.
    """
    logical_cores = multiprocessing.cpu_count()
    print(f"Logical cores: {logical_cores}")
    
    # Set cores based on logical cores, with a maximum of 16
    cores = logical_cores * 2
    if cores > 16:
        cores = 16
    
    config.set_cores(cores)
    print(f"Using {cores} cores for processing")


def validate_terraform_installation(config: ConfigurationManager) -> bool:
    """
    Validate Terraform installation and version.
    
    Args:
        config: Configuration manager with Terraform version info.
        
    Returns:
        True if Terraform is properly installed and configured.
    """
    import subprocess
    
    try:
        # Check Terraform version
        result = subprocess.run(
            ["terraform", "version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode != 0:
            print("ERROR: Terraform not found or not working properly")
            print("Please install Terraform and ensure it's in your PATH")
            return False
        
        # Extract version from output
        output_lines = result.stdout.strip().split('\n')
        if output_lines:
            tf_version_line = output_lines[0]
            print(f"Terraform version: {tf_version_line}, AWS provider version: {config.aws.tf_version}")
        
        return True
        
    except subprocess.TimeoutExpired:
        print("ERROR: Terraform version check timed out")
        return False
    except FileNotFoundError:
        print("ERROR: Terraform not found in PATH")
        print("Please install Terraform from https://www.terraform.io/downloads.html")
        return False
    except Exception as e:
        print(f"ERROR: Failed to check Terraform version: {str(e)}")
        return False


def setup_aws_credentials(config: ConfigurationManager) -> bool:
    """
    Set up and validate AWS credentials.
    
    Args:
        config: Configuration manager to update with AWS credentials.
        
    Returns:
        True if AWS credentials are properly configured.
    """
    print("Detecting AWS credentials...")
    
    # Configure AWS credentials
    if not configure_aws_credentials(config):
        print("ERROR: Could not detect valid AWS credentials")
        print_credentials_info(config)
        return False
    
    # Validate credentials
    validation = validate_aws_credentials(config)
    
    print(f"Credentials Type: {config.aws.credential_type}")
    print(f"Is SSO login: {config.aws.is_sso}")
    
    if not validation['valid']:
        print("ERROR: AWS credentials validation failed")
        for error in validation['errors']:
            print(f"  - {error}")
        print_credentials_info(config)
        return False
    
    print(f"Using region: {config.aws.region} account: {config.aws.account_id} profile: {config.aws.profile}\n")
    return True


def setup_processing_environment(config: ConfigurationManager) -> None:
    """
    Set up the processing environment and paths.
    
    Args:
        config: Configuration manager to configure.
    """
    # Set up paths based on configuration
    config.setup_paths()
    
    # Create necessary directories
    Path(config.runtime.path1).mkdir(parents=True, exist_ok=True)
    Path(config.runtime.path2).mkdir(parents=True, exist_ok=True)
    Path(config.runtime.path3).mkdir(parents=True, exist_ok=True)
    
    print(f"Output directory: {config.runtime.path1}")
    
    # Set up timed interrupt for progress reporting
    timed_interrupt.timed_int = SimpleTimedInterrupt(increment=20)
    timed_interrupt.timed_int.start()


def process_resources(config: ConfigurationManager) -> bool:
    """
    Process AWS resources based on configuration.
    
    Args:
        config: Configuration manager with processing settings.
        
    Returns:
        True if processing completed successfully.
    """
    try:
        # Start processing timer
        config.start_processing()
        
        # Determine what resources to process
        if config.runtime.target_type and config.runtime.target_id:
            # Process specific resource
            print(f"Processing specific resource: {config.runtime.target_type} {config.runtime.target_id}")
            config.set_tracking_message(f"Processing {config.runtime.target_type} {config.runtime.target_id}")
            
            # Call the appropriate resource processing function
            success = common.call_resource(config, config.runtime.target_type, config.runtime.target_id)
            
            if not success:
                print(f"Failed to process {config.runtime.target_type} {config.runtime.target_id}")
                return False
            
        elif config.runtime.target_type:
            # Process all resources of a specific type
            print(f"Processing all resources of type: {config.runtime.target_type}")
            config.set_tracking_message(f"Processing all {config.runtime.target_type} resources")
            
            # For minimal mode, just process the specified resource type
            # without importing the complex resources module
            if config.runtime.target_type in ['all', 'aws']:
                print("Processing all resource types not yet supported in minimal mode")
                print("Please specify a specific resource type with -t")
                return False
            else:
                # Process the specific resource type by calling common.call_resource with None ID
                # This will trigger the list_resources functionality
                success = common.call_resource(config, config.runtime.target_type, None)
            
                if not success:
                    print(f"Failed to process {config.runtime.target_type} resources")
                    return False
        
        else:
            print("No specific resource type specified. Use -t to specify resource type.")
            return False
        
        # Processing completed
        try:
            elapsed_time = config.get_elapsed_time()
            print(f"\nProcessing completed in {elapsed_time:.2f} seconds")
        except AttributeError:
            print(f"\nProcessing completed")
        
        # Show processing statistics
        try:
            stats = config.get_processing_stats()
            print(f"Processed {stats['processed_resources']} resources")
            if stats['failed_resources'] > 0:
                print(f"Failed to process {stats['failed_resources']} resources")
        except AttributeError:
            print("Processing statistics not available")
        
        return True
        
    except KeyboardInterrupt:
        print("\nProcessing interrupted by user")
        return False
    except Exception as e:
        print(f"\nERROR: Processing failed: {str(e)}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        return False
    finally:
        # Stop timed interrupt
        if hasattr(timed_interrupt, 'timed_int'):
            timed_interrupt.timed_int.stop()


def extra_help() -> None:
    """
    Display extra help information.
    """
    print("\nExtra Help Information:")
    print("=" * 50)
    print("\nSupported Resource Types:")
    
    # This would show all supported resource types
    # For now, just show some examples
    examples = [
        "aws_vpc - Virtual Private Clouds",
        "aws_subnet - Subnets",
        "aws_security_group - Security Groups",
        "aws_instance - EC2 Instances",
        "aws_s3_bucket - S3 Buckets",
        "aws_iam_role - IAM Roles",
        "aws_lambda_function - Lambda Functions"
    ]
    
    for example in examples:
        print(f"  {example}")
    
    print("\nExample Commands:")
    print("  aws2tf.py -t aws_vpc -i vpc-12345678")
    print("  aws2tf.py -t ec2 -r us-west-2")
    print("  aws2tf.py -t s3 -p production")
    print("  aws2tf.py -t all -r us-east-1 --fast")
    
    print("\nFor more information, visit: https://github.com/aws-samples/aws2tf")


def main() -> int:
    """
    Main entry point for aws2tf.
    
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    # Print startup message
    now = datetime.datetime.now()
    print(f"aws2tf v1010 started at {now}")
    start_time = now
    
    try:
        # Create configuration manager
        config = ConfigurationManager()
        
        # Parse command-line arguments
        try:
            args = parse_and_update_config(config)
        except SystemExit as e:
            # Handle help or argument parsing errors
            return e.code if e.code is not None else 0
        
        # Validate argument combinations
        arg_errors = validate_argument_combinations(args)
        if arg_errors:
            print("ERROR: Invalid argument combinations:")
            for error in arg_errors:
                print(f"  - {error}")
            return 1
        
        # Handle special flags
        if hasattr(args, 'list') and args.list:
            extra_help()
            return 0
        
        # Set up multiprocessing
        setup_multiprocessing(config)
        
        # Validate Terraform installation
        if not validate_terraform_installation(config):
            return 1
        
        # Set up AWS credentials
        if not setup_aws_credentials(config):
            return 1
        
        # Validate configuration
        config_errors = config.validate_all()
        if config_errors:
            print("ERROR: Configuration validation failed:")
            for error in config_errors:
                print(f"  - {error}")
            return 1
        
        # Set up processing environment
        setup_processing_environment(config)
        
        # Process resources
        if not process_resources(config):
            return 1
        
        # Success
        end_time = datetime.datetime.now()
        total_time = (end_time - start_time).total_seconds()
        print(f"\naws2tf completed successfully in {total_time:.2f} seconds")
        return 0
        
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return 130  # Standard exit code for SIGINT
    except Exception as e:
        print(f"\nFATAL ERROR: {str(e)}")
        # Only show traceback in debug mode
        try:
            if config.is_debug_enabled():
                import traceback
                traceback.print_exc()
        except:
            pass  # config might not be initialized
        return 1
    finally:
        # Clean up
        try:
            if hasattr(timed_interrupt, 'timed_int'):
                timed_interrupt.timed_int.stop()
        except:
            pass


if __name__ == "__main__":
    sys.exit(main())