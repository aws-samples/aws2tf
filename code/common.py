import boto3
from botocore.exceptions import ClientError
import sys
import subprocess
import os
import re
import ast
import shlex
import json
import time
from io import StringIO
from contextlib import suppress
import shutil
import context
import glob
import botocore
import fixtf
import inspect
from datetime import datetime,timezone
import resources
from timed_interrupt import timed_int, initialize_timer, stop_timer
import threading
import logging
from tqdm import tqdm

from pathlib import Path

# Get logger from parent aws2tf module
log = logging.getLogger('aws2tf')

# Conditional warning function
def log_warning(message, *args, **kwargs):
    """
    Log warning only if warnings are enabled via -w flag.
    Always logs in debug mode.
    """
    if context.warnings or context.debug:
        log.warning(message, *args, **kwargs)


def run_terraform_plan_with_progress(command, description="Terraform plan", record_time=False):
    """
    Run terraform plan command and show estimated progress with adaptive learning.
    
    Uses self-adjusting progress estimation that:
    - Caps at 75% until completion
    - Learns from previous plan executions to improve estimates
    - Adapts to actual system performance
    - Optionally records execution time for post-import estimates
    
    Args:
        command: Terraform plan command to execute
        description: Description for progress bar
        record_time: If True, records execution time in context.last_plan_time
        
    Returns:
        subprocess.CompletedProcess object
    """
    # Count import files to estimate total
    import_files = glob.glob("import__*.tf")
    total_resources = len(import_files)
    
    if total_resources == 0 or context.debug:
        # No progress bar in debug mode or if no resources
        return rc(command)
    
    try:
        # Run terraform with output capture
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        # Use adaptive rate from previous runs, or default estimate
        # Typical rate: 20-30 resources/second for plan
        estimated_rate = context.terraform_plan_rate
        estimated_time = total_resources / estimated_rate
        
        # Show estimated progress with 75% cap
        with tqdm(total=100, 
                 desc=description,
                 unit="%",
                 leave=False,
                 bar_format='{desc}: {percentage:3.0f}%|{bar}| [{elapsed}<{remaining}]') as pbar:
            
            start = time.time()
            
            while process.poll() is None:
                elapsed = time.time() - start
                
                # Calculate progress with 75% cap
                if elapsed < estimated_time:
                    # Normal progress up to estimated time, cap at 75%
                    progress = int((elapsed / estimated_time) * 75)
                else:
                    # If taking longer, hover around 75-78%
                    overtime = elapsed - estimated_time
                    # Asymptotically approach 78%, never quite reaching it
                    additional = 3 * (1 - (1 / (1 + overtime / 20)))
                    progress = 75 + int(additional)
                
                pbar.n = progress
                pbar.refresh()
                time.sleep(0.5)
            
            # Process completed - jump to 100%
            pbar.n = 100
            pbar.refresh()
            
            # Record actual time for adaptive learning
            actual_time = time.time() - start
            actual_rate = total_resources / actual_time if actual_time > 0 else estimated_rate
            
            # Update adaptive rate (exponential moving average)
            if context.terraform_plan_samples == 0:
                # First sample - use it directly
                context.terraform_plan_rate = actual_rate
            else:
                # Weighted average: 70% old rate, 30% new rate
                context.terraform_plan_rate = (context.terraform_plan_rate * 0.7) + (actual_rate * 0.3)
            
            context.terraform_plan_samples += 1
            
            # Record time if requested (for post-import estimate)
            if record_time:
                context.last_plan_time = actual_time
            
            if context.debug:
                log.debug(f"Terraform plan rate updated: {context.terraform_plan_rate:.2f} resources/sec (sample #{context.terraform_plan_samples})")
                if record_time:
                    log.debug(f"Recorded plan time: {actual_time:.2f} seconds")
        
        # Collect output
        stdout, stderr = process.communicate()
        
        # Create result object
        class Result:
            def __init__(self, returncode, stdout, stderr):
                self.returncode = returncode
                self.stdout = stdout.encode()
                self.stderr = stderr.encode()
        
        return Result(
            process.returncode,
            stdout,
            stderr
        )
    
    except Exception as e:
        # Fall back to regular execution if progress tracking fails
        if context.debug:
            log.debug(f"Progress tracking failed, using regular execution: {e}")
        return rc(command)


def run_terraform_command_with_spinner(command, description="Running terraform"):
    """
    Run terraform command with a simple spinner (for commands without progress).
    
    Args:
        command: Command to execute
        description: Description for spinner
        
    Returns:
        subprocess.CompletedProcess object
    """
    return rc(command)

    """
    if context.debug:
        # No spinner in debug mode
        return rc(command)
    
    try:
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Show spinner while running
        with tqdm(desc=description, 
                 bar_format='{desc}: {elapsed}',
                 leave=False) as pbar:
            while process.poll() is None:
                time.sleep(0.5)
                pbar.update(0)
        
        stdout, stderr = process.communicate()
        
        class Result:
            def __init__(self, returncode, stdout, stderr):
                self.returncode = returncode
                self.stdout = stdout
                self.stderr = stderr
        
        return Result(process.returncode, stdout, stderr)
    
    except Exception as e:
         if context.debug:
            log.debug(f"Spinner failed, using regular execution: {e}")
         log.info(f"Spinner failed, using regular execution: {e}")
         return rc(command)
   """


def get_import_count_from_plan(plan_file='plan2.json'):
    """
    Get number of resources to import from terraform plan JSON.
    
    Args:
        plan_file: Path to plan JSON file
        
    Returns:
        int: Number of resources to import
    """
    try:
        with open(plan_file) as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if data.get('type') == 'change_summary':
                        return data['changes'].get('import', 0)
                except (json.JSONDecodeError, KeyError):
                    continue
    except FileNotFoundError:
        pass
    
    return 0


def run_terraform_apply_with_progress(tfplan_file, plan_json='plan2.json'):
    """
    Run terraform apply command and show estimated progress with adaptive learning.
    
    Uses self-adjusting progress estimation that:
    - Caps at 75% until completion
    - Learns from actual apply performance
    - Adapts to system speed and network conditions
    
    Args:
        tfplan_file: Path to terraform plan file
        plan_json: Path to plan JSON file for getting total count
        
    Returns:
        subprocess.CompletedProcess object
    """
    # Get total resources to import
    total_resources = get_import_count_from_plan(plan_json)
    
    if total_resources == 0 or context.debug:
        # No progress bar in debug mode or if no resources
        command = f"terraform apply -no-color {tfplan_file}"
        return rc(command)
    
    try:
        # Run terraform apply with JSON output
        command = f"terraform apply -no-color -json {tfplan_file}"
        
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        # Use adaptive rate from previous runs, or default estimate
        # Apply is typically faster than plan (50-60 resources/second)
        estimated_rate = context.terraform_apply_rate
        estimated_time = total_resources / estimated_rate
        
        # Collect output for return
        stdout_lines = []
        stderr_lines = []
        
        # Track actual imports from JSON (for final rate calculation)
        imported_count = 0
        
        # Show estimated progress with 75% cap
        with tqdm(total=100,
                 desc="Importing resources",
                 unit="%",
                 leave=False,
                 bar_format='{desc}: {percentage:3.0f}%|{bar}| [{elapsed}<{remaining}]') as pbar:
            
            start = time.time()
            
            # Background thread to update progress
            def update_progress():
                while process.poll() is None:
                    elapsed = time.time() - start
                    
                    # Calculate progress with 75% cap
                    if elapsed < estimated_time:
                        # Normal progress up to estimated time, cap at 75%
                        progress = int((elapsed / estimated_time) * 75)
                    else:
                        # If taking longer, hover around 75-78%
                        overtime = elapsed - estimated_time
                        # Asymptotically approach 78%
                        additional = 3 * (1 - (1 / (1 + overtime / 20)))
                        progress = 75 + int(additional)
                    
                    pbar.n = progress
                    pbar.refresh()
                    time.sleep(0.5)
            
            # Start progress update thread
            progress_thread = threading.Thread(target=update_progress, daemon=True)
            progress_thread.start()
            
            # Read stdout line by line (for JSON parsing and output collection)
            for line in process.stdout:
                stdout_lines.append(line)
                
                # Try to parse JSON to count actual imports
                try:
                    if line.strip():
                        data = json.loads(line)
                        event_type = data.get('type', '')
                        
                        if event_type == 'apply_complete':
                            imported_count += 1
                
                except (json.JSONDecodeError, KeyError, AttributeError):
                    pass
            
            # Read any remaining stderr
            stderr_output = process.stderr.read()
            if stderr_output:
                stderr_lines.append(stderr_output)
            
            # Wait for process and progress thread to complete
            process.wait()
            progress_thread.join(timeout=1)
            
            # Process completed - jump to 100%
            pbar.n = 100
            pbar.refresh()
            
            # Record actual time for adaptive learning
            actual_time = time.time() - start
            # Use imported_count if available, otherwise use total_resources
            actual_count = imported_count if imported_count > 0 else total_resources
            actual_rate = actual_count / actual_time if actual_time > 0 else estimated_rate
            
            # Update adaptive rate (exponential moving average)
            if context.terraform_apply_samples == 0:
                # First sample - use it directly
                context.terraform_apply_rate = actual_rate
            else:
                # Weighted average: 70% old rate, 30% new rate
                context.terraform_apply_rate = (context.terraform_apply_rate * 0.7) + (actual_rate * 0.3)
            
            context.terraform_apply_samples += 1
            
            if context.debug:
                log.debug(f"Terraform apply rate updated: {context.terraform_apply_rate:.2f} resources/sec (sample #{context.terraform_apply_samples})")
        
        # Create result object
        class Result:
            def __init__(self, returncode, stdout, stderr):
                self.returncode = returncode
                self.stdout = stdout.encode()
                self.stderr = stderr.encode()
        
        return Result(
            process.returncode,
            ''.join(stdout_lines),
            ''.join(stderr_lines)
        )
    
    except Exception as e:
        # Fall back to regular execution if progress tracking fails
        if context.debug:
            log.debug(f"Apply progress tracking failed, using regular execution: {e}")
        command = f"terraform apply -no-color {tfplan_file}"
        return rc(command)

# Security Fix #3: Path traversal prevention
def safe_filename(filename: str, base_dir: str = None) -> str:
    """
    Validate and sanitize filename to prevent path traversal attacks.
    
    Args:
        filename: The filename to validate
        base_dir: Optional base directory to restrict to (defaults to current working dir)
    
    Returns:
        Sanitized filename safe for use
        
    Raises:
        ValueError: If path traversal attempt detected
    """
    if base_dir is None:
        base_dir = os.getcwd()
    
    # Convert to Path objects for safe manipulation
    base_path = Path(base_dir).resolve()
    
    # Remove any path separators and resolve the path
    # This prevents ../../../etc/passwd type attacks
    safe_name = os.path.basename(filename)
    
    # Additional sanitization - remove dangerous characters
    # Keep alphanumeric, dash, underscore, dot
    import re
    safe_name = re.sub(r'[^\w\-\.]', '_', safe_name)
    
    # Prevent hidden files (starting with .)
    if safe_name.startswith('.') and safe_name != '.terraform.lock.hcl':
        safe_name = '_' + safe_name
    
    # Construct full path
    full_path = (base_path / safe_name).resolve()
    
    # Verify the resolved path is still within base_dir
    try:
        full_path.relative_to(base_path)
    except ValueError:
        raise ValueError(f"Path traversal attempt detected: {filename}")
    
    return str(full_path)


