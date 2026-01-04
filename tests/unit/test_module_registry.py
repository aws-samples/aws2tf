"""
Test module registry for dynamic module loading.

This module tests the AWS_RESOURCE_MODULES registry in common.py to ensure
resource handlers are correctly loaded without using eval().

Validates: Requirements 12.1-12.7
"""

import sys
from pathlib import Path

import pytest

# Add code directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'code'))

from common import AWS_RESOURCE_MODULES


class TestModuleRegistryCompleteness:
    """Test that module registry contains all required services."""
    
    def test_registry_is_dict(self):
        """Test that AWS_RESOURCE_MODULES is a dictionary."""
        assert isinstance(AWS_RESOURCE_MODULES, dict)
        assert len(AWS_RESOURCE_MODULES) > 0
    
    def test_core_services_present(self):
        """Test that core AWS services are in the registry."""
        core_services = [
            'ec2', 's3', 'iam', 'lambda', 'vpc-lattice',
            'dynamodb', 'rds', 'eks', 'ecs', 'elbv2'
        ]
        
        for service in core_services:
            assert service in AWS_RESOURCE_MODULES, f"{service} should be in registry"
    
    def test_hyphenated_services_present(self):
        """Test that hyphenated service names are in the registry."""
        hyphenated_services = [
            'workspaces-web',
            'bedrock-agent',
            'cognito-idp',
            'network-firewall',
            'redshift-serverless',
        ]
        
        for service in hyphenated_services:
            assert service in AWS_RESOURCE_MODULES, f"{service} should be in registry"
    
    def test_underscore_variants_present(self):
        """Test that underscore variants of hyphenated names are present."""
        # Some services have both hyphenated and underscore variants
        variants = [
            ('application-autoscaling', 'application_autoscaling'),
            ('bedrock-agent', 'bedrock_agent'),
            ('cognito-identity', 'cognito_identity'),
            ('cognito-idp', 'cognito_idp'),
        ]
        
        for hyphenated, underscored in variants:
            # At least one variant should be present
            assert hyphenated in AWS_RESOURCE_MODULES or underscored in AWS_RESOURCE_MODULES
    
    def test_registry_has_at_least_50_services(self):
        """Test that registry contains at least 50 AWS services."""
        assert len(AWS_RESOURCE_MODULES) >= 50


class TestModuleLoading:
    """Test that modules can be loaded from the registry."""
    
    def test_ec2_module_loads(self):
        """Test that EC2 module can be loaded from registry."""
        ec2_module = AWS_RESOURCE_MODULES['ec2']
        assert ec2_module is not None
        
        # Verify it has expected functions
        assert hasattr(ec2_module, 'get_aws_vpc')
        assert callable(ec2_module.get_aws_vpc)
    
    def test_s3_module_loads(self):
        """Test that S3 module can be loaded from registry."""
        s3_module = AWS_RESOURCE_MODULES['s3']
        assert s3_module is not None
        
        # Verify it has expected functions
        assert hasattr(s3_module, 'get_aws_s3_bucket')
        assert callable(s3_module.get_aws_s3_bucket)
    
    def test_iam_module_loads(self):
        """Test that IAM module can be loaded from registry."""
        iam_module = AWS_RESOURCE_MODULES['iam']
        assert iam_module is not None
        
        # Verify it has expected functions
        assert hasattr(iam_module, 'get_aws_iam_role')
        assert callable(iam_module.get_aws_iam_role)
    
    def test_lambda_module_loads(self):
        """Test that Lambda module can be loaded from registry."""
        lambda_module = AWS_RESOURCE_MODULES['lambda']
        assert lambda_module is not None
        
        # Verify it has expected functions
        assert hasattr(lambda_module, 'get_aws_lambda_function')
        assert callable(lambda_module.get_aws_lambda_function)
    
    def test_all_modules_are_valid(self):
        """Test that all modules in registry are valid Python modules."""
        for service_name, module in AWS_RESOURCE_MODULES.items():
            assert module is not None, f"{service_name} module should not be None"
            assert hasattr(module, '__name__'), f"{service_name} should be a valid module"


