"""
Shared pytest fixtures for aws2tf test suite.

This module provides reusable fixtures for:
- Mocking boto3 AWS clients
- Initializing and resetting context state
- Creating temporary workspaces
- Mocking terraform command execution
"""

import os
import sys
from pathlib import Path
from unittest import mock

import pytest
from moto import mock_aws

# Add code directory to path so we can import modules
sys.path.insert(0, str(Path(__file__).parent.parent / 'code'))

import context


@pytest.fixture
def mock_boto3_client():
    """
    Mock boto3 client with configurable responses for common AWS services.
    
    Usage:
        def test_something(mock_boto3_client):
            # Configure mock responses
            mock_boto3_client.return_value.describe_vpcs.return_value = {
                'Vpcs': [{'VpcId': 'vpc-123', 'CidrBlock': '10.0.0.0/16'}]
            }
            
            # Your test code here
    """
    with mock.patch('boto3.client') as mock_client:
        # Configure default responses for common operations
        mock_instance = mock.MagicMock()
        
        # EC2 defaults
        mock_instance.describe_vpcs.return_value = {'Vpcs': []}
        mock_instance.describe_subnets.return_value = {'Subnets': []}
        mock_instance.describe_security_groups.return_value = {'SecurityGroups': []}
        mock_instance.describe_instances.return_value = {'Reservations': []}
        mock_instance.describe_transit_gateways.return_value = {'TransitGateways': []}
        mock_instance.describe_launch_templates.return_value = {'LaunchTemplates': []}
        
        # S3 defaults
        mock_instance.list_buckets.return_value = {'Buckets': []}
        mock_instance.list_objects_v2.return_value = {'Contents': []}
        
        # Lambda defaults
        mock_instance.list_functions.return_value = {'Functions': []}
        
        # IAM defaults
        mock_instance.list_roles.return_value = {'Roles': []}
        mock_instance.list_policies.return_value = {'Policies': []}
        mock_instance.list_instance_profiles.return_value = {'InstanceProfiles': []}
        mock_instance.list_attached_role_policies.return_value = {'AttachedPolicies': []}
        mock_instance.list_role_policies.return_value = {'PolicyNames': []}
        
        # STS defaults
        mock_instance.get_caller_identity.return_value = {'Account': '123456789012'}
        
        # Configure paginator support
        def get_paginator(operation_name):
            paginator = mock.MagicMock()
            paginator.paginate.return_value = []
            return paginator
        
        mock_instance.get_paginator = get_paginator
        mock_client.return_value = mock_instance
        
        yield mock_client


@pytest.fixture
def mock_context():
    """
    Initialize context with test defaults and reset after test.
    
    This fixture ensures context is in a known state before each test
    and cleans up after the test completes.
    
    Usage:
        def test_something(mock_context):
            assert mock_context.region == 'us-east-1'
            # Your test code here
    """
    # Save original values
    original_values = {}
    for attr in dir(context):
        if not attr.startswith('_') and not callable(getattr(context, attr)):
            original_values[attr] = getattr(context, attr)
    
    # Set test defaults
    context.region = 'us-east-1'
    context.acc = '123456789012'
    context.profile = 'default'
    context.debug = False
    context.debug5 = False
    context.fast = False
    context.merge = False
    context.validate = False
    context.warnings = False
    context.show_status = False
    context.expected = False
    context.serverless = False
    context.credtype = 'environment'
    context.sso = False
    
    # Initialize dictionaries
    context.rproc = {}
    context.rdep = {}
    context.trdep = {}
    context.subnetlist = {}
    context.sglist = {}
    context.vpclist = {}
    context.ltlist = {}
    context.lambdalist = {}
    context.s3list = {}
    context.rolelist = {}
    context.policylist = {}
    context.inplist = {}
    context.bucketlist = {}
    context.tgwlist = {}
    context.gluedbs = {}
    context.attached_role_policies_list = {}
    context.role_policies_list = {}
    
    # Initialize lists
    context.processed = []
    context.dependancies = []
    context.types = []
    context.all_extypes = []
    context.badlist = []
    context.policies = []
    context.policyarns = []
    context.roles = []
    
    # Initialize paths
    context.cwd = os.getcwd()
    context.path1 = ""
    context.path2 = ""
    context.path3 = ""
    
    # Initialize progress tracking
    context.terraform_plan_rate = 25.0
    context.terraform_plan_samples = 0
    context.terraform_apply_rate = 50.0
    context.terraform_apply_samples = 0
    context.last_plan_time = 0.0
    
    yield context
    
    # Restore original values
    for attr, value in original_values.items():
        setattr(context, attr, value)


@pytest.fixture
def temp_workspace(tmp_path):
    """
    Create temporary workspace directory structure for testing.
    
    Creates:
    - workspace/
    - workspace/generated/
    - workspace/generated/tf-123456789012-us-east-1/
    - workspace/generated/tf-123456789012-us-east-1/imported/
    - workspace/generated/tf-123456789012-us-east-1/notimported/
    
    Usage:
        def test_something(temp_workspace):
            # temp_workspace is a Path object
            assert temp_workspace.exists()
            generated_dir = temp_workspace / "generated"
            assert generated_dir.exists()
    """
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    
    generated = workspace / "generated"
    generated.mkdir()
    
    tf_dir = generated / "tf-123456789012-us-east-1"
    tf_dir.mkdir()
    
    imported = tf_dir / "imported"
    imported.mkdir()
    
    notimported = tf_dir / "notimported"
    notimported.mkdir()
    
    return workspace


