"""
Test context state management.

This module tests the context module to ensure global state is correctly
initialized, maintained, and isolated between operations.

Validates: Requirements 7.1-7.7
"""

import sys
from pathlib import Path
from unittest import mock
import threading
import time

import pytest

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

import context


class TestContextInitialization:
    """Test context initialization and default values."""
    
    def test_version_attributes_set(self):
        """Test that version attributes are set."""
        assert hasattr(context, 'aws2tfver')
        assert hasattr(context, 'tfver')
        assert isinstance(context.aws2tfver, str)
        assert isinstance(context.tfver, str)
    
    def test_region_and_account_attributes_exist(self):
        """Test that region and account attributes exist."""
        assert hasattr(context, 'region')
        assert hasattr(context, 'acc')
        assert hasattr(context, 'regionl')
    
    def test_flag_attributes_initialized(self):
        """Test that boolean flag attributes are initialized."""
        flags = [
            'debug', 'debug5', 'fast', 'merge', 'validate',
            'warnings', 'show_status', 'expected', 'serverless',
            'dnet', 'dkms', 'dkey', 'dsgs'
        ]
        
        for flag in flags:
            assert hasattr(context, flag)
            assert isinstance(getattr(context, flag), bool)
    
    def test_path_attributes_initialized(self):
        """Test that path attributes are initialized."""
        paths = ['cwd', 'path1', 'path2', 'path3', 'pathadd']
        
        for path_attr in paths:
            assert hasattr(context, path_attr)
            assert isinstance(getattr(context, path_attr), str)
    
    def test_progress_tracking_attributes_initialized(self):
        """Test that progress tracking attributes are initialized."""
        assert hasattr(context, 'terraform_plan_rate')
        assert hasattr(context, 'terraform_plan_samples')
        assert hasattr(context, 'terraform_apply_rate')
        assert hasattr(context, 'terraform_apply_samples')
        assert hasattr(context, 'last_plan_time')
        
        # Verify types
        assert isinstance(context.terraform_plan_rate, float)
        assert isinstance(context.terraform_plan_samples, int)
        assert isinstance(context.terraform_apply_rate, float)
        assert isinstance(context.terraform_apply_samples, int)
        assert isinstance(context.last_plan_time, float)
    
    def test_list_attributes_initialized(self):
        """Test that list attributes are initialized."""
        lists = ['processed', 'dependancies', 'types', 'all_extypes', 'badlist']
        
        for list_attr in lists:
            assert hasattr(context, list_attr)
            assert isinstance(getattr(context, list_attr), list)


class TestResourceTrackingDictionaries:
    """Test resource tracking dictionary initialization."""
    
    def test_processing_dictionaries_initialized(self):
        """Test that processing tracking dictionaries are initialized."""
        dicts = ['rproc', 'rdep', 'trdep']
        
        for dict_attr in dicts:
            assert hasattr(context, dict_attr)
            assert isinstance(getattr(context, dict_attr), dict)
    
    def test_resource_list_dictionaries_initialized(self):
        """Test that resource list dictionaries are initialized."""
        resource_dicts = [
            'subnetlist', 'sglist', 'vpclist', 'ltlist',
            'lambdalist', 's3list', 'rolelist', 'policylist',
            'inplist', 'bucketlist', 'tgwlist', 'gluedbs',
            'attached_role_policies_list', 'role_policies_list'
        ]
        
        for dict_attr in resource_dicts:
            assert hasattr(context, dict_attr)
            assert isinstance(getattr(context, dict_attr), dict)
    
    def test_special_dictionaries_initialized(self):
        """Test that special dictionaries are initialized."""
        assert hasattr(context, 'mopup')
        assert isinstance(context.mopup, dict)
        
        assert hasattr(context, 'noimport')
        assert isinstance(context.noimport, dict)
        
        assert hasattr(context, 'tested')
        assert isinstance(context.tested, dict)


