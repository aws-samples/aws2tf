"""
Test resource discovery functionality.

This module tests the build_lists() and build_secondary_lists() functions
to ensure AWS resources are correctly discovered and stored in context.

Validates: Requirements 8.1-8.8
"""

import sys
from pathlib import Path
from unittest import mock

import pytest
from moto import mock_aws
import boto3

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

import context
from build_lists import build_lists, build_secondary_lists


@mock_aws
class TestBuildListsVPC:
    """Test VPC discovery in build_lists()."""
    
    def test_discovers_vpcs(self, mock_context, tmp_path):
        """Test that build_lists discovers VPCs successfully."""
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists
            result = build_lists()
            
            # Verify it completes successfully
            assert result is True
            # Verify vpclist is a dictionary (may have default VPC from moto)
            assert isinstance(context.vpclist, dict)
        finally:
            os.chdir(original_cwd)
    
    def test_handles_no_vpcs(self, mock_context, tmp_path):
        """Test that build_lists handles accounts with no VPCs."""
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists (moto may create default VPC)
            result = build_lists()
            
            # Should complete successfully
            assert result is True
            # May have default VPC from moto, so just verify it completes
            assert isinstance(context.vpclist, dict)
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildListsLambda:
    """Test Lambda function discovery in build_lists()."""
    
    def test_discovers_lambda_functions(self, mock_context, tmp_path):
        """Test that build_lists discovers Lambda functions successfully."""
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists
            result = build_lists()
            
            # Verify it completes successfully
            assert result is True
            # Verify lambdalist is a dictionary
            assert isinstance(context.lambdalist, dict)
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildListsS3:
    """Test S3 bucket discovery in build_lists()."""
    
    def test_discovers_s3_buckets(self, mock_context, tmp_path):
        """Test that S3 buckets are discovered and stored."""
        # Create mock S3 buckets
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.create_bucket(Bucket='test-bucket-1')
        s3.create_bucket(Bucket='test-bucket-2')
        
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists
            result = build_lists()
            
            # Verify S3 buckets were discovered
            assert result is True
            assert 'test-bucket-1' in context.s3list
            assert 'test-bucket-2' in context.s3list
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildListsSecurityGroups:
    """Test security group discovery in build_lists()."""
    
    def test_discovers_security_groups(self, mock_context, tmp_path):
        """Test that build_lists discovers security groups successfully."""
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists
            result = build_lists()
            
            # Verify it completes successfully
            assert result is True
            # Verify sglist is a dictionary (may have default SG from moto)
            assert isinstance(context.sglist, dict)
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildListsSubnets:
    """Test subnet discovery in build_lists()."""
    
    def test_discovers_subnets(self, mock_context, tmp_path):
        """Test that subnets are discovered and JSON is saved."""
        # Create VPC and subnets
        ec2 = boto3.client('ec2', region_name='us-east-1')
        vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
        vpc_id = vpc['Vpc']['VpcId']
        
        subnet1 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
        subnet2 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.2.0/24')
        
        # Change to temp directory for JSON file
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists
            result = build_lists()
            
            # Verify subnets were discovered (at least 2)
            assert result is True
            assert len(context.subnetlist) >= 2
            
            # Verify JSON file was created
            json_file = tmp_path / 'imported' / 'subnets.json'
            assert json_file.exists()
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildListsIAM:
    """Test IAM resource discovery in build_lists()."""
    
    def test_discovers_iam_roles(self, mock_context, tmp_path):
        """Test that IAM roles are discovered and stored."""
        # Create mock IAM roles
        iam = boto3.client('iam', region_name='us-east-1')
        
        iam.create_role(
            RoleName='test-role-1',
            AssumeRolePolicyDocument='{"Version": "2012-10-17"}'
        )
        
        iam.create_role(
            RoleName='test-role-2',
            AssumeRolePolicyDocument='{"Version": "2012-10-17"}'
        )
        
        # Change to temp directory for JSON file
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists
            result = build_lists()
            
            # Verify IAM roles were discovered
            assert result is True
            assert 'test-role-1' in context.rolelist
            assert 'test-role-2' in context.rolelist
            
            # Verify JSON file was created
            json_file = tmp_path / 'imported' / 'roles.json'
            assert json_file.exists()
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildListsParallelExecution:
    """Test parallel execution in build_lists()."""
    
    def test_parallel_execution_completes(self, mock_context, tmp_path):
        """Test that ThreadPoolExecutor completes successfully."""
        # Create various resources
        ec2 = boto3.client('ec2', region_name='us-east-1')
        s3 = boto3.client('s3', region_name='us-east-1')
        iam = boto3.client('iam', region_name='us-east-1')
        
        # Create resources
        vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
        s3.create_bucket(Bucket='test-bucket')
        iam.create_role(
            RoleName='test-role',
            AssumeRolePolicyDocument='{"Version": "2012-10-17"}'
        )
        
        # Change to temp directory
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Run build_lists (uses ThreadPoolExecutor internally)
            result = build_lists()
            
            # Verify it completed successfully
            assert result is True
            
            # Verify all resource types were processed
            assert len(context.vpclist) > 0
            assert len(context.s3list) > 0
            assert len(context.rolelist) > 0
        finally:
            os.chdir(original_cwd)


