"""
Facade module for backward compatibility.

This module re-exports all public functions from the decomposed sub-modules
so that existing code using `import common` or `from common import X` continues
to work unchanged.
"""

# Standard library re-exports (some callers use common.boto3, common.os, etc.)
import boto3
import os
import sys
import json
import re
import glob
import shutil
import inspect
import subprocess
import botocore

# Re-export file operations
from file_ops import (
    safe_filename,
    safe_write_file,
    safe_write_sensitive_file,
    secure_terraform_files,
    get_file_permissions_info,
)

# Re-export error handling
from error_handler import (
    handle_error,
    handle_error2,
)

# Re-export dependency tracking
from dependency import (
    special_deps,
    add_known_dependancy,
    add_dependancy,
)

# Re-export import generation
from import_writer import (
    ref_skipped,
    is_self_ref,
    tfname,
    write_import,
    do_data,
)

# Re-export command runner utilities
from cmd_runner import (
    rc,
    splitf,
    splitf_old,
    fix_imports,
    ctrl_c_handler,
    check_python_version,
    aws_tf,
    log_warning,
)

# Re-export terraform runner
from terraform_runner import (
    run_terraform_plan_with_progress,
    run_terraform_command_with_spinner,
    get_import_count_from_plan,
    run_terraform_apply_with_progress,
    tfplan1,
    tfplan2,
    tfplan3,
    wrapup,
)

# Re-export resource processor
from resource_processor import (
    call_resource,
    getresource,
    call_boto3,
    get_test,
)

# Re-export S3 state operations
from s3_state import (
    create_bucket_if_not_exists,
    upload_directory_to_s3,
    empty_and_delete_bucket,
    download_from_s3,
)

# Re-export credentials utilities
from credentials import (
    detect_aws_credentials,
    print_credentials_info,
    trivy_check,
)

# Re-export module registry (dict and imports used by other modules)
from module_registry import (
    AWS_RESOURCE_MODULES,
    needid_dict,
    aws_no_import,
    aws_not_implemented,
)
