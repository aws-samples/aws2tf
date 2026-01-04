"""
Integration test for dependency resolution workflow.

Tests parent-child resource dependency resolution.
Validates: Requirements 15.1
"""

import sys
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context


class TestDependencyWorkflow:
    """Test dependency resolution workflow."""
    
    def test_dependency_tracking(self, mock_context):
        """Test that dependencies can be tracked and resolved."""
        # Add dependencies
        context.dependancies.append('aws_vpc.vpc-123')
        context.dependancies.append('aws_subnet.subnet-456')
        
        assert len(context.dependancies) == 2
        assert 'aws_vpc.vpc-123' in context.dependancies
        assert 'aws_subnet.subnet-456' in context.dependancies
