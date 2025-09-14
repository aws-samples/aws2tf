#!/usr/bin/env python3
"""
Demonstration of the new configuration management system.

This script shows how the ConfigurationManager replaces global variables
with proper dependency injection and encapsulation.
"""

import argparse
import sys
import os

# Add the current directory to Python path for imports
sys.path.insert(0, '.')

from code.config import (
    ConfigurationManager,
    create_test_config,
    create_debug_config,
    create_fast_config
)


def demonstrate_basic_usage():
    """Demonstrate basic configuration usage."""
    print("=== Basic Configuration Usage ===")
    
    # Create a configuration manager
    config = ConfigurationManager()
    
    # Show initial state
    print(f"Initial region: {config.aws.region}")
    print(f"Initial debug mode: {config.is_debug_enabled()}")
    print(f"Initial fast mode: {config.is_fast_mode()}")
    
    # Update configuration
    config.aws.region = "us-east-1"
    config.aws.account_id = "123456789012"
    config.debug.enabled = True
    
    print(f"Updated region: {config.aws.region}")
    print(f"Updated debug mode: {config.is_debug_enabled()}")
    print(f"Account ID: {config.aws.account_id}")
    
    # Validate configuration
    errors = config.validate_all()
    if errors:
        print(f"Validation errors: {errors}")
    else:
        print("Configuration is valid!")
    
    print()


def demonstrate_argument_parsing():
    """Demonstrate configuration from command-line arguments."""
    print("=== Command-Line Argument Integration ===")
    
    # Simulate command-line arguments
    args = argparse.Namespace()
    args.profile = "production"
    args.region = "us-west-2"
    args.debug = True
    args.fast = True  # This should be overridden by debug
    args.merge = True
    args.ec2tag = "Environment:Production"
    
    config = ConfigurationManager()
    config.update_from_args(args)
    
    print(f"Profile: {config.aws.profile}")
    print(f"Region: {config.aws.region}")
    print(f"Debug enabled: {config.debug.enabled}")
    print(f"Fast mode: {config.runtime.fast}")  # Should be False due to debug
    print(f"Merge mode: {config.runtime.merge}")
    print(f"EC2 tag: {config.runtime.ec2tag}")
    print(f"EC2 tag key: {config.runtime.ec2tagk}")
    print(f"EC2 tag value: {config.runtime.ec2tagv}")
    
    print()


def demonstrate_factory_functions():
    """Demonstrate factory functions for easy configuration creation."""
    print("=== Factory Functions ===")
    
    # Test configuration
    test_config = create_test_config(region="eu-west-1", debug=True)
    print(f"Test config - Region: {test_config.aws.region}, Debug: {test_config.debug.enabled}")
    
    # Debug configuration
    debug_config = create_debug_config()
    print(f"Debug config - Debug: {debug_config.debug.enabled}, Fast: {debug_config.runtime.fast}")
    
    # Fast configuration
    fast_config = create_fast_config()
    print(f"Fast config - Fast: {fast_config.runtime.fast}, Cores: {fast_config.processing.cores}")
    
    print()


def demonstrate_thread_safety():
    """Demonstrate thread-safe operations."""
    print("=== Thread Safety ===")
    
    import threading
    import time
    
    config = ConfigurationManager()
    results = []
    
    def worker(worker_id):
        for i in range(5):
            message = f"Worker {worker_id} - Step {i}"
            config.set_tracking_message(message)
            retrieved = config.get_tracking_message()
            results.append((worker_id, i, retrieved))
            time.sleep(0.01)
    
    # Start multiple threads
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for completion
    for thread in threads:
        thread.join()
    
    print(f"Completed {len(results)} thread-safe operations")
    print(f"Final tracking message: {config.get_tracking_message()}")
    
    print()


def demonstrate_dependency_injection():
    """Demonstrate dependency injection pattern."""
    print("=== Dependency Injection Pattern ===")
    
    def process_resources(config: ConfigurationManager):
        """Example function that receives configuration via dependency injection."""
        if config.is_debug_enabled():
            print("Debug mode: Processing resources with detailed logging")
        else:
            print("Normal mode: Processing resources")
        
        if config.is_fast_mode():
            cores = config.get_cores()
            print(f"Fast mode: Using {cores} cores for parallel processing")
        
        config.set_tracking_message("Processing AWS resources...")
        print(f"Status: {config.get_tracking_message()}")
    
    # Create different configurations and pass them to the function
    configs = [
        ("Debug Config", create_debug_config()),
        ("Fast Config", create_fast_config()),
        ("Test Config", create_test_config(debug=False, fast=False))
    ]
    
    for name, config in configs:
        print(f"\n--- {name} ---")
        process_resources(config)
    
    print()


def demonstrate_validation():
    """Demonstrate configuration validation."""
    print("=== Configuration Validation ===")
    
    # Invalid configuration
    invalid_config = ConfigurationManager()
    errors = invalid_config.validate_all()
    print(f"Invalid config errors: {len(errors)}")
    for error in errors:
        print(f"  - {error}")
    
    # Valid configuration
    valid_config = create_test_config()
    errors = valid_config.validate_all()
    print(f"Valid config errors: {len(errors)}")
    
    print()


def main():
    """Run all demonstrations."""
    print("Configuration Management System Demonstration")
    print("=" * 50)
    print()
    
    demonstrate_basic_usage()
    demonstrate_argument_parsing()
    demonstrate_factory_functions()
    demonstrate_thread_safety()
    demonstrate_dependency_injection()
    demonstrate_validation()
    
    print("Demonstration complete!")


if __name__ == "__main__":
    main()