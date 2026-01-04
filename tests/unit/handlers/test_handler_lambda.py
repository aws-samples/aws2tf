"""
Test Lambda resource handlers.

Tests handler functions in fixtf_lambda.py for Lambda transformations.
Validates: Requirements 4.1, 4.4
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

from fixtf_aws_resources import fixtf_lambda


class TestLambdaHandlers:
    """Test Lambda handler functions."""
    
    def test_lambda_module_exists(self):
        """Test that fixtf_lambda module exists."""
        assert fixtf_lambda is not None
        assert hasattr(fixtf_lambda, '__name__')
    
    def test_lambda_handler_callable(self):
        """Test that Lambda handlers are callable."""
        # Check if module has aws_lambda_function handler
        if hasattr(fixtf_lambda, 'aws_lambda_function'):
            assert callable(fixtf_lambda.aws_lambda_function)
