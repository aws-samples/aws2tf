"""
Configuration utility functions for aws2tf.

This module provides utility functions for working with configuration
instances, including serialization, comparison, and debugging helpers.
"""

import json
import os
from typing import Dict, Any, Optional, List
from pathlib import Path
import tempfile
import shutil

from .config_manager import ConfigurationManager
from .factory import create_test_config


def serialize_config(config: ConfigurationManager) -> Dict[str, Any]:
    """
    Serialize configuration to a dictionary.
    
    Args:
        config: Configuration manager to serialize.
        
    Returns:
        Dictionary representation of the configuration.
    """
    return {
        'aws': config.aws.to_dict(),
        'debug': config.debug.to_dict(),
        'processing': config.processing.to_dict(),
        'runtime': config.runtime.to_dict(),
        'resources': config.resources.to_dict()
    }


def deserialize_config(data: Dict[str, Any]) -> ConfigurationManager:
    """
    Deserialize configuration from a dictionary.
    
    Args:
        data: Dictionary containing configuration data.
        
    Returns:
        ConfigurationManager instance populated from the data.
    """
    config = ConfigurationManager()
    
    if 'aws' in data:
        config.aws.from_dict(data['aws'])
    if 'debug' in data:
        config.debug.from_dict(data['debug'])
    if 'processing' in data:
        config.processing.from_dict(data['processing'])
    if 'runtime' in data:
        config.runtime.from_dict(data['runtime'])
    if 'resources' in data:
        config.resources.from_dict(data['resources'])
    
    return config


def save_config_to_file(config: ConfigurationManager, file_path: str) -> None:
    """
    Save configuration to a JSON file.
    
    Args:
        config: Configuration manager to save.
        file_path: Path to save the configuration file.
    """
    data = serialize_config(config)
    
    # Create directory if it doesn't exist
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2, default=str)