class TestContextStateManagement:
    """Test context state management during operations."""
    
    def test_region_and_account_storage(self, mock_context):
        """Test that region and account information is stored correctly."""
        mock_context.region = 'eu-west-1'
        mock_context.acc = '987654321012'
        mock_context.regionl = len('eu-west-1')
        
        assert mock_context.region == 'eu-west-1'
        assert mock_context.acc == '987654321012'
        assert mock_context.regionl == 9
    
    def test_merge_mode_state_tracking(self, mock_context):
        """Test that merge mode state is tracked correctly."""
        assert mock_context.merge is False
        
        mock_context.merge = True
        assert mock_context.merge is True
        
        # Verify rproc dictionary can track processed resources
        mock_context.rproc['aws_vpc.vpc-123'] = True
        assert 'aws_vpc.vpc-123' in mock_context.rproc
    
    def test_exclusion_list_maintenance(self, mock_context):
        """Test that exclusion lists are maintained correctly."""
        assert isinstance(mock_context.all_extypes, list)
        
        # Add exclusions
        mock_context.all_extypes = ['aws_vpc', 'aws_subnet']
        assert 'aws_vpc' in mock_context.all_extypes
        assert 'aws_subnet' in mock_context.all_extypes
    
    def test_resource_tracking_updates(self, mock_context):
        """Test that resource tracking dictionaries can be updated."""
        # Track VPCs
        mock_context.vpclist['vpc-123'] = True
        mock_context.vpclist['vpc-456'] = True
        assert len(mock_context.vpclist) == 2
        
        # Track Lambda functions
        mock_context.lambdalist['function-1'] = True
        assert 'function-1' in mock_context.lambdalist
        
        # Track S3 buckets
        mock_context.s3list['bucket-1'] = True
        assert 'bucket-1' in mock_context.s3list
    
    def test_dependency_tracking(self, mock_context):
        """Test that dependencies can be tracked."""
        mock_context.dependancies.append('aws_vpc.vpc-123')
        mock_context.dependancies.append('aws_subnet.subnet-456')
        
        assert len(mock_context.dependancies) == 2
        assert 'aws_vpc.vpc-123' in mock_context.dependancies
    
    def test_processed_resources_tracking(self, mock_context):
        """Test that processed resources are tracked."""
        mock_context.rproc['aws_vpc.vpc-123'] = True
        mock_context.rproc['aws_subnet.subnet-456'] = True
        
        assert 'aws_vpc.vpc-123' in mock_context.rproc
        assert 'aws_subnet.subnet-456' in mock_context.rproc
        assert mock_context.rproc['aws_vpc.vpc-123'] is True


class TestContextIsolation:
    """Test context isolation between tests."""
    
    def test_context_modifications_in_test_1(self):
        """Test that context can be modified in a test."""
        import context
        
        # Modify context
        context.vpclist['vpc-test1'] = True
        context.region = 'test-region-1'
        
        # Verify modifications
        assert 'vpc-test1' in context.vpclist
        assert context.region == 'test-region-1'
    
    def test_context_reset_from_test_1(self):
        """Test that context was reset from previous test."""
        import context
        
        # Verify context was reset by reset_context fixture
        # (vpclist should be empty, region should be default)
        assert 'vpc-test1' not in context.vpclist
        # Note: region might be set by mock_context fixture if used
    
    def test_context_modifications_in_test_2(self):
        """Test that context can be modified independently."""
        import context
        
        # Modify context differently
        context.lambdalist['function-test2'] = True
        context.region = 'test-region-2'
        
        # Verify modifications
        assert 'function-test2' in context.lambdalist
        assert context.region == 'test-region-2'
        
        # Verify previous test's modifications are gone
        assert 'vpc-test1' not in context.vpclist


class TestContextThreadSafety:
    """Test context thread safety for multi-threaded operations."""
    
    def test_concurrent_dictionary_access(self, mock_context):
        """Test that concurrent access to context dictionaries works."""
        errors = []
        
        def add_vpc(vpc_id):
            try:
                mock_context.vpclist[vpc_id] = True
            except Exception as e:
                errors.append(e)
        
        # Create multiple threads that modify vpclist
        threads = []
        for i in range(10):
            thread = threading.Thread(target=add_vpc, args=(f'vpc-{i}',))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads
        for thread in threads:
            thread.join()
        
        # Verify no errors occurred
        assert len(errors) == 0
        
        # Verify all VPCs were added
        assert len(mock_context.vpclist) == 10
        for i in range(10):
            assert f'vpc-{i}' in mock_context.vpclist
    
    def test_concurrent_list_access(self, mock_context):
        """Test that concurrent access to context lists works."""
        errors = []
        
        def add_dependency(dep):
            try:
                mock_context.dependancies.append(dep)
            except Exception as e:
                errors.append(e)
        
        # Create multiple threads that modify dependancies list
        threads = []
        for i in range(10):
            thread = threading.Thread(target=add_dependency, args=(f'aws_vpc.vpc-{i}',))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads
        for thread in threads:
            thread.join()
        
        # Verify no errors occurred
        assert len(errors) == 0
        
        # Verify all dependencies were added
        assert len(mock_context.dependancies) == 10
    
    def test_concurrent_read_write(self, mock_context):
        """Test concurrent reads and writes to context."""
        errors = []
        read_values = []
        
        def writer():
            try:
                for i in range(5):
                    mock_context.vpclist[f'vpc-write-{i}'] = True
                    time.sleep(0.001)
            except Exception as e:
                errors.append(e)
        
        def reader():
            try:
                for _ in range(5):
                    # Read current state
                    vpc_count = len(mock_context.vpclist)
                    read_values.append(vpc_count)
                    time.sleep(0.001)
            except Exception as e:
                errors.append(e)
        
        # Start writer and reader threads
        writer_thread = threading.Thread(target=writer)
        reader_thread = threading.Thread(target=reader)
        
        writer_thread.start()
        reader_thread.start()
        
        writer_thread.join()
        reader_thread.join()
        
        # Verify no errors occurred
        assert len(errors) == 0
        
        # Verify writer completed
        assert len(mock_context.vpclist) == 5


