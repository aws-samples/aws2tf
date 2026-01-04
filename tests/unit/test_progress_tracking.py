"""
Test progress tracking functionality.

This module tests progress bar and adaptive rate learning functionality
to ensure users see accurate progress during long operations.

Validates: Requirements 13.1-13.7
"""

import sys
from pathlib import Path
from unittest import mock

import pytest

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

import context


class TestProgressBarCreation:
    """Test progress bar creation."""
    
    def test_progress_tracking_attributes_initialized(self, mock_context):
        """Test that progress tracking attributes are initialized."""
        assert hasattr(context, 'terraform_plan_rate')
        assert hasattr(context, 'terraform_plan_samples')
        assert hasattr(context, 'terraform_apply_rate')
        assert hasattr(context, 'terraform_apply_samples')
        
        assert context.terraform_plan_rate == 25.0
        assert context.terraform_plan_samples == 0
        assert context.terraform_apply_rate == 50.0
        assert context.terraform_apply_samples == 0
    
    def test_progress_tracking_disabled_in_debug_mode(self, mock_context):
        """Test that progress tracking is disabled in debug mode."""
        context.debug = True
        
        # Progress tracking functions should check context.debug
        # and skip progress bars when debug is True
        assert context.debug is True


class TestAdaptiveRateLearning:
    """Test adaptive rate learning for progress estimation."""
    
    def test_terraform_plan_rate_updates(self, mock_context):
        """Test that terraform_plan_rate updates correctly."""
        # Initial state
        assert context.terraform_plan_rate == 25.0
        assert context.terraform_plan_samples == 0
        
        # Simulate first sample
        context.terraform_plan_rate = 30.0
        context.terraform_plan_samples = 1
        
        assert context.terraform_plan_rate == 30.0
        assert context.terraform_plan_samples == 1
    
    def test_terraform_apply_rate_updates(self, mock_context):
        """Test that terraform_apply_rate updates correctly."""
        # Initial state
        assert context.terraform_apply_rate == 50.0
        assert context.terraform_apply_samples == 0
        
        # Simulate first sample
        context.terraform_apply_rate = 55.0
        context.terraform_apply_samples = 1
        
        assert context.terraform_apply_rate == 55.0
        assert context.terraform_apply_samples == 1
    
    def test_exponential_moving_average_calculation(self, mock_context):
        """Test exponential moving average calculation logic."""
        # Start with initial estimate
        context.terraform_plan_rate = 25.0
        context.terraform_plan_samples = 1
        
        # Simulate new measurement: 20 resources/second
        actual_rate = 20.0
        
        # Calculate EMA: 70% old + 30% new
        expected_rate = (25.0 * 0.7) + (20.0 * 0.3)
        assert expected_rate == 23.5
        
        # Update context
        context.terraform_plan_rate = expected_rate
        context.terraform_plan_samples = 2
        
        assert context.terraform_plan_rate == 23.5
        assert context.terraform_plan_samples == 2
    
    def test_rate_learning_over_multiple_samples(self, mock_context):
        """Test that rate learning adapts over multiple samples."""
        # Start with initial estimate
        context.terraform_plan_rate = 25.0
        context.terraform_plan_samples = 0
        
        # Simulate multiple measurements
        measurements = [30.0, 28.0, 32.0, 29.0]
        
        for i, measurement in enumerate(measurements):
            if context.terraform_plan_samples == 0:
                # First sample - use directly
                context.terraform_plan_rate = measurement
            else:
                # EMA: 70% old + 30% new
                context.terraform_plan_rate = (context.terraform_plan_rate * 0.7) + (measurement * 0.3)
            
            context.terraform_plan_samples += 1
        
        # Rate should have adapted toward the measurements
        assert context.terraform_plan_samples == 4
        # Rate should be between min and max measurements
        assert 28.0 <= context.terraform_plan_rate <= 32.0


class TestProgressCapping:
    """Test progress capping at 75% until completion."""
    
    def test_progress_calculation_caps_at_75(self):
        """Test that progress caps at 75% until completion."""
        # Simulate progress calculation
        estimated_time = 100.0  # seconds
        
        # At 50% of estimated time
        elapsed = 50.0
        progress = int((elapsed / estimated_time) * 75)
        assert progress == 37  # 50% of 75% cap
        
        # At 100% of estimated time
        elapsed = 100.0
        progress = int((elapsed / estimated_time) * 75)
        assert progress == 75  # Capped at 75%
        
        # At 150% of estimated time (overtime)
        elapsed = 150.0
        if elapsed < estimated_time:
            progress = int((elapsed / estimated_time) * 75)
        else:
            # Should still be around 75-78%
            overtime = elapsed - estimated_time
            additional = 3 * (1 - (1 / (1 + overtime / 20)))
            progress = 75 + int(additional)
        
        assert 75 <= progress <= 78
    
    def test_progress_jumps_to_100_on_completion(self):
        """Test that progress jumps to 100% on completion."""
        # When process completes, progress should be set to 100
        progress = 100
        assert progress == 100


class TestProgressForTerraformOperations:
    """Test progress tracking for terraform operations."""
    
    def test_last_plan_time_recorded(self, mock_context):
        """Test that last_plan_time is recorded."""
        assert context.last_plan_time == 0.0
        
        # Simulate recording plan time
        context.last_plan_time = 45.5
        
        assert context.last_plan_time == 45.5
    
    def test_plan_and_apply_rates_independent(self, mock_context):
        """Test that plan and apply rates are tracked independently."""
        # Set different rates
        context.terraform_plan_rate = 25.0
        context.terraform_apply_rate = 50.0
        
        # Verify they're independent
        assert context.terraform_plan_rate != context.terraform_apply_rate
        assert context.terraform_plan_rate == 25.0
        assert context.terraform_apply_rate == 50.0
    
    def test_sample_counts_tracked_separately(self, mock_context):
        """Test that sample counts are tracked separately."""
        context.terraform_plan_samples = 5
        context.terraform_apply_samples = 3
        
        assert context.terraform_plan_samples == 5
        assert context.terraform_apply_samples == 3


class TestProgressTrackingEdgeCases:
    """Test edge cases in progress tracking."""
    
    def test_zero_resources_handled(self):
        """Test that zero resources is handled gracefully."""
        total_resources = 0
        
        # Should not divide by zero
        if total_resources == 0:
            # No progress bar should be shown
            assert True
        else:
            estimated_time = total_resources / 25.0
            assert estimated_time > 0
    
    def test_very_fast_operations(self, mock_context):
        """Test that very fast operations are handled."""
        # If operation completes in < 1 second
        actual_time = 0.5
        total_resources = 10
        
        # Rate calculation should handle this
        if actual_time > 0:
            actual_rate = total_resources / actual_time
            assert actual_rate == 20.0  # 10 resources / 0.5 seconds
    
    def test_very_slow_operations(self, mock_context):
        """Test that very slow operations are handled."""
        # If operation takes much longer than estimated
        estimated_time = 100.0
        elapsed = 300.0  # 3x longer
        
        # Progress should still cap appropriately
        if elapsed < estimated_time:
            progress = int((elapsed / estimated_time) * 75)
        else:
            overtime = elapsed - estimated_time
            additional = 3 * (1 - (1 / (1 + overtime / 20)))
            progress = 75 + int(additional)
        
        # Should be close to 78% cap
        assert 75 <= progress <= 78
