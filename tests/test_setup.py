"""
Test that the testing infrastructure is set up correctly.

This is a simple smoke test to verify pytest is working.
"""

def test_pytest_works():
    """Test that pytest can discover and run tests."""
    assert True


def test_imports_work():
    """Test that we can import required testing libraries."""
    import pytest
    import hypothesis
    from moto import mock_aws
    
    assert pytest is not None
    assert hypothesis is not None
    assert mock_aws is not None
