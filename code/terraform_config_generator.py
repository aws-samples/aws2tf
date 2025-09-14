#!/usr/bin/env python3
"""
Terraform Configuration File Generator for aws2tf.

This module provides comprehensive terraform configuration generation including:
1. Terraform resource block generation from AWS resource data
2. Dependency management and reference resolution
3. Configuration file organization and naming conventions
4. Provider configuration and version constraints
5. Variable and output generation
6. Integration with configuration management system
"""

import os
import re
import json
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import threading
from datetime import datetime

from .config import ConfigurationManager

class ConfigFileType(Enum):
    """Types of terraform configuration files."""
    MAIN = "main"
    VARIABLES = "variables"
    OUTPUTS = "outputs"
    PROVIDERS = "providers"
    VERSIONS = "versions"
    LOCALS = "locals"
    DATA = "data"


class ResourceBlockStyle(Enum):
    """Styles for generating resource blocks."""
    COMPACT = "compact"
    EXPANDED = "expanded"
    MINIMAL = "minimal"


@dataclass
class TerraformResource:
    """Represents a terraform resource configuration."""
    resource_type: str
    resource_name: str
    attributes: Dict[str, Any] = field(default_factory=dict)
    dependencies: Set[str] = field(default_factory=set)
    tags: Dict[str, str] = field(default_factory=dict)
    lifecycle_rules: Dict[str, Any] = field(default_factory=dict)
    count_expression: Optional[str] = None
    for_each_expression: Optional[str] = None
    
    @property
    def full_address(self) -> str:
        """Get the full terraform address."""
        return f"{self.resource_type}.{self.resource_name}"
    
    def add_dependency(self, dependency: str) -> None:
        """Add a dependency reference."""
        self.dependencies.add(dependency)
    
    def set_attribute(self, key: str, value: Any) -> None:
        """Set a resource attribute."""
        self.attributes[key] = value
    
    def add_tag(self, key: str, value: str) -> None:
        """Add a tag to the resource."""
        self.tags[key] = value


@dataclass
class TerraformVariable:
    """Represents a terraform variable."""
    name: str
    type_constraint: str = "string"
    description: str = ""
    default_value: Any = None
    sensitive: bool = False
    validation_rules: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class TerraformOutput:
    """Represents a terraform output."""
    name: str
    value: str
    description: str = ""
    sensitive: bool = False


@dataclass
class GeneratedFile:
    """Represents a generated terraform configuration file."""
    file_path: Path
    file_type: ConfigFileType
    content: str
    resources: List[str] = field(default_factory=list)
    checksum: str = ""
    
    def calculate_checksum(self) -> str:
        """Calculate content checksum."""
        import hashlib
        self.checksum = hashlib.sha256(self.content.encode()).hexdigest()
        return self.checksumclass T