class TestContextSpecialAttributes:
    """Test special context attributes and their behavior."""
    
    def test_noimport_dictionary(self):
        """Test that noimport dictionary contains expected resources."""
        assert isinstance(context.noimport, dict)
        
        # Verify some known no-import resources
        assert 'aws_iam_user_group_membership' in context.noimport
        assert context.noimport['aws_iam_user_group_membership'] is True
    
    def test_mopup_dictionary(self):
        """Test that mopup dictionary is initialized."""
        assert isinstance(context.mopup, dict)
        
        # Verify it has expected structure
        if context.mopup:
            for key, value in context.mopup.items():
                assert isinstance(key, str)
                assert isinstance(value, str)
    
    def test_cores_attribute(self):
        """Test that cores attribute is set."""
        assert hasattr(context, 'cores')
        assert isinstance(context.cores, int)
        assert context.cores > 0
    
    def test_tracking_message_attribute(self):
        """Test that tracking_message attribute exists."""
        assert hasattr(context, 'tracking_message')
        assert isinstance(context.tracking_message, str)
    
    def test_credential_type_attribute(self):
        """Test that credtype attribute exists."""
        assert hasattr(context, 'credtype')
        assert isinstance(context.credtype, str)
    
    def test_sso_attribute(self):
        """Test that sso attribute exists."""
        assert hasattr(context, 'sso')
        assert isinstance(context.sso, bool)


class TestContextEdgeCases:
    """Test edge cases in context management."""
    
    def test_large_resource_lists(self, mock_context):
        """Test that context can handle large resource lists."""
        # Add 1000 VPCs
        for i in range(1000):
            mock_context.vpclist[f'vpc-{i:04d}'] = True
        
        assert len(mock_context.vpclist) == 1000
        assert 'vpc-0000' in mock_context.vpclist
        assert 'vpc-0999' in mock_context.vpclist
    
    def test_nested_dictionary_access(self, mock_context):
        """Test that nested dictionary structures work."""
        # Some context attributes might have nested structures
        mock_context.rproc['aws_vpc.vpc-123'] = True
        mock_context.rproc['aws_subnet.subnet-456'] = True
        
        # Verify we can iterate and access
        for key in mock_context.rproc:
            assert '.' in key
            assert mock_context.rproc[key] is True
    
    def test_empty_dictionaries_and_lists(self, mock_context):
        """Test that empty dictionaries and lists are handled."""
        # Verify empty state
        assert len(mock_context.vpclist) == 0
        assert len(mock_context.processed) == 0
        assert len(mock_context.dependancies) == 0
        
        # Verify operations on empty structures work
        assert 'vpc-123' not in mock_context.vpclist
        assert 'item' not in mock_context.processed
    
    def test_context_attribute_types_are_correct(self):
        """Test that all context attributes have correct types."""
        # String attributes
        string_attrs = ['region', 'acc', 'profile', 'cwd', 'credtype']
        for attr in string_attrs:
            assert isinstance(getattr(context, attr), str)
        
        # Boolean attributes
        bool_attrs = ['debug', 'fast', 'merge', 'sso']
        for attr in bool_attrs:
            assert isinstance(getattr(context, attr), bool)
        
        # Integer attributes
        int_attrs = ['cores', 'terraform_plan_samples', 'terraform_apply_samples']
        for attr in int_attrs:
            assert isinstance(getattr(context, attr), int)
        
        # Float attributes
        float_attrs = ['terraform_plan_rate', 'terraform_apply_rate', 'last_plan_time', 'esttime']
        for attr in float_attrs:
            assert isinstance(getattr(context, attr), float)
        
        # Dictionary attributes
        dict_attrs = ['rproc', 'vpclist', 'lambdalist', 's3list']
        for attr in dict_attrs:
            assert isinstance(getattr(context, attr), dict)
        
        # List attributes
        list_attrs = ['processed', 'dependancies', 'types']
        for attr in list_attrs:
            assert isinstance(getattr(context, attr), list)
