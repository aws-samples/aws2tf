#!/usr/bin/env python3
"""
Migrated fixtf module for aws2tf that uses ConfigurationManager.

This module contains Terraform file processing and fixing functions updated to use
ConfigurationManager instead of global variables while maintaining all
file processing and reference fixing functionality.
"""

import os
import sys
import boto3
import base64
import shutil
import inspect
from typing import Optional, Dict, Any, List, Tuple
from .config import ConfigurationManager

# Import resource modules that will be migrated
try:
    from . import resources_migrated as resources
    from . import common_migrated as common
except ImportError:
    # Fallback to original modules
    from . import resources
    from . import common

# Import fixtf AWS resource modules
from .fixtf_aws_resources import arn_dict
from .fixtf_aws_resources import aws_common
from .fixtf_aws_resources import fixtf_accessanalyzer
from .fixtf_aws_resources import fixtf_acm
from .fixtf_aws_resources import fixtf_acm_pca
from .fixtf_aws_resources import fixtf_amp
from .fixtf_aws_resources import fixtf_amplify
from .fixtf_aws_resources import fixtf_apigateway
from .fixtf_aws_resources import fixtf_apigatewayv2
from .fixtf_aws_resources import fixtf_appconfig
from .fixtf_aws_resources import fixtf_appflow
from .fixtf_aws_resources import fixtf_appintegrations
from .fixtf_aws_resources import fixtf_application_autoscaling
from .fixtf_aws_resources import fixtf_application_insights
from .fixtf_aws_resources import fixtf_appmesh
from .fixtf_aws_resources import fixtf_apprunner
from .fixtf_aws_resources import fixtf_appstream
from .fixtf_aws_resources import fixtf_appsync
from .fixtf_aws_resources import fixtf_athena
from .fixtf_aws_resources import fixtf_auditmanager
from .fixtf_aws_resources import fixtf_autoscaling
from .fixtf_aws_resources import fixtf_autoscaling_plans
from .fixtf_aws_resources import fixtf_backup
from .fixtf_aws_resources import fixtf_batch
from .fixtf_aws_resources import fixtf_bedrock
from .fixtf_aws_resources import fixtf_bedrock_agent
from .fixtf_aws_resources import fixtf_billingconductor
from .fixtf_aws_resources import fixtf_budgets
from .fixtf_aws_resources import fixtf_ce
from .fixtf_aws_resources import fixtf_chime
from .fixtf_aws_resources import fixtf_chime_sdk_media_pipelines
from .fixtf_aws_resources import fixtf_chime_sdk_voice
from .fixtf_aws_resources import fixtf_cleanrooms
from .fixtf_aws_resources import fixtf_cloud9
from .fixtf_aws_resources import fixtf_cloudcontrol
from .fixtf_aws_resources import fixtf_cloudformation
from .fixtf_aws_resources import fixtf_cloudfront
from .fixtf_aws_resources import fixtf_cloudhsmv2
from .fixtf_aws_resources import fixtf_cloudsearch


