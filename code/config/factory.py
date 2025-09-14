"""
Factory functions for creating configuration instances.

This module provides convenient factory functions for creating ConfigurationManager
instances with specific configurations, particularly useful for testing.
"""

from typing import Dict, Any, Optional
from .config_manager import ConfigurationManager


def create_test_config(**overrides) -> ConfigurationManager:
    """
    Create a ConfigurationManager instance with test-friendly defaults.
    
    Args:
        **overrides: Configuration values to override defaults.
        
    Returns:
        ConfigurationManager instance configured for testing.
    """
    config = ConfigurationManager()
    
    # Set test-friendly AWS defaults
    config.aws.region = overrides.get('region', 'us-east-1')
    config.aws.account_id = overrides.get('account_id', '123456789012')
    config.aws.credential_type = overrides.get('credential_type', 'profile')
    config.aws.profile = overrides.get('profile', 'test-profile')
    
    # Set debug defaults
    config.debug.enabled = overrides.get('debug', False)
    config.debug.debug5 = overrides.get('debug5', False)
    config.debug.validate_mode = overrides.get('validate', False)
    config.debug.fast = overrides.get('fast', False)
    
    # Set processing defaults
    config.processing.cores = overrides.get('cores', 2)
    config.processing.estimated_time = overrides.get('estimated_time', 60.0)
    
    # Set runtime defaults
    config.runtime.merge = overrides.get('merge', False)
    config.runtime.serverless = overrides.get('serverless', False)
    config.runtime.expected = overrides.get('expected', False)
    
    # Apply any additional overrides
    for key, value in overrides.items():
        if '.' in key:
            # Handle nested configuration like 'aws.region'
            category, field = key.split('.', 1)
            if hasattr(config, category):
                category_obj = getattr(config, category)
                if hasattr(category_obj, field):
                    setattr(category_obj, field, value)
    
    return config


def create_production_config() -> ConfigurationManager:
    """
    Create a ConfigurationManager instance with production defaults.
    
    Returns:
        ConfigurationManager instance configured for production use.
    """
    config = ConfigurationManager()
    
    # Production typically uses more cores
    config.processing.cores = 8
    
    # Production might have different timeouts
    config.processing.estimated_time = 300.0
    
    return config


def create_debug_config() -> ConfigurationManager:
    """
    Create a ConfigurationManager instance with debug mode enabled.
    
    Returns:
        ConfigurationManager instance configured for debugging.
    """
    config = create_test_config()
    
    config.debug.enabled = True
    config.debug.debug5 = True
    config.runtime.fast = False  # Debug disables fast mode
    
    return config


def create_fast_config() -> ConfigurationManager:
    """
    Create a ConfigurationManager instance with fast mode enabled.
    
    Returns:
        ConfigurationManager instance configured for fast processing.
    """
    config = create_test_config()
    
    config.runtime.fast = True
    config.debug.enabled = False  # Fast mode typically disables debug
    config.processing.cores = 16  # Use more cores in fast mode
    
    return config


def create_serverless_config() -> ConfigurationManager:
    """
    Create a ConfigurationManager instance configured for serverless execution.
    
    Returns:
        ConfigurationManager instance configured for serverless mode.
    """
    config = create_test_config()
    
    config.runtime.serverless = True
    config.processing.cores = 4  # Serverless might have limited cores
    
    return config


def create_config_from_dict(config_dict: Dict[str, Any]) -> ConfigurationManager:
    """
    Create a ConfigurationManager instance from a dictionary configuration.
    
    Args:
        config_dict: Dictionary containing configuration values.
        
    Returns:
        ConfigurationManager instance populated from the dictionary.
    """
    config = ConfigurationManager()
    
    # Update each category from the dictionary
    if 'aws' in config_dict:
        config.aws.from_dict(config_dict['aws'])
    
    if 'debug' in config_dict:
        config.debug.from_dict(config_dict['debug'])
    
    if 'processing' in config_dict:
        config.processing.from_dict(config_dict['processing'])
    
    if 'runtime' in config_dict:
        config.runtime.from_dict(config_dict['runtime'])
    
    if 'resources' in config_dict:
        config.resources.from_dict(config_dict['resources'])
    
    return config


def create_minimal_config() -> ConfigurationManager:
    """
    Create a ConfigurationManager instance with minimal valid configuration.
    
    Returns:
        ConfigurationManager instance with minimal valid settings.
    """
    config = ConfigurationManager()
    
    # Set minimal valid AWS configuration
    config.aws.region = "us-east-1"
    config.aws.account_id = "123456789012"
    config.aws.credential_type = "profile"
    
    return config