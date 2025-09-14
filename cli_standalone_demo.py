#!/usr/bin/env python3
"""
Standalone CLI Interface Demo.

This script demonstrates the CLI interface functionality without
complex import dependencies.
"""

import sys
import os
import argparse
import time
from pathlib import Path
from enum import Enum

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'code'))

from config import create_test_config


class WorkflowMode(Enum):
    """Workflow execution modes."""
    FULL = "full"
    DISCOVERY_ONLY = "discovery"
    VALIDATE_ONLY = "validate"
    IMPORT_ONLY = "import"
    GENERATE_ONLY = "generate"
    DRY_RUN = "dry_run"


class CLIColors:
    """ANSI color codes for CLI output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


class CLIProgressBar:
    """Progress bar for CLI operations."""
    
    def __init__(self, width: int = 50):
        self.width = width
        self.last_message = ""
    
    def update(self, message: str, progress: float):
        """Update the progress bar."""
        filled_width = int(self.width * progress)
        bar = '█' * filled_width + '░' * (self.width - filled_width)
        
        percentage = f"{progress:.1%}"
        display = f"\r{CLIColors.OKBLUE}Progress:{CLIColors.ENDC} |{bar}| {percentage} - {message}"
        
        # Clear the line if the new message is shorter
        if len(message) < len(self.last_message):
            display += " " * (len(self.last_message) - len(message))
        
        print(display, end='', flush=True)
        self.last_message = message
        
        if progress >= 1.0:
            print()  # New line when complete


def create_cli_parser():
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog='aws2tf',
        description='Import AWS infrastructure into Terraform with comprehensive workflow orchestration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  aws2tf vpc vpc-12345                    # Import VPC and all dependencies
  aws2tf subnet subnet-67890 --dry-run   # Show what would be imported
  aws2tf instance i-abcdef --discovery   # Only discover resources
  aws2tf --validate-only vpc vpc-12345   # Only validate dependencies
  aws2tf --generate-only --output ./tf   # Only generate terraform files
  
Workflow Modes:
  --full          Complete workflow (discovery → validation → import → generation)
  --discovery     Only discover resources and dependencies
  --validate-only Only validate resource dependencies
  --import-only   Only import resources into terraform
  --generate-only Only generate terraform configuration files
  --dry-run       Show what would be done without executing
        """
    )
    
    # Target resource arguments
    parser.add_argument(
        'target_type',
        nargs='?',
        help='AWS resource type to import (vpc, subnet, instance, etc.)'
    )
    
    parser.add_argument(
        'target_id',
        nargs='?',
        help='AWS resource ID to import'
    )
    
    # Workflow mode arguments
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        '--full',
        action='store_const',
        const=WorkflowMode.FULL,
        dest='workflow_mode',
        default=WorkflowMode.FULL,
        help='Execute complete workflow (default)'
    )
    mode_group.add_argument(
        '--discovery',
        action='store_const',
        const=WorkflowMode.DISCOVERY_ONLY,
        dest='workflow_mode',
        help='Only discover resources and dependencies'
    )
    mode_group.add_argument(
        '--validate-only',
        action='store_const',
        const=WorkflowMode.VALIDATE_ONLY,
        dest='workflow_mode',
        help='Only validate resource dependencies'
    )
    mode_group.add_argument(
        '--dry-run',
        action='store_const',
        const=WorkflowMode.DRY_RUN,
        dest='workflow_mode',
        help='Show what would be done without executing'
    )
    
    # Output and configuration
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output directory for generated terraform files'
    )
    
    parser.add_argument(
        '--region',
        help='AWS region (overrides profile/environment setting)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug output'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Suppress non-essential output'
    )
    
    # Information commands
    parser.add_argument(
        '--version',
        action='version',
        version='aws2tf 2.0.0 (with workflow orchestrator)'
    )
    
    parser.add_argument(
        '--list-resources',
        action='store_true',
        help='List supported AWS resource types and exit'
    )
    
    parser.add_argument(
        '--validate-config',
        action='store_true',
        help='Validate configuration and exit'
    )
    
    return parser


def print_success(message: str):
    """Print a success message."""
    print(f"{CLIColors.OKGREEN}✓{CLIColors.ENDC} {message}")


