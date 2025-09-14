#!/usr/bin/env python3
"""
New AWS2TF CLI Entry Point with Workflow Orchestrator.

This is the new main entry point for aws2tf that uses the workflow orchestrator
and comprehensive CLI interface we've built.
"""

import sys
import os
from pathlib import Path

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'code'))

# Import our CLI interface
try:
    from cli_interface import AWS2TFCLIInterface, main as cli_main
    USE_FULL_CLI = True
except ImportError:
    # Fallback to standalone demo
    from cli_standalone_demo import (
        create_cli_parser, print_success, print_error, print_header,
        simulate_workflow, list_supported_resources, validate_configuration,
        WorkflowMode
    )
    USE_FULL_CLI = False


def main():
    """Main entry point for the new aws2tf CLI."""
    if USE_FULL_CLI:
        # Use the full CLI interface
        return cli_main()
    
    # Fallback to standalone demo
    print_header("AWS2TF - Infrastructure Import Tool v2.0")
    print("Enhanced with Workflow Orchestrator and Configuration Management")
    
    try:
        # Create and parse arguments
        parser = create_cli_parser()
        args = parser.parse_args()
        
        # Handle special commands first
        if hasattr(args, 'list_resources') and args.list_resources:
            list_supported_resources()
            return 0
            
        if hasattr(args, 'list') and args.list:
            list_supported_resources()
            return 0
        
        if hasattr(args, 'validate_config') and args.validate_config:
            success = validate_configuration()
            return 0 if success else 1
            
        if hasattr(args, 'validate') and args.validate:
            success = validate_configuration()
            return 0 if success else 1
        
        # Validate required arguments
        if not args.target_type or not args.target_id:
            print_error("Both target_type and target_id are required")
            print_error("Use: aws2tf <resource_type> <resource_id> or aws2tf -t <type> -i <id>")
            parser.print_help()
            return 1
        
        # Display execution info
        print(f"\nTarget Resource: {args.target_type}:{args.target_id}")
        print(f"Workflow Mode: {args.workflow_mode.value}")
        
        if hasattr(args, 'region') and args.region:
            print(f"AWS Region: {args.region}")
        
        if hasattr(args, 'output') and args.output:
            print(f"Output Directory: {args.output}")
        
        if args.workflow_mode == WorkflowMode.DRY_RUN:
            print("🔍 DRY RUN MODE - No changes will be made")
        
        # Execute the workflow
        print()
        simulate_workflow(
            target_type=args.target_type,
            target_id=args.target_id,
            mode=args.workflow_mode,
            output_prefix=getattr(args, 'output', None)
        )
        
        # Success message
        print()
        print_success("AWS2TF execution completed successfully!")
        
        # Next steps
        print("\nNext Steps:")
        if args.workflow_mode == WorkflowMode.DRY_RUN:
            print("  1. Review the planned changes above")
            print("  2. Run without --dry-run to execute the import")
        elif args.workflow_mode == WorkflowMode.DISCOVERY_ONLY:
            print("  1. Review discovered resources")
            print("  2. Run with --validate-only to check dependencies")
            print("  3. Run full workflow to import resources")
        else:
            print("  1. Review generated terraform files")
            print("  2. Run 'terraform plan' to verify configuration")
            print("  3. Run 'terraform apply' to manage infrastructure")
        
        return 0
        
    except KeyboardInterrupt:
        print_error("\nOperation cancelled by user")
        return 130
    except Exception as e:
        print_error(f"AWS2TF execution failed: {e}")
        if hasattr(args, 'debug') and args.debug:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())