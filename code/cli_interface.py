#!/usr/bin/env python3
"""
Command-Line Interface for aws2tf with Main Workflow Integration.

This module provides a comprehensive command-line interface that integrates with
the main workflow orchestrator to provide all aws2tf operations with proper
argument parsing, validation, and user interaction.
"""

import sys
import os
import argparse
import time
import json
from typing import Dict, List, Optional, Any, Callable
from pathlib import Path
import signal
import threading
from datetime import datetime

try:
    from .config import (
        ConfigurationManager, create_test_config, create_production_config,
        parse_and_update_config, validate_argument_combinations
    )
    from .main_workflow import (
        MainWorkflow, WorkflowPhase, WorkflowMode, WorkflowResult,
        create_main_workflow, execute_aws2tf_workflow
    )
except ImportError:
    # For standalone testing
    from config import (
        ConfigurationManager, create_test_config, create_production_config,
        parse_and_update_config, validate_argument_combinations
    )
    from main_workflow import (
        MainWorkflow, WorkflowPhase, WorkflowMode, WorkflowResult,
        create_main_workflow, execute_aws2tf_workflow
    )


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
    UNDERLINE = '\033[4m'


class CLIProgressBar:
    """Progress bar for CLI operations."""
    
    def __init__(self, width: int = 50, show_percentage: bool = True):
        self.width = width
        self.show_percentage = show_percentage
        self.last_message = ""
    
    def update(self, message: str, progress: float):
        """Update the progress bar."""
        filled_width = int(self.width * progress)
        bar = '█' * filled_width + '░' * (self.width - filled_width)
        
        if self.show_percentage:
            percentage = f"{progress:.1%}"
            display = f"\r{CLIColors.OKBLUE}Progress:{CLIColors.ENDC} |{bar}| {percentage} - {message}"
        else:
            display = f"\r{CLIColors.OKBLUE}Progress:{CLIColors.ENDC} |{bar}| {message}"
        
        # Clear the line if the new message is shorter
        if len(message) < len(self.last_message):
            display += " " * (len(self.last_message) - len(message))
        
        print(display, end='', flush=True)
        self.last_message = message
        
        if progress >= 1.0:
            print()  # New line when complete