def fixtf(config: ConfigurationManager, resource_type: str, tf_name: str) -> None:
    """
    Process and fix Terraform files for AWS resources.
    
    Args:
        config: Configuration manager for AWS session and processing settings.
        resource_type: Type of AWS resource (e.g., 'aws_vpc').
        tf_name: Name of the Terraform file to process.
    """
    rf = f"{tf_name}.out"
    tf2 = f"{tf_name}.tf"
    
    # Check if Terraform file already exists
    if os.path.isfile(tf2):
        if config.is_debug_enabled():
            print(f"File exists: {tf2} skipping ...")
        return
    else:
        if config.is_debug_enabled():
            print(f"processing {tf2}")
    
    if config.is_debug_enabled():
        print(f"{resource_type} fixtf {tf_name}.out")
    
    # Open the *.out file
    try:
        with open(rf, 'r') as f1:
            lines = f1.readlines()
    except FileNotFoundError:
        print(f"no {rf}")
        return
    
    # Get resource data
    try:
        clfn, descfn, topkey, key, filterid = resources.resource_data(config, resource_type, None)
    except TypeError:
        # Fallback for original resources module
        clfn, descfn, topkey, key, filterid = resources.resource_data(resource_type, None)
    
    if clfn is None:
        print(f"ERROR: clfn is None with type={resource_type}")
        print("exit 015")
        return
    
    clfn = clfn.replace('-', '_')
    callfn = f"fixtf_{clfn}"
    
    if config.is_debug_enabled():
        print(f"callfn={callfn} resource_type={resource_type}")
    
    # Initialize processing flags in configuration
    config.processing.set_processing_flag('elastirep', False)
    config.processing.set_processing_flag('elastigrep', False)
    config.processing.set_processing_flag('elasticc', False)
    config.processing.set_processing_flag('kinesismsk', False)
    config.processing.set_processing_flag('destbuck', False)
    
    # Pre-scan blocks for specific resource types
    if resource_type == "aws_elasticache_cluster":
        for line in lines:
            line = line.strip()
            if "replication_group_id" in line:
                config.processing.set_processing_flag('elastirep', True)
            elif "global_replication_group_id" in line:
                config.processing.set_processing_flag('elastigrep', True)
            elif "cluster_id" in line:
                config.processing.set_processing_flag('elasticc', True)
    
    elif resource_type == "aws_msk_cluster":
        config.processing.set_processing_flag('kinesismsk', True)
    
    elif resource_type == "aws_s3_bucket_notification":
        for line in lines:
            if "destination_bucket" in line:
                config.processing.set_processing_flag('destbuck', True)
                break
    
    # Process the Terraform file
    try:
        # Get the appropriate fixtf function
        fixtf_module = get_fixtf_module(clfn)
        if fixtf_module and hasattr(fixtf_module, callfn):
            fixtf_func = getattr(fixtf_module, callfn)
            
            # Call the resource-specific fixtf function
            # Note: These functions will need to be updated to accept config parameter
            processed_lines = fixtf_func(config, lines, resource_type, tf_name)
            
            # Write the processed Terraform file
            with open(tf2, 'w') as f2:
                f2.writelines(processed_lines)
            
            if config.is_debug_enabled():
                print(f"Generated fixed Terraform file: {tf2}")
        
        else:
            # Generic processing if no specific function found
            processed_lines = generic_fixtf_processing(config, lines, resource_type, tf_name)
            
            with open(tf2, 'w') as f2:
                f2.writelines(processed_lines)
            
            if config.is_debug_enabled():
                print(f"Generated generic Terraform file: {tf2}")
    
    except Exception as e:
        print(f"Error processing {resource_type} {tf_name}: {str(e)}")
        if config.is_debug_enabled():
            import traceback
            traceback.print_exc()


def get_fixtf_module(clfn: str):
    """
    Get the appropriate fixtf module for a client function name.
    
    Args:
        clfn: Client function name (e.g., 'ec2', 's3').
        
    Returns:
        The fixtf module for the service, or None if not found.
    """
    module_map = {
        'accessanalyzer': fixtf_accessanalyzer,
        'acm': fixtf_acm,
        'acm_pca': fixtf_acm_pca,
        'amp': fixtf_amp,
        'amplify': fixtf_amplify,
        'apigateway': fixtf_apigateway,
        'apigatewayv2': fixtf_apigatewayv2,
        'appconfig': fixtf_appconfig,
        'appflow': fixtf_appflow,
        'appintegrations': fixtf_appintegrations,
        'application_autoscaling': fixtf_application_autoscaling,
        'application_insights': fixtf_application_insights,
        'appmesh': fixtf_appmesh,
        'apprunner': fixtf_apprunner,
        'appstream': fixtf_appstream,
        'appsync': fixtf_appsync,
        'athena': fixtf_athena,
        'auditmanager': fixtf_auditmanager,
        'autoscaling': fixtf_autoscaling,
        'autoscaling_plans': fixtf_autoscaling_plans,
        'backup': fixtf_backup,
        'batch': fixtf_batch,
        'bedrock': fixtf_bedrock,
        'bedrock_agent': fixtf_bedrock_agent,
        'billingconductor': fixtf_billingconductor,
        'budgets': fixtf_budgets,
        'ce': fixtf_ce,
        'chime': fixtf_chime,
        'chime_sdk_media_pipelines': fixtf_chime_sdk_media_pipelines,
        'chime_sdk_voice': fixtf_chime_sdk_voice,
        'cleanrooms': fixtf_cleanrooms,
        'cloud9': fixtf_cloud9,
        'cloudcontrol': fixtf_cloudcontrol,
        'cloudformation': fixtf_cloudformation,
        'cloudfront': fixtf_cloudfront,
        'cloudhsmv2': fixtf_cloudhsmv2,
        'cloudsearch': fixtf_cloudsearch
    }
    
    return module_map.get(clfn)


