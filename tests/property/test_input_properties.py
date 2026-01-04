"""
Property-based tests for input validation.

This module uses hypothesis to generate random inputs and test that
validation functions handle all possible inputs correctly.

Validates: Requirements 14.2
"""

import sys
from pathlib import Path

import pytest
from hypothesis import given, strategies as st, settings

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aws2tf import validate_region, validate_resource_type, validate_resource_id


class TestRegionValidationProperties:
    """Property-based tests for region validation."""
    
    @settings(max_examples=50, deadline=None)
    @given(region=st.from_regex(r'^[a-z]{2}-[a-z]{4,10}-\d{1}$', fullmatch=True))
    def test_valid_region_format_always_passes(self, region):
        """
        Property: All strings matching AWS region format should validate.
        
        For any string that matches the AWS region regex pattern,
        validate_region() should return the same string unchanged.
        """
        result = validate_region(region)
        assert result == region
    
    @settings(max_examples=100)
    @given(invalid_region=st.text(min_size=1, max_size=50).filter(
        lambda x: not x.startswith('.') and '..' not in x and '/' not in x
    ))
    def test_invalid_regions_raise_or_pass(self, invalid_region):
        """
        Property: Invalid regions either raise ValueError or pass validation.
        
        For any string, validate_region() should either accept it or
        raise ValueError - it should never crash or return unexpected values.
        """
        try:
            result = validate_region(invalid_region)
            # If it passes, should return the same string
            assert result == invalid_region
        except ValueError:
            # Expected for invalid formats
            pass


class TestResourceTypeValidationProperties:
    """Property-based tests for resource type validation."""
    
    @settings(max_examples=100)
    @given(resource_type=st.from_regex(r'^[a-z][a-z0-9_]*$', fullmatch=True))
    def test_valid_resource_type_format_always_passes(self, resource_type):
        """
        Property: All strings matching resource type format should validate.
        
        For any string that matches the terraform resource type pattern,
        validate_resource_type() should return the same string unchanged.
        """
        result = validate_resource_type(resource_type)
        assert result == resource_type
    
    @settings(max_examples=100)
    @given(invalid_type=st.text(min_size=1, max_size=50).filter(
        lambda x: not x.startswith('.') and '..' not in x
    ))
    def test_invalid_types_raise_or_pass(self, invalid_type):
        """
        Property: Invalid types either raise ValueError or pass validation.
        
        For any string, validate_resource_type() should either accept it or
        raise ValueError - it should never crash.
        """
        try:
            result = validate_resource_type(invalid_type)
            assert result == invalid_type
        except ValueError:
            pass


class TestResourceIdValidationProperties:
    """Property-based tests for resource ID validation."""
    
    @settings(max_examples=100)
    @given(resource_id=st.from_regex(r'^[a-zA-Z0-9:/_.\-]+$', fullmatch=True))
    def test_valid_resource_id_format_always_passes(self, resource_id):
        """
        Property: All strings matching resource ID format should validate.
        
        For any string that matches the AWS resource ID pattern,
        validate_resource_id() should return the same string unchanged.
        """
        # Skip if contains path traversal
        if '..' in resource_id:
            return
        
        result = validate_resource_id(resource_id)
        assert result == resource_id
    
    @settings(max_examples=100)
    @given(text=st.text(min_size=1, max_size=100))
    def test_path_traversal_always_rejected(self, text):
        """
        Property: Any string containing '..' should be rejected.
        
        For any string containing path traversal patterns,
        validate_resource_id() should raise ValueError.
        """
        if '..' in text:
            with pytest.raises(ValueError, match="Path traversal"):
                validate_resource_id(text)
    
    @settings(max_examples=100)
    @given(text=st.text(min_size=1, max_size=100))
    def test_shell_metacharacters_rejected(self, text):
        """
        Property: Strings with shell metacharacters should be rejected.
        
        For any string containing dangerous shell characters,
        validate_resource_id() should raise ValueError.
        """
        dangerous_chars = [';', '|', '&', '`', '\n', '\r']
        
        if any(char in text for char in dangerous_chars):
            with pytest.raises(ValueError):
                validate_resource_id(text)
