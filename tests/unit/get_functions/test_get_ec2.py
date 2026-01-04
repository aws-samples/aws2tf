"""
Test EC2 get functions.

This module tests get functions in aws_ec2.py to ensure EC2 resources
are correctly discovered and imported.

Validates: Requirements 3.2-3.6
"""

import sys
from pathlib import Path
from unittest import mock

import pytest

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from get_aws_resources.aws_ec2 import get_aws_vpc


class TestGetAwsVpc:
    """Test get_aws_vpc() function."""
    
    def test_list_all_vpcs(self, mock_context):
        """Test listing all VPCs when id is None."""
        # Set up context with VPCs
        context.vpclist = {
            'vpc-123': True,
            'vpc-456': True,
        }
        
        # Mock write_import
        with mock.patch('common.write_import') as mock_write:
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy'):
                    # Call get_aws_vpc with id=None
                    result = get_aws_vpc('aws_vpc', None, 'ec2', 'describe_vpcs', 
                                        'Vpcs', 'VpcId', 'VpcId')
                    
                    # Verify write_import was called for each VPC
                    assert mock_write.call_count == 2
                    mock_write.assert_any_call('aws_vpc', 'vpc-123', None)
                    mock_write.assert_any_call('aws_vpc', 'vpc-456', None)
    
    def test_get_specific_vpc(self, mock_context):
        """Test getting a specific VPC by ID."""
        # Set up context with VPC
        context.vpclist = {'vpc-123': True}
        
        # Mock write_import
        with mock.patch('common.write_import') as mock_write:
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy'):
                    # Call get_aws_vpc with specific id
                    result = get_aws_vpc('aws_vpc', 'vpc-123', 'ec2', 'describe_vpcs',
                                        'Vpcs', 'VpcId', 'VpcId')
                    
                    # Verify write_import was called once
                    mock_write.assert_called_once_with('aws_vpc', 'vpc-123', None)
                    
                    # Verify resource was marked as processed
                    assert 'aws_vpc.vpc-123' in context.rproc
    
    def test_vpc_not_in_list_warning(self, mock_context, caplog):
        """Test that warning is logged for VPC not in vpclist."""
        import logging
        
        # Set up empty vpclist
        context.vpclist = {}
        context.warnings = True
        
        caplog.set_level(logging.WARNING, logger='aws2tf')
        
        # Mock write_import
        with mock.patch('common.write_import'):
            # Call get_aws_vpc with VPC not in list
            get_aws_vpc('aws_vpc', 'vpc-nonexistent', 'ec2', 'describe_vpcs',
                       'Vpcs', 'VpcId', 'VpcId')
            
            # Verify warning was logged
            assert 'vpc not in vpclist' in caplog.text.lower()
    
    def test_adds_subnet_dependency(self, mock_context):
        """Test that subnet dependency is added."""
        context.vpclist = {'vpc-123': True}
        
        with mock.patch('common.write_import'):
            with mock.patch('common.add_known_dependancy') as mock_add_known:
                with mock.patch('common.add_dependancy'):
                    get_aws_vpc('aws_vpc', 'vpc-123', 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
                    
                    # Verify subnet dependency was added
                    mock_add_known.assert_any_call('aws_subnet', 'vpc-123')
    
    def test_adds_route_table_dependency_when_not_dnet(self, mock_context):
        """Test that route table dependency is added when dnet is False."""
        context.vpclist = {'vpc-123': True}
        context.dnet = False
        
        with mock.patch('common.write_import'):
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy') as mock_add_dep:
                    get_aws_vpc('aws_vpc', 'vpc-123', 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
                    
                    # Verify route table dependency was added
                    mock_add_dep.assert_any_call('aws_route_table_association', 'vpc-123')
    
    def test_skips_route_table_dependency_when_dnet(self, mock_context):
        """Test that route table dependency is skipped when dnet is True."""
        context.vpclist = {'vpc-123': True}
        context.dnet = True
        
        with mock.patch('common.write_import'):
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy') as mock_add_dep:
                    get_aws_vpc('aws_vpc', 'vpc-123', 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
                    
                    # Verify route table dependency was NOT added
                    for call in mock_add_dep.call_args_list:
                        assert call[0][0] != 'aws_route_table_association'