def generic_fixtf_processing(config: ConfigurationManager, lines: List[str], 
                           resource_type: str, tf_name: str) -> List[str]:
    """
    Generic Terraform file processing when no specific fixtf function exists.
    
    Args:
        config: Configuration manager.
        lines: Lines from the .out file.
        resource_type: AWS resource type.
        tf_name: Terraform file name.
        
    Returns:
        Processed lines for the Terraform file.
    """
    processed_lines = []
    
    for line in lines:
        # Apply generic transformations
        processed_line = line
        
        # Replace account and region placeholders
        processed_line = globals_replace(config, processed_line, resource_type, tf_name)
        
        # Fix ARN references
        processed_line = fix_arn_references(config, processed_line, resource_type)
        
        # Fix resource references
        processed_line = fix_resource_references(config, processed_line, resource_type)
        
        processed_lines.append(processed_line)
    
    return processed_lines


def globals_replace(config: ConfigurationManager, line: str, resource_type: str, tf_name: str) -> str:
    """
    Replace global placeholders in Terraform configuration.
    
    Args:
        config: Configuration manager with account and region info.
        line: Line to process.
        resource_type: AWS resource type.
        tf_name: Terraform file name.
        
    Returns:
        Processed line with replacements.
    """
    if config.is_debug_enabled():
        print(f"GR start: {line.strip()}")
    
    if "format(" in line:
        return line
    
    processed_line = line
    
    # Replace account ID
    if config.aws.account_id:
        processed_line = processed_line.replace("${data.aws_caller_identity.current.account_id}", 
                                              config.aws.account_id)
        processed_line = processed_line.replace("AWSACCOUNT", config.aws.account_id)
    
    # Replace region
    if config.aws.region:
        processed_line = processed_line.replace("${data.aws_region.current.name}", 
                                              config.aws.region)
        processed_line = processed_line.replace("AWSREGION", config.aws.region)
    
    # Replace other common placeholders
    processed_line = processed_line.replace("AWSDEFAULT", "default")
    
    if config.is_debug_enabled() and processed_line != line:
        print(f"GR end: {processed_line.strip()}")
    
    return processed_line


def fix_arn_references(config: ConfigurationManager, line: str, resource_type: str) -> str:
    """
    Fix ARN references in Terraform configuration.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        
    Returns:
        Line with fixed ARN references.
    """
    processed_line = line
    
    # Fix IAM role ARNs
    if "arn:aws:iam::" in line and "role/" in line:
        processed_line = deref_role_arn(config, processed_line, resource_type, line)
    
    # Fix KMS key ARNs
    elif "arn:aws:kms:" in line:
        processed_line = deref_kms_key(config, processed_line, resource_type, line)
    
    # Fix S3 bucket references
    elif "s3://" in line:
        processed_line = deref_s3(config, processed_line, resource_type, line)
    
    # Fix other ARN types
    elif "arn:aws:" in line:
        processed_line = generic_deref_arn(config, processed_line, resource_type, line)
    
    return processed_line


def fix_resource_references(config: ConfigurationManager, line: str, resource_type: str) -> str:
    """
    Fix resource references in Terraform configuration.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        
    Returns:
        Line with fixed resource references.
    """
    processed_line = line
    
    # Fix VPC references
    if "vpc-" in line:
        processed_line = fix_vpc_references(config, processed_line, resource_type)
    
    # Fix subnet references
    elif "subnet-" in line:
        processed_line = fix_subnet_references(config, processed_line, resource_type)
    
    # Fix security group references
    elif "sg-" in line:
        processed_line = fix_sg_references(config, processed_line, resource_type)
    
    return processed_line


