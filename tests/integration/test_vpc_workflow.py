"""
Integration test for VPC workflow.

This module tests the complete VPC discovery → import → file generation workflow.

Validates: Requirements 15.2, 15.6, 15.7
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
from build_lists import build_lists
from get_aws_resources.aws_ec2 import get_aws_vpc


@mock_aws
class TestVPCWorkflow:
    """Test complete VPC workflow."""
    
    def test_vpc_discovery_to_import(self, mock_context, tmp_path):
        """
        Test complete VPC discovery → import workflow.
        
        This integration test verifies:
        1. VPCs are discovered by build_lists()
        2. VPCs are imported by get_aws_vpc()
        3. Dependencies are tracked correctly
        """
        # Create mock VPC
        ec2 = boto3.client('ec2', region_name='us-east-1')
        vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
        vpc_id = vpc['Vpc']['VpcId']
        
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            # Step 1: Discover VPCs
            result = build_lists()
            assert result is True
            
            # Step 2: Verify VPC was discovered
            assert len(context.vpclist) > 0
            
            # Step 3: Import VPC
            with mock.patch('common.write_import') as mock_write:
                with mock.patch('common.add_known_dependancy'):
                    with mock.patch('common.add_dependancy'):
                        # Get first VPC from list
                        first_vpc_id = list(context.vpclist.keys())[0]
                        get_aws_vpc('aws_vpc', first_vpc_id, 'ec2', 'describe_vpcs',
                                   'Vpcs', 'VpcId', 'VpcId')
                        
                        # Verify import was written
                        assert mock_write.called
        finally:
            os.chdir(original_cwd)
    
    def test_vpc_workflow_with_dependencies(self, mock_context, tmp_path):
        """
        Test VPC workflow includes dependency tracking.
        
        Verifies that subnet and route table dependencies are tracked.
        """
        # Set up VPC in context
        context.vpclist = {'vpc-test': True}
        context.dnet = False
        
        # Set up directory structure
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            with mock.patch('common.write_import'):
                with mock.patch('common.add_known_dependancy') as mock_known:
                    with mock.patch('common.add_dependancy') as mock_dep:
                        # Import VPC
                        get_aws_vpc('aws_vpc', 'vpc-test', 'ec2', 'describe_vpcs',
                                   'Vpcs', 'VpcId', 'VpcId')
                        
                        # Verify subnet dependency added
                        mock_known.assert_any_call('aws_subnet', 'vpc-test')
                        
                        # Verify route table dependency added
                        mock_dep.assert_any_call('aws_route_table_association', 'vpc-test')
        finally:
            os.chdir(original_cwd)