@pytest.fixture
def mock_terraform():
    """
    Mock terraform command execution via common.rc().
    
    Provides default responses for common terraform commands:
    - terraform version
    - terraform init
    - terraform validate
    - terraform plan
    - terraform apply
    
    Usage:
        def test_something(mock_terraform):
            # Configure specific response
            mock_terraform.return_value.stdout.decode.return_value = "Success"
            mock_terraform.return_value.returncode = 0
            
            # Your test code here
    """
    with mock.patch('common.rc') as mock_rc:
        # Create mock result object
        mock_result = mock.MagicMock()
        mock_result.returncode = 0
        mock_result.stdout.decode.return_value = "Terraform v1.9.5\n"
        mock_result.stderr.decode.return_value = ""
        
        mock_rc.return_value = mock_result
        
        yield mock_rc


@pytest.fixture(autouse=True)
def reset_context():
    """
    Automatically reset context before and after each test.
    
    This fixture runs automatically for every test (autouse=True)
    to ensure test isolation. Tests don't need to explicitly use this fixture.
    """
    # Reset dictionaries before test
    context.rproc = {}
    context.rdep = {}
    context.trdep = {}
    context.subnetlist = {}
    context.sglist = {}
    context.vpclist = {}
    context.ltlist = {}
    context.lambdalist = {}
    context.s3list = {}
    context.rolelist = {}
    context.policylist = {}
    context.inplist = {}
    context.bucketlist = {}
    context.tgwlist = {}
    context.gluedbs = {}
    context.attached_role_policies_list = {}
    context.role_policies_list = {}
    
    # Reset lists
    context.processed = []
    context.dependancies = []
    context.types = []
    context.all_extypes = []
    context.badlist = []
    
    yield
    
    # Reset again after test
    context.rproc = {}
    context.rdep = {}
    context.trdep = {}
    context.subnetlist = {}
    context.sglist = {}
    context.vpclist = {}
    context.ltlist = {}
    context.lambdalist = {}
    context.s3list = {}
    context.rolelist = {}
    context.policylist = {}
    context.inplist = {}
    context.bucketlist = {}
    context.tgwlist = {}
    context.gluedbs = {}
    context.attached_role_policies_list = {}
    context.role_policies_list = {}
    context.processed = []
    context.dependancies = []
    context.types = []
    context.all_extypes = []
    context.badlist = []


@pytest.fixture
def mock_aws_session():
    """
    Mock AWS session setup with moto.
    
    This fixture uses moto's @mock_aws decorator to mock AWS services.
    Use this for integration tests that need realistic AWS API responses.
    
    Usage:
        def test_something(mock_aws_session):
            import boto3
            # Create real boto3 client (mocked by moto)
            ec2 = boto3.client('ec2', region_name='us-east-1')
            
            # Create resources
            vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
            
            # Test your code
    """
    with mock_aws():
        yield


@pytest.fixture
def sample_vpc_response():
    """
    Sample VPC response data for testing.
    
    Returns a realistic VPC describe_vpcs response structure.
    """
    return {
        'Vpcs': [
            {
                'VpcId': 'vpc-12345678',
                'CidrBlock': '10.0.0.0/16',
                'State': 'available',
                'Tags': [
                    {'Key': 'Name', 'Value': 'test-vpc'},
                    {'Key': 'Environment', 'Value': 'test'}
                ],
                'IsDefault': False,
                'InstanceTenancy': 'default',
                'EnableDnsHostnames': True,
                'EnableDnsSupport': True
            }
        ]
    }


@pytest.fixture
def sample_lambda_response():
    """
    Sample Lambda function response data for testing.
    
    Returns a realistic Lambda list_functions response structure.
    """
    return {
        'Functions': [
            {
                'FunctionName': 'test-function',
                'FunctionArn': 'arn:aws:lambda:us-east-1:123456789012:function:test-function',
                'Runtime': 'python3.12',
                'Handler': 'index.handler',
                'Role': 'arn:aws:iam::123456789012:role/lambda-role',
                'CodeSize': 1024,
                'Description': 'Test Lambda function',
                'Timeout': 30,
                'MemorySize': 128,
                'LastModified': '2024-01-01T00:00:00.000+0000',
                'Environment': {
                    'Variables': {
                        'ENV': 'test'
                    }
                }
            }
        ]
    }


@pytest.fixture
def sample_s3_response():
    """
    Sample S3 bucket response data for testing.
    
    Returns a realistic S3 list_buckets response structure.
    """
    return {
        'Buckets': [
            {
                'Name': 'test-bucket-123456',
                'CreationDate': '2024-01-01T00:00:00.000Z'
            }
        ],
        'Owner': {
            'DisplayName': 'test-owner',
            'ID': 'abc123'
        }
    }


@pytest.fixture
def sample_iam_role_response():
    """
    Sample IAM role response data for testing.
    
    Returns a realistic IAM list_roles response structure.
    """
    return {
        'Roles': [
            {
                'RoleName': 'test-role',
                'RoleId': 'AIDACKCEVSQ6C2EXAMPLE',
                'Arn': 'arn:aws:iam::123456789012:role/test-role',
                'CreateDate': '2024-01-01T00:00:00.000Z',
                'AssumeRolePolicyDocument': {
                    'Version': '2012-10-17',
                    'Statement': [
                        {
                            'Effect': 'Allow',
                            'Principal': {
                                'Service': 'lambda.amazonaws.com'
                            },
                            'Action': 'sts:AssumeRole'
                        }
                    ]
                },
                'Path': '/',
                'MaxSessionDuration': 3600
            }
        ]
    }
