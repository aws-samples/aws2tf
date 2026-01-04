"""
Test EC2 resource handlers.

Tests handler functions in fixtf_ec2.py for EC2 resource transformations.
Validates: Requirements 4.1, 4.2, 4.3
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'code'))

import context
from fixtf_aws_resources import fixtf_ec2


class TestAwsEbsVolumeHandler:
    """Test aws_ebs_volume() handler."""
    
    def test_skips_zero_throughput(self):
        """Test that throughput=0 is skipped."""
        skip, t1, flag1, flag2 = fixtf_ec2.aws_ebs_volume(
            "throughput = 0\n",
            "throughput",
            "0",
            0,
            0
        )
        
        assert skip == 1
    
    def test_keeps_nonzero_throughput(self):
        """Test that non-zero throughput is kept."""
        skip, t1, flag1, flag2 = fixtf_ec2.aws_ebs_volume(
            "throughput = 125\n",
            "throughput",
            "125",
            0,
            0
        )
        
        assert skip == 0
    
    def test_skips_zero_volume_initialization_rate(self):
        """Test that volume_initialization_rate=0 is skipped."""
        skip, t1, flag1, flag2 = fixtf_ec2.aws_ebs_volume(
            "volume_initialization_rate = 0\n",
            "volume_initialization_rate",
            "0",
            0,
            0
        )
        
        assert skip == 1


class TestAwsDefaultSecurityGroupHandler:
    """Test aws_default_security_group() handler."""
    
    def test_name_field_sets_flag(self):
        """Test that name field sets flag1."""
        context.lbc = 0
        
        skip, t1, flag1, flag2 = fixtf_ec2.aws_default_security_group(
            'name = "default"\n',
            "name",
            '"default"',
            0,
            0
        )
        
        assert flag1 == True
    
    def test_skips_empty_egress_block(self):
        """Test that empty egress block is skipped."""
        context.lbc = 0
        
        skip, t1, flag1, flag2 = fixtf_ec2.aws_default_security_group(
            "egress = []\n",
            "egress",
            "[]",
            0,
            0
        )
        
        assert skip == 1
    
    def test_skips_empty_ingress_block(self):
        """Test that empty ingress block is skipped."""
        context.lbc = 0
        
        skip, t1, flag1, flag2 = fixtf_ec2.aws_default_security_group(
            "ingress = []\n",
            "ingress",
            "[]",
            0,
            0
        )
        
        assert skip == 1


class TestHandlerPatterns:
    """Test common handler patterns."""
    
    def test_handlers_return_four_values(self):
        """Test that handlers return (skip, t1, flag1, flag2)."""
        result = fixtf_ec2.aws_ebs_volume("test\n", "test", "test", 0, 0)
        
        assert isinstance(result, tuple)
        assert len(result) == 4
        
        skip, t1, flag1, flag2 = result
        assert isinstance(skip, int)
        assert isinstance(t1, str)
        assert isinstance(flag1, int)
        assert isinstance(flag2, int)
    
    def test_skip_values_are_binary(self):
        """Test that skip values are 0 or 1."""
        skip, t1, flag1, flag2 = fixtf_ec2.aws_ebs_volume("test\n", "test", "test", 0, 0)
        
        assert skip in [0, 1]
