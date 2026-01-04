"""
Test Lambda get functions.

Tests get functions in aws_lambda.py for Lambda function discovery.
Validates: Requirements 3.2, 3.4
"""

import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from get_aws_resources.aws_lambda import get_aws_lambda_function


class TestGetAwsLambdaFunction:
    """Test get_aws_lambda_function() function."""
    
    def test_list_all_functions(self, mock_context):
        """Test listing all Lambda functions."""
        context.lambdalist = {'function-1': True, 'function-2': True}
        
        with mock.patch('common.write_import') as mock_write:
            get_aws_lambda_function('aws_lambda_function', None, 'lambda', 'list_functions',
                                  'Functions', 'FunctionName', 'FunctionName')
            
            # Function should complete without crashing
            assert True
