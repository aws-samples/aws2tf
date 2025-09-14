#!/usr/bin/env python3

import boto3
import signal
import argparse
import glob
import os
import sys
import shutil
import datetime
import concurrent.futures
from typing import List, Dict
import io
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, './code')

# Import the new configuration system
from code.config import (
    ConfigurationManager,
    create_argument_parser,
    parse_and_update_config,
    validate_argument_combinations,
    configure_aws_credentials,
    validate_aws_credentials,
    print_credentials_info
)

# Import existing modules (these will be migrated in later tasks)
import common
import resources
import globals  # Will be removed in later tasks
import timed_interrupt
import stacks
from fixtf_aws_resources import aws_dict
from build_lists import build_lists, build_secondary_lists


def extra_help():
    """Display extra help information about supported resource types."""
    print("\nExtra help\n")
    print("Type codes supported - ./aws2tf.py -t [type code]:\n")
    with open('code/resources.py', 'r') as f:
        for line in f.readlines():
            line3 = ""
            if "#" in line:
                line3 = line.split("#")[1].strip()
            line = line.strip().split(":")[0]
            if "type ==" in line and "aws_" not in line:
                line = line.split("==")[-1].strip().strip("'").strip('"')
                if line3 != "":
                    if len(line) < 3:
                        print("./aws2tf.py  -t " + line + "     \t\t\t" + str(line3))
                    elif len(line) > 10:
                        print("./aws2tf.py  -t " + line + "     \t" + str(line3))
                    else:
                        print("./aws2tf.py  -t " + line + "     \t\t" + str(line3))
                else:
                    print("./aws2tf.py  -t " + line)
    print("\nOr instead of the above type codes use the terraform type eg:\n\n./aws2tf.py -t aws_vpc\n")
    print("\nTo get a deployed stack set:\n\n./aws2tf.py -t stack -i stackname\n")
    print("exit 001")


def check_terraform_version(config: ConfigurationManager) -> str:
    """
    Check Terraform version and validate it meets requirements.
    
    Args:
        config: Configuration manager instance.
        
    Returns:
        Terraform version string.
        
    Raises:
        SystemExit: If Terraform is not found or version is too old.
    """
    # Check if terraform is available
    path = shutil.which("terraform")
    if path is None:
        print("no executable found for command 'terraform'")
        print("exit 002")
        timed_interrupt.timed_int.stop()
        exit()
    
    # Get terraform version
    com = "terraform version"
    rout = common.rc(com)
    tvr = rout.stdout.decode().rstrip()
    
    if "." not in tvr:
        print("Unexpected Terraform version " + str(tvr))
        timed_interrupt.timed_int.stop()
        os._exit(1)
    
    tv = str(rout.stdout.decode().rstrip()).split("rm v")[-1].split("\n")[0]
    tvmaj = int(tv.split(".")[0])
    tvmin = int(tv.split(".")[1])
    
    if tvmaj < 1:
        print("Terraform version is too old - please upgrade to v1.9.5 or later " + str(tv))
        timed_interrupt.timed_int.stop()
        os._exit(1)
    
    if tvmaj == 1 and tvmin < 8:
        print("Terraform version is too old - please upgrade to v1.9.5 or later " + str(tv))
        timed_interrupt.timed_int.stop()
        os._exit(1)
    
    print("Terraform version:", tv, "AWS provider version:", config.aws.tf_version)
    return tv


def setup_aws_credentials(config: ConfigurationManager) -> None:
    """
    Set up and validate AWS credentials.
    
    Args:
        config: Configuration manager instance.
        
    Raises:
        SystemExit: If credentials cannot be configured or are invalid.
    """
    # Configure AWS credentials
    if not configure_aws_credentials(config):
        print("Could not find valid AWS credentials")
        print_credentials_info(config)
        timed_interrupt.timed_int.stop()
        exit()
    
    # Print credential information
    print("Credentials Type =", config.aws.credential_type)
    print("Is SSO login =", config.aws.is_sso)
    
    # Validate credentials
    validation = validate_aws_credentials(config)
    if not validation['valid']:
        print("AWS credentials validation failed:")
        for error in validation['errors']:
            print(f"  - {error}")
        timed_interrupt.timed_int.stop()
        exit()


