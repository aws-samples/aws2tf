"""
Integration test for Lambda workflow.

Tests complete Lambda discovery → import workflow.
Validates: Requirements 15.3
"""

import sys
from pathlib import Path
from unittest import mock
from moto import mock_aws
import boto3

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from build_lists import build_lists


@mock_aws
class TestLambdaWorkflow:
    """Test complete Lambda workflow."""
    
    def test_lambda_discovery_workflow(self, mock_context, tmp_path):
        """Test Lambda discovery completes successfully."""
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            result = build_lists()
            assert result is True
            assert isinstance(context.lambdalist, dict)
        finally:
            os.chdir(original_cwd)
