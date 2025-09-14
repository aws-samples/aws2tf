"""
Argument parser configuration for aws2tf.

This module provides functions to create and configure the argument parser
for aws2tf with all supported command-line arguments.
"""

import argparse
from typing import Optional
from .config_manager import ConfigurationManager


def create_argument_parser(config: Optional[ConfigurationManager] = None) -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for aws2tf.
    
    Args:
        config: Optional configuration manager to get default values from.
        
    Returns:
        Configured ArgumentParser instance.
    """
    # Get default values from config if provided
    default_tfver = config.aws.tf_version if config else "5.100.0"
    
    parser = argparse.ArgumentParser(
        description="aws2tf - Import AWS resources to Terraform",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  aws2tf.py -t aws_vpc -i vpc-12345678
  aws2tf.py -t ec2 -r us-west-2
  aws2tf.py -t s3 -p production
        """
    )
    
    # Core resource selection
    parser.add_argument(
        "-t", "--type", 
        help="Resource type (aws_s3, ec2, aws_vpc, etc.)"
    )
    parser.add_argument(
        "-i", "--id", 
        help="Resource ID to import"
    )
    
    # AWS configuration
    parser.add_argument(
        "-r", "--region", 
        help="AWS region to use"
    )
    parser.add_argument(
        "-p", "--profile", 
        help="AWS profile to use"
    )
    
    # Output configuration
    parser.add_argument(
        "-o", "--output", 
        help="Add custom string to output folder"
    )
    parser.add_argument(
        "-s", "--singlefile", 
        help="Only a single file main.tf is produced", 
        action='store_true'
    )
    
    # Processing modes
    parser.add_argument(
        "-m", "--merge", 
        help="Merge mode", 
        action='store_true'
    )
    parser.add_argument(
        "-f", "--fast", 
        help="Fast multi-threaded mode", 
        action='store_true'
    )
    parser.add_argument(
        "-la", "--serverless", 
        help="Lambda mode - when running in a Lambda container", 
        action='store_true'
    )
    
    # Debug and validation
    parser.add_argument(
        "-d", "--debug", 
        help="Enable debug mode", 
        action='store_true'
    )
    parser.add_argument(
        "-d5", "--debug5", 
        help="Enable debug5 special debug flag", 
        action='store_true'
    )
    parser.add_argument(
        "-v", "--validate", 
        help="Validate and exit", 
        action='store_true'
    )
    parser.add_argument(
        "-b3", "--boto3error", 
        help="Exit on boto3 API error (for debugging)", 
        action='store_true'
    )
    
    # Resource filtering
    parser.add_argument(
        "-e", "--exclude", 
        help="Resource types to exclude (comma-separated)"
    )
    parser.add_argument(
        "-ec2tag", "--ec2tag", 
        help="EC2 key:value pair to import"
    )
    
    # Data source flags
    parser.add_argument(
        "-dnet", "--datanet", 
        help="Write data statements for aws_vpc, aws_subnet", 
        action='store_true'
    )
    parser.add_argument(
        "-dsgs", "--datasgs", 
        help="Write data statements for aws_security_groups", 
        action='store_true'
    )
    parser.add_argument(
        "-dkms", "--datakms", 
        help="Write data statements for aws_kms_key", 
        action='store_true'
    )
    parser.add_argument(
        "-dkey", "--datakey", 
        help="Write data statements for aws_key_pair", 
        action='store_true'
    )
    
    # Terraform configuration
    parser.add_argument(
        "-tv", "--tv", 
        help=f"Specify version of Terraform AWS provider (default: {default_tfver})"
    )
    
    # Acceptance and help
    parser.add_argument(
        "-a", "--accept", 
        help="Expected plan changes accepted", 
        action='store_true'
    )
    parser.add_argument(
        "-l", "--list", 
        help="List extra help information", 
        action='store_true'
    )
    
    return parser


def parse_and_update_config(config: ConfigurationManager, args: Optional[list] = None) -> argparse.Namespace:
    """
    Parse command-line arguments and update configuration.
    
    Args:
        config: Configuration manager to update.
        args: Optional list of arguments to parse (defaults to sys.argv).
        
    Returns:
        Parsed arguments namespace.
        
    Raises:
        SystemExit: If argument parsing fails or help is requested.
    """
    parser = create_argument_parser(config)
    parsed_args = parser.parse_args(args)
    
    # Update configuration from parsed arguments
    config.update_from_args(parsed_args)
    
    return parsed_args


def validate_argument_combinations(args: argparse.Namespace) -> list[str]:
    """
    Validate argument combinations and return any errors.
    
    Args:
        args: Parsed arguments to validate.
        
    Returns:
        List of validation error messages.
    """
    errors = []
    
    # Check for conflicting debug and fast modes
    if args.debug and args.fast:
        errors.append("Debug mode and fast mode cannot both be enabled")
    
    if args.debug5 and args.fast:
        errors.append("Debug5 mode and fast mode cannot both be enabled")
    
    # Check EC2 tag format
    if args.ec2tag and ":" not in args.ec2tag:
        errors.append("EC2 tag must be in format 'key:value'")
    
    # Check that type is provided for targeted operations
    if args.id and not args.type:
        errors.append("Resource type (-t/--type) must be specified when using resource ID (-i/--id)")
    
    return errors


def get_argument_summary(args: argparse.Namespace) -> dict:
    """
    Get a summary of parsed arguments for logging/debugging.
    
    Args:
        args: Parsed arguments.
        
    Returns:
        Dictionary containing argument summary.
    """
    summary = {}
    
    # Core arguments
    if args.type:
        summary['resource_type'] = args.type
    if args.id:
        summary['resource_id'] = args.id
    if args.region:
        summary['region'] = args.region
    if args.profile:
        summary['profile'] = args.profile
    
    # Modes
    modes = []
    if args.fast:
        modes.append('fast')
    if args.debug:
        modes.append('debug')
    if args.debug5:
        modes.append('debug5')
    if args.merge:
        modes.append('merge')
    if args.serverless:
        modes.append('serverless')
    if args.validate:
        modes.append('validate')
    
    if modes:
        summary['modes'] = modes
    
    # Data source flags
    data_sources = []
    if args.datanet:
        data_sources.append('net')
    if args.datasgs:
        data_sources.append('sgs')
    if args.datakms:
        data_sources.append('kms')
    if args.datakey:
        data_sources.append('key')
    
    if data_sources:
        summary['data_sources'] = data_sources
    
    # Filtering
    if args.exclude:
        summary['exclude'] = args.exclude
    if args.ec2tag:
        summary['ec2_tag'] = args.ec2tag
    
    return summary