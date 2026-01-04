"""
Integration test for IAM workflow.

Tests complete IAM discovery → import workflow.
Validates: Requirements 15.1
"""

import sys
from pathlib import Path
from moto import mock_aws

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from build_lists import build_lists


@mock_aws
class TestIAMWorkflow:
    """Test complete IAM workflow."""
    
    def test_iam_discovery_workflow(self, mock_context, tmp_path):
        """Test IAM role discovery completes successfully."""
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            result = build_lists()
            assert result is True
            assert isinstance(context.rolelist, dict)
        finally:
            os.chdir(original_cwd)
