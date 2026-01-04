"""
Test that shared fixtures work correctly.

This module verifies that all fixtures in conftest.py are properly configured
and provide the expected functionality.
"""

import os
from pathlib import Path


def test_mock_boto3_client_fixture(mock_boto3_client):
    """Test that mock_boto3_client fixture provides mocked AWS client."""
    import boto3
    
    # Create a client
    client = boto3.client('ec2', region_name='us-east-1')
    
    # Verify it's mocked
    assert mock_boto3_client.called
    
    # Verify default responses work
    vpcs = client.describe_vpcs()
    assert 'Vpcs' in vpcs
    assert isinstance(vpcs['Vpcs'], list)


def test_mock_context_fixture(mock_context):
    """Test that mock_context fixture initializes context correctly."""
    # Verify basic attributes
    assert mock_context.region == 'us-east-1'
    assert mock_context.acc == '123456789012'
    assert mock_context.profile == 'default'
    assert mock_context.debug is False
    assert mock_context.fast is False
    
    # Verify dictionaries are initialized
    assert isinstance(mock_context.rproc, dict)
    assert isinstance(mock_context.vpclist, dict)
    assert isinstance(mock_context.lambdalist, dict)
    assert isinstance(mock_context.s3list, dict)
    
    # Verify lists are initialized
    assert isinstance(mock_context.processed, list)
    assert isinstance(mock_context.dependancies, list)
    
    # Verify progress tracking is initialized
    assert mock_context.terraform_plan_rate == 25.0
    assert mock_context.terraform_plan_samples == 0


def test_temp_workspace_fixture(temp_workspace):
    """Test that temp_workspace fixture creates directory structure."""
    # Verify workspace exists
    assert temp_workspace.exists()
    assert temp_workspace.is_dir()
    
    # Verify generated directory exists
    generated = temp_workspace / "generated"
    assert generated.exists()
    assert generated.is_dir()
    
    # Verify tf directory exists
    tf_dir = generated / "tf-123456789012-us-east-1"
    assert tf_dir.exists()
    assert tf_dir.is_dir()
    
    # Verify imported directory exists
    imported = tf_dir / "imported"
    assert imported.exists()
    assert imported.is_dir()
    
    # Verify notimported directory exists
    notimported = tf_dir / "notimported"
    assert notimported.exists()
    assert notimported.is_dir()


def test_temp_workspace_is_writable(temp_workspace):
    """Test that temp_workspace is writable."""
    test_file = temp_workspace / "test.txt"
    test_file.write_text("test content")
    
    assert test_file.exists()
    assert test_file.read_text() == "test content"


def test_mock_terraform_fixture(mock_terraform):
    """Test that mock_terraform fixture mocks terraform commands."""
    # Verify mock is configured
    result = mock_terraform.return_value
    assert result.returncode == 0
    assert "Terraform" in result.stdout.decode.return_value


def test_reset_context_fixture_isolation():
    """Test that reset_context fixture ensures test isolation."""
    import context
    
    # Modify context
    context.vpclist['vpc-123'] = True
    context.processed.append('test-item')
    
    # Verify modifications
    assert 'vpc-123' in context.vpclist
    assert 'test-item' in context.processed


def test_reset_context_fixture_isolation_part2():
    """Test that context was reset from previous test."""
    import context
    
    # Verify context was reset (previous test's modifications are gone)
    assert 'vpc-123' not in context.vpclist
    assert 'test-item' not in context.processed
    assert len(context.vpclist) == 0
    assert len(context.processed) == 0


def test_sample_vpc_response_fixture(sample_vpc_response):
    """Test that sample_vpc_response fixture provides valid data."""
    assert 'Vpcs' in sample_vpc_response
    assert len(sample_vpc_response['Vpcs']) == 1
    
    vpc = sample_vpc_response['Vpcs'][0]
    assert vpc['VpcId'] == 'vpc-12345678'
    assert vpc['CidrBlock'] == '10.0.0.0/16'
    assert vpc['State'] == 'available'


def test_sample_lambda_response_fixture(sample_lambda_response):
    """Test that sample_lambda_response fixture provides valid data."""
    assert 'Functions' in sample_lambda_response
    assert len(sample_lambda_response['Functions']) == 1
    
    function = sample_lambda_response['Functions'][0]
    assert function['FunctionName'] == 'test-function'
    assert function['Runtime'] == 'python3.12'
    assert function['Handler'] == 'index.handler'


def test_sample_s3_response_fixture(sample_s3_response):
    """Test that sample_s3_response fixture provides valid data."""
    assert 'Buckets' in sample_s3_response
    assert len(sample_s3_response['Buckets']) == 1
    
    bucket = sample_s3_response['Buckets'][0]
    assert bucket['Name'] == 'test-bucket-123456'
    assert 'CreationDate' in bucket


def test_sample_iam_role_response_fixture(sample_iam_role_response):
    """Test that sample_iam_role_response fixture provides valid data."""
    assert 'Roles' in sample_iam_role_response
    assert len(sample_iam_role_response['Roles']) == 1
    
    role = sample_iam_role_response['Roles'][0]
    assert role['RoleName'] == 'test-role'
    assert 'Arn' in role
    assert 'AssumeRolePolicyDocument' in role


def test_mock_aws_session_fixture(mock_aws_session):
    """Test that mock_aws_session fixture provides mocked AWS services."""
    import boto3
    
    # Create a real boto3 client (mocked by moto)
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    # Create a VPC
    response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = response['Vpc']['VpcId']
    
    # Verify we can describe it
    vpcs = ec2.describe_vpcs(VpcIds=[vpc_id])
    assert len(vpcs['Vpcs']) == 1
    assert vpcs['Vpcs'][0]['CidrBlock'] == '10.0.0.0/16'


def test_fixtures_can_be_combined(mock_context, temp_workspace, mock_boto3_client):
    """Test that multiple fixtures can be used together."""
    # Verify all fixtures are available
    assert mock_context.region == 'us-east-1'
    assert temp_workspace.exists()
    assert mock_boto3_client is not None
    
    # Test interaction between fixtures
    import context
    context.path1 = str(temp_workspace / "generated" / "tf-123456789012-us-east-1")
    assert Path(context.path1).exists()
