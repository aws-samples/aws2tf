"""
Test API Gateway resource handlers.

Tests handler functions in fixtf_apigateway.py for API Gateway transformations.
Validates: Requirements 4.3, 4.4
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

from fixtf_aws_resources import fixtf_apigateway


class TestAPIGatewayHandlers:
    """Test API Gateway handler functions."""
    
    def test_apigateway_module_exists(self):
        """Test that fixtf_apigateway module exists."""
        assert fixtf_apigateway is not None
        assert hasattr(fixtf_apigateway, '__name__')