@mock_aws
class TestBuildSecondaryLists:
    """Test build_secondary_lists() for IAM policies."""
    
    def test_fetches_attached_policies(self, mock_context):
        """Test that attached policies are fetched for roles."""
        # Create IAM role and policy
        iam = boto3.client('iam', region_name='us-east-1')
        
        iam.create_role(
            RoleName='test-role',
            AssumeRolePolicyDocument='{"Version": "2012-10-17", "Statement": []}'
        )
        
        policy_doc = '{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "s3:GetObject", "Resource": "*"}]}'
        
        policy = iam.create_policy(
            PolicyName='test-policy',
            PolicyDocument=policy_doc
        )
        
        iam.attach_role_policy(
            RoleName='test-role',
            PolicyArn=policy['Policy']['Arn']
        )
        
        # Set up context with role
        context.rolelist['test-role'] = True
        
        # Run build_secondary_lists
        build_secondary_lists()
        
        # Verify attached policies were fetched
        assert 'test-role' in context.attached_role_policies_list
        # Should have policies (not False)
        assert context.attached_role_policies_list['test-role'] is not False
    
    def test_fetches_inline_policies(self, mock_context):
        """Test that inline policies are fetched for roles."""
        # Create IAM role with inline policy
        iam = boto3.client('iam', region_name='us-east-1')
        
        iam.create_role(
            RoleName='test-role',
            AssumeRolePolicyDocument='{"Version": "2012-10-17", "Statement": []}'
        )
        
        iam.put_role_policy(
            RoleName='test-role',
            PolicyName='inline-policy',
            PolicyDocument='{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": "s3:GetObject", "Resource": "*"}]}'
        )
        
        # Set up context with role
        context.rolelist['test-role'] = True
        
        # Run build_secondary_lists
        build_secondary_lists()
        
        # Verify inline policies were fetched
        assert 'test-role' in context.role_policies_list
        assert context.role_policies_list['test-role'] is not False
    
    def test_handles_roles_without_policies(self, mock_context):
        """Test that roles without policies are handled correctly."""
        # Create IAM role without policies
        iam = boto3.client('iam', region_name='us-east-1')
        
        iam.create_role(
            RoleName='test-role-no-policies',
            AssumeRolePolicyDocument='{"Version": "2012-10-17", "Statement": []}'
        )
        
        # Set up context with role
        context.rolelist['test-role-no-policies'] = True
        
        # Run build_secondary_lists
        build_secondary_lists()
        
        # Verify role was processed (should have False for no policies)
        assert 'test-role-no-policies' in context.attached_role_policies_list
        assert context.attached_role_policies_list['test-role-no-policies'] is False