def load_config_from_file(file_path: str) -> ConfigurationManager:
    """
    Load configuration from a JSON file.
    
    Args:
        file_path: Path to the configuration file.
        
    Returns:
        ConfigurationManager instance loaded from the file.
        
    Raises:
        FileNotFoundError: If the configuration file doesn't exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    return deserialize_config(data)


def compare_configs(config1: ConfigurationManager, config2: ConfigurationManager) -> Dict[str, Any]:
    """
    Compare two configuration instances and return differences.
    
    Args:
        config1: First configuration to compare.
        config2: Second configuration to compare.
        
    Returns:
        Dictionary containing differences between the configurations.
    """
    data1 = serialize_config(config1)
    data2 = serialize_config(config2)
    
    differences = {}
    
    for category in ['aws', 'debug', 'processing', 'runtime', 'resources']:
        category_diffs = {}
        
        if category in data1 and category in data2:
            for key in set(data1[category].keys()) | set(data2[category].keys()):
                val1 = data1[category].get(key)
                val2 = data2[category].get(key)
                
                if val1 != val2:
                    category_diffs[key] = {
                        'config1': val1,
                        'config2': val2
                    }
        
        if category_diffs:
            differences[category] = category_diffs
    
    return differences


def merge_configs(base_config: ConfigurationManager, override_config: ConfigurationManager) -> ConfigurationManager:
    """
    Merge two configurations, with override_config taking precedence.
    
    Args:
        base_config: Base configuration.
        override_config: Configuration with values to override.
        
    Returns:
        New ConfigurationManager with merged values.
    """
    # Serialize both configs
    base_data = serialize_config(base_config)
    override_data = serialize_config(override_config)
    
    # Merge the data
    merged_data = {}
    for category in ['aws', 'debug', 'processing', 'runtime', 'resources']:
        merged_data[category] = {}
        
        # Start with base values
        if category in base_data:
            merged_data[category].update(base_data[category])
        
        # Override with new values
        if category in override_data:
            merged_data[category].update(override_data[category])
    
    return deserialize_config(merged_data)


def create_config_backup(config: ConfigurationManager, backup_dir: Optional[str] = None) -> str:
    """
    Create a backup of the current configuration.
    
    Args:
        config: Configuration to backup.
        backup_dir: Directory to store the backup (defaults to temp directory).
        
    Returns:
        Path to the backup file.
    """
    if backup_dir is None:
        backup_dir = tempfile.gettempdir()
    
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"aws2tf_config_backup_{timestamp}.json")
    
    save_config_to_file(config, backup_file)
    return backup_file


def restore_config_from_backup(backup_file: str) -> ConfigurationManager:
    """
    Restore configuration from a backup file.
    
    Args:
        backup_file: Path to the backup file.
        
    Returns:
        ConfigurationManager instance restored from backup.
    """
    return load_config_from_file(backup_file)


def validate_config_file(file_path: str) -> Dict[str, Any]:
    """
    Validate a configuration file without loading it.
    
    Args:
        file_path: Path to the configuration file.
        
    Returns:
        Dictionary with validation results.
    """
    result = {
        'valid': False,
        'errors': [],
        'warnings': []
    }
    
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            result['errors'].append(f"Configuration file not found: {file_path}")
            return result
        
        # Try to parse JSON
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Check required categories
        required_categories = ['aws', 'debug', 'processing', 'runtime', 'resources']
        for category in required_categories:
            if category not in data:
                result['warnings'].append(f"Missing configuration category: {category}")
        
        # Try to create config from data
        config = deserialize_config(data)
        
        # Validate the configuration
        validation_errors = config.validate_all()
        if validation_errors:
            result['errors'].extend(validation_errors)
        else:
            result['valid'] = True
        
    except json.JSONDecodeError as e:
        result['errors'].append(f"Invalid JSON in configuration file: {str(e)}")
    except Exception as e:
        result['errors'].append(f"Error validating configuration file: {str(e)}")
    
    return result


def get_config_summary(config: ConfigurationManager) -> Dict[str, Any]:
    """
    Get a summary of the configuration for logging/debugging.
    
    Args:
        config: Configuration to summarize.
        
    Returns:
        Dictionary containing configuration summary.
    """
    summary = {
        'aws': {
            'profile': config.aws.profile,
            'region': config.aws.region,
            'credential_type': config.aws.credential_type,
            'is_sso': config.aws.is_sso,
            'account_id': config.aws.account_id[:8] + '****' if config.aws.account_id != 'xxxxxxxxxxxx' else config.aws.account_id
        },
        'debug': {
            'enabled': config.debug.enabled,
            'debug5': config.debug.debug5,
            'log_level': config.debug.log_level,
            'fast_mode': config.runtime.fast
        },
        'processing': {
            'cores': config.processing.cores,
            'total_resources': config.processing.total_resources,
            'processed_resources': config.processing.processed_resources,
            'progress_percentage': config.processing.get_progress_percentage()
        },
        'runtime': {
            'mode': config.runtime.get_runtime_mode(),
            'serverless': config.runtime.serverless,
            'has_ec2_filter': config.runtime.has_ec2_tag_filter(),
            'data_sources_enabled': config.runtime.is_any_data_source_enabled()
        },
        'resources': {
            'resource_counts': config.resources.get_all_resource_counts(),
            'cache_stats': config.resources.get_cache_stats(),
            'bad_resources': len(config.resources.badlist)
        }
    }
    
    return summary


def create_config_for_environment(environment: str, **overrides) -> ConfigurationManager:
    """
    Create a configuration tailored for a specific environment.
    
    Args:
        environment: Environment name (dev, staging, prod, test).
        **overrides: Additional configuration overrides.
        
    Returns:
        ConfigurationManager configured for the environment.
    """
    if environment.lower() in ['dev', 'development']:
        config = create_test_config()
        config.debug.enabled = True
        config.debug.log_level = 'DEBUG'
        config.processing.cores = 2
        
    elif environment.lower() in ['staging', 'stage']:
        config = create_test_config()
        config.debug.enabled = False
        config.debug.log_level = 'INFO'
        config.processing.cores = 4
        config.runtime.fast = True
        
    elif environment.lower() in ['prod', 'production']:
        config = create_test_config()
        config.debug.enabled = False
        config.debug.log_level = 'WARNING'
        config.processing.cores = 8
        config.runtime.fast = True
        
    elif environment.lower() == 'test':
        config = create_test_config()
        config.debug.enabled = True
        config.debug.log_level = 'DEBUG'
        config.processing.cores = 1
        
    else:
        # Default to test configuration
        config = create_test_config()
    
    # Apply any overrides
    for key, value in overrides.items():
        if '.' in key:
            category, field = key.split('.', 1)
            if hasattr(config, category):
                category_obj = getattr(config, category)
                if hasattr(category_obj, field):
                    setattr(category_obj, field, value)
    
    return config


def cleanup_temp_configs(temp_dir: Optional[str] = None) -> int:
    """
    Clean up temporary configuration files.
    
    Args:
        temp_dir: Directory to clean (defaults to system temp directory).
        
    Returns:
        Number of files cleaned up.
    """
    if temp_dir is None:
        temp_dir = tempfile.gettempdir()
    
    cleanup_count = 0
    
    try:
        for file_name in os.listdir(temp_dir):
            if file_name.startswith('aws2tf_config_backup_') and file_name.endswith('.json'):
                file_path = os.path.join(temp_dir, file_name)
                try:
                    os.remove(file_path)
                    cleanup_count += 1
                except OSError:
                    pass  # Ignore errors removing individual files
    except OSError:
        pass  # Ignore errors listing directory
    
    return cleanup_count


def copy_config(config: ConfigurationManager) -> ConfigurationManager:
    """
    Create a deep copy of a configuration.
    
    Args:
        config: Configuration to copy.
        
    Returns:
        New ConfigurationManager instance with copied values.
    """
    data = serialize_config(config)
    return deserialize_config(data)