erraformConfigGenerator:
    """Main terraform configuration file generator."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.output_dir = Path(config.runtime.path1) if config.runtime.path1 else Path(".")
        self.lock = threading.Lock()
        
        # Generated resources and files
        self.resources: Dict[str, TerraformResource] = {}
        self.variables: Dict[str, TerraformVariable] = {}
        self.outputs: Dict[str, TerraformOutput] = {}
        self.generated_files: Dict[str, GeneratedFile] = {}
        
        # Configuration settings
        self.block_style = ResourceBlockStyle.EXPANDED
        self.include_comments = True
        self.sort_attributes = True
        self.group_by_type = True
        
        # AWS resource attribute mappings
        self.attribute_mappings = self._initialize_attribute_mappings()
        
        # Terraform formatting settings
        self.indent_size = 2
        self.max_line_length = 120 
   def _initialize_attribute_mappings(self) -> Dict[str, Dict[str, Any]]:
        """Initialize AWS resource attribute mappings for terraform."""
        return {
            "aws_vpc": {
                "required": ["cidr_block"],
                "optional": ["enable_dns_hostnames", "enable_dns_support", "instance_tenancy"],
                "computed": ["id", "arn", "default_network_acl_id", "default_route_table_id"],
                "references": {},
                "tags_supported": True
            },
            "aws_subnet": {
                "required": ["vpc_id", "cidr_block"],
                "optional": ["availability_zone", "map_public_ip_on_launch"],
                "computed": ["id", "arn", "availability_zone_id"],
                "references": {"vpc_id": "aws_vpc"},
                "tags_supported": True
            },
            "aws_internet_gateway": {
                "required": ["vpc_id"],
                "optional": [],
                "computed": ["id", "arn"],
                "references": {"vpc_id": "aws_vpc"},
                "tags_supported": True
            },
            "aws_nat_gateway": {
                "required": ["allocation_id", "subnet_id"],
                "optional": ["connectivity_type"],
                "computed": ["id", "network_interface_id", "private_ip", "public_ip"],
                "references": {"subnet_id": "aws_subnet", "allocation_id": "aws_eip"},
                "tags_supported": True
            },
            "aws_route_table": {
                "required": ["vpc_id"],
                "optional": ["route"],
                "computed": ["id", "arn"],
                "references": {"vpc_id": "aws_vpc"},
                "tags_supported": True
            },
            "aws_security_group": {
                "required": ["name", "vpc_id"],
                "optional": ["description", "ingress", "egress"],
                "computed": ["id", "arn"],
                "references": {"vpc_id": "aws_vpc"},
                "tags_supported": True
            },
            "aws_instance": {
                "required": ["ami", "instance_type"],
                "optional": ["subnet_id", "vpc_security_group_ids", "key_name", "user_data"],
                "computed": ["id", "arn", "private_ip", "public_ip", "private_dns", "public_dns"],
                "references": {"subnet_id": "aws_subnet", "vpc_security_group_ids": "aws_security_group"},
                "tags_supported": True
            }
        }    d
ef add_resource_from_aws_data(self, resource_type: str, resource_name: str, 
                                  aws_data: Dict[str, Any]) -> TerraformResource:
        """
        Create terraform resource from AWS resource data.
        
        Args:
            resource_type: Terraform resource type (e.g., 'aws_vpc')
            resource_name: Terraform resource name
            aws_data: AWS resource data from discovery
            
        Returns:
            Created TerraformResource
        """
        resource = TerraformResource(
            resource_type=resource_type,
            resource_name=resource_name
        )
        
        # Get attribute mapping for this resource type
        mapping = self.attribute_mappings.get(resource_type, {})
        required_attrs = mapping.get("required", [])
        optional_attrs = mapping.get("optional", [])
        references = mapping.get("references", {})
        
        # Map AWS attributes to terraform attributes
        for attr in required_attrs + optional_attrs:
            if attr in aws_data:
                value = aws_data[attr]
                
                # Handle reference attributes
                if attr in references:
                    ref_type = references[attr]
                    if isinstance(value, str) and value:
                        # Create terraform reference
                        ref_name = self._sanitize_name(value)
                        terraform_ref = f"{ref_type}.{ref_name}.id"
                        resource.set_attribute(attr, f"${{{terraform_ref}}}")
                        resource.add_dependency(f"{ref_type}.{ref_name}")
                    elif isinstance(value, list):
                        # Handle list of references
                        refs = []
                        for item in value:
                            if isinstance(item, str) and item:
                                ref_name = self._sanitize_name(item)
                                refs.append(f"${{{ref_type}.{ref_name}.id}}")
                                resource.add_dependency(f"{ref_type}.{ref_name}")
                        resource.set_attribute(attr, refs)
                else:
                    # Direct attribute mapping
                    resource.set_attribute(attr, value)
        
        # Handle tags
        if mapping.get("tags_supported", False) and "Tags" in aws_data:
            tags = {}
            for tag in aws_data.get("Tags", []):
                if isinstance(tag, dict) and "Key" in tag and "Value" in tag:
                    tags[tag["Key"]] = tag["Value"]
            
            if tags:
                resource.tags = tags
        
        # Store resource
        with self.lock:
            self.resources[resource.full_address] = resource
        
        return resource 
   def _sanitize_name(self, name: str) -> str:
        """Sanitize AWS resource ID for use as terraform resource name."""
        # Replace hyphens and other special characters with underscores
        sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        
        # Ensure it starts with a letter or underscore
        if sanitized and sanitized[0].isdigit():
            sanitized = f"_{sanitized}"
        
        return sanitized or "unnamed"
    
    def add_variable(self, name: str, type_constraint: str = "string", 
                    description: str = "", default_value: Any = None) -> TerraformVariable:
        """Add a terraform variable."""
        variable = TerraformVariable(
            name=name,
            type_constraint=type_constraint,
            description=description,
            default_value=default_value
        )
        
        with self.lock:
            self.variables[name] = variable
        
        return variable
    
    def add_output(self, name: str, value: str, description: str = "") -> TerraformOutput:
        """Add a terraform output."""
        output = TerraformOutput(
            name=name,
            value=value,
            description=description
        )
        
        with self.lock:
            self.outputs[name] = output
        
        return output    d
ef generate_resource_block(self, resource: TerraformResource) -> str:
        """Generate terraform resource block."""
        lines = []
        
        # Resource declaration
        if self.include_comments:
            lines.append(f"# {resource.resource_type} - {resource.resource_name}")
        
        lines.append(f'resource "{resource.resource_type}" "{resource.resource_name}" {{')
        
        # Attributes
        attributes = resource.attributes.copy()
        if self.sort_attributes:
            # Sort attributes with required ones first
            mapping = self.attribute_mappings.get(resource.resource_type, {})
            required = mapping.get("required", [])
            
            sorted_attrs = []
            # Add required attributes first
            for attr in required:
                if attr in attributes:
                    sorted_attrs.append((attr, attributes.pop(attr)))
            
            # Add remaining attributes alphabetically
            for attr in sorted(attributes.keys()):
                sorted_attrs.append((attr, attributes[attr]))
            
            attributes = dict(sorted_attrs)
        
        # Generate attribute lines
        for key, value in attributes.items():
            attr_line = self._format_attribute(key, value)
            lines.append(f"  {attr_line}")
        
        # Tags
        if resource.tags:
            lines.append("")
            lines.append("  tags = {")
            for tag_key, tag_value in sorted(resource.tags.items()):
                lines.append(f'    {tag_key} = "{tag_value}"')
            lines.append("  }")
        
        # Lifecycle rules
        if resource.lifecycle_rules:
            lines.append("")
            lines.append("  lifecycle {")
            for rule, value in resource.lifecycle_rules.items():
                if isinstance(value, bool):
                    lines.append(f"    {rule} = {str(value).lower()}")
                elif isinstance(value, list):
                    formatted_list = "[" + ", ".join(f'"{item}"' for item in value) + "]"
                    lines.append(f"    {rule} = {formatted_list}")
                else:
                    lines.append(f"    {rule} = {value}")
            lines.append("  }")
        
        lines.append("}")
        
        return "\n".join(lines)    def 
_format_attribute(self, key: str, value: Any) -> str:
        """Format a terraform attribute."""
        if isinstance(value, str):
            if value.startswith("${") and value.endswith("}"):
                # Terraform expression/reference
                return f"{key} = {value}"
            else:
                # String literal
                return f'{key} = "{value}"'
        elif isinstance(value, bool):
            return f"{key} = {str(value).lower()}"
        elif isinstance(value, (int, float)):
            return f"{key} = {value}"
        elif isinstance(value, list):
            if not value:
                return f"{key} = []"
            
            # Format list elements
            formatted_items = []
            for item in value:
                if isinstance(item, str):
                    if item.startswith("${") and item.endswith("}"):
                        formatted_items.append(item)
                    else:
                        formatted_items.append(f'"{item}"')
                else:
                    formatted_items.append(str(item))
            
            if len(formatted_items) == 1:
                return f"{key} = [{formatted_items[0]}]"
            else:
                items_str = ",\n    ".join(formatted_items)
                return f"{key} = [\n    {items_str}\n  ]"
        elif isinstance(value, dict):
            if not value:
                return f"{key} = {{}}"
            
            # Format nested object
            items = []
            for k, v in value.items():
                if isinstance(v, str):
                    items.append(f'{k} = "{v}"')
                else:
                    items.append(f"{k} = {v}")
            
            if len(items) == 1:
                return f"{key} = {{ {items[0]} }}"
            else:
                items_str = "\n    ".join(items)
                return f"{key} = {{\n    {items_str}\n  }}"
        else:
            return f"{key} = {value}"    de
f generate_variables_file(self) -> str:
        """Generate variables.tf content."""
        if not self.variables:
            return ""
        
        lines = []
        lines.append("# Terraform Variables")
        lines.append(f"# Generated by aws2tf on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        for var_name, variable in sorted(self.variables.items()):
            if self.include_comments and variable.description:
                lines.append(f"# {variable.description}")
            
            lines.append(f'variable "{var_name}" {{')
            lines.append(f'  type = {variable.type_constraint}')
            
            if variable.description:
                lines.append(f'  description = "{variable.description}"')
            
            if variable.default_value is not None:
                if isinstance(variable.default_value, str):
                    lines.append(f'  default = "{variable.default_value}"')
                else:
                    lines.append(f'  default = {variable.default_value}')
            
            if variable.sensitive:
                lines.append("  sensitive = true")
            
            for validation in variable.validation_rules:
                lines.append("  validation {")
                lines.append(f'    condition = {validation["condition"]}')
                lines.append(f'    error_message = "{validation["error_message"]}"')
                lines.append("  }")
            
            lines.append("}")
            lines.append("")
        
        return "\n".join(lines)
    
    def generate_outputs_file(self) -> str:
        """Generate outputs.tf content."""
        if not self.outputs:
            return ""
        
        lines = []
        lines.append("# Terraform Outputs")
        lines.append(f"# Generated by aws2tf on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        for output_name, output in sorted(self.outputs.items()):
            if self.include_comments and output.description:
                lines.append(f"# {output.description}")
            
            lines.append(f'output "{output_name}" {{')
            lines.append(f"  value = {output.value}")
            
            if output.description:
                lines.append(f'  description = "{output.description}"')
            
            if output.sensitive:
                lines.append("  sensitive = true")
            
            lines.append("}")
            lines.append("")
        
        return "\n".join(lines) 
   def generate_providers_file(self) -> str:
        """Generate providers.tf content."""
        lines = []
        lines.append("# Terraform Providers Configuration")
        lines.append(f"# Generated by aws2tf on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # AWS Provider
        lines.append('provider "aws" {')
        if self.config.aws.region:
            lines.append(f'  region = "{self.config.aws.region}"')
        if self.config.aws.profile:
            lines.append(f'  profile = "{self.config.aws.profile}"')
        lines.append("")
        lines.append("  # Default tags for all resources")
        lines.append("  default_tags {")
        lines.append("    tags = {")
        lines.append('      ManagedBy = "terraform"')
        lines.append('      CreatedBy = "aws2tf"')
        if self.config.aws.account_id:
            lines.append(f'      Account = "{self.config.aws.account_id}"')
        lines.append("    }")
        lines.append("  }")
        lines.append("}")
        lines.append("")
        
        return "\n".join(lines)
    
    def generate_versions_file(self) -> str:
        """Generate versions.tf content."""
        lines = []
        lines.append("# Terraform Version Constraints")
        lines.append(f"# Generated by aws2tf on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        lines.append("terraform {")
        lines.append("  required_version = \">= 1.0\"")
        lines.append("")
        lines.append("  required_providers {")
        lines.append("    aws = {")
        lines.append('      source  = "hashicorp/aws"')
        lines.append('      version = "~> 5.0"')
        lines.append("    }")
        lines.append("  }")
        lines.append("}")
        lines.append("")
        
        return "\n".join(lines)    def 
generate_main_file(self, resources_to_include: Optional[List[str]] = None) -> str:
        """Generate main.tf content with resources."""
        lines = []
        lines.append("# Main Terraform Configuration")
        lines.append(f"# Generated by aws2tf on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # Filter resources if specified
        if resources_to_include:
            resources_to_generate = {
                addr: res for addr, res in self.resources.items() 
                if addr in resources_to_include
            }
        else:
            resources_to_generate = self.resources
        
        if not resources_to_generate:
            lines.append("# No resources to generate")
            return "\n".join(lines)
        
        # Group resources by type if enabled
        if self.group_by_type:
            resources_by_type = {}
            for addr, resource in resources_to_generate.items():
                resource_type = resource.resource_type
                if resource_type not in resources_by_type:
                    resources_by_type[resource_type] = []
                resources_by_type[resource_type].append(resource)
            
            # Generate resources grouped by type
            for resource_type in sorted(resources_by_type.keys()):
                lines.append(f"# {resource_type.upper()} Resources")
                lines.append("")
                
                for resource in sorted(resources_by_type[resource_type], 
                                     key=lambda r: r.resource_name):
                    resource_block = self.generate_resource_block(resource)
                    lines.append(resource_block)
                    lines.append("")
        else:
            # Generate resources in alphabetical order
            for addr in sorted(resources_to_generate.keys()):
                resource = resources_to_generate[addr]
                resource_block = self.generate_resource_block(resource)
                lines.append(resource_block)
                lines.append("")
        
        return "\n".join(lines)    def g
enerate_all_files(self) -> Dict[str, GeneratedFile]:
        """Generate all terraform configuration files."""
        generated_files = {}
        
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate main configuration
        main_content = self.generate_main_file()
        if main_content.strip():
            main_file = GeneratedFile(
                file_path=self.output_dir / "main.tf",
                file_type=ConfigFileType.MAIN,
                content=main_content,
                resources=list(self.resources.keys())
            )
            main_file.calculate_checksum()
            generated_files["main.tf"] = main_file
        
        # Generate variables
        variables_content = self.generate_variables_file()
        if variables_content.strip():
            variables_file = GeneratedFile(
                file_path=self.output_dir / "variables.tf",
                file_type=ConfigFileType.VARIABLES,
                content=variables_content
            )
            variables_file.calculate_checksum()
            generated_files["variables.tf"] = variables_file
        
        # Generate outputs
        outputs_content = self.generate_outputs_file()
        if outputs_content.strip():
            outputs_file = GeneratedFile(
                file_path=self.output_dir / "outputs.tf",
                file_type=ConfigFileType.OUTPUTS,
                content=outputs_content
            )
            outputs_file.calculate_checksum()
            generated_files["outputs.tf"] = outputs_file
        
        # Generate providers
        providers_content = self.generate_providers_file()
        providers_file = GeneratedFile(
            file_path=self.output_dir / "providers.tf",
            file_type=ConfigFileType.PROVIDERS,
            content=providers_content
        )
        providers_file.calculate_checksum()
        generated_files["providers.tf"] = providers_file
        
        # Generate versions
        versions_content = self.generate_versions_file()
        versions_file = GeneratedFile(
            file_path=self.output_dir / "versions.tf",
            file_type=ConfigFileType.VERSIONS,
            content=versions_content
        )
        versions_file.calculate_checksum()
        generated_files["versions.tf"] = versions_file
        
        # Store generated files
        with self.lock:
            self.generated_files.update(generated_files)
        
        return generated_files    def 
write_files_to_disk(self, files: Optional[Dict[str, GeneratedFile]] = None) -> List[Path]:
        """Write generated files to disk."""
        if files is None:
            files = self.generated_files
        
        written_files = []
        
        for filename, generated_file in files.items():
            try:
                with open(generated_file.file_path, 'w') as f:
                    f.write(generated_file.content)
                
                written_files.append(generated_file.file_path)
                
                if self.config.debug.enabled:
                    print(f"Generated terraform file: {generated_file.file_path}")
                    
            except Exception as e:
                if self.config.debug.enabled:
                    print(f"Error writing file {generated_file.file_path}: {e}")
        
        return written_files
    
    def add_common_outputs(self) -> None:
        """Add common outputs for AWS resources."""
        # VPC outputs
        vpc_resources = [r for r in self.resources.values() if r.resource_type == "aws_vpc"]
        for vpc in vpc_resources:
            self.add_output(
                f"vpc_{vpc.resource_name}_id",
                f"${{{vpc.full_address}.id}}",
                f"ID of VPC {vpc.resource_name}"
            )
        
        # Subnet outputs
        subnet_resources = [r for r in self.resources.values() if r.resource_type == "aws_subnet"]
        for subnet in subnet_resources:
            self.add_output(
                f"subnet_{subnet.resource_name}_id",
                f"${{{subnet.full_address}.id}}",
                f"ID of subnet {subnet.resource_name}"
            )
        
        # Security group outputs
        sg_resources = [r for r in self.resources.values() if r.resource_type == "aws_security_group"]
        for sg in sg_resources:
            self.add_output(
                f"security_group_{sg.resource_name}_id",
                f"${{{sg.full_address}.id}}",
                f"ID of security group {sg.resource_name}"
            )    def a
dd_common_variables(self) -> None:
        """Add common variables for AWS resources."""
        self.add_variable(
            "aws_region",
            "string",
            "AWS region for resources",
            self.config.aws.region or "us-east-1"
        )
        
        self.add_variable(
            "environment",
            "string",
            "Environment name (e.g., dev, staging, prod)",
            "dev"
        )
        
        self.add_variable(
            "project_name",
            "string",
            "Name of the project",
            "aws2tf-imported"
        )
        
        # Add validation for environment
        if "environment" in self.variables:
            self.variables["environment"].validation_rules.append({
                "condition": "contains([\"dev\", \"staging\", \"prod\"], var.environment)",
                "error_message": "Environment must be dev, staging, or prod."
            })
    
    def optimize_references(self) -> None:
        """Optimize terraform references between resources."""
        # Build reference map
        resource_ids = {}
        for resource in self.resources.values():
            if "id" in resource.attributes:
                aws_id = resource.attributes["id"]
                if isinstance(aws_id, str) and not aws_id.startswith("${"):
                    resource_ids[aws_id] = resource.full_address
        
        # Update references in all resources
        for resource in self.resources.values():
            for attr_name, attr_value in resource.attributes.items():
                if isinstance(attr_value, str) and attr_value in resource_ids:
                    # Replace with terraform reference
                    ref_address = resource_ids[attr_value]
                    resource.attributes[attr_name] = f"${{{ref_address}.id}}"
                    resource.add_dependency(ref_address)
                elif isinstance(attr_value, list):
                    # Handle list of IDs
                    updated_list = []
                    for item in attr_value:
                        if isinstance(item, str) and item in resource_ids:
                            ref_address = resource_ids[item]
                            updated_list.append(f"${{{ref_address}.id}}")
                            resource.add_dependency(ref_address)
                        else:
                            updated_list.append(item)
                    resource.attributes[attr_name] = updated_list    def
 get_generation_summary(self) -> Dict[str, Any]:
        """Get summary of configuration generation."""
        resource_counts = {}
        for resource in self.resources.values():
            resource_type = resource.resource_type
            resource_counts[resource_type] = resource_counts.get(resource_type, 0) + 1
        
        return {
            "total_resources": len(self.resources),
            "resource_types": resource_counts,
            "variables_count": len(self.variables),
            "outputs_count": len(self.outputs),
            "generated_files": len(self.generated_files),
            "output_directory": str(self.output_dir)
        }
    
    def clear_all(self) -> None:
        """Clear all generated content."""
        with self.lock:
            self.resources.clear()
            self.variables.clear()
            self.outputs.clear()
            self.generated_files.clear()


def create_terraform_config_generator(config: ConfigurationManager) -> TerraformConfigGenerator:
    """Factory function to create TerraformConfigGenerator."""
    return TerraformConfigGenerator(config)


def generate_terraform_configs_from_resources(config: ConfigurationManager,
                                            discovered_resources: Dict[str, Any]) -> TerraformConfigGenerator:
    """
    Generate terraform configurations from discovered resources.
    
    Args:
        config: Configuration manager
        discovered_resources: Dictionary of discovered resources
        
    Returns:
        TerraformConfigGenerator with generated configurations
    """
    generator = create_terraform_config_generator(config)
    
    # Add resources from discovery data
    for resource_name, resource_info in discovered_resources.items():
        if '.' in resource_name:
            resource_type, resource_id = resource_name.split('.', 1)
            
            # Sanitize resource name for terraform
            terraform_name = generator._sanitize_name(resource_id)
            
            # Get AWS data
            aws_data = resource_info.get('aws_data', {})
            
            # Add resource
            generator.add_resource_from_aws_data(
                resource_type=resource_type,
                resource_name=terraform_name,
                aws_data=aws_data
            )
    
    # Optimize references between resources
    generator.optimize_references()
    
    # Add common variables and outputs
    generator.add_common_variables()
    generator.add_common_outputs()
    
    return generator