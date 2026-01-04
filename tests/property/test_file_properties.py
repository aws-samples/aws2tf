"""
Property-based tests for file operations.

Uses hypothesis to test file operation functions with generated inputs.
Validates: Requirements 14.4
"""

import sys
from pathlib import Path
from hypothesis import given, strategies as st, settings

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

from common import safe_filename


class TestFileProperties:
    """Property-based tests for file operations."""
    
    @settings(max_examples=50, deadline=None)
    @given(filename=st.text(
        alphabet='abcdefghijklmnopqrstuvwxyz0123456789-_.',
        min_size=1,
        max_size=20
    ))
    def test_safe_filename_never_crashes(self, filename):
        """
        Property: safe_filename should never crash on any input.
        
        For any filename string, safe_filename() should return a valid
        path string without raising exceptions.
        """
        try:
            result = safe_filename(filename)
            assert isinstance(result, str)
            assert len(result) > 0
        except ValueError:
            # Path traversal detection is acceptable
            pass