def safe_write_file(filename: str, content: str, mode: str = 'w', base_dir: str = None, permissions: int = 0o644) -> None:
    """
    Safely write content to a file with path validation and secure permissions.
    
    Args:
        filename: The filename to write to
        content: Content to write
        mode: File mode ('w' or 'wb')
        base_dir: Optional base directory to restrict to
        permissions: Unix file permissions (default: 0o644 = rw-r--r--)
                    Use 0o600 for sensitive files (rw-------)
    
    Security Features:
    - Path traversal prevention
    - Secure file permissions
    - Atomic write operation
    """
    # For files in subdirectories like 'imported/', handle specially
    if '/' in filename:
        # Split into directory and filename
        parts = filename.split('/')
        subdir = '/'.join(parts[:-1])
        fname = parts[-1]
        
        # Validate subdirectory doesn't contain traversal
        if '..' in subdir:
            raise ValueError(f"Path traversal attempt in directory: {subdir}")
        
        # Create subdirectory if it doesn't exist
        if base_dir:
            full_subdir = os.path.join(base_dir, subdir)
        else:
            full_subdir = subdir
            
        os.makedirs(full_subdir, mode=0o755, exist_ok=True)
        
        # Validate the filename part
        safe_fname = safe_filename(fname, full_subdir)
        safe_path = safe_fname
    else:
        # Simple filename, validate it
        safe_path = safe_filename(filename, base_dir)
    
    # Write the file with specified permissions
    if 'b' in mode:
        # Binary mode
        fd = os.open(safe_path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, permissions)
        with os.fdopen(fd, mode) as f:
            f.write(content)
    else:
        # Text mode - use os.open for atomic creation with permissions
        fd = os.open(safe_path, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, permissions)
        with os.fdopen(fd, mode) as f:
            f.write(content)
    
    # Verify permissions were set correctly
    actual_perms = os.stat(safe_path).st_mode & 0o777
    if actual_perms != permissions:
        # Try to fix permissions
        os.chmod(safe_path, permissions)


def safe_write_sensitive_file(filename: str, content: str, mode: str = 'w', base_dir: str = None) -> None:
    """
    Write sensitive files (state, credentials, etc.) with restricted permissions.
    
    Uses 0o600 permissions (rw-------) - only owner can read/write.
    """
    safe_write_file(filename, content, mode, base_dir, permissions=0o600)


def secure_terraform_files(directory: str = '.') -> None:
    """
    Secure terraform state files and other sensitive files with appropriate permissions.
    
    Security Fix #7: Set restrictive permissions on sensitive files
    
    Files secured:
    - terraform.tfstate (0o600) - Contains sensitive data
    - terraform.tfstate.backup (0o600) - Contains sensitive data
    - .terraform.lock.hcl (0o644) - Lock file, less sensitive
    - *.tfvars (0o600) - May contain secrets
    - aws2tf.log (0o600) - May contain sensitive information
    
    Args:
        directory: Directory to secure files in (default: current directory)
    """
    sensitive_files = {
        'terraform.tfstate': 0o600,
        'terraform.tfstate.backup': 0o600,
        '.terraform.lock.hcl': 0o644,
        'aws2tf.log': 0o600,
    }
    
    # Secure specific files
    for filename, perms in sensitive_files.items():
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            try:
                os.chmod(filepath, perms)
                if context.debug:
                    log.debug(f"Secured {filename} with permissions {oct(perms)}")
            except Exception as e:
                log.warning(f"Could not set permissions on {filename}: {e}")
    
    # Secure all .tfvars files
    import glob
    for tfvars_file in glob.glob(os.path.join(directory, '*.tfvars')):
        try:
            os.chmod(tfvars_file, 0o600)
            if context.debug:
                log.debug(f"Secured {os.path.basename(tfvars_file)} with permissions 0o600")
        except Exception as e:
            log.warning(f"Could not set permissions on {tfvars_file}: {e}")


def get_file_permissions_info() -> dict:
    """
    Get information about file permissions for security documentation.
    
    Returns:
        Dictionary with file types and their recommended permissions
    """
    return {
        'terraform_files': {
            'description': 'Terraform configuration files',
            'pattern': '*.tf',
            'permissions': 0o644,
            'reason': 'Configuration files, readable by group'
        },
        'state_files': {
            'description': 'Terraform state files (SENSITIVE)',
            'pattern': 'terraform.tfstate*',
            'permissions': 0o600,
            'reason': 'Contains secrets, credentials, and sensitive resource data'
        },
        'variable_files': {
            'description': 'Terraform variable files (POTENTIALLY SENSITIVE)',
            'pattern': '*.tfvars',
            'permissions': 0o600,
            'reason': 'May contain secrets and sensitive configuration'
        },
        'log_files': {
            'description': 'Application log files (POTENTIALLY SENSITIVE)',
            'pattern': '*.log',
            'permissions': 0o600,
            'reason': 'May contain AWS resource IDs, ARNs, and debugging information'
        },
        'import_files': {
            'description': 'Terraform import files',
            'pattern': 'import__*.tf',
            'permissions': 0o644,
            'reason': 'Import declarations, less sensitive'
        },
    }


#####################

from get_aws_resources import aws_acm
from get_aws_resources import aws_amp
from get_aws_resources import aws_amplify
from get_aws_resources import aws_athena
from get_aws_resources import aws_autoscaling
from get_aws_resources import aws_apigateway
from get_aws_resources import aws_apigatewayv2
from get_aws_resources import aws_appmesh
from get_aws_resources import aws_application_autoscaling
from get_aws_resources import aws_appstream
from get_aws_resources import aws_batch
from get_aws_resources import aws_backup
from get_aws_resources import aws_bedrock
from get_aws_resources import aws_bedrock_agent
from get_aws_resources import aws_bedrock_agentcore_control
from get_aws_resources import aws_cleanrooms
from get_aws_resources import aws_cloud9
from get_aws_resources import aws_cloudformation
from get_aws_resources import aws_cloudfront
from get_aws_resources import aws_cloudtrail
from get_aws_resources import aws_cloudwatch
from get_aws_resources import aws_codebuild
from get_aws_resources import aws_codecommit
from get_aws_resources import aws_codeartifact
from get_aws_resources import aws_codedeploy
from get_aws_resources import aws_codepipeline
from get_aws_resources import aws_codeguruprofiler
from get_aws_resources import aws_codestar_notifications
from get_aws_resources import aws_cognito_identity
from get_aws_resources import aws_cognito_idp
from get_aws_resources import aws_config
from get_aws_resources import aws_connect
from get_aws_resources import aws_customer_profiles
from get_aws_resources import aws_datazone
from get_aws_resources import aws_devops_guru
from get_aws_resources import aws_directconnect
from get_aws_resources import aws_dms
from get_aws_resources import aws_docdb
from get_aws_resources import aws_ds
from get_aws_resources import aws_dynamodb
from get_aws_resources import aws_kms
from get_aws_resources import aws_ec2
from get_aws_resources import aws_ecs
from get_aws_resources import aws_efs
from get_aws_resources import aws_ecr_public
from get_aws_resources import aws_ecr
from get_aws_resources import aws_eks
from get_aws_resources import aws_elasticache
from get_aws_resources import aws_elbv2
from get_aws_resources import aws_emr
from get_aws_resources import aws_events
from get_aws_resources import aws_firehose
from get_aws_resources import aws_glue
from get_aws_resources import aws_guardduty
from get_aws_resources import aws_iam
from get_aws_resources import aws_kafka
from get_aws_resources import aws_kendra
from get_aws_resources import aws_kinesis
from get_aws_resources import aws_logs
from get_aws_resources import aws_lakeformation
from get_aws_resources import aws_lambda
from get_aws_resources import aws_license_manager
from get_aws_resources import aws_lightsail
from get_aws_resources import aws_memorydb
from get_aws_resources import aws_mwaa
from get_aws_resources import aws_neptune
from get_aws_resources import aws_network_firewall
from get_aws_resources import aws_networkmanager
from get_aws_resources import aws_organizations
from get_aws_resources import aws_opensearchserverless
from get_aws_resources import aws_ram
from get_aws_resources import aws_rds
from get_aws_resources import aws_redshift
from get_aws_resources import aws_redshift_serverless
from get_aws_resources import aws_resource_explorer_2
from get_aws_resources import aws_route53
from get_aws_resources import aws_route53resolver
from get_aws_resources import aws_s3
from get_aws_resources import aws_s3control
from get_aws_resources import aws_s3tables
from get_aws_resources import aws_s3vectors
from get_aws_resources import aws_sagemaker
from get_aws_resources import aws_schemas
from get_aws_resources import aws_scheduler
from get_aws_resources import aws_securityhub
from get_aws_resources import aws_secretsmanager
from get_aws_resources import aws_servicecatalog
from get_aws_resources import aws_servicediscovery
from get_aws_resources import aws_shield
from get_aws_resources import aws_ses
from get_aws_resources import aws_sesv2
from get_aws_resources import aws_signer
from get_aws_resources import aws_sns
from get_aws_resources import aws_sqs
from get_aws_resources import aws_ssm
from get_aws_resources import aws_sso_admin
from get_aws_resources import aws_transfer
from get_aws_resources import aws_vpc_lattice
from get_aws_resources import aws_waf
from get_aws_resources import aws_wafv2
from get_aws_resources import aws_workspaces_web
from get_aws_resources import aws_xray

from fixtf_aws_resources import needid_dict
from fixtf_aws_resources import aws_no_import
from fixtf_aws_resources import aws_not_implemented

# Security Fix #2: Module registry to replace eval()
# This prevents arbitrary code execution via eval()
AWS_RESOURCE_MODULES = {
    'acm': aws_acm,
    'amp': aws_amp,
    'amplify': aws_amplify,
    'athena': aws_athena,
    'autoscaling': aws_autoscaling,
    'apigateway': aws_apigateway,
    'apigatewayv2': aws_apigatewayv2,
    'appmesh': aws_appmesh,
    'application-autoscaling': aws_application_autoscaling,
    'application_autoscaling': aws_application_autoscaling,
    'appstream': aws_appstream,
    'batch': aws_batch,
    'backup': aws_backup,
    'bedrock': aws_bedrock,
    'bedrock-agent': aws_bedrock_agent,
    'bedrock_agent': aws_bedrock_agent,
    'bedrock-agentcore-control': aws_bedrock_agentcore_control,
    'cleanrooms': aws_cleanrooms,
    'cloud9': aws_cloud9,
    'cloudformation': aws_cloudformation,
    'cloudfront': aws_cloudfront,
    'cloudtrail': aws_cloudtrail,
    'cloudwatch': aws_cloudwatch,
    'codebuild': aws_codebuild,
    'codecommit': aws_codecommit,
    'codeartifact': aws_codeartifact,
    'codedeploy': aws_codedeploy,
    'codepipeline': aws_codepipeline,
    'codeguruprofiler': aws_codeguruprofiler,
    'codestar-notifications': aws_codestar_notifications,
    'codestar_notifications': aws_codestar_notifications,
    'cognito-identity': aws_cognito_identity,
    'cognito_identity': aws_cognito_identity,
    'cognito-idp': aws_cognito_idp,
    'cognito_idp': aws_cognito_idp,
    'config': aws_config,
    'connect': aws_connect,
    'customer-profiles': aws_customer_profiles,
    'customer_profiles': aws_customer_profiles,
    'datazone': aws_datazone,
    'devops-guru': aws_devops_guru,
    'directconnect': aws_directconnect,
    'dms': aws_dms,
    'docdb': aws_docdb,
    'ds': aws_ds,
    'dynamodb': aws_dynamodb,
    'kms': aws_kms,
    'ec2': aws_ec2,
    'ecs': aws_ecs,
    'efs': aws_efs,
    'ecr-public': aws_ecr_public,
    'ecr_public': aws_ecr_public,
    'ecr': aws_ecr,
    'eks': aws_eks,
    'elasticache': aws_elasticache,
    'elbv2': aws_elbv2,
    'emr': aws_emr,
    'events': aws_events,
    'firehose': aws_firehose,
    'glue': aws_glue,
    'guardduty': aws_guardduty,
    'iam': aws_iam,
    'kafka': aws_kafka,
    'kendra': aws_kendra,
    'kinesis': aws_kinesis,
    'logs': aws_logs,
    'lakeformation': aws_lakeformation,
    'lambda': aws_lambda,
    'license-manager': aws_license_manager,
    'license_manager': aws_license_manager,
    'lightsail': aws_lightsail,
    'memorydb': aws_memorydb,
    'mwaa': aws_mwaa,
    'neptune': aws_neptune,
    'network-firewall': aws_network_firewall,
    'network_firewall': aws_network_firewall,
    'networkmanager': aws_networkmanager,
    'organizations': aws_organizations,
    'opensearchserverless': aws_opensearchserverless,
    'ram': aws_ram,
    'rds': aws_rds,
    'redshift': aws_redshift,
    'redshift-serverless': aws_redshift_serverless,
    'redshift_serverless': aws_redshift_serverless,
    'resource-explorer-2': aws_resource_explorer_2,
    'resource_explorer_2': aws_resource_explorer_2,
    'route53': aws_route53,
    'route53resolver': aws_route53resolver,
    's3': aws_s3,
    's3control': aws_s3control,
    's3tables': aws_s3tables,
    's3vectors': aws_s3vectors,
    'sagemaker': aws_sagemaker,
    'schemas': aws_schemas,
    'scheduler': aws_scheduler,
    'securityhub': aws_securityhub,
    'secretsmanager': aws_secretsmanager,
    'servicecatalog': aws_servicecatalog,
    'servicediscovery': aws_servicediscovery,
    'shield': aws_shield,
    'ses': aws_ses,
    'sesv2': aws_sesv2,
    'signer': aws_signer,
    'sns': aws_sns,
    'sqs': aws_sqs,
    'ssm': aws_ssm,
    'sso-admin': aws_sso_admin,
    'sso_admin': aws_sso_admin,
    'transfer': aws_transfer,
    'vpc-lattice': aws_vpc_lattice,
    'vpc_lattice': aws_vpc_lattice,
    'waf': aws_waf,
    'wafv2': aws_wafv2,
    'workspaces-web': aws_workspaces_web,
    'xray': aws_xray,
}


