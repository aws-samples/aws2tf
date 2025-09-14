"""
Configuration management system for aws2tf.

This module provides a centralized configuration management system that replaces
the global variables pattern with proper dependency injection and encapsulation.
"""

from .config_manager import ConfigurationManager
from .config_categories import (
    ConfigCategory,
    AWSConfig,
    DebugConfig,
    ProcessingConfig,
    RuntimeConfig,
    ResourceConfig
)
from .factory import (
    create_test_config,
    create_production_config,
    create_debug_config,
    create_fast_config,
    create_serverless_config,
    create_config_from_dict,
    create_minimal_config
)
from .argument_parser import (
    create_argument_parser,
    parse_and_update_config,
    validate_argument_combinations,
    get_argument_summary
)
from .aws_credentials import (
    detect_aws_credentials,
    configure_aws_credentials,
    validate_aws_credentials,
    print_credentials_info,
    setup_aws_session_with_retry
)
from .utilities import (
    serialize_config,
    deserialize_config,
    save_config_to_file,
    load_config_from_file,
    compare_configs,
    merge_configs,
    create_config_backup,
    restore_config_from_backup,
    validate_config_file,
    get_config_summary,
    create_config_for_environment,
    cleanup_temp_configs,
    copy_config
)

__all__ = [
    'ConfigurationManager',
    'ConfigCategory',
    'AWSConfig',
    'DebugConfig',
    'ProcessingConfig',
    'RuntimeConfig',
    'ResourceConfig',
    'create_test_config',
    'create_production_config',
    'create_debug_config',
    'create_fast_config',
    'create_serverless_config',
    'create_config_from_dict',
    'create_minimal_config',
    'create_argument_parser',
    'parse_and_update_config',
    'validate_argument_combinations',
    'get_argument_summary',
    'detect_aws_credentials',
    'configure_aws_credentials',
    'validate_aws_credentials',
    'print_credentials_info',
    'setup_aws_session_with_retry',
    'serialize_config',
    'deserialize_config',
    'save_config_to_file',
    'load_config_from_file',
    'compare_configs',
    'merge_configs',
    'create_config_backup',
    'restore_config_from_backup',
    'validate_config_file',
    'get_config_summary',
    'create_config_for_environment',
    'cleanup_temp_configs',
    'copy_config'
]