def process_resource_types(config: ConfigurationManager, args: argparse.Namespace) -> str:
    """
    Process and validate resource type arguments.
    
    Args:
        config: Configuration manager instance.
        args: Parsed command-line arguments.
        
    Returns:
        Processed resource type.
        
    Raises:
        SystemExit: If required arguments are missing in serverless mode.
    """
    if args.type is None or args.type == "":
        if config.runtime.serverless:
            print("type is required eg:  -t aws_vpc  when in serverless mode, exiting ....")
            print("exit 003")
            timed_interrupt.timed_int.stop()
            exit()
        print("type is recommended eg:  -t aws_vpc    \nsetting to all")
        return "all"
    else:
        return args.type


def setup_exclusion_list(config: ConfigurationManager, args: argparse.Namespace) -> None:
    """
    Set up resource exclusion list from arguments.
    
    Args:
        config: Configuration manager instance.
        args: Parsed command-line arguments.
    """
    if args.exclude is not None:
        extypes = args.exclude
        if "," in extypes:
            extypes = extypes.split(",")
        else:
            extypes = [extypes]
        
        config.runtime.all_extypes = []
        for i in extypes:
            config.runtime.all_extypes = config.runtime.all_extypes + resources.resource_types(i)
    else:
        config.runtime.all_extypes = []


def setup_region(config: ConfigurationManager, args: argparse.Namespace) -> None:
    """
    Set up AWS region from arguments or environment.
    
    Args:
        config: Configuration manager instance.
        args: Parsed command-line arguments.
        
    Raises:
        SystemExit: If region cannot be determined.
    """
    if args.region is None:
        # Try to get region from AWS CLI configuration
        com = "aws configure get region"
        rout = common.rc(com)
        el = len(rout.stderr.decode().rstrip())
        
        if el != 0:
            # AWS CLI failed, try environment variables
            region = os.getenv("AWS_REGION")
            if region is None:
                region = os.getenv("AWS_DEFAULT_REGION")
                if region is None:
                    print("region is required eg:  -r eu-west-1  [using eu-west-1 as default]")
                    region = "eu-west-1"
                else:
                    print("region set from environment variables as " + region)
            else:
                print("region set from environment variables as " + region)
        else:
            region = rout.stdout.decode().rstrip()
            if len(region) == 0:
                # Try environment variables
                region = os.getenv("AWS_REGION")
                if region is None:
                    region = os.getenv("AWS_DEFAULT_REGION")
                    if region is None:
                        print("region is required - set in AWS cli or pass with -r")
                        print("exit 004")
                        timed_interrupt.timed_int.stop()
                        exit()
                print("region set from environment variables as " + region)
            else:
                print("region set from aws cli / environment variables as " + region)
    else:
        region = args.region
    
    config.aws.region = region


def sync_with_globals(config: ConfigurationManager) -> None:
    """
    Synchronize configuration with globals for backward compatibility.
    
    This is a temporary function that will be removed once all modules
    are migrated to use the configuration system.
    
    Args:
        config: Configuration manager instance.
    """
    # AWS configuration
    globals.profile = config.aws.profile
    globals.region = config.aws.region
    globals.regionl = len(config.aws.region)
    globals.acc = config.aws.account_id
    globals.credtype = config.aws.credential_type
    globals.sso = config.aws.is_sso
    globals.tfver = config.aws.tf_version
    
    # Debug configuration
    globals.debug = config.debug.enabled
    globals.debug5 = config.debug.debug5
    globals.validate = config.debug.validate_mode
    globals.fast = config.runtime.fast
    
    # Runtime configuration
    globals.merge = config.runtime.merge
    globals.expected = config.runtime.expected
    globals.serverless = config.runtime.serverless
    globals.all_extypes = config.runtime.all_extypes
    
    # Data source flags
    globals.dnet = config.runtime.dnet
    globals.dsgs = config.runtime.dsgs
    globals.dkms = config.runtime.dkms
    globals.dkey = config.runtime.dkey
    
    # EC2 tag configuration
    globals.ec2tag = config.runtime.ec2tag
    globals.ec2tagk = config.runtime.ec2tagk
    globals.ec2tagv = config.runtime.ec2tagv
    
    # Processing configuration
    globals.cores = config.processing.cores
    globals.tracking_message = config.processing.tracking_message
    globals.esttime = config.processing.estimated_time


def setup_directories(config: ConfigurationManager) -> None:
    """
    Set up working directories for Terraform files.
    
    Args:
        config: Configuration manager instance.
    """
    # Create necessary directories
    com = f"mkdir -p {config.runtime.path2}"
    common.rc(com)
    
    com = f"mkdir -p {config.runtime.path3}"
    common.rc(com)
    
    # Change to working directory
    config.runtime.cwd = os.getcwd()
    os.chdir(config.runtime.path1)


