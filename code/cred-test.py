import boto3
import json
import os
import configparser
from pathlib import Path
from datetime import datetime, timezone

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
    
    print("AWS Credentials Analysis")
    print("=" * 40)
    print(f"Status: {info['status']}")
    print(f"Profile: {info['profile_name']}")
    print(f"Credential Type: {info['credential_type']}")
    print(f"Using SSO: {'Yes' if info['is_sso'] else 'No'}")
    print()
    
    if info['details']:
        print("Details:")
        print("-" * 20)
        
        # Print caller identity if available
        if 'caller_identity' in info['details']:
            ci = info['details']['caller_identity']
            print(f"Account ID: {ci.get('account', 'N/A')}")
            print(f"User ARN: {ci.get('arn', 'N/A')}")
            print(f"User ID: {ci.get('user_id', 'N/A')}")
            print()
        
        # Print SSO token info if available and relevant
        if 'sso_tokens' in info['details'] and info['is_sso']:
            tokens = info['details']['sso_tokens']
            print(f"Active SSO Tokens for this session: {len(tokens)}")
            for token in tokens:
                print(f"  - Expires: {token['expires_at']}")
                print(f"    Region: {token['region']}")
            print()
        elif 'available_sso_tokens' in info['details']:
            tokens = info['details']['available_sso_tokens']
            print(f"Available SSO Tokens (not used by current session): {len(tokens)}")
            print()
        
        # Print SSO configuration if available
        if 'sso_config' in info['details']:
            sso_config = info['details']['sso_config']
            print("SSO Configuration:")
            print(f"  Profile: {sso_config.get('profile', 'N/A')}")
            print(f"  Start URL: {sso_config.get('sso_start_url', 'N/A')}")
            print(f"  Account ID: {sso_config.get('sso_account_id', 'N/A')}")
            print(f"  Role Name: {sso_config.get('sso_role_name', 'N/A')}")
            print()
        
        # Print environment variables
        if 'environment_variables' in info['details']:
            env_vars = info['details']['environment_variables']
            print("Environment Variables:")
            for var, status in env_vars.items():
                print(f"  {var}: {status}")
            print()
        
        # Print any important notes
        if 'note' in info['details']:
            print(f"Note: {info['details']['note']}")
            print()
        
        # Print any errors
        if 'error' in info['details']:
            print(f"Error: {info['details']['error']}")
        if 'sts_error' in info['details']:
            print(f"STS Error: {info['details']['sts_error']}")

if __name__ == "__main__":
    import sys
    
    # Simple argument parsing for profile
    profile = None
    if len(sys.argv) > 1:
        if sys.argv[1] == '--profile' and len(sys.argv) > 2:
            profile = sys.argv[2]
        else:
            profile = sys.argv[1]
    
    print_credentials_info(profile)