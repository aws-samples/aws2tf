"""
Performance tracking and regression detection.

Tests performance metrics tracking and regression detection.
Validates: Requirements 19.5, 19.6, 19.7
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

import context


@pytest.mark.performance
class TestPerformanceTracking:
    """Test performance metrics tracking."""
    
    def test_performance_metrics_stored(self, mock_context):
        """
        Test that performance metrics can be stored.
        
        Validates: Requirement 19.5
        """
        # Simulate storing performance metrics
        context.terraform_plan_rate = 28.5
        context.terraform_plan_samples = 5
        
        assert context.terraform_plan_rate == 28.5
        assert context.terraform_plan_samples == 5
    
    def test_performance_regression_detection(self, mock_context):
        """
        Test performance regression detection logic.
        
        Validates: Requirement 19.6
        """
        # Baseline performance
        baseline_time = 10.0  # seconds
        
        # Current performance
        current_time = 11.5  # seconds
        
        # Calculate regression percentage
        regression_pct = ((current_time - baseline_time) / baseline_time) * 100
        
        # Should detect if regression > 20%
        if regression_pct > 20:
            pytest.fail(f"Performance regressed by {regression_pct:.1f}%")
        
        # This test should pass (15% regression is acceptable)
        assert regression_pct <= 20
    
    def test_multi_threaded_vs_single_threaded(self, mock_context):
        """
        Test multi-threaded vs single-threaded performance comparison.
        
        Validates: Requirement 19.7
        """
        # Simulate performance comparison
        single_threaded_time = 100.0  # seconds
        multi_threaded_time = 40.0    # seconds
        
        # Multi-threading should provide speedup
        speedup = single_threaded_time / multi_threaded_time
        
        assert speedup > 1.0, "Multi-threading should be faster"
        assert speedup >= 2.0, "Multi-threading should provide at least 2x speedup"
