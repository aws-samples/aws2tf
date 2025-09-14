"""
AWS credential detection and configuration integration.

This module provides functions to detect AWS credentials and integrate
them with the configuration management system.
"""

import os
import json
import configparser
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Any, Optional
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

from .config_manager import ConfigurationManager


def detect_aws_credentials(profile_name: Optional[str] = None) -> Dict[str, Any]:
    """
    Detect the type of AWS credentials currently in use and check for SSO login.
    
    Args:
        profile_name: AWS profile to check. If None, uses default or AWS_PROFILE env var.
    
    Returns:
        Dictionary with credential information.
    """
    result = {
        'credential_type': 'invalid',
        'is_sso': False,
        'profile_name': None,
        'account_id': None,
        'region': None,
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
        
        # Get region
        result['region'] = session.region_name or os.environ.get('AWS_REGION', 'us-east-1')
        
        # Method 1: Check for ACTIVE SSO token cache
        sso_cache_dir = Path.home() / '.aws' / 'sso' / 'cache'
        active_sso_tokens = []
        
        if sso_cache_dir.exists():
            cache_files = list(sso_cache_dir.glob('*.json'))
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
            
            result['details']['available_sso_tokens'] = active_sso_tokens
        
        # Method 2: Check AWS config file for SSO settings
        config_file = Path.home() / '.aws' / 'config'
        sso_configured = False
        if config_file.exists():
            try:
                config = configparser.ConfigParser()
                config.read(config_file)
                
                # Check current profile for SSO settings
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
                result['credential_type'] = 'temporary_credentials'
            else:
                result['credential_type'] = 'static_credentials'
        
        result['details']['environment_variables'] = {
            k: 'SET' if v else 'NOT_SET' for k, v in env_vars.items()
        }
        
        # Method 4: Check credential source using STS (definitive method)
        try:
            sts = session.client('sts')
            caller_identity = sts.get_caller_identity()
            
            result['account_id'] = caller_identity.get('Account')
            result['details']['caller_identity'] = {
                'user_id': caller_identity.get('UserId'),
                'account': caller_identity.get('Account'),
                'arn': caller_identity.get('Arn')
            }
            
            # The ARN is the definitive source of truth
            arn = caller_identity.get('Arn', '')
            if ':assumed-role/AWSReservedSSO_' in arn:
                # This IS definitely SSO
                result['is_sso'] = True
                result['credential_type'] = 'sso'
            elif ':assumed-role/' in arn:
                # Regular assumed role (not SSO)
                result['credential_type'] = 'assumed_role'
                result['is_sso'] = False
            elif ':user/' in arn:
                # IAM user
                result['credential_type'] = 'iam_user'
                result['is_sso'] = False
            else:
                # Unknown ARN pattern
                result['credential_type'] = 'unknown'
                result['is_sso'] = False
                
        except (ClientError, NoCredentialsError) as e:
            result['details']['sts_error'] = str(e)
            result['credential_type'] = 'invalid'
        
        # Method 5: Check credentials source metadata
        if hasattr(credentials, 'method'):
            result['details']['credentials_method'] = credentials.method
        
        # If still unknown, make best guess
        if result['credential_type'] == 'invalid':
            if sso_configured:
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
        result['credential_type'] = 'invalid'
    
    return result


def configure_aws_credentials(config: ConfigurationManager, profile_name: Optional[str] = None) -> bool:
    """
    Detect and configure AWS credentials in the configuration manager.
    
    Args:
        config: Configuration manager to update.
        profile_name: AWS profile to use for detection.
        
    Returns:
        True if credentials were successfully detected and configured.
    """
    # Use profile from config if not specified
    if profile_name is None:
        profile_name = config.aws.profile
    
    # Detect credentials
    cred_info = detect_aws_credentials(profile_name)
    
    # Update configuration with detected information
    config.aws.credential_type = cred_info['credential_type']
    config.aws.is_sso = cred_info['is_sso']
    
    if cred_info['profile_name']:
        config.aws.profile = cred_info['profile_name']
    
    if cred_info['account_id']:
        config.aws.account_id = cred_info['account_id']
    
    if cred_info['region']:
        config.aws.region = cred_info['region']
    
    # Store SSO instance if available
    sso_config = cred_info['details'].get('sso_config', {})
    if sso_config.get('sso_start_url'):
        config.aws.sso_instance = sso_config['sso_start_url']
    
    return cred_info['status'] == 'found' and cred_info['credential_type'] != 'invalid'


def validate_aws_credentials(config: ConfigurationManager) -> Dict[str, Any]:
    """
    Validate AWS credentials configuration.
    
    Args:
        config: Configuration manager to validate.
        
    Returns:
        Dictionary with validation results.
    """
    result = {
        'valid': False,
        'can_make_api_calls': False,
        'errors': [],
        'warnings': []
    }
    
    # Check basic configuration
    if config.aws.credential_type == 'invalid':
        result['errors'].append('No valid AWS credentials detected')
        return result
    
    if config.aws.region == 'xx-xxxx-x':
        result['errors'].append('AWS region not properly configured')
    
    if config.aws.account_id == 'xxxxxxxxxxxx':
        result['warnings'].append('AWS account ID not detected')
    
    # Test API access
    try:
        session = config.get_aws_session()
        sts = session.client('sts')
        caller_identity = sts.get_caller_identity()
        
        result['can_make_api_calls'] = True
        result['account_id'] = caller_identity.get('Account')
        result['user_arn'] = caller_identity.get('Arn')
        
    except Exception as e:
        result['errors'].append(f'Cannot make AWS API calls: {str(e)}')
        result['can_make_api_calls'] = False
    
    # Overall validation
    result['valid'] = len(result['errors']) == 0 and result['can_make_api_calls']
    
    return result


def print_credentials_info(config: ConfigurationManager) -> None:
    """
    Print formatted AWS credentials information.
    
    Args:
        config: Configuration manager with AWS credentials.
    """
    print("AWS Credentials Analysis")
    print("=" * 50)
    
    print(f"Profile: {config.aws.profile}")
    print(f"Region: {config.aws.region}")
    print(f"Account ID: {config.aws.account_id}")
    print(f"Credential Type: {config.aws.credential_type}")
    print(f"Is SSO: {config.aws.is_sso}")
    
    if config.aws.sso_instance:
        print(f"SSO Instance: {config.aws.sso_instance}")
    
    # Validate credentials
    validation = validate_aws_credentials(config)
    
    print(f"\nValidation Status: {'VALID' if validation['valid'] else 'INVALID'}")
    print(f"Can Make API Calls: {'YES' if validation['can_make_api_calls'] else 'NO'}")
    
    if validation['errors']:
        print("\nErrors:")
        for error in validation['errors']:
            print(f"  - {error}")
    
    if validation['warnings']:
        print("\nWarnings:")
        for warning in validation['warnings']:
            print(f"  - {warning}")


def setup_aws_session_with_retry(config: ConfigurationManager, max_retries: int = 3) -> boto3.Session:
    """
    Set up AWS session with retry logic for credential issues.
    
    Args:
        config: Configuration manager.
        max_retries: Maximum number of retry attempts.
        
    Returns:
        Configured boto3 session.
        
    Raises:
        Exception: If session setup fails after all retries.
    """
    for attempt in range(max_retries):
        try:
            # Try to configure credentials
            if configure_aws_credentials(config):
                session = config.get_aws_session()
                
                # Test the session
                sts = session.client('sts')
                sts.get_caller_identity()
                
                return session
                
        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to set up AWS session after {max_retries} attempts: {str(e)}")
            
            # Wait and retry (could add exponential backoff here)
            continue
    
    raise Exception("Failed to set up AWS session")