"""
Integration test for S3 workflow.

Tests complete S3 discovery → import workflow.
Validates: Requirements 15.4
"""

import sys
from pathlib import Path
from unittest import mock
from moto import mock_aws

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from build_lists import build_lists


@mock_aws
class TestS3Workflow:
    """Test complete S3 workflow."""
    
    def test_s3_discovery_workflow(self, mock_context, tmp_path):
        """Test S3 discovery completes successfully."""
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            result = build_lists()
            assert result is True
            assert isinstance(context.s3list, dict)
        finally:
            os.chdir(original_cwd)
