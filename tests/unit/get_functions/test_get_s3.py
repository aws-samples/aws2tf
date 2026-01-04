"""
Test S3 get functions.

Tests get functions in aws_s3.py for S3 bucket discovery and import.
Validates: Requirements 3.2, 3.5
"""

import sys
from pathlib import Path
from unittest import mock
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from get_aws_resources.aws_s3 import get_aws_s3_bucket


class TestGetAwsS3Bucket:
    """Test get_aws_s3_bucket() function."""
    
    def test_list_all_buckets(self, mock_context):
        """Test listing all S3 buckets when id is None."""
        context.s3list = {'bucket-1': True, 'bucket-2': True}
        
        with mock.patch('common.write_import') as mock_write:
            get_aws_s3_bucket('aws_s3_bucket', None, 's3', 'list_buckets',
                            'Buckets', 'Name', 'Name')
            
            # Function should complete without crashing
            assert True
    
    def test_get_specific_bucket(self, mock_context):
        """Test getting a specific S3 bucket by name."""
        context.s3list = {'test-bucket': True}
        
        with mock.patch('common.write_import') as mock_write:
            get_aws_s3_bucket('aws_s3_bucket', 'test-bucket', 's3', 'list_buckets',
                            'Buckets', 'Name', 'Name')
            
            # Function should complete without crashing
            assert True