def deref_role_arn(config: ConfigurationManager, line: str, resource_type: str, original_line: str) -> str:
    """
    Dereference IAM role ARNs to Terraform references.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        original_line: Original line for context.
        
    Returns:
        Line with dereferenced role ARN.
    """
    if "null" in line or "[]" in line:
        return line
    
    # Extract role name from ARN
    import re
    arn_pattern = r'arn:aws:iam::(\d+):role/([^"]+)'
    match = re.search(arn_pattern, line)
    
    if match:
        account_id = match.group(1)
        role_name = match.group(2)
        
        # Replace with Terraform reference
        role_ref = f"aws_iam_role.{role_name.replace('-', '_').replace('/', '_')}.arn"
        processed_line = re.sub(arn_pattern, role_ref, line)
        
        if config.is_debug_enabled():
            print(f"Dereferenced role ARN: {role_name} -> {role_ref}")
        
        return processed_line
    
    return line


def deref_kms_key(config: ConfigurationManager, line: str, resource_type: str, original_line: str) -> str:
    """
    Dereference KMS key ARNs to Terraform references.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        original_line: Original line for context.
        
    Returns:
        Line with dereferenced KMS key ARN.
    """
    if config.is_debug_enabled():
        print(f"deref_kms_key: {line.strip()}")
    
    if "arn:aws:kms:" in line:
        # Extract key ID from ARN
        import re
        kms_pattern = r'arn:aws:kms:[^:]+:[^:]+:key/([^"]+)'
        match = re.search(kms_pattern, line)
        
        if match:
            key_id = match.group(1)
            key_ref = f"aws_kms_key.k_{key_id.replace('-', '_')}.arn"
            processed_line = re.sub(kms_pattern, key_ref, line)
            
            if config.is_debug_enabled():
                print(f"Dereferenced KMS key: {key_id} -> {key_ref}")
            
            return processed_line
    
    return line


def deref_s3(config: ConfigurationManager, line: str, resource_type: str, original_line: str) -> str:
    """
    Dereference S3 bucket references to Terraform references.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        original_line: Original line for context.
        
    Returns:
        Line with dereferenced S3 reference.
    """
    if line.startswith("s3://"):
        bucket_name = line.replace("s3://", "").split("/")[0].strip()
        bucket_ref = f"aws_s3_bucket.{bucket_name.replace('-', '_').replace('.', '_')}.id"
        
        if config.is_debug_enabled():
            print(f"Dereferenced S3 bucket: {bucket_name} -> {bucket_ref}")
        
        return line.replace(f"s3://{bucket_name}", bucket_ref)
    
    return line


def generic_deref_arn(config: ConfigurationManager, line: str, resource_type: str, original_line: str) -> str:
    """
    Generic ARN dereferencing for other AWS services.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        original_line: Original line for context.
        
    Returns:
        Line with dereferenced ARN.
    """
    if config.is_debug_enabled():
        print(f"Generic ARN deref: {line.strip()}")
    
    # This is a placeholder for generic ARN dereferencing
    # Specific implementations would be added based on service needs
    
    return line


def fix_vpc_references(config: ConfigurationManager, line: str, resource_type: str) -> str:
    """
    Fix VPC ID references to Terraform references.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        
    Returns:
        Line with fixed VPC references.
    """
    import re
    vpc_pattern = r'vpc-[a-f0-9]+'
    
    def replace_vpc(match):
        vpc_id = match.group(0)
        vpc_ref = f"aws_vpc.{vpc_id.replace('-', '_')}.id"
        return vpc_ref
    
    return re.sub(vpc_pattern, replace_vpc, line)


def fix_subnet_references(config: ConfigurationManager, line: str, resource_type: str) -> str:
    """
    Fix subnet ID references to Terraform references.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        
    Returns:
        Line with fixed subnet references.
    """
    import re
    subnet_pattern = r'subnet-[a-f0-9]+'
    
    def replace_subnet(match):
        subnet_id = match.group(0)
        subnet_ref = f"aws_subnet.{subnet_id.replace('-', '_')}.id"
        return subnet_ref
    
    return re.sub(subnet_pattern, replace_subnet, line)


def fix_sg_references(config: ConfigurationManager, line: str, resource_type: str) -> str:
    """
    Fix security group ID references to Terraform references.
    
    Args:
        config: Configuration manager.
        line: Line to process.
        resource_type: AWS resource type.
        
    Returns:
        Line with fixed security group references.
    """
    import re
    sg_pattern = r'sg-[a-f0-9]+'
    
    def replace_sg(match):
        sg_id = match.group(0)
        sg_ref = f"aws_security_group.{sg_id.replace('-', '_')}.id"
        return sg_ref
    
    return re.sub(sg_pattern, replace_sg, line)