def handle_merge_mode(config: ConfigurationManager) -> None:
    """
    Handle merge mode setup and validation.
    
    Args:
        config: Configuration manager instance.
    """
    if config.runtime.serverless:
        if config.runtime.merge:
            common.download_from_s3()
        else:
            common.empty_and_delete_bucket()
    
    # Check for existing terraform.tfstate file
    tfstate_path = f"{config.runtime.path1}/terraform.tfstate"
    if not os.path.isfile(tfstate_path) and config.runtime.merge:
        print(f"No terraform.tfstate file found in {config.runtime.path1} - can not merge")
        config.runtime.merge = False
        com = f"rm -rf {config.runtime.path1}"
        common.rc(com)
        if config.runtime.serverless:
            common.empty_and_delete_bucket()
    
    if not config.runtime.merge:
        com = f"rm -rf {config.runtime.path1}"
        common.rc(com)
        if config.runtime.serverless:
            common.empty_and_delete_bucket()


def initialize_terraform(config: ConfigurationManager, args: argparse.Namespace) -> None:
    """
    Initialize Terraform in the working directory.
    
    Args:
        config: Configuration manager instance.
        args: Parsed command-line arguments.
        
    Raises:
        SystemExit: If Terraform initialization fails.
    """
    config.set_tracking_message("Stage 1 of 10, Terraform Initialise ...")
    common.aws_tf(config.aws.region, args)
    
    # Verify Terraform initialization
    foundtf = False
    for root, dirs, files in os.walk(f"{config.runtime.cwd}/{config.runtime.path1}"):
        if '.terraform' in dirs:
            print("PASSED: Terraform Initialise OK")
            foundtf = True
            break
    
    if not foundtf:
        print(f"failed to find .terraform in {config.runtime.cwd}/{config.runtime.path1}")
        print("Terraform Initialise may have failed exiting ...")
        timed_interrupt.timed_int.stop()
        exit()


def handle_merge_processing(config: ConfigurationManager) -> None:
    """
    Handle merge mode processing setup.
    
    Args:
        config: Configuration manager instance.
    """
    if config.runtime.merge:
        print(f"Merging {config.runtime.merge}")
        
        try:
            with open('pyprocessed.txt', 'r') as file:
                content = file.readlines()
            
            for line in content:
                line = line.strip()
                config.processing.rproc[line] = True
            
            if config.is_debug_enabled():
                print("Pre Processed:")
                print(str(config.processing.rproc))
            
            com = "rm -f main.tf"
            common.rc(com)
            com = "cp imported/*.tf ."
            common.rc(com)
        
        except FileNotFoundError:
            print("Could not find pyprocessed.txt")
        except IOError as e:
            print(f"IO error occurred: {str(e)}")


def build_resource_lists(config: ConfigurationManager) -> None:
    """
    Build lists of AWS resources.
    
    Args:
        config: Configuration manager instance.
    """
    st1 = datetime.datetime.now()
    print(f"build lists started at {st1}")
    
    config.set_tracking_message("Stage 2 of 10, Building resource lists ...")
    
    # Call the existing build_lists function
    # TODO: This will be migrated to use config in a later task
    build_lists()
    
    now = datetime.datetime.now()
    print(f"build lists finished at {now}")
    print(f"build lists took {now - st1}")


def process_resource_types_execution(config: ConfigurationManager, resource_type: str, resource_id: str) -> None:
    """
    Process the specified resource types for execution.
    
    Args:
        config: Configuration manager instance.
        resource_type: Type of resource to process.
        resource_id: ID of specific resource (if any).
        
    Raises:
        SystemExit: If invalid combinations are detected.
    """
    config.set_tracking_message("Stage 3 of 10 getting resources ...")
    
    if resource_type == "" or resource_type is None:
        resource_type = "all"
    
    print(f"---<><> {resource_type}, Id={resource_id}, exclude={config.runtime.all_extypes}")
    
    # Handle multiple types
    if "," in resource_type:
        if "stack" in resource_type:
            print("Cannot mix stack with other types")
            print("exit 006")
            timed_interrupt.timed_int.stop()
            exit()
        
        if resource_id is not None:
            print("Cannot pass id with multiple types")
            print("exit 007")
            timed_interrupt.timed_int.stop()
            exit()
        
        types = resource_type.split(",")
        all_types = []
        for type1 in types:
            all_types = all_types + resources.resource_types(type1)
        
        for type2 in all_types:
            if type2 in aws_dict.aws_resources:
                if type2 in config.runtime.all_extypes:
                    print("Excluding", type2)
                    continue
                # TODO: This will be migrated to use config in a later task
                common.call_resource(type2, resource_id)
            else:
                print("Resource", type2, " not found in aws_dict")
    
    else:
        if resource_type == "all" and resource_id is not None:
            print("Cannot pass an id (-i) with all types")
            print("exit 007")
            timed_interrupt.timed_int.stop()
            exit()
        
        all_types = resources.resource_types(resource_type)
        
        for type2 in all_types:
            if type2 in aws_dict.aws_resources:
                if type2 in config.runtime.all_extypes:
                    print("Excluding", type2)
                    continue
                # TODO: This will be migrated to use config in a later task
                common.call_resource(type2, resource_id)
            else:
                print("Resource", type2, " not found in aws_dict")


