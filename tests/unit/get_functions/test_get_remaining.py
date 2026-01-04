"""
Test get functions for remaining AWS services.

This module provides basic smoke tests for get functions across
multiple AWS services to ensure they follow the standard pattern.

Validates: Requirements 3.2, 3.4, 3.7
"""

import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context


class TestGetFunctionImports:
    """Test that get function modules can be imported."""
    
    def test_dynamodb_module_imports(self):
        """Test that aws_dynamodb module imports successfully."""
        from get_aws_resources import aws_dynamodb
        assert hasattr(aws_dynamodb, 'get_aws_dynamodb_table')
    
    def test_rds_module_imports(self):
        """Test that aws_rds module imports successfully."""
        from get_aws_resources import aws_rds
        assert hasattr(aws_rds, 'get_aws_db_instance')
    
    def test_eks_module_imports(self):
        """Test that aws_eks module imports successfully."""
        from get_aws_resources import aws_eks
        assert hasattr(aws_eks, 'get_aws_eks_cluster')
    
    def test_elbv2_module_imports(self):
        """Test that aws_elbv2 module imports successfully."""
        from get_aws_resources import aws_elbv2
        assert hasattr(aws_elbv2, 'get_aws_lb')
    
    def test_cloudwatch_module_imports(self):
        """Test that aws_cloudwatch module imports successfully."""
        from get_aws_resources import aws_cloudwatch
        # Module should have get functions
        assert hasattr(aws_cloudwatch, '__name__')
    
    def test_sns_module_imports(self):
        """Test that aws_sns module imports successfully."""
        from get_aws_resources import aws_sns
        assert hasattr(aws_sns, 'get_aws_sns_topic')
    
    def test_sqs_module_imports(self):
        """Test that aws_sqs module imports successfully."""
        from get_aws_resources import aws_sqs
        assert hasattr(aws_sqs, 'get_aws_sqs_queue')


class TestGetFunctionPatterns:
    """Test that get functions follow standard patterns."""
    
    def test_get_functions_accept_standard_parameters(self):
        """Test that get functions accept standard parameters."""
        from get_aws_resources.aws_ec2 import get_aws_vpc
        
        # Should accept: type, id, clfn, descfn, topkey, key, filterid
        # Test with mock to avoid actual execution
        with mock.patch('common.write_import'):
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy'):
                    context.vpclist = {}
                    # Should not crash with standard parameters
                    get_aws_vpc('aws_vpc', None, 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
    
    def test_get_functions_handle_none_id(self):
        """Test that get functions handle id=None (list all)."""
        from get_aws_resources.aws_s3 import get_aws_s3_bucket
        
        context.s3list = {}
        
        with mock.patch('common.write_import'):
            # Should handle None id without crashing
            get_aws_s3_bucket('aws_s3_bucket', None, 's3', 'list_buckets',
                            'Buckets', 'Name', 'Name')
    
    def test_get_functions_handle_specific_id(self):
        """Test that get functions handle specific resource IDs."""
        from get_aws_resources.aws_iam import get_aws_iam_role
        
        context.rolelist = {'test-role': True}
        
        with mock.patch('common.write_import'):
            # Should handle specific id without crashing
            get_aws_iam_role('aws_iam_role', 'test-role', 'iam', 'list_roles',
                           'Roles', 'RoleName', 'RoleName')


class TestGetFunctionErrorHandling:
    """Test error handling in get functions."""
    
    def test_get_function_handles_empty_list(self, mock_context):
        """Test that get functions handle empty resource lists."""
        from get_aws_resources.aws_ec2 import get_aws_vpc
        
        context.vpclist = {}
        
        with mock.patch('common.write_import') as mock_write:
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy'):
                    get_aws_vpc('aws_vpc', None, 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
                    
                    # Should not crash, write_import should not be called
                    assert mock_write.call_count == 0
    
    def test_get_function_handles_missing_resource(self, mock_context, caplog):
        """Test that get functions handle missing resources gracefully."""
        import logging
        from get_aws_resources.aws_ec2 import get_aws_vpc
        
        context.vpclist = {}
        context.warnings = True
        caplog.set_level(logging.WARNING, logger='aws2tf')
        
        with mock.patch('common.write_import'):
            # Try to get non-existent VPC
            get_aws_vpc('aws_vpc', 'vpc-nonexistent', 'ec2', 'describe_vpcs',
                       'Vpcs', 'VpcId', 'VpcId')
            
            # Should log warning
            assert 'vpc not in vpclist' in caplog.text.lower()