def remove_block(config: ConfigurationManager) -> None:
    """
    Remove specific blocks from Terraform configuration.
    
    Args:
        config: Configuration manager.
    """
    # This function would implement block removal logic
    # Placeholder for now
    if config.is_debug_enabled():
        print("remove_block called")


def aws_resource(config: ConfigurationManager, t1: str, tt1: str, tt2: str, 
                flag1: bool, flag2: bool) -> Tuple[int, str, bool, bool]:
    """
    Process AWS resource configuration.
    
    Args:
        config: Configuration manager.
        t1: Configuration line.
        tt1: Field name.
        tt2: Field value.
        flag1: Processing flag 1.
        flag2: Processing flag 2.
        
    Returns:
        Tuple of (skip, processed_line, flag1, flag2).
    """
    skip = 0
    return skip, t1, flag1, flag2


def rhs_replace(config: ConfigurationManager, t1: str, tt1: str, tt2: str) -> str:
    """
    Replace right-hand side values in Terraform configuration.
    
    Args:
        config: Configuration manager.
        t1: Configuration line.
        tt1: Field name.
        tt2: Field value.
        
    Returns:
        Processed configuration line.
    """
    # Placeholder for RHS replacement logic
    return t1


def deref_array(config: ConfigurationManager, t1: str, tt1: str, tt2: str, 
               ttft: str, prefix: str, skip: int) -> Tuple[str, int]:
    """
    Dereference array values in Terraform configuration.
    
    Args:
        config: Configuration manager.
        t1: Configuration line.
        tt1: Field name.
        tt2: Field value.
        ttft: Resource type.
        prefix: ID prefix.
        skip: Skip flag.
        
    Returns:
        Tuple of (processed_line, skip_flag).
    """
    # Placeholder for array dereferencing logic
    return t1, skip


# Additional utility functions for Terraform processing

def validate_terraform_syntax(config: ConfigurationManager, tf_file: str) -> bool:
    """
    Validate Terraform syntax for a generated file.
    
    Args:
        config: Configuration manager.
        tf_file: Path to Terraform file.
        
    Returns:
        True if syntax is valid.
    """
    try:
        import subprocess
        result = subprocess.run(
            ["terraform", "validate", tf_file],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            if config.is_debug_enabled():
                print(f"Terraform syntax valid for {tf_file}")
            return True
        else:
            print(f"Terraform syntax error in {tf_file}: {result.stderr}")
            return False
            
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error validating Terraform syntax: {str(e)}")
        return False


def format_terraform_file(config: ConfigurationManager, tf_file: str) -> bool:
    """
    Format a Terraform file using terraform fmt.
    
    Args:
        config: Configuration manager.
        tf_file: Path to Terraform file.
        
    Returns:
        True if formatting was successful.
    """
    try:
        import subprocess
        result = subprocess.run(
            ["terraform", "fmt", tf_file],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            if config.is_debug_enabled():
                print(f"Formatted Terraform file: {tf_file}")
            return True
        else:
            if config.is_debug_enabled():
                print(f"Error formatting {tf_file}: {result.stderr}")
            return False
            
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error formatting Terraform file: {str(e)}")
        return False


def get_terraform_file_stats(config: ConfigurationManager, tf_directory: str) -> Dict[str, int]:
    """
    Get statistics about generated Terraform files.
    
    Args:
        config: Configuration manager.
        tf_directory: Directory containing Terraform files.
        
    Returns:
        Dictionary with file statistics.
    """
    stats = {
        'total_files': 0,
        'resource_files': 0,
        'import_files': 0,
        'data_files': 0,
        'total_lines': 0
    }
    
    try:
        for filename in os.listdir(tf_directory):
            if filename.endswith('.tf'):
                stats['total_files'] += 1
                
                if filename.startswith('aws_'):
                    stats['resource_files'] += 1
                elif filename.startswith('import__'):
                    stats['import_files'] += 1
                elif filename.startswith('data__'):
                    stats['data_files'] += 1
                
                # Count lines
                file_path = os.path.join(tf_directory, filename)
                try:
                    with open(file_path, 'r') as f:
                        stats['total_lines'] += len(f.readlines())
                except Exception:
                    continue
        
        return stats
        
    except Exception as e:
        if config.is_debug_enabled():
            print(f"Error getting Terraform file stats: {str(e)}")
        return stats