def call_resource(type, id):
   #log.debug("--1-- in call_resources >>>>> "+type+"   "+str(id))
   if type in context.all_extypes:
      log.debug("Common Excluding: %s %s %s",  type, id) 
      pkey=type+"."+id
      context.rproc[pkey] = True
      return
   
   if type in aws_no_import.noimport:
      log_warning("WARNING: Can not import type: " + type)
      if id is not None:
         with open('not-imported.log', 'a') as f2:
            f2.write(type + " : " + str(id) + "\n")
         context.rproc[type+"."+id] = True
      return

   if type in aws_not_implemented.notimplemented:
      log_warning("Not supported by aws2tf currently: " + type +
            " please submit github issue to request support")
      return

   elif type == "aws_null":
      with open('stack-null.err', 'a') as f3:
         f3.write("-->> called aws_null for: "+id+"\n")
      return

    # don't get it if we alreay have it
    # if context.rproc
   log.debug("---->>>>> "+type+"   "+str(id))
   if id is not None:
      ti = type+"."+id
      try:
         if context.rproc[ti]:
            log.debug("Already processed " + ti)
            log.debug("Already processed " + ti)
            return
      except:
         pass
   else:
      if type in needid_dict.aws_needid:
         log_warning("WARNING: " + type + " can not have null id must pass parameter " +
               needid_dict.aws_needid[type]['param'])
         # TODO api only
         return
   #log.debug("--2-- in call_resources >>>>> "+type+"   "+str(id))
   rr = False
   sr = False
   clfn, descfn, topkey, key, filterid = resources.resource_data(type, id)
   if key == "NOIMPORT":
      log_warning("WARNING: Can not import type: " + type)
      return

   if clfn is None:
        log.error("ERROR: clfn is None with type="+type)
        log.info("exit 016")
        stop_timer()
        exit()
