#!/usr/bin/env python3
"""
Interactive test script for the aws2tf pipeline.
Allows you to test different scenarios interactively.
"""

import sys
sys.path.insert(0, '.')

from code.config import ConfigurationManager, create_test_config
from code.resource_discovery import ResourceDiscovery
from code.dependency_mapper import ResourceDependencyMapper
from code.resource_processor import ResourceProcessor


def interactive_menu():
    """Interactive testing menu."""
    config = create_test_config()
    config.debug.debug = True
    
    while True:
        print("\n" + "="*50)
        print("AWS2TF Pipeline Interactive Test")
        print("="*50)
        print("1. Test Configuration System")
        print("2. Test Resource Discovery")
        print("3. Test Dependency Mapping")
        print("4. Test Resource Processor")
        print("5. Test Complete Pipeline")
        print("6. Run Unit Tests")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            test_configuration(config)
        elif choice == "2":
            test_discovery_interactive(config)
        elif choice == "3":
            test_dependency_interactive(config)
        elif choice == "4":
            test_processor_interactive(config)
        elif choice == "5":
            test_pipeline_interactive(config)
        elif choice == "6":
            run_unit_tests()
        else:
            print("Invalid choice. Please try again.")


def test_configuration(config):
    """Test configuration system."""
    print("\n--- Configuration System Test ---")
    
    print(f"AWS Region: {config.aws.region}")
    print(f"Debug Mode: {config.debug.debug}")
    print(f"Cores: {config.get_cores()}")
    
    # Test configuration updates
    new_region = input("Enter new region (or press Enter to skip): ").strip()
    if new_region:
        config.aws.region = new_region
        print(f"Updated region to: {config.aws.region}")
    
    # Test validation
    errors = config.validate_all()
    print(f"Configuration validation errors: {len(errors)}")
    for error in errors[:3]:
        print(f"  - {error}")


def test_discovery_interactive(config):
    """Test resource discovery interactively."""
    print("\n--- Resource Discovery Test ---")
    
    discovery = ResourceDiscovery(config)
    
    resource_type = input("Enter resource type (e.g., aws_vpc): ").strip()
    resource_id = input("Enter resource ID (e.g., vpc-123456): ").strip()
    
    if resource_type and resource_id:
        print(f"Discovering {resource_type}.{resource_id}...")
        
        # Note: This will fail without real AWS credentials
        # but will show the discovery process
        try:
            resource_info = discovery.discover_resource(resource_type, resource_id)
            print(f"Status: {resource_info.status.value}")
            if resource_info.error_message:
                print(f"Error: {resource_info.error_message}")
        except Exception as e:
            print(f"Discovery error: {e}")
    
    # Show discovery summary
    summary = discovery.get_discovery_summary()
    print(f"Total discovered: {summary['total_resources']}")


def test_dependency_interactive(config):
    """Test dependency mapping interactively."""
    print("\n--- Dependency Mapping Test ---")
    
    mapper = ResourceDependencyMapper(config)
    
    # Test with sample data
    sample_resources = {
        "aws_vpc.vpc-test": {
            "resource_type": "aws_vpc",
            "aws_data": {"VpcId": "vpc-test"}
        },
        "aws_subnet.subnet-test": {
            "resource_type": "aws_subnet", 
            "aws_data": {"SubnetId": "subnet-test", "VpcId": "vpc-test"}
        }
    }
    
    print("Testing with sample resources...")
    issues = mapper.validate_dependencies(sample_resources)
    
    print(f"Validation issues found: {len(issues)}")
    for issue in issues:
        print(f"  - {issue.severity.value}: {issue.message}")
    
    # Test dependency rules
    print(f"Total dependency rules: {len(mapper.dependency_rules)}")
    
    # Show some rules
    print("Sample dependency rules:")
    for rule in mapper.dependency_rules[:5]:
        print(f"  - {rule.source_type} -> {rule.target_type} ({rule.dependency_type.value})")


def test_processor_interactive(config):
    """Test resource processor interactively."""
    print("\n--- Resource Processor Test ---")
    
    processor = ResourceProcessor(config)
    
    # Add some test tasks
    print("Adding test tasks...")
    task1 = processor.add_discovery_task("aws_vpc", "vpc-test")
    task2 = processor.add_discovery_task("aws_subnet", "subnet-test")
    task3 = processor.add_validation_task({})
    
    print(f"Added {len(processor.tasks)} tasks")
    
    # Show execution order
    order = processor._build_execution_order()
    print(f"Execution order: {len(order)} levels")
    
    # Show status
    status = processor.get_processing_status()
    print(f"Status: {status['pending']} pending, {status['completed']} completed")


def test_pipeline_interactive(config):
    """Test complete pipeline interactively."""
    print("\n--- Complete Pipeline Test ---")
    
    target_type = input("Enter target type (e.g., vpc, subnet, ec2): ").strip()
    target_id = input("Enter target ID: ").strip()
    
    if target_type and target_id:
        print(f"Testing pipeline for {target_type}:{target_id}")
        print("Note: This will use mock data since real AWS credentials may not be available")
        
        # This would normally call the real pipeline
        print("Pipeline phases:")
        print("  1. Discovery - Find resources and dependencies")
        print("  2. Validation - Check dependency relationships") 
        print("  3. Import - Generate terraform import commands")
        print("  4. Generation - Create terraform configuration files")
        
        include_validation = input("Include validation? (y/n): ").lower().startswith('y')
        include_import = input("Include import? (y/n): ").lower().startswith('y')
        include_generation = input("Include generation? (y/n): ").lower().startswith('y')
        
        print(f"Would run pipeline with:")
        print(f"  - Validation: {include_validation}")
        print(f"  - Import: {include_import}")
        print(f"  - Generation: {include_generation}")


def run_unit_tests():
    """Run the unit tests."""
    print("\n--- Running Unit Tests ---")
    
    import subprocess
    import os
    
    test_files = [
        "tests/test_resource_discovery.py",
        "tests/test_dependency_mapper.py", 
        "tests/test_resource_processor.py"
    ]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"\nRunning {test_file}...")
            try:
                result = subprocess.run([sys.executable, test_file], 
                                      capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    print("  ✓ PASSED")
                else:
                    print("  ✗ FAILED")
                    print(f"  Error: {result.stderr}")
            except subprocess.TimeoutExpired:
                print("  ⚠ TIMEOUT")
            except Exception as e:
                print(f"  ✗ ERROR: {e}")
        else:
            print(f"  ⚠ {test_file} not found")


if __name__ == "__main__":
    interactive_menu()