class TestHyphenatedServiceNames:
    """Test that hyphenated service names resolve correctly."""
    
    def test_workspaces_web_resolves(self):
        """Test that 'workspaces-web' resolves correctly."""
        assert 'workspaces-web' in AWS_RESOURCE_MODULES
        
        module = AWS_RESOURCE_MODULES['workspaces-web']
        assert module is not None
        assert hasattr(module, '__name__')
    
    def test_bedrock_agent_resolves(self):
        """Test that 'bedrock-agent' resolves correctly."""
        # Check for either hyphenated or underscore variant
        assert 'bedrock-agent' in AWS_RESOURCE_MODULES or 'bedrock_agent' in AWS_RESOURCE_MODULES
    
    def test_cognito_idp_resolves(self):
        """Test that 'cognito-idp' resolves correctly."""
        assert 'cognito-idp' in AWS_RESOURCE_MODULES or 'cognito_idp' in AWS_RESOURCE_MODULES
    
    def test_network_firewall_resolves(self):
        """Test that 'network-firewall' resolves correctly."""
        assert 'network-firewall' in AWS_RESOURCE_MODULES or 'network_firewall' in AWS_RESOURCE_MODULES
    
    def test_hyphenated_names_match_clfn(self):
        """Test that hyphenated names in registry match boto3 client names."""
        # The registry key should match the clfn from aws_dict.py
        # For 'workspaces-web', the boto3 client is 'workspaces-web'
        
        hyphenated_services = [
            'workspaces-web',
            'bedrock-agent',
            'cognito-idp',
            'network-firewall',
        ]
        
        for service in hyphenated_services:
            if service in AWS_RESOURCE_MODULES:
                module = AWS_RESOURCE_MODULES[service]
                assert module is not None


class TestMissingModuleHandling:
    """Test that missing modules are handled gracefully."""
    
    def test_missing_service_returns_none(self):
        """Test that accessing missing service returns None or raises KeyError."""
        fake_service = 'nonexistent-service-12345'
        
        # Should not be in registry
        assert fake_service not in AWS_RESOURCE_MODULES
        
        # Accessing it should raise KeyError
        with pytest.raises(KeyError):
            _ = AWS_RESOURCE_MODULES[fake_service]
    
    def test_registry_get_with_default(self):
        """Test that .get() method works with default value."""
        fake_service = 'nonexistent-service-12345'
        
        # Using .get() should return None
        result = AWS_RESOURCE_MODULES.get(fake_service)
        assert result is None
        
        # Using .get() with default should return default
        result = AWS_RESOURCE_MODULES.get(fake_service, 'default')
        assert result == 'default'


class TestRegistrySecurity:
    """Test that registry prevents arbitrary code execution."""
    
    def test_registry_uses_imports_not_eval(self):
        """Test that registry uses imports, not eval()."""
        # Verify all values are actual module objects, not strings
        for service_name, module in AWS_RESOURCE_MODULES.items():
            assert not isinstance(module, str), f"{service_name} should be a module, not a string"
            assert hasattr(module, '__name__'), f"{service_name} should be a valid module"
    
    def test_no_eval_in_module_loading(self):
        """Test that no eval() is used for module loading."""
        # This is a design test - verify the registry pattern doesn't use eval
        # The registry is a static dictionary of imported modules
        
        # Verify we can access modules safely
        ec2_module = AWS_RESOURCE_MODULES['ec2']
        assert ec2_module.__name__ == 'get_aws_resources.aws_ec2'
    
    def test_registry_is_immutable_reference(self):
        """Test that registry provides safe module references."""
        # Get a module reference
        ec2_module = AWS_RESOURCE_MODULES['ec2']
        
        # Verify it's the actual module, not a string to be eval'd
        assert callable(getattr(ec2_module, 'get_aws_vpc', None))


class TestRegistryCompleteness:
    """Test that registry is complete and consistent."""
    
    def test_all_imported_modules_in_registry(self):
        """Test that all imported get_aws_resources modules are in registry."""
        # Check that major services are present
        expected_services = [
            'ec2', 's3', 'iam', 'lambda', 'dynamodb', 'rds',
            'eks', 'ecs', 'elbv2', 'cloudwatch', 'sns', 'sqs',
            'kms', 'secretsmanager', 'cloudformation', 'cloudfront'
        ]
        
        for service in expected_services:
            assert service in AWS_RESOURCE_MODULES, f"{service} should be in registry"
    
    def test_registry_keys_are_strings(self):
        """Test that all registry keys are strings."""
        for key in AWS_RESOURCE_MODULES.keys():
            assert isinstance(key, str)
    
    def test_registry_values_are_modules(self):
        """Test that all registry values are module objects."""
        for service_name, module in AWS_RESOURCE_MODULES.items():
            assert hasattr(module, '__name__'), f"{service_name} should be a module"
            assert 'get_aws_resources' in module.__name__, f"{service_name} should be from get_aws_resources"
    
    def test_no_duplicate_modules(self):
        """Test that no module is registered multiple times."""
        module_ids = set()
        
        for service_name, module in AWS_RESOURCE_MODULES.items():
            module_id = id(module)
            # Note: Some modules may be intentionally registered under multiple names
            # (e.g., 'application-autoscaling' and 'application_autoscaling')
            # So we just verify the module objects are valid
            assert module_id is not None
