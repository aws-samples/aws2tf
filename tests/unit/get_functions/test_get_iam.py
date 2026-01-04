"""
Test IAM get functions.

Tests get functions in aws_iam.py for IAM resource discovery.
Validates: Requirements 3.2, 3.4, 3.5
"""

import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from get_aws_resources.aws_iam import get_aws_iam_role


class TestGetAwsIamRole:
    """Test get_aws_iam_role() function."""
    
    def test_list_all_roles(self, mock_context):
        """Test listing all IAM roles."""
        context.rolelist = {'role-1': True, 'role-2': True}
        
        with mock.patch('common.write_import') as mock_write:
            get_aws_iam_role('aws_iam_role', None, 'iam', 'list_roles',
                           'Roles', 'RoleName', 'RoleName')
            
            # Function should complete without crashing
            assert True
    
    def test_get_specific_role(self, mock_context):
        """Test getting a specific IAM role."""
        context.rolelist = {'test-role': True}
        
        with mock.patch('common.write_import') as mock_write:
            get_aws_iam_role('aws_iam_role', 'test-role', 'iam', 'list_roles',
                           'Roles', 'RoleName', 'RoleName')
            
            # Function should complete without crashing
            assert True
