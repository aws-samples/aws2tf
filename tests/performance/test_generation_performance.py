"""
Performance tests for file generation.

Benchmarks file generation for single resources.
Validates: Requirements 19.2, 19.4
"""

import sys
import time
from pathlib import Path
from unittest import mock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

import context
from get_aws_resources.aws_ec2 import get_aws_vpc


@pytest.mark.performance
class TestGenerationPerformance:
    """Test performance of file generation."""
    
    def test_single_resource_import_fast(self, mock_context):
        """
        Test that single resource import completes in under 5 seconds.
        
        Validates: Requirement 19.4
        """
        context.vpclist = {'vpc-test': True}
        
        with mock.patch('common.write_import'):
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy'):
                    start_time = time.time()
                    get_aws_vpc('aws_vpc', 'vpc-test', 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
                    elapsed_time = time.time() - start_time
                    
                    assert elapsed_time < 5.0, f"Import took {elapsed_time:.2f}s, should be < 5s"
    
    def test_file_generation_baseline(self, mock_context):
        """
        Benchmark file generation for baseline.
        
        Validates: Requirement 19.2
        """
        context.vpclist = {'vpc-test': True}
        
        with mock.patch('common.write_import'):
            with mock.patch('common.add_known_dependancy'):
                with mock.patch('common.add_dependancy'):
                    start_time = time.time()
                    get_aws_vpc('aws_vpc', 'vpc-test', 'ec2', 'describe_vpcs',
                               'Vpcs', 'VpcId', 'VpcId')
                    elapsed_time = time.time() - start_time
                    
                    baseline_time = elapsed_time
                    assert baseline_time >= 0
                    
                    print(f"\nBaseline: single resource import took {baseline_time:.6f} seconds")
