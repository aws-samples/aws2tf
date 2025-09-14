#!/usr/bin/env python3
"""Debug script for terraform importer."""

import sys
sys.path.insert(0, '.')

from code.config import create_test_config
from code.terraform_importer import TerraformImporter, ImportValidationResult

# Create test config and importer
config = create_test_config()
importer = TerraformImporter(config)

# Test VPC command generation
command = importer.generate_import_command(
    "aws_vpc", "main_vpc", "vpc-123456"
)

print(f"Resource type: {command.resource_type}")
print(f"Resource name: {command.resource_name}")
print(f"AWS resource ID: {command.aws_resource_id}")
print(f"Validation result: {command.validation_result}")
print(f"Validation message: {command.validation_message}")
print(f"Import command: {command.import_command}")

# Check if aws_vpc is supported
supported = importer._is_supported_resource_type("aws_vpc")
print(f"aws_vpc supported: {supported}")

# Check validation patterns
print(f"Available patterns: {list(importer.resource_id_patterns.keys())[:10]}")

# Test validation directly
validation_result, message = importer._validate_resource_id("aws_vpc", "vpc-123456")
print(f"Direct validation: {validation_result}, {message}")