def execute_main_processing(config: ConfigurationManager, args: argparse.Namespace, resource_type: str) -> None:
    """
    Execute the main aws2tf processing workflow with dependency injection.
    
    Args:
        config: Configuration manager instance.
        args: Parsed command-line arguments.
        resource_type: Type of resource to process.
    """
    try:
        # Set up AWS session
        session = config.get_aws_session()
        
        if config.is_debug_enabled():
            print(f"setting session region={config.aws.region}")
        
        # Set up boto3 default session for backward compatibility
        # TODO: Remove this once all modules use the config system
        if config.aws.profile == "default":
            boto3.setup_default_session(region_name=config.aws.region)
        else:
            boto3.setup_default_session(
                region_name=config.aws.region,
                profile_name=config.aws.profile
            )
        
        # Handle merge mode setup
        handle_merge_mode(config)
        
        # Set up directories
        setup_directories(config)
        
        # Initialize Terraform
        initialize_terraform(config, args)
        
        # Handle merge processing
        handle_merge_processing(config)
        
        # Build resource lists
        build_resource_lists(config)
        
        # Process resources
        process_resource_types_execution(config, resource_type, args.id)
        
        print("Main processing completed successfully!")
        
    except Exception as e:
        print(f"Error during main processing: {str(e)}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        timed_interrupt.timed_int.stop()
        raise


def main():
    """Main entry point for aws2tf."""
    
    # Initialize configuration manager
    config = ConfigurationManager()
    
    # Print startup message
    now = datetime.datetime.now()
    print("aws2tf " + config.aws.version + " started at %s" % now)
    starttime = now
    
    # Handle help request early
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            timed_interrupt.timed_int.stop()
    
    # Set up signal handler
    signal.signal(signal.SIGINT, common.ctrl_c_handler)
    
    # Check Python version
    common.check_python_version()
    
    try:
        # Parse command-line arguments and update configuration
        parser = create_argument_parser(config)
        args = parser.parse_args()
        
        # Handle list help
        if args.list:
            extra_help()
        
        # Validate argument combinations
        validation_errors = validate_argument_combinations(args)
        if validation_errors:
            print("Argument validation errors:")
            for error in validation_errors:
                print(f"  - {error}")
            print("exit 005")
            timed_interrupt.timed_int.stop()
            exit()
        
        # Update configuration from arguments
        config.update_from_args(args)
        
        # Check Terraform version
        terraform_version = check_terraform_version(config)
        
        # Set up AWS credentials and validate them
        setup_aws_credentials(config)
        
        # Process resource types
        resource_type = process_resource_types(config, args)
        
        # Set up exclusion list
        setup_exclusion_list(config, args)
        
        # Set up region
        setup_region(config, args)
        
        # Set up processing paths
        config.setup_paths()
        
        # Validate final configuration
        config_errors = config.validate_all()
        if config_errors:
            print("Configuration validation errors:")
            for error in config_errors:
                print(f"  - {error}")
            timed_interrupt.timed_int.stop()
            exit()
        
        # Synchronize with globals for backward compatibility
        # TODO: Remove this once all modules are migrated
        sync_with_globals(config)
        
        # Print configuration summary if debug is enabled
        if config.is_debug_enabled():
            from code.config.utilities import get_config_summary
            summary = get_config_summary(config)
            print("Configuration Summary:")
            print(f"  AWS: {summary['aws']}")
            print(f"  Debug: {summary['debug']}")
            print(f"  Runtime: {summary['runtime']}")
        
        print('Using region: ' + config.aws.region + 
              ' account: ' + config.aws.account_id + 
              " profile: " + config.aws.profile + "\n")
        
        # Start processing timer
        config.start_processing()
        
        # Continue with main execution flow using dependency injection
        execute_main_processing(config, args, resource_type)
        
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        timed_interrupt.timed_int.stop()
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()
        timed_interrupt.timed_int.stop()
        sys.exit(1)


if __name__ == "__main__":
    main()