class AWS2TFCLIInterface:
    """
    Main command-line interface for aws2tf operations.
    
    Provides comprehensive CLI functionality including argument parsing,
    workflow execution, progress reporting, and user interaction.
    """
    
    def __init__(self):
        """Initialize the CLI interface."""
        self.config: Optional[ConfigurationManager] = None
        self.workflow: Optional[MainWorkflow] = None
        self.progress_bar = CLIProgressBar()
        self.interrupted = False
        self.start_time = time.time()
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle interrupt signals gracefully."""
        print(f"\n{CLIColors.WARNING}Received interrupt signal. Cancelling workflow...{CLIColors.ENDC}")
        self.interrupted = True
        if self.workflow:
            self.workflow.cancel_workflow()
    
    def create_argument_parser(self) -> argparse.ArgumentParser:
        """Create the main argument parser with all aws2tf options."""
        parser = argparse.ArgumentParser(
            prog='aws2tf',
            description='Import AWS infrastructure into Terraform with comprehensive workflow orchestration',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  aws2tf vpc vpc-12345                    # Import VPC and all dependencies
  aws2tf -t vpc -i vpc-12345              # Same as above (original syntax)
  aws2tf subnet subnet-67890 --dry-run   # Show what would be imported
  aws2tf -t ec2 -i i-abcdef --fast       # Fast mode EC2 import
  aws2tf vpc vpc-12345 -o networking     # Custom output folder
  aws2tf -t aws_s3 -i my-bucket --debug  # Debug mode S3 import
  aws2tf --list                          # List help information
  aws2tf --validate vpc vpc-12345        # Validate and exit
  
Original aws2tf Options:
  -t, --type      Resource type (aws_s3, ec2, aws_vpc, etc.)
  -i, --id        Resource ID
  -r, --region    AWS region
  -p, --profile   AWS profile
  -o, --output    Custom output folder prefix
  -m, --merge     Merge mode
  -d, --debug     Debug mode
  -s, --singlefile Single main.tf file
  -f, --fast      Fast multi-threaded mode
  -v, --validate  Validate and exit
  -a, --accept    Accept expected plan changes
  -e, --exclude   Exclude resource types
  -la, --serverless Lambda/serverless mode
  
Data Source Options:
  -dnet, --datanet  Data statements for VPC/subnet
  -dsgs, --datasgs  Data statements for security groups
  -dkms, --datakms  Data statements for KMS keys
  -dkey, --datakey  Data statements for key pairs
  
New Workflow Modes:
  --full          Complete workflow (default)
  --discovery     Only discover resources and dependencies
  --validate-only Only validate resource dependencies
  --import-only   Only import resources into terraform
  --generate-only Only generate terraform configuration files
  --dry-run       Show what would be done without executing
  
For more information, visit: https://github.com/aws-samples/aws2tf
            """
        )
        
        # Target resource arguments (compatible with original aws2tf)
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
        
        # Original aws2tf compatibility arguments
        parser.add_argument(
            '-t', '--type',
            help='Resource type (aws_s3, ec2, aws_vpc, etc.) - same as target_type'
        )
        
        parser.add_argument(
            '-i', '--id',
            help='Resource ID - same as target_id'
        )
        
        parser.add_argument(
            '-l', '--list',
            action='store_true',
            help='List extra help information'
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
            '--import-only',
            action='store_const',
            const=WorkflowMode.IMPORT_ONLY,
            dest='workflow_mode',
            help='Only import resources into terraform'
        )
        mode_group.add_argument(
            '--generate-only',
            action='store_const',
            const=WorkflowMode.GENERATE_ONLY,
            dest='workflow_mode',
            help='Only generate terraform configuration files'
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
            type=str,
            help='Add custom string to output folder (creates generated/tf-{output}-{account}-{region}/)'
        )
        
        parser.add_argument(
            '-r', '--region',
            help='AWS region (overrides profile/environment setting)'
        )
        
        parser.add_argument(
            '-p', '--profile',
            help='AWS profile to use'
        )
        
        parser.add_argument(
            '--account-id',
            help='AWS account ID (for validation)'
        )
        
        # Original aws2tf behavior flags
        parser.add_argument(
            '-m', '--merge',
            action='store_true',
            help='Merge mode'
        )
        
        parser.add_argument(
            '-d', '--debug',
            action='store_true',
            help='Enable debug output'
        )
        
        parser.add_argument(
            '-s', '--singlefile',
            action='store_true',
            help='Only a single file main.tf is produced'
        )
        
        parser.add_argument(
            '-f', '--fast',
            action='store_true',
            help='Fast multi-threaded mode'
        )
        
        parser.add_argument(
            '-v', '--validate',
            action='store_true',
            help='Validate and exit'
        )
        
        parser.add_argument(
            '-a', '--accept',
            action='store_true',
            help='Expected plan changes accepted'
        )
        
        parser.add_argument(
            '-e', '--exclude',
            help='Resource types to exclude'
        )
        
        parser.add_argument(
            '-ec2tag', '--ec2tag',
            help='EC2 key:value pair to import'
        )
        
        # Data source options
        parser.add_argument(
            '-dnet', '--datanet',
            action='store_true',
            help='Write data statements for aws_vpc, aws_subnet'
        )
        
        parser.add_argument(
            '-dsgs', '--datasgs',
            action='store_true',
            help='Write data statements for aws_security_groups'
        )
        
        parser.add_argument(
            '-dkms', '--datakms',
            action='store_true',
            help='Write data statements for aws_kms_key'
        )
        
        parser.add_argument(
            '-dkey', '--datakey',
            action='store_true',
            help='Write data statements for aws_key_pair'
        )
        
        # Advanced debugging and deployment options
        parser.add_argument(
            '-b3', '--boto3error',
            action='store_true',
            help='Exit on boto3 API error (for debugging)'
        )
        
        parser.add_argument(
            '-la', '--serverless',
            action='store_true',
            help='Lambda mode - when running in a Lambda container'
        )
        
        parser.add_argument(
            '-tv', '--tv',
            help='Specify version of Terraform AWS provider (default: 5.100.0)'
        )
        
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Enable verbose output'
        )
        
        parser.add_argument(
            '--quiet', '-q',
            action='store_true',
            help='Suppress non-essential output'
        )
        
        parser.add_argument(
            '--no-progress',
            action='store_true',
            help='Disable progress bar'
        )
        
        parser.add_argument(
            '--no-color',
            action='store_true',
            help='Disable colored output'
        )
        
        # Advanced options
        parser.add_argument(
            '--cores',
            type=int,
            help='Number of CPU cores to use for parallel processing'
        )
        
        parser.add_argument(
            '--timeout',
            type=int,
            default=3600,
            help='Workflow timeout in seconds (default: 3600)'
        )
        
        parser.add_argument(
            '--ignore-errors',
            action='store_true',
            help='Continue workflow even if non-critical errors occur'
        )
        
        parser.add_argument(
            '--backup',
            action='store_true',
            default=True,
            help='Create terraform state backup before import (default: true)'
        )
        
        parser.add_argument(
            '--no-backup',
            action='store_false',
            dest='backup',
            help='Skip terraform state backup'
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
    
    def _setup_output_directory(self, output_prefix: Optional[str] = None) -> Path:
        """Setup output directory using aws2tf convention: generated/tf-{prefix}-{account}-{region}/"""
        if not self.config:
            raise ValueError("Configuration must be setup before creating output directory")
        
        # Build directory name using aws2tf convention
        prefix_part = f"{output_prefix}-" if output_prefix else ""
        dir_name = f"tf-{prefix_part}{self.config.aws.account_id}-{self.config.aws.region}"
        
        # Use serverless path if in serverless mode
        if hasattr(self.config.runtime, 'serverless') and self.config.runtime.serverless:
            output_dir = Path(f"/tmp/aws2tf/generated/{dir_name}")
        else:
            output_dir = Path(f"generated/{dir_name}")
        
        # Create directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Also create imported subdirectory (aws2tf convention)
        imported_dir = output_dir / "imported"
        imported_dir.mkdir(exist_ok=True)
        
        return output_dir
    
    def setup_configuration(self, args: argparse.Namespace) -> ConfigurationManager:
        """Setup configuration from command-line arguments."""
        try:
            # Create base configuration
            if args.debug:
                config = create_test_config(debug=True)
            else:
                config = create_production_config()
            
            # Update configuration from arguments
            parse_and_update_config(config, args)
            
            # Validate argument combinations
            validation_errors = validate_argument_combinations(args)
            if validation_errors:
                for error in validation_errors:
                    self.print_error(f"Argument validation error: {error}")
                sys.exit(1)
            
            # Validate configuration
            config_errors = []
            config_errors.extend(config.aws.validate())
            config_errors.extend(config.runtime.validate())
            
            if config_errors:
                for error in config_errors:
                    self.print_error(f"Configuration error: {error}")
                sys.exit(1)
            
            return config
            
        except Exception as e:
            self.print_error(f"Configuration setup failed: {e}")
            sys.exit(1)
    
    def print_header(self, title: str):
        """Print a formatted header."""
        if not hasattr(self, '_no_color') or not self._no_color:
            print(f"\n{CLIColors.HEADER}{CLIColors.BOLD}{title}{CLIColors.ENDC}")
            print(f"{CLIColors.HEADER}{'=' * len(title)}{CLIColors.ENDC}")
        else:
            print(f"\n{title}")
            print("=" * len(title))
    
    def print_success(self, message: str):
        """Print a success message."""
        if not hasattr(self, '_no_color') or not self._no_color:
            print(f"{CLIColors.OKGREEN}✓{CLIColors.ENDC} {message}")
        else:
            print(f"✓ {message}")
    
    def print_warning(self, message: str):
        """Print a warning message."""
        if not hasattr(self, '_no_color') or not self._no_color:
            print(f"{CLIColors.WARNING}⚠{CLIColors.ENDC} {message}")
        else:
            print(f"⚠ {message}")
    
    def print_error(self, message: str):
        """Print an error message."""
        if not hasattr(self, '_no_color') or not self._no_color:
            print(f"{CLIColors.FAIL}✗{CLIColors.ENDC} {message}", file=sys.stderr)
        else:
            print(f"✗ {message}", file=sys.stderr)
    
    def print_info(self, message: str):
        """Print an info message."""
        if not hasattr(self, '_no_color') or not self._no_color:
            print(f"{CLIColors.OKBLUE}ℹ{CLIColors.ENDC} {message}")
        else:
            print(f"ℹ {message}")
    
    def progress_callback(self, message: str, progress: float):
        """Progress callback for workflow execution."""
        if not hasattr(self, '_no_progress') or not self._no_progress:
            self.progress_bar.update(message, progress)
    
    def status_callback(self, phase: WorkflowPhase, message: str):
        """Status callback for workflow execution."""
        if not hasattr(self, '_quiet') or not self._quiet:
            phase_name = phase.value.replace('_', ' ').title()
            if not hasattr(self, '_no_color') or not self._no_color:
                print(f"\n{CLIColors.OKCYAN}Phase:{CLIColors.ENDC} {phase_name} - {message}")
            else:
                print(f"\nPhase: {phase_name} - {message}")
    
    def list_supported_resources(self):
        """List supported AWS resource types."""
        self.print_header("Supported AWS Resource Types")
        
        # This would normally come from the resource discovery module
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
    
    def validate_configuration_only(self, config: ConfigurationManager):
        """Validate configuration and display results."""
        self.print_header("Configuration Validation")
        
        # AWS Configuration
        aws_errors = config.aws.validate()
        if aws_errors:
            self.print_error("AWS Configuration Issues:")
            for error in aws_errors:
                print(f"    - {error}")
        else:
            self.print_success("AWS configuration is valid")
            print(f"    Region: {config.aws.region}")
            print(f"    Account ID: {config.aws.account_id}")
            print(f"    Profile: {config.aws.profile}")
        
        # Runtime Configuration
        runtime_errors = config.runtime.validate()
        if runtime_errors:
            self.print_error("Runtime Configuration Issues:")
            for error in runtime_errors:
                print(f"    - {error}")
        else:
            self.print_success("Runtime configuration is valid")
        
        # Debug Configuration
        if config.debug.enabled:
            self.print_info("Debug mode is enabled")
        
        # Processing Configuration
        print(f"\nProcessing Configuration:")
        print(f"    CPU Cores: {config.processing.cores}")
        print(f"    Tracking: {config.processing.tracking_message}")
        
        total_errors = len(aws_errors) + len(runtime_errors)
        if total_errors == 0:
            self.print_success("All configuration validation passed")
            return True
        else:
            self.print_error(f"Configuration validation failed with {total_errors} errors")
            return False
    
    def _normalize_arguments(self, args: argparse.Namespace) -> argparse.Namespace:
        """Normalize arguments to handle both old (-t/-i) and new (positional) syntax."""
        # If -t/--type is used, copy to target_type
        if hasattr(args, 'type') and args.type and not args.target_type:
            args.target_type = args.type
        
        # If -i/--id is used, copy to target_id  
        if hasattr(args, 'id') and args.id and not args.target_id:
            args.target_id = args.id
            
        return args
    
    def execute_workflow(self, args: argparse.Namespace) -> int:
        """Execute the main aws2tf workflow."""
        try:
            # Normalize arguments to handle both old and new syntax
            args = self._normalize_arguments(args)
            
            # Setup configuration
            self.config = self.setup_configuration(args)
            
            # Store CLI options
            self._no_color = args.no_color
            self._no_progress = args.no_progress
            self._quiet = args.quiet
            self._verbose = args.verbose
            
            # Setup output directory using aws2tf convention
            output_dir = self._setup_output_directory(args.output)
            
            # Print workflow information
            if not args.quiet:
                self.print_header(f"AWS2TF Workflow Execution")
                print(f"Target Resource: {args.target_type}:{args.target_id}")
                print(f"Workflow Mode: {args.workflow_mode.value}")
                print(f"AWS Region: {self.config.aws.region}")
                print(f"AWS Account: {self.config.aws.account_id}")
                print(f"Output Directory: {output_dir}")
                if args.workflow_mode == WorkflowMode.DRY_RUN:
                    self.print_info("DRY RUN MODE - No changes will be made")
            
            # Create and configure workflow
            self.workflow = create_main_workflow(self.config)
            
            if not args.no_progress:
                self.workflow.add_progress_callback(self.progress_callback)
            
            if not args.quiet:
                self.workflow.add_status_callback(self.status_callback)
            
            # Execute workflow with timeout
            start_time = time.time()
            
            try:
                summary = self.workflow.execute_workflow(
                    target_type=args.target_type,
                    target_id=args.target_id,
                    mode=args.workflow_mode,
                    output_dir=output_dir
                )
            except KeyboardInterrupt:
                self.print_warning("Workflow interrupted by user")
                return 130  # Standard exit code for SIGINT
            
            execution_time = time.time() - start_time
            
            # Print results
            if not args.quiet:
                self.print_workflow_summary(summary, execution_time)
            
            # Return appropriate exit code
            if summary.result == WorkflowResult.SUCCESS:
                return 0
            elif summary.result == WorkflowResult.PARTIAL_SUCCESS:
                return 2
            elif summary.result == WorkflowResult.CANCELLED:
                return 130
            else:
                return 1
                
        except Exception as e:
            self.print_error(f"Workflow execution failed: {e}")
            if args.debug:
                import traceback
                print(traceback.format_exc())
            return 1
    
    def print_workflow_summary(self, summary, execution_time: float):
        """Print a comprehensive workflow summary."""
        self.print_header("Workflow Summary")
        
        # Overall result
        if summary.result == WorkflowResult.SUCCESS:
            self.print_success(f"Workflow completed successfully")
        elif summary.result == WorkflowResult.PARTIAL_SUCCESS:
            self.print_warning(f"Workflow completed with warnings")
        elif summary.result == WorkflowResult.CANCELLED:
            self.print_warning(f"Workflow was cancelled")
        else:
            self.print_error(f"Workflow failed")
        
        print(f"Phase Completed: {summary.phase_completed.value}")
        print(f"Execution Time: {execution_time:.2f}s")
        
        # Metrics
        print(f"\nMetrics:")
        print(f"  Resources Discovered: {summary.metrics.resources_discovered}")
        print(f"  Resources Validated: {summary.metrics.resources_validated}")
        print(f"  Resources Imported: {summary.metrics.resources_imported}")
        print(f"  Configs Generated: {summary.metrics.configs_generated}")
        
        # Issues
        if summary.errors:
            self.print_error(f"Errors ({len(summary.errors)}):")
            for error in summary.errors[:5]:  # Show first 5 errors
                print(f"    - {error}")
            if len(summary.errors) > 5:
                print(f"    ... and {len(summary.errors) - 5} more errors")
        
        if summary.warnings:
            self.print_warning(f"Warnings ({len(summary.warnings)}):")
            for warning in summary.warnings[:3]:  # Show first 3 warnings
                print(f"    - {warning}")
            if len(summary.warnings) > 3:
                print(f"    ... and {len(summary.warnings) - 3} more warnings")
        
        # Generated files
        if summary.generated_files:
            self.print_success(f"Generated Files ({len(summary.generated_files)}):")
            for file_path in summary.generated_files:
                print(f"    - {file_path}")
        
        # Next steps
        if summary.result == WorkflowResult.SUCCESS:
            print(f"\nNext Steps:")
            if summary.generated_files:
                print(f"  1. Review generated terraform files")
                print(f"  2. Run 'terraform plan' to verify configuration")
                print(f"  3. Run 'terraform apply' to manage infrastructure")
            else:
                print(f"  1. Check the terraform state for imported resources")
                print(f"  2. Generate terraform configuration files if needed")
    
    def run(self, argv: Optional[List[str]] = None) -> int:
        """Main entry point for the CLI interface."""
        try:
            # Parse arguments
            parser = self.create_argument_parser()
            args = parser.parse_args(argv)
            
            # Normalize arguments
            args = self._normalize_arguments(args)
            
            # Handle special commands
            if hasattr(args, 'list_resources') and args.list_resources:
                self.list_supported_resources()
                return 0
                
            if hasattr(args, 'list') and args.list:
                self.list_supported_resources()
                return 0
            
            if hasattr(args, 'validate_config') and args.validate_config:
                config = self.setup_configuration(args)
                success = self.validate_configuration_only(config)
                return 0 if success else 1
                
            if hasattr(args, 'validate') and args.validate:
                config = self.setup_configuration(args)
                success = self.validate_configuration_only(config)
                return 0 if success else 1
            
            # Validate required arguments
            if not args.target_type or not args.target_id:
                self.print_error("Both target_type and target_id are required")
                self.print_error("Use: aws2tf <resource_type> <resource_id> or aws2tf -t <type> -i <id>")
                parser.print_help()
                return 1
            
            # Execute main workflow
            return self.execute_workflow(args)
            
        except KeyboardInterrupt:
            print(f"\n{CLIColors.WARNING}Operation cancelled by user{CLIColors.ENDC}")
            return 130
        except Exception as e:
            self.print_error(f"CLI execution failed: {e}")
            return 1


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry point for aws2tf CLI."""
    cli = AWS2TFCLIInterface()
    return cli.run(argv)


if __name__ == '__main__':
    sys.exit(main())