"""AWS credential detection utilities for aws2tf."""

import boto3
import os
import json
import subprocess
import shutil
import context
import logging
from pathlib import Path
from datetime import datetime, timezone
import configparser

log = logging.getLogger('aws2tf')


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
