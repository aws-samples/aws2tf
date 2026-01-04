"""
Performance tests for resource discovery.

Benchmarks build_lists() execution time to ensure it completes quickly.
Validates: Requirements 19.1, 19.3
"""

import sys
import time
from pathlib import Path
from moto import mock_aws

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

import context
from build_lists import build_lists


@pytest.mark.performance
@mock_aws
class TestDiscoveryPerformance:
    """Test performance of resource discovery."""
    
    def test_build_lists_completes_quickly(self, mock_context, tmp_path):
        """
        Test that build_lists() completes in under 30 seconds.
        
        Validates: Requirement 19.3
        """
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            start_time = time.time()
            result = build_lists()
            elapsed_time = time.time() - start_time
            
            assert result is True
            assert elapsed_time < 30.0, f"build_lists took {elapsed_time:.2f}s, should be < 30s"
        finally:
            os.chdir(original_cwd)
    
    def test_build_lists_performance_baseline(self, mock_context, tmp_path):
        """
        Benchmark build_lists() execution time for baseline.
        
        Validates: Requirement 19.1
        """
        import os
        original_cwd = os.getcwd()
        os.chdir(tmp_path)
        (tmp_path / 'imported').mkdir()
        
        try:
            start_time = time.time()
            result = build_lists()
            elapsed_time = time.time() - start_time
            
            # Store baseline (in real implementation, would save to file)
            baseline_time = elapsed_time
            
            assert result is True
            assert baseline_time >= 0
            
            # Log performance for tracking
            print(f"\nbaseline: build_lists took {baseline_time:.3f} seconds")
        finally:
            os.chdir(original_cwd)