# Try specific

   try:
            if context.debug:
               log.debug("calling specific common.get_"+type+" with type="+type+" id="+str(id)+"   clfn=" +
                    clfn+" descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)

            # Security Fix #2: Use module registry instead of eval()
            # Convert clfn to normalized form (replace hyphens with underscores)
            mclfn = clfn.replace("-", "_")
            
            # Look up module in registry
            module = AWS_RESOURCE_MODULES.get(clfn) or AWS_RESOURCE_MODULES.get(mclfn)
            
            if module is None:
                # Module not in registry - will try generic handler instead
                if context.debug:
                    log.debug(f"Module not found in registry for clfn={clfn}, will try generic handler")
                sr = False
            else:
                # Get the function from the module
                getfn = getattr(module, "get_"+type)
                
                #log.debug("type %s", type, "id",id, "clfn",clfn, "descfn",descfn, "topkey", topkey,"key",key, "filterid",filterid)   
                sr = getfn(type, id, clfn, descfn, topkey, key, filterid)

   except AttributeError as e:
      if context.debug:
         log.debug("AttributeError: name 'getfn' - no aws_"+clfn+".py file ?")
         log.debug(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.debug("%s %s %s %s",  exc_type, fname, exc_tb.tb_lineno)
      pass

   except SyntaxError:
      log.debug("SyntaxError: name 'getfn' - no aws_"+clfn+".py file ?")
      pass

   except NameError as e:
      if context.debug:
         log.debug("WARNING: NameError: name 'getfn' - no aws_"+clfn+".py file ?")
         log.debug(f"{e=}")
         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.debug("%s %s %s %s",  exc_type, fname, exc_tb.tb_lineno)

      pass

   except Exception as e:
      handle_error(e, str(inspect.currentframe().f_code.co_name),
                   clfn, descfn, topkey, id)

   if not sr:
      try:
         if context.debug:
               log.debug("calling generic getresource with type="+type+" id="+str(id)+"   clfn="+clfn +
               " descfn="+str(descfn)+" topkey="+topkey + "  key="+key + "  filterid="+filterid)
         rr = getresource(type, id, clfn, descfn, topkey, key, filterid)
      except Exception as e:
         log.error(f"{e=}")

         exc_type, exc_obj, exc_tb = sys.exc_info()
         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
         log.error("%s %s %s %s",  exc_type, fname, exc_tb.tb_lineno)
         if rr is False:
            log.error("--->> Could not get resource "+type+" id="+str(id))
            pass


   with open('processed-resources.log', 'a') as f4:
      f4.write(str(type) + " : " + str(id)+"\n")

def tfplan1(mymess):

   rf = "resources.out"
   # com="terraform plan -generate-config-out="+ rf + " -out tfplan -json > plan2.json"

   if not glob.glob("import*.tf"):

      log.info("INFO: No import*.tf files found - nothing to import, exiting ....")
      log.info("INFO: Confirm the resource type exists in your account: "+context.acc+" & region: "+context.region)
      context.tracking_message="No import*.tf files found for this resource, exiting ...."
      stop_timer()
      # Use sys.exit to allow proper cleanup of threading resources
      sys.exit(0)

   com = "cp imported/provider.tf provider.tf"
   rout = rc(com)

   com = "mv aws_*.tf imported"
   rout = rc(com)

   com = "terraform plan -generate-config-out=" + \
       rf + " -out tfplan -json > plan1.json"
   if not context.fast: log.info(com)
   
   # Use progress bar for terraform plan
   rout = run_terraform_plan_with_progress(com, "Terraform plan "+mymess)
      
   file = "plan1.json"
   f2 = open(file, "r")
   plan2 = True

   while True:
      line = f2.readline()
      if not line:
         break
      # log.debug(line)
      if '@level": "error"' in line:
         if context.debug is True:
            log.debug("Error" + line)
         try:
               mess = f2.readline()
               try:
                  if "VPC Lattice" in mess and "404" in mess:
                     log.error("ERROR: VPC Lattice 404 error - see plan1.json")
                     i = mess.split('(')[1].split(')')[0].split('/')[-1]
                     if i != "":
                        log.error("ERROR: Removing "+i +
                              " import files - plan errors see plan1.json [p1]")
                        context.badlist = context.badlist+[i]
                        shutil.move("import__*"+i+"*.tf",
                                    "notimported/import__*"+i+"*.tf")

                  elif "Error: Cannot import non-existent remote object" in mess:
                     log.error(
                         "ERROR: Cannot import non-existent remote object - see plan1.json")
                     i = mess.split('(')[1].split(')')[0].split('/')[-1]
                     if i != "":
                        log.error("ERROR: Removing "+i +
                              " import files - plan errors see plan1.json [p2]")
                        context.badlist = context.badlist+[i]
                        shutil.move("import__*"+i+"*.tf",
                                    "notimported/import__*"+i+"*.tf")

               except:
                  pass

               try:
                  i = mess.split('(')[2].split(')')[0]
                  if i != "":
                     log.error("ERROR: Removing "+i +
                           " files - plan errors see plan1.json [p3]")
                     context.badlist = context.badlist+[i]
                     shutil.move("import__*"+i+"*.tf",
                                 "notimported/import__*"+i+"*.tf")
                     shutil.move("aws_*"+i+"*.tf",
                                 "notimported/aws_*"+i+"*.tf")

               except:
                  if context.debug is True:
                     log.debug(mess.strip())
                  context.plan2 = True

         except:
               log.error("Error - no error message, check plan1.json")
               dt = datetime.now().isoformat(timespec='seconds')
               com = "cp plan1.json plan1.json."+dt
               log.info(com)
               rout = rc(com)
               # continue
               log.info("exit 018")
               stop_timer()
               exit()

   # log.debug("Plan 1 complete -- resources.out generated")

   if not os.path.isfile("resources.out"):
         log.error("could not find expected resources.out file after Plan 1 - exiting")
         dt = datetime.now().isoformat(timespec='seconds')
         com = "cp plan1.json plan1.json."+dt
         log.info(com)
         rout = rc(com)

         # exit()
   return


def tfplan2():
   # log.debug("fix tf files.....")
   if not os.path.isfile("resources.out"):
         log.error("could not find expected resources.out file in tfplan2 - exiting")
         # exit()
         return

   # log.debug("split resources.out")
   splitf("resources.out")  # generated *.out files
   # zap the badlist
   for i in context.badlist:
      # com="rm -f aws_*"+i+"*.out"+" aws_*"+i+"*.tf"
      log.error("ERROR: Removing "+i+" files - plan errors see plan1.json [p4]")

      # log.debug(com)
      # rout=rc(com)
      try:
         shutil.move("aws_*"+i+"*.tf", "notimported/aws_*"+i+"*.tf")
         shutil.move("aws_*"+i+"*.out", "notimported/aws_*"+i+"*.out")
      except FileNotFoundError as e:
         log.error(f"{e=}")
         pass
      # sed to remove references


   # copy all imported/aws_*.tf to here ?
   com = "cp imported/aws_*.tf ."
   rout = rc(com)

   # Process .out files with fixtf (fix terraform files)
   x = glob.glob("aws_*__*.out")
   
   if len(x) > 0:
      for fil in tqdm(x, desc="Fixing terraform files", unit="file", leave=False):
         type = fil.split('__')[0]
         tf = fil.split('.')[0]
         fixtf.fixtf(type, tf)
   
   com = "mv aws_*.out imported"
   rout = rc(com)

   com = "terraform fmt"
   rout = rc(com)


def tfplan3():

   #### move tfproto files
   x=glob.glob("data*.tfproto")
   for fil in x:
      tf=fil.split('.tfproto',1)[0]
      com = "mv "+fil +" "+ tf+".tf"
      log.info(com)
      rout = rc(com)

   context.tracking_message="Validate and Test Plan  ..."
   log.info("\nValidate and Test Plan  ... ")
   if context.merge:
      com = "cp imported/aws_*.tf ."
      rout = rc(com)
   if not glob.glob("aws_*.tf"):
      log.error("No aws_*.tf files found for this resource, exiting ....")
      log.info("exit 019")
      stop_timer()
      exit()

   rf = "resources.out"
   com = "cp imported/provider.tf provider.tf"
   rout = rc(com)

   com = "terraform validate -no-color"
   rout = rc(com)
   el = len(rout.stderr.decode().rstrip())
   if el != 0:
      errm = rout.stderr.decode().rstrip()
      log.error(errm)
      com = "terraform validate -no-color -json > validate2.json"
      rout = rc(com)

   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      log.error(str(rout.stdout.decode().rstrip()))
      log.error("Validation after fix failed - exiting")
      context.tracking_message="Validation after fix failed - exiting"
      log.info("exit 020 %s", str(context.aws2tfver))
      stop_timer()
      exit()

   else:
      log.info("Valid Configuration.")
      if context.validate:
         log.info("Validate Only..")
         return
   zeroi=0    

################################################################################
   x = glob.glob("aws_*__*.tf")
   context.esttime=len(x)/4
   awsf=len(x)
   y = glob.glob("import__*.tf")
   impf=len(y)

   if awsf != impf:
      if context.workaround=="":
         if not context.merge:
            log.error("ERROR: "+str(awsf)+ "x aws_*.tf and " + str(impf) +"x import__*.tf file counts do not match")      
            #log.info("\nLikely import error [1] - do the following and report errors in github issue:")
            #log.info("cd "+context.path1)
            #log.info("terraform plan -generate-config-out=resources.out")
            fix_imports()
         #exit()
      else:
         log.info("INFO: "+str(awsf)+ "x aws_*.tf and " + str(impf) +"x import__*.tf file counts do not match")
         log.info("INFO: Continuing due to workaround "+context.workaround)
   else:
      log.info("PASSED: aws_*.tf and import__*.tf file counts match = %s", awsf)


################################################################################

   #if context.merge:
   context.plan2=True

   if context.plan2:

      log.info("Stage 7 of 10, Penultimate Terraform Plan ... ")
      context.tracking_message="Stage 7 of 10, Penultimate Terraform Plan ..."
      # redo plan

      com="ls imported/import*"
      rout = rc(com)
      print(rout.stdout.decode().rstrip())



      com = "rm -f resources.out tfplan"
      #log.debug(com)
      rout = rc(com)
      
      com = "terraform plan -generate-config-out=" + \
          rf + " -out tfplan -json > plan2.json"
      if not context.fast: log.info(com)
      
      # Use progress bar for terraform plan
      rout = run_terraform_plan_with_progress(com, "Terraform plan (validation)", record_time=True)
      
      zerod = False
      zeroc = False
      zeroa = False
      zeroi = -1
      planList = []
      planDict = {}
      changeList = []
      with open('plan2.json') as f:
         for jsonObj in f:
            planDict = json.loads(jsonObj)
            planList.append(planDict)
      for pe in planList:
         if pe['type'] == "change_summary":  
            zeroi=pe['changes']['import']
            zeroa=pe['changes']['add']
            zeroc=pe['changes']['change']
            zerod=pe['changes']['remove']

      log.info("Plan: %s to import, %s to add, %s to change, %s to destroy", zeroi, zeroa, zeroc, zerod)

      with open('plan2.json', 'r') as f:
         for line in f.readlines():
            if '@level":"error"' in line:
              if "Error: Conflicting configuration arguments" in line and "aws_security_group_rule." in line:
                 log.warning(
                     "WARNING: Conflicting configuration arguments in aws_security_group_rule")
              else:
                  if context.debug is True:
                     log.debug("Error" + line)

                  log.error("-->> Plan 2 errors exiting - check plan2.json - or run terraform plan")
                  log.info("exit 021 %s", str(context.aws2tfver))
                  stop_timer()
                  exit()

      if zerod != 0:
         log.error("-->> plan will destroy resources! - unexpected, is there existing state ?")
         log.error("-->> look at plan2.json - or run terraform plan")
         log.info("exit 022")
         stop_timer()
         sys.exit(1)

      if zeroc != 0:
         # decide if to ignore ot not
         planList = []
         planDict = {}
         changeList = []
         allowedchange = False
         nchanges = 0
         nallowedchanges = 0
         all_force_destroy_only = True  # Track if all changes are force_destroy only
         
         with open('plan2.json') as f:
            for jsonObj in f:
               planDict = json.loads(jsonObj)
               planList.append(planDict)
         for pe in planList:
            if pe['type'] == "planned_change" and pe['change']['action'] == "update":
               nchanges = nchanges+1
               ctype = pe['change']['resource']['resource_type']
               caddr = pe['change']['resource']['addr']
               
               # Check if only force_destroy is changing
               force_destroy_only = False
               try:
                  # Run terraform plan and grep for force_destroy
                  plan_output = subprocess.run(['terraform', 'plan'], 
                                             capture_output=True, text=True, check=True)
                  grep_output = subprocess.run(['grep', 'force_destroy'], 
                                             input=plan_output.stdout,
                                             capture_output=True, text=True)
                  
                  # Count lines with force_destroy
                  force_destroy_lines = [line.strip() for line in grep_output.stdout.split('\n') if line.strip()]
                  
                  # If we found force_destroy lines and the count matches the number of changes, it's safe
                  if force_destroy_lines and len(force_destroy_lines) == nchanges:
                     force_destroy_only = True
                     log.info("Only force_destroy changes detected (count matches)")
                  else:
                     all_force_destroy_only = False
                     if context.debug:
                        log.debug("force_destroy lines: %d, nchanges: %d", len(force_destroy_lines), nchanges)
               except Exception as e:
                  all_force_destroy_only = False
                  if context.debug:
                     log.debug("Could not parse terraform plan output: %s", e)
               
               if ctype == "aws_lb_listener" or ctype == "aws_cognito_user_pool_client" \
                  or ctype=="aws_bedrockagent_agent" or ctype=="aws_bedrockagent_agent_action_group" \
                  or force_destroy_only:
                  
                  changeList.append(pe['change']['resource']['addr'])
                  log.info("Planned changes found in Terraform Plan for type: " +
                        str(pe['change']['resource']['resource_type']))
                  allowedchange = True
                  nallowedchanges = nallowedchanges+1
               else:
                  all_force_destroy_only = False
                  log.warning("Unexpected plan changes found in Terraform Plan for resource: " +
                        str(pe['change']['resource']['addr']))
         if nchanges == nallowedchanges:
            log.info("\n-->> plan will change " + str(nchanges) +
                  " resources! - these are expected changes only (should be non-consequential)")
            ci = 1

            log.info(
                "-->> Check the planned changes in these resources listed below by running: terraform plan\n")

            for i in changeList:
               log.info(str(ci)+": "+str(i))
               ci = ci+1
            log.info("\n")

            # Auto-accept if all changes are force_destroy only
            if all_force_destroy_only and nchanges > 0:
               log.info("All changes are force_destroy only - automatically continuing")
               context.expected = True

            if context.expected is False:
               log.info("You can check the changes by running 'terraform plan' in %s\n", context.path1)
               log.info("Then rerun the same ./aws2tf.py command and add the '-a' flag to accept these plan changes and continue to import")
               log.info("exit 023")
               stop_timer()
               exit()

            if context.debug is True:
               log.debug("\n-->> Then if happy with the output changes for the above resources, run this command to complete aws2tf-py tasks:")
               log.info("exit 024")
               stop_timer()
               log.info("terraform apply -no-color tfplan")
               exit()
         else:
            log.error("-->> plan will change resources! - unexpected")
            log.error("-->> look at plan2.json - or run terraform plan")
            log.info("exit 025 %s", str(context.aws2tfver))
            stop_timer()
            exit()

      if zeroa !=0:
         log.error("-->> plan will add resources! - unexpected")
         log.error("-->> look at plan2.json - or run terraform plan")
         log.info("exit 026")
         stop_timer()
         exit()

      log.debug("Plan complete")
      ## if merging get .out files from imported ?

   ### validations checks
   # import__ == aws_*.tf - and import number
   #   
   if not context.merge:
      if zeroi == awsf:
         log.info("PASSED: import count = file counts = %s", str(zeroi))
      else:
         log.info("INFO: import count "+str(zeroi) +" != file counts "+ str(awsf))
         if context.workaround=="":
            log.error("\nLikely import error [2] - do the following and report errors in github issue")
            log.info("cd "+context.path1)
            log.info("terraform plan -generate-config-out=resources.out")
            log.info("exit 027")
            stop_timer()
            exit()
         else:
            log.info("INFO: Continuing due to workaround "+context.workaround)
         
   if context.merge:
         log.info("Merge check")
         if zeroi==0:
            log.info("Nothing to merge exiting ...")
            log.info("exit 028")
            stop_timer()
            exit()
         # get imported
         x = glob.glob("imported/import__*.tf")
         #log.debug("Imported files ="+str(x))
         preimpf=len(x)
         log.info("previous imports %s",str(preimpf))
         # impf-preimpf  (num import* files - number import files in imported)
         #toimp=impf-preimpf
         toimp=awsf-preimpf
         com = "terraform state list | grep ^aws_ | wc -l"
         rout = rc(com)
         stc=int(rout.stdout.decode().rstrip())

         if preimpf != stc:
            log.error("Miss-matched previous imports %s and state file resources %s exiting", str(preimpf), str(stc))
            log.info("exit 029")
            stop_timer()
            exit() 
         else:
            log.info("Existing import file = Existing state count = %s", str(stc))
         if toimp != zeroi:
            log.warning("Unexpected import number exiting")
            #log.info("exit 030")
            #stop_timer()
            #exit() 
         else:
            log.info("PASSED: importing expected number of resources = %s", str(toimp))    

   if not os.path.isfile("tfplan"):
      log.error("Plan - could not find expected tfplan file - exiting")
      log.info("exit 031")
      stop_timer()
      sys.exit(1)

   #if context.merge:
   #   exit()
   #   log.info("merge - exit after plan2")

def wrapup():
   ### copy predefined import files
   log.info("Stage 8 of 10, Final Terraform Validation")
   context.tracking_message="Stage 8 of 10, Final Terraform Validation"
   com = "terraform validate -no-color"
   rout = rc(com)
   el = len(rout.stderr.decode().rstrip())
   if el != 0:
      errm = rout.stderr.decode().rstrip()
      log.error(errm)
   if "Success! The configuration is valid" not in str(rout.stdout.decode().rstrip()):
      log.error(str(rout.stdout.decode().rstrip()))
      log.info("exit 032")
      stop_timer()
      exit()
   else:
      log.info("PASSED: Valid Configuration.")

   if context.merge:
      log.info("Pre apply merge check")
      if not os.path.isfile("plan2.json"):
         log.error("ERROR: Could not find plan2.json, unexpected on merge - exiting ....")
         log.info("exit 033")
         stop_timer()
         exit()
      
   log.info("Stage 9 of 10, Terraform import via apply of tfplan....")
   context.tracking_message="Stage 9 of 10, Terraform import via apply of tfplan...."
   
   # Use progress bar for terraform apply
   rout = run_terraform_apply_with_progress("tfplan")
   
   zerod = False
   zeroc = False
   if "Error" in str(rout.stderr.decode().rstrip()):
      log.error("ERROR: problem in apply ... further checks ....")
      errs=str(rout.stderr.decode().rstrip())
      ## Plan check
      log.info("\nPost Error Import Plan Check .....")
      com = "terraform plan -no-color -out tfplan"
      rout = run_terraform_command_with_spinner(com, "Post-error validation")
      
      if "No changes. Your infrastructure matches the configuration" not in str(rout.stdout.decode().rstrip()):
         log.error(errs)
         log.error("ERROR: unexpected final plan stuff - exiting")

         if "aws_bedrockagent_agent" not in errs:
            log.info("exit 034")
            stop_timer()
            exit()
         else:
            log.warning("WARNING: aws_bedrockagent_agent - continuing")
      else:
         log.info("PASSED: No changes in plan")
         patterns = ["import__aws_*.tf", "*.out", "*.json"]
         files_to_move = [f for pattern in patterns for f in glob.glob(pattern)]
         if files_to_move:
            for tf in tqdm(files_to_move, desc="Moving files to imported/", unit="file", leave=False):
               try:
                     shutil.move(tf, f"imported/{tf}")
               except (FileNotFoundError, shutil.Error):
                     pass
         x = glob.glob("aws_*.tf")        
         if len(x) > 0:
            for tf in tqdm(x, desc=f"Moving files", unit="file", leave=False):
               try:
                  shutil.copy(tf, f"imported/{tf}")
               except (FileNotFoundError, shutil.Error):
                  pass  # File already moved or doesn't exist
         
         # Security Fix #7: Secure sensitive files after import
         secure_terraform_files('.')
         return


         
   log.info("\nStage 10 of 10, Post Import Plan Check .....")
   context.tracking_message="Stage 10 of 10, Post Import Plan Check ....."
   com = "terraform plan -no-color -out tfplan -json > final.json"
   # Get reference file size for progress estimation
   plan2_size = os.path.getsize('plan2.json') if os.path.exists('plan2.json') else 0
   
   com = "terraform plan -no-color -out tfplan -json > final.json"
   
   # Run with progress bar based on file size
   if plan2_size > 0 and not context.debug:
       process = subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       with tqdm(total=100, desc="Post-import validation", unit="%", bar_format='{desc}: {percentage:3.0f}%|{bar}| [{elapsed}]') as pbar:
           start_time = time.time()
           max_wait = plan2_size / 50000
           while process.poll() is None:
               elapsed = time.time() - start_time
               if os.path.exists('final.json'):
                   current_size = os.path.getsize('final.json')
                   size_progress = min(75, int((current_size / plan2_size) * 75))
                   pbar.n = size_progress
               else:
                   time_progress = min(50, int((elapsed / max_wait) * 50))
                   pbar.n = time_progress
               pbar.refresh()
               time.sleep(0.5)
           pbar.n = 100
           pbar.refresh()
       stdout, stderr = process.communicate()
       class Result:
           def __init__(self, returncode, stdout, stderr):
               self.returncode = returncode
               self.stdout = stdout
               self.stderr = stderr
       rout = Result(process.returncode, stdout, stderr)
   else:
       rout = rc(com)
   com = "sync"
   rout = rc(com)
   zeroi=0
   zeroa=0
   zeroc=0
   zerod=0
   planList = []
   planDict = {}
   changeList = []
   with open('final.json','r') as f:
        for jsonObj in f:
            planDict = json.loads(jsonObj)
            planList.append(planDict)
   with open('final.warn', 'w') as f:
      for pe in planList:
         if pe['type'] == "change_summary":  
            zeroi=int(pe['changes']['import'])
            zeroa=int(pe['changes']['add'])
            zeroc=int(pe['changes']['change'])
            zerod=int(pe['changes']['remove'])
            json.dump(pe, f, indent=2, default=str)
         elif pe['type'] == "diagnostic":
            json.dump(pe, f, indent=2, default=str)


   log.info("Plan: %s to import, %s to add, %s to change, %s to destroy", zeroi, zeroa, zeroc, zerod)
   nchged=zeroi+zeroa+zeroc+zerod
   if nchged == 0:
      context.tracking_message="Stage 10 of 10, Passed post import check - No changes in plan"
      log.info("Stage 10 of 10, Passed post import check - No changes in plan")

      # Move multiple file types in one operation
      patterns = ["import__aws_*.tf", "*.out", "*.json"]
      files_to_move = [f for pattern in patterns for f in glob.glob(pattern)]
      if files_to_move:
         for tf in tqdm(files_to_move, desc="Moving files to imported/", unit="file", leave=False):
            try:
                  shutil.move(tf, f"imported/{tf}")
            except (FileNotFoundError, shutil.Error):
                  pass

      
      x = glob.glob("aws_*.tf")        
      if len(x) > 0:
         for tf in tqdm(x, desc=f"Moving files", unit="file", leave=False):
            try:
               shutil.copy(tf, f"imported/{tf}")
            except (FileNotFoundError, shutil.Error):
               pass  # File already moved or doesn't exist
      
      # Security Fix #7: Secure sensitive files after import
      secure_terraform_files('.')

   else:
      log.error("ERROR: unexpected final plan failure")
      out1=str(rout.stdout.decode().rstrip())
      log.error(out1)
      #if "aws_bedrockagent_agent" in out1:
      #   log.warning("WARNING: aws_bedrockagent_agent - continuing")"
      log.error(str(rout.stderr.decode().rstrip()))
      log.info("exit 035")
      stop_timer()
      exit()

######################################################################

def rc(cmd):
    """
    Execute a command safely without shell=True.
    
    Args:
        cmd: Either a string (for backwards compatibility, will be parsed) 
             or a list of command arguments
    
    Returns:
        subprocess.CompletedProcess object
    """
    # If cmd is a string, parse it into a list for safe execution
    if isinstance(cmd, str):
        # For simple commands, split on spaces
        # For complex commands with pipes/redirects, we need special handling
        if '>' in cmd or '|' in cmd or '&&' in cmd or ';' in cmd:
            # These require shell, but we'll use shell=True only for these cases
            # and log a warning
            if context.debug:
                log.debug(f"WARNING: Command requires shell features: {cmd[:100]}")
            out = subprocess.run(cmd, shell=True, capture_output=True)
        else:
            # Safe to split and run without shell
            import shlex
            try:
                cmd_list = shlex.split(cmd)
                out = subprocess.run(cmd_list, capture_output=True, shell=False)
            except Exception as e:
                # Fallback to shell if parsing fails
                log.warning(f"Command parsing failed, using shell: {e}")
                out = subprocess.run(cmd, shell=True, capture_output=True)
    else:
        # cmd is already a list
        out = subprocess.run(cmd, capture_output=True, shell=False)
    
    ol = len(out.stdout.decode('utf-8').rstrip())
    el = len(out.stderr.decode().rstrip())
    if el != 0:
         errm = out.stderr.decode().rstrip()
         # log.error(errm)
         # exit(1)

    return out


def fix_imports():
   x = glob.glob("aws_*__*.tf")
   context.esttime=len(x)/4
   awsf=len(x)
   y = glob.glob("import__*.tf")
   impf=len(y)
   log.info("\nFix Import Intervention")



   #more import files than aws files - picked up via dependancies
   #if impf > awsf:
   for fil2 in y:  # all import files  
         impok=False
         for fil in x: # all aws_ files
            
            tf=fil.split('.tf',1)[0]
            iseg=fil2.replace("import__","").replace(".tf", "")
            if tf == iseg:
                  #com = "mv "+fil2+" imported/"+fil2
                  #rc(com)
                  impok=True
                  break
         
         ## out of for loop
         # got an import file we 
         if impok is False:
            com = "mv "+fil2+" "+fil2.replace(".tf",".err")
            log.warning(fil2.replace(".tf",".err"))
            rc(com)

   y = glob.glob("import__*.tf")
   impf=len(y)  

           

def ctrl_c_handler(signum, frame):
  log.info("Ctrl-C pressed.")
  log.info("exit 036")
  stop_timer()
  exit()


def check_python_version():
   version = sys.version_info
   major = version.major
   minor = version.minor
   bv = str(boto3.__version__)
   log.info("boto3 version: %s", bv)
   if major < 3 or (major == 3 and minor < 8):
      log.error("This program requires Python 3.8 or later.")
      sys.exit(1)
# check boto3 version
   if boto3.__version__ < '1.42.16':
      bv = str(boto3.__version__)
      log.info("boto3 version: %s", bv)
      vs = bv.split(".")
      v1 = int(vs[0])*100000+int(vs[1])*1000+int(vs[2])
      if v1 < 142016:
         log.error("boto3 version: %s", bv)
         log.error("This program requires boto3 1.42.16 or later.")
         log.error("Try: pip install boto3  -or-  pip install boto3==1.42.16")
         log.info("exit 037")
         stop_timer()
         sys.exit(1)


def aws_tf(region,args):
   # os.chdir(context.path1)
   #if not os.path.isfile("aws.tf"):

   with open("provider.tf", 'w') as f3:
      f3.write('terraform {\n')
      f3.write('  required_version = "> 1.10.4"\n')
      f3.write('  required_providers {\n')
      f3.write('    aws = {\n')
      f3.write('      source  = "hashicorp/aws"\n')
      # f3.write('      version = "5.48.0"\n')
      f3.write('      version = "'+context.tfver+'"\n')
      f3.write('    }\n')
      f3.write('  }\n')
      f3.write('}\n')
      f3.write('provider "aws" {\n')
      f3.write('  region                   = "' + region + '"\n')
      if args.profile is not None:
         f3.write('  profile                  = "' + context.profile + '"\n')
      if not context.serverless: f3.write('  shared_credentials_files = ["~/.aws/credentials"]\n')
      f3.write('}\n')

   com = "cp provider.tf imported/provider.tf"
   rout = rc(com)
   if not os.path.isfile("data-aws.tf"):   
      with open("data-aws.tf", 'w') as f3:
         f3.write('data "aws_region" "current" {}\n')
         f3.write('data "aws_caller_identity" "current" {}\n')
         f3.write('data "aws_availability_zones" "az" {\n')
         f3.write('state = "available"\n')
         f3.write('}\n')
   if not context.merge:
      #log.info("terraform init")
      com = "terraform init -no-color -upgrade"
      rout = rc(com)
      el = len(rout.stderr.decode().rstrip())
      if el != 0:
         log.error(rout.stdout.decode().rstrip())
         log.error(str(rout.stderr.decode().rstrip()))
   else:
      log.info("skipping terraform init")


# split resources.out
def splitf_old(file):
   lhs = 0
   rhs = 0
   if os.path.isfile(file):
      if context.debug: log.debug("split file:" + file)
      with open(file, "r") as f:
         Lines = f.readlines()
      for tt1 in Lines:
         if "{" in tt1: lhs = lhs+1
         if "}" in tt1: rhs = rhs+1
         if lhs > 1:
               if lhs == rhs:
                  try:
                     f2.write(tt1+"\n")
                     f2.close()
                     lhs = 0
                     rhs = 0
                     continue
                  except:
                     pass

         if tt1.startswith("resource"):
               ttft = tt1.split('"')[1]
               taddr = tt1.split('"')[3]
               # if context.acc in taddr:
               #   a1=taddr.find(context.acc)
               #   taddr=taddr[:a1]+taddr[a1+12:]


               f2 = open(ttft+"__"+taddr+".out", "w")
               f2.write(tt1)

         elif tt1.startswith("#"):
               continue
         elif tt1 == "" or tt1 == "\n":
               continue
         else:
               try:
                  f2.write(tt1)
               except:
                  log.warning("tried to write to closed file: >" + tt1 + "<")
   else:
      log.error("could not find expected resources.out file")

   # moves resources.out to imported
   f2.close()
   shutil.move(file, "imported/"+file)


#################################

def splitf(input_file):
   # Compile regex patterns for better performance
   resource_pattern = re.compile(r'resource "(\w+)" "(.+?)"')
   comment_pattern = re.compile(r'^\s*#')
   if context.debug: log.debug("split file: " + input_file)
   # Read the entire file content at once
   with open(input_file, 'r') as f:
        content = f.read()
   
    # Use a more efficient splitting method
   resource_blocks = re.split(r'(?=\nresource ")', '\n' + content)

   for block in resource_blocks[1:]:  # Skip the first (empty) block
        match = resource_pattern.search(block)
        if match:
            resource_type = match.group(1)
            resource_name = match.group(2)

            # Create filename
            resource_name_safe = resource_name.replace('/', '__')
            # Security Fix #3: Sanitize filename
            resource_name_safe = re.sub(r'[^\w\-\.]', '_', resource_name_safe)
            filename = f"{resource_type}__{resource_name_safe}.out"

            # Use StringIO for efficient string operations
            output = StringIO()

            for line in block.split('\n'):
                if not comment_pattern.match(line):
                    output.write(line + '\n')

            # Write the filtered resource block to a new file
            
            if len(filename) > 255: filename=filename[:250]+".out"
            try:
               # Security Fix #3: Use safe file write
               safe_write_file(filename, output.getvalue().strip() + '\n')
            except ValueError as e:
               log.error(f"ERROR: Path validation failed: {e}")
               log.info("exit 038")
               stop_timer()
               exit()
            except Exception as e:
               log.error(f"ERROR: could not write to file: {filename} - {e}")
               log.info("exit 038")
               stop_timer()
               exit()
   shutil.move(input_file,"imported/"+input_file)


################################



# if type == "aws_vpc_endpoint": return "ec2","describe_vpc_endpoints","VpcEndpoints","VpcEndpointId","vpc-id"

#generally pass 3rd param as None - unless overriding
def write_import(type,theid,tfid):
   try:
      ## todo -  if theid starts with a number or is an od (but what if its hexdecimal  ?)

      if tfid is None:
            tfid=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")
      else:
            tfid=tfid.replace("/", "_").replace(".", "_").replace(":", "_").replace("|", "_").replace("$", "_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_").replace(" ","_").replace("*","star").replace("\\052","star").replace("@","_").replace("\\64","_")

         #catch tfid starts with number
      if tfid[:1].isdigit(): tfid="r-"+tfid

      # Security Fix #3: Additional sanitization to prevent path traversal
      tfid = re.sub(r'\.\.', '_', tfid)  # Remove any remaining ..
      tfid = tfid.replace('/', '_')  # Ensure no path separators

      if "!" in theid:
         fn="notimported/import__"+type+"__"+tfid+".tf"
         log.error("ERROR: Not importing "+type+" "+theid)
         log.error("ERROR: Invalid character ! in name")
      else:
         fn="import__"+type+"__"+tfid+".tf"

      #fn=fn.replace(context.acc,"012345678912")

      if context.debug: log.debug(fn)
         
         # check if file exists:
         #
      if context.merge:   
         #y = glob.glob("imported/import__*.tf")
         if os.path.isfile("imported/"+fn):
            return
         
      if os.path.isfile(fn):
            if context.debug: log.debug("File exists: " + fn)
            pkey=type+"."+tfid
            context.rproc[pkey]=True
            return

      done_data=False
      done_data=do_data(type,theid)

      if not done_data:
         output = StringIO()
         output.write('import {\n')
         output.write('  to = ' +type + '.' + tfid + '\n')
         output.write('  id = "'+ theid + '"\n')
         output.write('}\n')

                  # Write the filtered resource block to a new file
         
         if len(fn) > 255: fn=fn[:250]+".tf"
         #if context.merge:   print("Merge import",fn)
         try:
            # Security Fix #3: Use safe file write with path validation
            safe_write_file(fn, output.getvalue().strip() + '\n')
         except ValueError as e:
            log.error(f"ERROR: Path validation failed: {e}")
            log.info("exit 039")
            stop_timer()
            exit()
         except Exception as e:
            log.error(f"ERROR: could not write to file: {fn} - {e}")
            log.info("exit 039")
            stop_timer()
            exit()


      pkey=type+"."+tfid
      context.rproc[pkey]=True
      pkey=type+"."+theid
      context.rproc[pkey]=True


   except Exception as e:  
      handle_error2(e,str(inspect.currentframe().f_code.co_name),id)    

   return


def do_data(type,theid):
   if context.dnet:
      if type == "aws_vpc" or type=="aws_subnet":
         fn="data-"+type+"_"+theid+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "'+theid+'" {\n')
            f3.write(' id = "'+theid+'"\n')
            f3.write('}\n')
         return True
      
   if context.dsgs:
      if type=="aws_security_groups":
         fn="data-"+type+"_"+theid+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "'+theid+'" {\n')
            f3.write(' id = "'+theid+'"\n')
            f3.write('}\n')
         return True
   if context.dkms:
      if type == "aws_kms_key":
         fn="data-"+type+"_"+theid+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "k-'+theid+'" {\n')
            f3.write(' key_id = "'+theid+'"\n')
            f3.write('}\n')
         return True
   if context.dkey:
      if type == "aws_key_pair":
         tfil=theid.replace("/","_").replace(".","_").replace(":","_").replace("|","_").replace("$","_").replace(",","_").replace("&","_").replace("#","_").replace("[","_").replace("]","_").replace("=","_").replace("!","_").replace(";","_")
         fn="data-"+type+"_"+tfil+".tf"
         with open(fn, 'w') as f3:
            f3.write('data "'+type+'" "'+tfil+'" {\n')
            f3.write(' key_name = "'+theid+'"\n')
            f3.write('}\n')
         return True


   return False


#########################################################################################################################

def getresource(type,id,clfn,descfn,topkey,key,filterid):
   #for j in context.specials:
   #   if type == j: 
   #      print(type + " in specials list returning ..")
   #      return False
   if context.debug: log.debug("-1-> In getresource doing "+ type + ' with id ' + str(id)+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" key="+key+" filterid="+filterid)

   if type in str(context.types): 
      log.info("Found "+type+"in types skipping ...")
      return True
   try:
      if id is not None:
         pt=type+"."+id
         if pt in context.rproc:
            if context.rproc[pt] is True:
               log.info("Found "+pt+" in processed skipping ...") 
               return True
      response=call_boto3(type,clfn,descfn,topkey,key,id)   
      if str(response) != "[]":
            for item in response:
               if id is None or filterid=="": # do it all
                  if context.debug: log.debug("--"+str(item))
                  try:
                     if "aws-service-role" in str(item["Path"]): 
                        if context.debug:  log.debug("Skipping service role " + str(item[key])) 
                        continue
                  except:
                     pass

                  try:
                     theid=item[key]
                  except TypeError:
                     log.error("ERROR: getresource TypeError: "+str(response)+" key="+key+" type="+type,descfn)
                     with open('boto3-error.err', 'a') as f:
                        f.write("ERROR: getresource TypeError: type="+type+" key="+key+" descfn="+descfn+"\n"+str(response)+"\n")
                     continue
                  pt=type+"."+theid
                  if pt not in context.rproc:
                     write_import(type,theid,None)
                  else:
                     if context.rproc[pt] is True:
                        log.info("Found "+pt+" in processed skipping ...") 
                        continue
                  #special_deps(type,theid)
               
               
               #
               # id has something
               #
               else:  
                  if context.debug: 
                     log.debug("-gr31-"+"filterid="+str(filterid)+" id="+str(id)+"  key="+key)
                     log.debug(str(item))
                  if "." not in filterid:
                     try:
                        if id == str(item[filterid]):
                           #if context.debug: print("-gr31 item-"+str(item))
                           theid=item[key]
                           #special_deps(type,theid)
                           write_import(type,theid,None)
                        elif filterid != key:
                           if context.debug:
                              log.debug("id="+id+" filterid="+filterid)
                              log.debug("item="+str(item))
                           theid=item[filterid]
                           write_import(type,theid,None)
                     except Exception as e:
                        log.error(f"{e=}")
                        if context.mopup.get(type) is not None:
                           if id.startswith(context.mopup[type]):
                              write_import(type,id,None)
                              return True

                        else:
                           with open('missed-getresource.log', 'a') as f4:
                              f4.write("Could have done write_import "+type+" id="+id+" filterid="+filterid+"/n")
                           return False
                  else:
                     ### There IS a dot in the filterid so we need to dig deeper
                     log.debug(str(item))
                     log.debug("id="+id+" filterid="+filterid)
                     filt1=filterid.split('.')[1]
                     filt2=filterid.split('.')[3]
                     log.debug("filt1="+filt1+" filt2="+filt2)
                     dotc=len(item[filt1])
                     log.debug("dotc="+str(dotc))

                     for j in range(0,dotc):
                        try:
                           val=str(item[filt1][j][filt2])
                           log.debug("val="+val + " id=" + id)
                           if id == val:
                              theid=item[key]
                              if dotc>1: theid=id+"/"+item[key]
                              write_import(type,theid,None)
                        except:
                           log.error("-------- error on processing")
                           log.error(str(item))
                           log.error("filterid="+filterid)
                           log.error("----------------------------")
                           pass
      else:
         if id is not None:
            if context.debug: log.debug("No "+type+" "+id+" found - empty response (common)") 
            pkey=type+"."+id  
            context.rproc[pkey]=True      
         else:
            if context.debug: log.debug("No "+type+" found - empty response (common)")
            return True
   
   except Exception as e:
      handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return True               
  
    #tfplan(type)

def special_deps(ttft,taddr):
   """
   if ttft == "aws_security_group": 
      print("##### special dep security group") 
      #add_known_dependancy("aws_security_group_rule",taddr) 
      #add_dependancy("aws_security_group_rule",taddr)
   if ttft == "aws_subnet":
      print("##### special dep subnet") 
      #add_known_dependancy("aws_route_table_association",taddr) 
      #add_dependancy("aws_route_table_association",taddr)  
   elif ttft == "aws_vpc": 
      print("##### special dep vpc") 
      #add_known_dependancy("aws_route_table_association",taddr)  
      #add_known_dependancy("aws_subnet",taddr)  
      #add_dependancy("aws_route_table_association",taddr)
      #add_dependancy("aws_vpc_ipv4_cidr_block_association",taddr)
      #add_dependancy("aws_vpc_endpoint", taddr)
   
   if ttft == "aws_vpclattice_service_network":
      print("##### special lattice sn") 
      add_known_dependancy("aws_vpclattice_service",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_vpc_association",taddr) 
      add_known_dependancy("aws_vpclattice_service_network_service_association",taddr)
   """
   return  


def get_test(type,id,clfn,descfn,topkey,key,filterid):
   log.debug("in get_test")
   log.debug("--> In get_test doing "+ type + ' with id ' + str(id))   
   return



def add_known_dependancy(type,id):
    # check if we alredy have it
    pkey=type+"."+id
    if pkey not in context.rdep:
        if context.debug: log.debug("add_known_dependancy: " + pkey)
        context.rdep[pkey]=False
    return

def add_dependancy(type,id):
    # check if we alredy have it
   if id is None: 
      log.warning("WARNING: add_dependancy: id is None")
      return
   try:
   #   if type=="aws_kms_alias" and id=="k-817bb810-7154-4d9b-b582-7dbb62e77876":
   #      raise Exception("aws_kms_alias")
      if type=="aws_glue_catalog_database":
         if ":" not in id: id=context.acc+":"+id
      pkey=type+"."+id
      if pkey not in context.rproc:
         if context.debug: log.debug("add_dependancy: " + pkey)
         context.rproc[pkey]=False
   except Exception as e:
      handle_error(e, str(inspect.currentframe().f_code.co_name), type, id)
   return


## TODO - always get all / paginate all - save in globals - filter on id in get_aws_ ??
## but in smaller use cases may be better to make filtered boto3 calls ?
## this call doesn't take the key

## can't pass filterid - not possible to use for page in paginator.paginate(filterid=id)
# TODO ? won't accept filter id as string param1 in paginate(param1,id) ??
# hench working around using descfn - not ideal

def call_boto3(type,clfn,descfn,topkey,key,id): 
   try:
      if context.debug: 
         log.debug("call_boto3 clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
      #if context.debug: print("pre-response")
      # get any pre-saved response
      #response=get_boto3_resp(descfn)  # sets response to [] if nothing saved
      response=[]
      if response == []:
         client = boto3.client(clfn) 
         #if context.debug: print("client")
         try:
            paginator = client.get_paginator(descfn)
            #if context.debug: print("paginator")
    
            if "apigatewayv2" in str(type):
               for page in paginator.paginate(ApiId=id): 
                  response.extend(page[topkey]) 
               pkey=type+"."+id
               context.rproc[pkey]=True
               #if response != []:
               #   print(str(response))
               

            elif descfn == "describe_launch_templates":
               if id is not None:
                  if id.startswith("lt-"):
                     for page in paginator.paginate(LaunchTemplateIds=[id]): response.extend(page[topkey])
                  else:
                     for page in paginator.paginate(LaunchTemplateNames=[id]): response.extend(page[topkey])
               else:
                  for page in paginator.paginate(): response.extend(page[topkey])

            elif descfn == "describe_instances":
               if id is not None:
                  if "i-" in id:
                     for page in paginator.paginate(InstanceIds=[id]): response.extend(page[topkey][0]['Instances'])
               else:
                  for page in paginator.paginate(): 
                     if len(page[topkey])==0:
                        continue
                     response.extend(page[topkey][0]['Instances'])
                  #sav_boto3_rep(descfn,response)
               

            elif descfn == "describe_pod_identity_association" or descfn == "list_fargate_profiles" or descfn == "list_nodegroups" or descfn == "list_identity_provider_configs" or descfn == "list_addons":
               for page in paginator.paginate(clusterName=id): response.extend(page[topkey])
            
            
            elif descfn == "list_access_keys" and id is not None:
               for page in paginator.paginate(UserName=id): response.extend(page[topkey])
                    
            
            elif clfn=="kms" and descfn=="list_aliases" and id is not None:
               if id.startswith("k-"): id=id[2:]
               for page in paginator.paginate(KeyId=id): response.extend(page[topkey])
               return response
            
            elif clfn=="lambda" and descfn=="list_aliases" and id is not None:
               for page in paginator.paginate(FunctionName=id): response.extend(page[topkey])
               return response
                
            elif clfn=="describe_config_rules" and id is not None:
               for page in paginator.paginate(ConfigRuleNames=id): response.extend(page[topkey])
               return response
            
            elif clfn=="describe_log_groups" and id is not None:
               if "arn:" in id:  
                  ## arn filtering done in get_aws_cloudwatch_log_group()
                  for page in paginator.paginate(): response.extend(page[topkey])
                  return response
               else:
                  for page in paginator.paginate(logGroupNamePattern=id): response.extend(page[topkey])
                  return response            
               
            
            else:
               if context.debug: log.debug("--1b")
               # main get all call - usually a list- describe- or get- 
               for page in paginator.paginate(): 
                  response.extend(page[topkey])
               #sav_boto3_rep(descfn,response)

               if id is not None:
                  fresp=response
                  if context.debug:log.debug("--2")
                  response=[]
                  if context.debug: log.debug(str(fresp))
                  # get by id - useually a describe- or get-
                  for i in fresp:
                     if context.debug: 
                        try:
                           log.debug("%s %s %s",  i[key], id)
                        except TypeError:
                           log.debug("%s %s %s",  i, id)
                     try:
                        if id in i[key]:
                           response=[i]
                           break
                     except TypeError:
                        if id in i:
                           response=[i]
                           break
                  # get by filter - useually a list- describe- or get-   
               # save a full paginate as we don't want to do it many times
               

         except botocore.exceptions.ParamValidationError as e:

            log.error("ParamValidationError 1 in common.call_boto3: type="+type+" clfn="+clfn)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.error(f"{e=} [pv1] %s %s", fname, exc_tb.tb_lineno)
            with open('boto3-error.err', 'a') as f:
                     f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
                     f.write(f"{e=} [pv1] \n")
                     f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
                     f.write("-----------------------------------------------------------------------------\n")
            return []
            

         except botocore.exceptions.OperationNotPageableError as err:
               if context.debug:
                  log.debug(f"{err=}")
                  log.debug("calling non paginated fn "+str(descfn)+" id="+str(id))
               try:
                  getfn = getattr(client, descfn)                     
                  response1 = getfn()
                  response1=response1[topkey]
                  if context.debug: log.debug("Non-pag response1="+str(response1))
                  if id is None:
                     if context.debug: log.debug("id None")
                     response=response1
                     if context.debug: log.debug("Non-pag response no ID ="+str(response))
                  else: #try a match
                     for j in response1:
                        if id==j[key]:
                           response=[j]
                           if context.debug: log.debug("Non-pag response with ID ="+str(response))
                           

               except botocore.exceptions.ParamValidationError as e:

                  log.error("ParamValidationError 2 in common.call_boto3: type="+type+" clfn="+clfn)
                  exc_type, exc_obj, exc_tb = sys.exc_info()
                  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                  log.error(f"{e=} [pv2] %s %s", fname, exc_tb.tb_lineno)    
                                    
                  with open('boto3-error.err', 'a') as f:
                     f.write("type="+type+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
                     f.write(f"{e=} [pv2] \n")
                     f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
                     f.write("-----------------------------------------------------------------------------\n")
                  return []
               

         except Exception as e:
            handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

         rl=len(response)
         if rl==0:
            if context.debug: log.debug("** zero response length for "+ descfn + " in call_boto3 returning .. []")
            return []

         if context.debug:
            log.debug("response length="+str(len(response)))
            
            for item in response:
               log.debug(item)
            log.debug("--------------------------------------")
   
      else:
         return response
      
   except Exception as e:
      handle_error(e,str(inspect.currentframe().f_code.co_name),clfn,descfn,topkey,id)

   return response

"""
def sav_boto3_rep(descfn,response):
   if str(descfn)=="describe_subnets" and context.aws_subnet_resp==[]: context.aws_subnet_resp=response  
   elif str(descfn)=="describe_vpcs" and context.aws_vpc_resp==[]: context.aws_vpc_resp=response  
   elif str(descfn)=="describe_route_tables" and context.aws_route_table_resp==[]: context.aws_route_table_resp=response  
   elif str(descfn)=="list_aliases" and context.aws_kms_alias_resp==[]: context.aws_kms_alias_resp=response  
   elif str(descfn)=="list_roles" and context.aws_iam_role_resp==[]: context.aws_iam_role_resp=response  
   elif str(descfn)=="describe_instances" and context.aws_instance_resp==[]: context.aws_instance_resp=response  
   return 

def get_boto3_resp(descfn):
   response=[]
   if str(descfn)=="describe_subnets" and context.aws_subnet_resp != []: response=context.aws_subnet_resp
   elif str(descfn)=="describe_vpcs" and context.aws_vpc_resp != []: response=context.aws_vpc_resp
   elif str(descfn)=="describe_route_tables" and context.aws_route_table_resp != []: response=context.aws_route_table_resp 
   elif str(descfn)=="list_aliases" and context.aws_kms_alias_resp != []: response=context.aws_kms_alias_resp 
   elif str(descfn)=="list_roles" and context.aws_iam_role_resp != []: response=context.aws_iam_role_resp
   elif str(descfn)=="describe_instances" and context.aws_instance_resp != []: response=context.aws_instance_resp
   return response
"""


def handle_error(e,frame,clfn,descfn,topkey,id):
   
   exc_type, exc_obj, exc_tb = sys.exc_info()
   exn=str(exc_type.__name__)
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   if exn == "EndpointConnectionError":
      log.debug("No endpoint in this region for "+descfn+" - returning")
      return
   elif exn=="ClientError":
      if "does not exist" in str(e):
         log.warning(id+" does not exist " + fname + " " + str(exc_tb.tb_lineno) )
         return
      log.debug("Exception message :"+str(e))
      return
   elif exn=="ForbiddenException":
      log.debug("Call Forbidden exception for "+fname+" - returning")
      return
   elif exn == "ParamValidationError" or exn=="ValidationException" or exn=="InvalidRequestException" or exn =="InvalidParameterValueException" or exn=="InvalidParameterException":
      log.warning(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return
   elif exn == "BadRequestException" and clfn=="guardduty":
      log.warning(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return  
   
   elif exn=="AccessDeniedException":
      pkey=frame.split("get_")[1]
      log.warning("AccessDeniedException exception for "+fname+" - returning")
      return


   elif "NotFoundException" in exn:
      if frame.startswith("get_"):
         log.debug("NOT FOUND: "+frame.split("get_")[1]+" "+str(id)+" check if it exists and what references it - returning")
         pkey=frame.split("get_")[1]+"."+str(id)
         if "aws_glue_catalog_database" in pkey:
            pkey=frame.split("get_")[1]+"."+context.acc+":"+id
         context.rproc[pkey]=True
      else:
         log.debug("NOT FOUND: "+frame+" "+id+" check if it exists - returning")
      return    

   elif exn=="ResourceNotFoundException" or exn=="EntityNotFoundException" or exn=="NoSuchEntityException" or exn=="NotFoundException" or exn=="LoadBalancerNotFoundException" or exn=="NamespaceNotFound" or exn=="NoSuchHostedZone":
      if frame.startswith("get_"):
         log.debug("NOT FOUND: "+frame.split("get_")[1]+" "+str(id)+" check if it exists and what references it - returning")
         pkey=frame.split("get_")[1]+"."+str(id)
         context.rproc[pkey]=True
      else:
         log.debug("RESOURCE NOT FOUND: "+frame+" "+str(id)+" check if it exists - returning")
      return    
   
   elif exn == "KeyError":
      if "kms" in str(exc_obj):
         log.warning("KeyError can not find key for " +fname+" id="+str(id)+" - returning")
         return
      
      if clfn=="sqs":
         log.warning("KeyError can not find queue url for " +fname+" id="+str(id)+" - returning")
         return
      
   elif exn == "InvalidDocument":
      if clfn=="ssm":
         log.warning("KeyError can not find ssm document for " +fname+" id="+str(id)+" - returning")
         return

   elif exn == "AWSOrganizationsNotInUseException" or exn =="OrganizationAccessDeniedException":
      log.warning("NO ORG: "+frame+" this account doesn't appear to be in an AWS Organisation (or you don't have org permissions) - returning")
      return

   elif "NoSuch" in exn and clfn=="cloudfront":
      log.warning(str(exc_obj)+" for "+frame+" id="+str(id)+" - returning")
      return
   
   elif "BadRequest" in exn:
      if "The requested feature is not enabled for this AWS account" in str(exc_obj):
            log.warning(descfn + " returned feature not enabled for this account - returning")
            return
      elif "Your account isn't authorized to call this operation" in str(exc_obj):
            log.warning(descfn + " returned Your account isn't authorized to call this operation - returning")
            return
      log.error(exn)
      log.error(str(exc_obj)+" for "+frame+" id="+str(id)+" - exit")
      log.info("exit 040")
      #stop_timer() # as it is multi-threaded
      exit()


   elif "InvalidAccessException" in exn:
      if "is not subscribed" in str(exc_obj):
         log.warning(descfn + " returned Not subscribed "+clfn+" - returning")
         return
      log.info("exit 041")
      stop_timer()
      exit()
      



   log.error("\nERROR: in "+frame+" clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id))
   try:   
      log.error(f"{e=} [e1]")
      log.error(f"{exn=} [e1]")
      log.error("%s %s", fname, exc_tb.tb_lineno)
   except:
      log.error("except err")
      pass
   with open('boto3-error.err', 'a') as f:
      f.write("clfn="+clfn+" descfn="+descfn+" topkey="+topkey+" id="+str(id)+"\n")
      f.write(f"{e=} [e1] \n")
      f.write(f"{fname=} {exc_tb.tb_lineno=} [e1] \n")
      f.write("-----------------------------------------------------------------------------\n")
   log.error("stopping process ...")
   #threading.
   stop_timer()
   sys.exit(1)
   

def handle_error2(e,frame,id):
   log.error("\nERROR: in "+frame)
   log.error("id="+str(id))
   exc_type, exc_obj, exc_tb = sys.exc_info()
   fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
   exn=str(exc_type.__name__)
   if exn == "EndpointConnectionError":
      log.debug("No endpoint in this region - returning")
      return
   log.error(f"{e=} [e2] %s %s", fname, exc_tb.tb_lineno)
   with open('boto3-error.err', 'a') as f:
      f.write("id="+str(id)+"\n")
      f.write(f"{e=} [e2] ")
      f.write(f"{fname=} {exc_tb.tb_lineno=} [e2] \n")
      f.write("-----------------------------------------------------------------------------\n")
   log.info("exit 042")
   stop_timer()
   sys.exit(1)




def create_bucket_if_not_exists(bucket_name):
    s3_client = boto3.client('s3')
    
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        log.info(f"Bucket {bucket_name} already exists.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            log.info(f"Bucket {bucket_name} does not exist. Creating now...")
            try:
               s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': context.region})
               log.info(f"Bucket {bucket_name} created successfully.")
            except ClientError as create_error:
               log.error(f"Error creating bucket {bucket_name}: {create_error}")
               return False
        else:
            log.error(f"Error checking bucket {bucket_name}: {e}")
            return False
    
    return True



def upload_directory_to_s3():
   log.info("Uploading to S3...")
   s3_client = boto3.client('s3')
   local_directory="/tmp/aws2tf/generated/tf-"+context.pathadd+context.acc+"-"+context.region
   bucket_name="aws2tf-"+context.acc+"-"+context.region
   s3_prefix=''
   log.info("Calling create_bucket_if_not_exists for %s",  bucket_name)
   bret=create_bucket_if_not_exists(bucket_name)
   if bret:
      log.info("Upload files to s3 %s",  bucket_name)
      for root, dirs, files in os.walk(local_directory):
         if '.terraform' in dirs:  dirs.remove('.terraform')
         if 'tfplan' in files: files.remove('tfplan')
         if '.terraform.lock.hcl' in files: files.remove('.terraform.lock.hcl')
         for filename in files:
               local_path = os.path.join(root, filename)
               
               # Calculate relative path
               relative_path = os.path.relpath(local_path, local_directory)
               s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")
               
               try:
                  s3_client.upload_file(local_path, bucket_name, s3_path)
               except ClientError as e:
                  log.error(f"Error uploading {local_path}: {e}")
                  return False
      log.info("Upload to S3 complete.")
   else:
      log.error("Upload to S3 failed - False return from create_bucket_if_not_exists for %s",  bucket_name)
      return False

def empty_and_delete_bucket():
    bucket_name="aws2tf-"+context.acc+"-"+context.region
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    bucket = s3.Bucket(bucket_name)
    log.info("Emptying and deleting bucket... %s",  bucket_name)
    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            log.info(f"Bucket {bucket_name} does not exist. Nothing to delete.")
            return
        else:
            log.error(f"Error checking bucket {bucket_name}: {e}")
            return

    # Empty the bucket
    try:
        bucket.objects.all().delete()
        log.info(f"Bucket {bucket_name} emptied successfully.")
    except ClientError as e:
        log.error(f"Error emptying bucket {bucket_name}: {e}")
        return

    # Delete the bucket
    try:
        bucket.delete()
        log.info(f"Bucket {bucket_name} deleted successfully.")
    except ClientError as e:
        log.error(f"Error deleting bucket {bucket_name}: {e}")
        return

    log.info(f"Bucket {bucket_name} has been emptied and deleted.")


def download_from_s3():
    log.info("Restore S3")
    s3_client = boto3.client('s3')
    local_directory="/tmp/aws2tf/generated/tf-"+context.pathadd+context.acc+"-"+context.region
    bucket_name="aws2tf-"+context.acc+"-"+context.region
    s3_prefix=''
    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            log.error(f"Bucket {bucket_name} does not exist. Cannot download.")
            return
        else:
            log.error(f"Error checking bucket {bucket_name}: {e}")
            return

    # Create the local directory if it doesn't exist
    os.makedirs(local_directory, exist_ok=True)

    # List objects in the bucket with the specified prefix
    paginator = s3_client.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' not in page:
            continue

        for obj in page['Contents']:
            # Skip the .terraform directory
            if '.terraform' in obj['Key']:
                continue

            # Get the relative path of the file
            relative_path = os.path.relpath(obj['Key'], s3_prefix)
            local_file_path = os.path.join(local_directory, relative_path)

            # Create the directory structure if it doesn't exist
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

            # Download the file
            try:
                s3_client.download_file(bucket_name, obj['Key'], local_file_path)
            except ClientError as e:
                log.error(f"Error downloading {obj['Key']}: {e}")

    log.info(f"Download from {bucket_name}/{s3_prefix} to {local_directory} completed.")

def trivy_check():
    # Get current directory and extract the last two parts
    mydir = os.getcwd()
    mydir = '/'.join(mydir.split('/')[-2:])

    # Check if jq is installed
    if shutil.which('jq') is None:
        log.warning("jq is not installed. skipping security report")
        return

    # Check if trivy is installed
    if shutil.which('trivy') is None:
        log.warning("trivy is not installed. skipping security report")
        return

    # Get trivy version
    try:
        trivy_version = subprocess.check_output(['trivy', 'version'], universal_newlines=True)
        ver = int(''.join(filter(str.isdigit, trivy_version.split('\n')[0].split(':')[1].strip())))
    except subprocess.CalledProcessError:
        log.error("Error getting trivy version")
        return

    if ver < 480:
        log.warning("Please upgrade trivy to version v0.48.0 or higher")
        return

    log.info("Generating trivy security report ....")
    
    with open('security-report.txt', 'w') as report:
        report.write("trivy security report\n")
        
        for severity in ['CRITICAL', 'HIGH']:
            report.write(f"{severity}:\n")
            try:
                output = subprocess.check_output(['trivy', 'fs', '--scanners', 'misconfig', '.', '-s', severity, '--format', 'json', '-q'], universal_newlines=True)
                results = json.loads(output)
                for result in results.get('Results', []):
                    misconfigurations = result.get('Misconfigurations', [])
                    if misconfigurations:
                        for misconfig in misconfigurations:
                            resource = misconfig.get('CauseMetadata', {}).get('Resource', '')
                            description = misconfig.get('Description', '')
                            references = misconfig.get('References', [])
                            report.write(json.dumps([resource, description, references]) + '\n')
            except subprocess.CalledProcessError:
                log.error(f"Error running trivy for {severity} severity")

    log.info(f"Trivy security report: {mydir}/security-report.txt")


def detect_aws_credentials(profile_name=None):
    """
    Detect the type of AWS credentials currently in use and check for SSO login.
    
    Args:
        profile_name (str, optional): AWS profile to check. If None, uses default or AWS_PROFILE env var.
    
    Returns a dictionary with credential information.
    """
    result = {
        'credential_type': None,
        'is_sso': False,
        'profile_name': None,
        'details': {},
        'status': 'unknown'
    }
    
    try:
        # Get session for specific profile or default
        if profile_name:
            session = boto3.Session(profile_name=profile_name)
        else:
            session = boto3.Session()
        
        credentials = session.get_credentials()
        
        if not credentials:
            result['status'] = 'no_credentials'
            return result
            
        result['status'] = 'found'
        
        # Check current profile
        actual_profile = session.profile_name or profile_name or os.environ.get('AWS_PROFILE', 'default')
        result['profile_name'] = actual_profile
        
        # Method 1: Check for ACTIVE SSO token cache that matches current session
        sso_cache_dir = Path.home() / '.aws' / 'sso' / 'cache'
        active_sso_tokens = []
        current_session_uses_sso = False
        
        if sso_cache_dir.exists():
            cache_files = list(sso_cache_dir.glob('*.json'))
            if cache_files:
                # First, we'll collect all valid tokens but not assume they're for current session
                for cache_file in cache_files:
                    try:
                        with open(cache_file, 'r') as f:
                            token_data = json.load(f)
                            expires_at_str = token_data.get('expiresAt', '')
                            if expires_at_str:
                                expires_at = datetime.fromisoformat(
                                    expires_at_str.replace('Z', '+00:00')
                                )
                                if expires_at > datetime.now(timezone.utc):
                                    active_sso_tokens.append({
                                        'file': cache_file.name,
                                        'expires_at': expires_at.isoformat(),
                                        'region': token_data.get('region', 'unknown'),
                                        'start_url': token_data.get('startUrl', 'unknown')
                                    })
                    except (json.JSONDecodeError, ValueError, KeyError):
                        continue
                
                # Store token info for debugging but don't use for detection yet
                result['details']['available_sso_tokens'] = active_sso_tokens
        
        # Method 2: Check AWS config file for SSO settings (but don't assume active SSO)
        config_file = Path.home() / '.aws' / 'config'
        sso_configured = False
        if config_file.exists():
            try:
                config = configparser.ConfigParser()
                config.read(config_file)
                
                # Check current profile and default profile for SSO settings
                profiles_to_check = []
                if actual_profile != 'default':
                    profiles_to_check.append(f'profile {actual_profile}')
                else:
                    profiles_to_check.append('default')
                
                for profile_section in profiles_to_check:
                    if profile_section in config:
                        section = config[profile_section]
                        if ('sso_start_url' in section or 
                            'sso_session' in section or 
                            'sso_account_id' in section or
                            'sso_role_name' in section):
                            sso_configured = True
                            
                            result['details']['sso_config'] = {
                                'profile': profile_section,
                                'sso_start_url': section.get('sso_start_url'),
                                'sso_region': section.get('sso_region'),
                                'sso_account_id': section.get('sso_account_id'),
                                'sso_role_name': section.get('sso_role_name'),
                                'sso_session': section.get('sso_session')
                            }
                            break
                            
            except Exception as e:
                result['details']['config_read_error'] = str(e)
        
        # Method 3: Check environment variables
        env_vars = {
            'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
            'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
            'AWS_SESSION_TOKEN': os.environ.get('AWS_SESSION_TOKEN'),
            'AWS_PROFILE': os.environ.get('AWS_PROFILE'),
            'AWS_REGION': os.environ.get('AWS_REGION'),
        }
        
        if env_vars['AWS_ACCESS_KEY_ID'] and env_vars['AWS_SECRET_ACCESS_KEY']:
            if env_vars['AWS_SESSION_TOKEN']:
                if result['credential_type'] is None:
                    result['credential_type'] = 'temporary_credentials'
            else:
                if result['credential_type'] is None:
                    result['credential_type'] = 'static_credentials'
        
        result['details']['environment_variables'] = {
            k: 'SET' if v else 'NOT_SET' for k, v in env_vars.items()
        }
        
        # Method 4: Check credential source using STS with the specified session
        # This is the DEFINITIVE method - the ARN tells us exactly what we're using
        try:
            sts = session.client('sts')
            caller_identity = sts.get_caller_identity()
            
            result['details']['caller_identity'] = {
                'user_id': caller_identity.get('UserId'),
                'account': caller_identity.get('Account'),
                'arn': caller_identity.get('Arn')
            }
            
            # The ARN is the definitive source of truth
            arn = caller_identity.get('Arn', '')
            if ':assumed-role/AWSReservedSSO_' in arn:
                # This IS definitely SSO - the ARN proves it
                result['is_sso'] = True
                result['credential_type'] = 'sso_assumed_role'
                current_session_uses_sso = True
                
                # Now find the matching SSO token for this session
                matching_tokens = []
                for token in active_sso_tokens:
                    # You could add more sophisticated matching here if needed
                    matching_tokens.append(token)
                result['details']['sso_tokens'] = matching_tokens
                
            elif ':assumed-role/' in arn:
                # Regular assumed role (not SSO)
                result['credential_type'] = 'assumed_role'
                result['is_sso'] = False
            elif ':user/' in arn:
                # IAM user - definitely not SSO for this session
                result['credential_type'] = 'iam_user'
                result['is_sso'] = False
            else:
                # Unknown ARN pattern
                result['credential_type'] = 'unknown_arn_pattern'
                result['is_sso'] = False
                
        except Exception as e:
            result['details']['sts_error'] = str(e)
        
        # Method 5: Check credentials source metadata
        if hasattr(credentials, 'method'):
            result['details']['credentials_method'] = credentials.method
            
        # If still unknown, make best guess based on what we found
        if result['credential_type'] is None:
            if result['is_sso']:
                result['credential_type'] = 'sso'
            elif sso_configured:
                result['credential_type'] = 'sso_configured_but_inactive'
            else:
                result['credential_type'] = 'unknown'
        
        # Add notes about SSO configuration vs actual usage
        if sso_configured and not result['is_sso']:
            result['details']['note'] = 'SSO is configured but current session is not using SSO'
        elif active_sso_tokens and not result['is_sso']:
            result['details']['note'] = 'Valid SSO tokens exist but current session is not using SSO'
                
    except Exception as e:
        result['status'] = 'error'
        result['details']['error'] = str(e)
    
    return result

def print_credentials_info(profile_name=None):
    """Print a formatted report of AWS credentials information."""
    info = detect_aws_credentials(profile_name)
    
    log.info("AWS Credentials Analysis")
    log.info("=" * 40)
    log.info(f"Status: {info['status']}")
    log.info(f"Profile: {info['profile_name']}")
    log.info(f"Credential Type: {info['credential_type']}")
    log.info(f"Using SSO: {'Yes' if info['is_sso'] else 'No'}")
    
    if info['details']:
        log.info("Details:")
        log.info("-" * 20)
        
        # Print caller identity if available
        if 'caller_identity' in info['details']:
            ci = info['details']['caller_identity']
            log.info(f"Account ID: {ci.get('account', 'N/A')}")
            log.info(f"User ARN: {ci.get('arn', 'N/A')}")
            log.info(f"User ID: {ci.get('user_id', 'N/A')}")
        
        # Print SSO token info if available and relevant
        if 'sso_tokens' in info['details'] and info['is_sso']:
            tokens = info['details']['sso_tokens']
            log.info(f"Active SSO Tokens for this session: {len(tokens)}")
            for token in tokens:
                log.info(f"  - Expires: {token['expires_at']}")
                log.info(f"    Region: {token['region']}")
        elif 'available_sso_tokens' in info['details']:
            tokens = info['details']['available_sso_tokens']
            log.info(f"Available SSO Tokens (not used by current session): {len(tokens)}")
        
        # Print SSO configuration if available
        if 'sso_config' in info['details']:
            sso_config = info['details']['sso_config']
            log.info("SSO Configuration:")
            log.info(f"  Profile: {sso_config.get('profile', 'N/A')}")
            log.info(f"  Start URL: {sso_config.get('sso_start_url', 'N/A')}")
            log.info(f"  Account ID: {sso_config.get('sso_account_id', 'N/A')}")
            log.info(f"  Role Name: {sso_config.get('sso_role_name', 'N/A')}")
        
        # Print environment variables
        if 'environment_variables' in info['details']:
            env_vars = info['details']['environment_variables']
            log.info("Environment Variables:")
            for var, status in env_vars.items():
                log.info(f"  {var}: {status}")
        
        # Print any important notes
        if 'note' in info['details']:
            log.info(f"Note: {info['details']['note']}")
        
        # Print any errors
        if 'error' in info['details']:
            log.error(f"Error: {info['details']['error']}")
        if 'sts_error' in info['details']:
            log.error(f"STS Error: {info['details']['sts_error']}")