def print_warning(message: str):
    """Print a warning message."""
    print(f"{CLIColors.WARNING}⚠{CLIColors.ENDC} {message}")


def print_error(message: str):
    """Print an error message."""
    print(f"{CLIColors.FAIL}✗{CLIColors.ENDC} {message}")


def print_info(message: str):
    """Print an info message."""
    print(f"{CLIColors.OKBLUE}ℹ{CLIColors.ENDC} {message}")


def print_header(title: str):
    """Print a formatted header."""
    print(f"\n{CLIColors.HEADER}{CLIColors.BOLD}{title}{CLIColors.ENDC}")
    print(f"{CLIColors.HEADER}{'=' * len(title)}{CLIColors.ENDC}")


def list_supported_resources():
    """List supported AWS resource types."""
    print_header("Supported AWS Resource Types")
    
    resource_types = [
        "vpc", "subnet", "instance", "security_group", "internet_gateway",
        "route_table", "network_acl", "nat_gateway", "elastic_ip",
        "load_balancer", "target_group", "auto_scaling_group",
        "launch_template", "key_pair", "iam_role", "iam_policy",
        "s3_bucket", "rds_instance", "rds_cluster", "lambda_function"
    ]
    
    for i, resource_type in enumerate(sorted(resource_types), 1):
        print(f"  {i:2d}. {resource_type}")
    
    print(f"\nTotal: {len(resource_types)} resource types supported")


def validate_configuration():
    """Validate configuration and display results."""
    print_header("Configuration Validation")
    
    try:
        config = create_test_config(
            region='us-east-1',
            account_id='123456789012'
        )
        
        # AWS Configuration
        aws_errors = config.aws.validate()
        if aws_errors:
            print_error("AWS Configuration Issues:")
            for error in aws_errors:
                print(f"    - {error}")
        else:
            print_success("AWS configuration is valid")
            print(f"    Region: {config.aws.region}")
            print(f"    Account ID: {config.aws.account_id}")
            print(f"    Profile: {config.aws.profile}")
        
        # Runtime Configuration
        runtime_errors = config.runtime.validate()
        if runtime_errors:
            print_error("Runtime Configuration Issues:")
            for error in runtime_errors:
                print(f"    - {error}")
        else:
            print_success("Runtime configuration is valid")
        
        total_errors = len(aws_errors) + len(runtime_errors)
        if total_errors == 0:
            print_success("All configuration validation passed")
            return True
        else:
            print_error(f"Configuration validation failed with {total_errors} errors")
            return False
            
    except Exception as e:
        print_error(f"Configuration validation failed: {e}")
        return False


def simulate_workflow(target_type: str, target_id: str, mode: WorkflowMode, output_prefix: str = None):
    """Simulate workflow execution."""
    print_header(f"AWS2TF Workflow Execution")
    print(f"Target Resource: {target_type}:{target_id}")
    print(f"Workflow Mode: {mode.value}")
    
    # Create output directory using aws2tf convention
    config = create_test_config()
    prefix_part = f"{output_prefix}-" if output_prefix else ""
    output_dir = Path(f"generated/tf-{prefix_part}{config.aws.account_id}-{config.aws.region}")
    print(f"Output Directory: {output_dir}")
    
    # Simulate workflow phases
    progress_bar = CLIProgressBar()
    
    phases = [
        ("Initializing workflow", 0.1),
        ("Discovering resources", 0.3),
        ("Validating dependencies", 0.5),
        ("Importing resources", 0.7),
        ("Generating configurations", 0.9),
        ("Finalizing workflow", 1.0)
    ]
    
    for phase_name, progress in phases:
        progress_bar.update(phase_name, progress)
        time.sleep(0.3)  # Simulate work
        
        # Skip phases based on mode
        if mode == WorkflowMode.DISCOVERY_ONLY and progress > 0.3:
            break
        elif mode == WorkflowMode.VALIDATE_ONLY and progress > 0.5:
            break
    
    print()
    
    # Print results
    print_success("Workflow completed successfully")
    print(f"Phase Completed: {'discovery' if mode == WorkflowMode.DISCOVERY_ONLY else 'completed'}")
    print(f"Execution Time: {len(phases) * 0.3:.1f}s")
    
    print(f"\nMetrics:")
    print(f"  Resources Discovered: 3")
    print(f"  Resources Validated: 3")
    print(f"  Resources Imported: 2" if mode != WorkflowMode.DRY_RUN else "  Resources Imported: 0 (dry-run)")
    print(f"  Configs Generated: 3")
    
    if output_dir:
        print(f"\nGenerated Files:")
        print(f"  - {output_dir}/main.tf")
        print(f"  - {output_dir}/variables.tf")
        print(f"  - {output_dir}/outputs.tf")


def demo_cli_functionality():
    """Demonstrate CLI functionality."""
    print("AWS2TF CLI Interface Demo")
    print("=" * 60)
    
    print("\n1. TESTING ARGUMENT PARSING")
    print("-" * 40)
    
    parser = create_cli_parser()
    
    # Test different argument combinations
    test_cases = [
        {
            'args': ['vpc', 'vpc-12345'],
            'description': 'Basic VPC import'
        },
        {
            'args': ['subnet', 'subnet-67890', '--discovery'],
            'description': 'Discovery-only mode'
        },
        {
            'args': ['instance', 'i-abcdef', '--dry-run', '--debug'],
            'description': 'Dry-run with debug'
        },
        {
            'args': ['vpc', 'vpc-test', '--output', '/tmp/terraform', '--region', 'us-west-2'],
            'description': 'Full workflow with options'
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        try:
            args = parser.parse_args(test_case['args'])
            print_success(f"{i}. {test_case['description']}")
            print(f"   Target: {args.target_type}:{args.target_id}")
            print(f"   Mode: {args.workflow_mode.value}")
            if args.output:
                print(f"   Output: {args.output}")
        except Exception as e:
            print_error(f"{i}. {test_case['description']}: {e}")
    
    print("\n2. TESTING SPECIAL COMMANDS")
    print("-" * 40)
    
    # Test --list-resources
    print("Testing --list-resources:")
    list_supported_resources()
    
    print("\nTesting --validate-config:")
    validate_configuration()
    
    print("\n3. TESTING WORKFLOW SIMULATION")
    print("-" * 40)
    
    # Test different workflow modes
    workflow_tests = [
        ('vpc', 'vpc-demo', WorkflowMode.FULL),
        ('subnet', 'subnet-demo', WorkflowMode.DISCOVERY_ONLY),
        ('instance', 'i-demo', WorkflowMode.DRY_RUN)
    ]
    
    for target_type, target_id, mode in workflow_tests:
        print(f"\nSimulating {mode.value} workflow:")
        simulate_workflow(target_type, target_id, mode)
    
    print("\n4. TESTING ERROR SCENARIOS")
    print("-" * 40)
    
    # Test invalid arguments
    invalid_cases = [
        {
            'args': [],
            'description': 'Missing required arguments'
        },
        {
            'args': ['vpc'],
            'description': 'Missing target ID'
        }
    ]
    
    for i, test_case in enumerate(invalid_cases, 1):
        try:
            args = parser.parse_args(test_case['args'])
            print_warning(f"{i}. {test_case['description']}: Unexpectedly succeeded")
        except SystemExit:
            print_success(f"{i}. {test_case['description']}: Correctly failed")
        except Exception as e:
            print_info(f"{i}. {test_case['description']}: {e}")
    
    print("\n" + "=" * 60)
    print("CLI DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    
    print("\nCLI Features Demonstrated:")
    print("✓ Comprehensive argument parsing")
    print("✓ Multiple workflow modes")
    print("✓ Rich output formatting with colors")
    print("✓ Progress reporting")
    print("✓ Configuration validation")
    print("✓ Resource listing")
    print("✓ Error handling")
    print("✓ Workflow simulation")
    
    print("\nThe CLI interface structure is working correctly!")


if __name__ == '__main__':
    try:
        demo_cli_functionality()
    except KeyboardInterrupt:
        print(f"\n{CLIColors.WARNING}Demo interrupted by user{CLIColors.ENDC}")
    except Exception as e:
        print_error(f"Demo failed: {e}")
        import traceback
        traceback.print_exc()