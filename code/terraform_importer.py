#!/usr/bin/env python3
"""
Terraform Import Command Generator for aws2tf.

This module provides comprehensive terraform import functionality including:
1. Import command generation for all AWS resource types
2. Resource ID validation and transformation
3. Import command validation and error handling
4. Batch import operations with dependency ordering
5. Integration with configuration management system
"""

import os
import re
import json
import subprocess
import time
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config import ConfigurationManager


class ImportStatus(Enum):
    """Status of terraform import operations."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class ImportValidationResult(Enum):
    """Result of import command validation."""
    VALID = "valid"
    INVALID_RESOURCE_TYPE = "invalid_resource_type"
    INVALID_RESOURCE_ID = "invalid_resource_id"
    MISSING_TERRAFORM_RESOURCE = "missing_terraform_resource"
    ALREADY_IMPORTED = "already_imported"


@dataclass
class ImportCommand:
    """Represents a terraform import command."""
    resource_type: str
    resource_name: str
    terraform_address: str
    aws_resource_id: str
    import_command: str
    validation_result: ImportValidationResult = ImportValidationResult.VALID
    validation_message: Optional[str] = None
    dependencies: Set[str] = field(default_factory=set)
    status: ImportStatus = ImportStatus.PENDING
    execution_time: Optional[float] = None
    error_message: Optional[str] = None
    
    @property
    def full_terraform_address(self) -> str:
        """Get the full terraform address."""
        return f"{self.resource_type}.{self.resource_name}"
    
    def is_valid(self) -> bool:
        """Check if the import command is valid."""
        return self.validation_result == ImportValidationResult.VALID


@dataclass
class ImportResult:
    """Result of a terraform import operation."""
    command: ImportCommand
    success: bool
    stdout: str = ""
    stderr: str = ""
    return_code: int = 0
    execution_time: float = 0.0
    imported_resources: List[str] = field(default_factory=list)


class TerraformImporter:
    """Main terraform import command generator and executor."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.import_commands: Dict[str, ImportCommand] = {}
        self.import_results: Dict[str, ImportResult] = {}
        self.lock = threading.Lock()
        
        # Resource ID patterns for validation
        self.resource_id_patterns = self._initialize_resource_patterns()
        
        # Resource type mappings
        self.resource_type_mappings = self._initialize_resource_mappings()
        
        # Terraform working directory
        self.terraform_dir = Path(config.runtime.path1) if config.runtime.path1 else Path(".")
    
    def _initialize_resource_patterns(self) -> Dict[str, str]:
        """Initialize AWS resource ID validation patterns."""
        return {
            # VPC Resources
            "aws_vpc": r"^vpc-[0-9a-fA-F]{8,17}$",
            "aws_subnet": r"^subnet-[0-9a-fA-F]{8,17}$",
            "aws_internet_gateway": r"^igw-[0-9a-fA-F]{8,17}$",
            "aws_nat_gateway": r"^nat-[0-9a-fA-F]{17}$",
            "aws_route_table": r"^rtb-[0-9a-fA-F]{8,17}$",
            "aws_security_group": r"^sg-[0-9a-fA-F]{8,17}$",
            "aws_network_acl": r"^acl-[0-9a-fA-F]{8,17}$",
            "aws_vpc_endpoint": r"^vpce-[0-9a-fA-F]{8,17}$",
            
            # EC2 Resources
            "aws_instance": r"^i-[0-9a-f]{8,17}$",
            "aws_key_pair": r"^[a-zA-Z0-9\-_\.]{1,255}$",
            "aws_eip": r"^eipalloc-[0-9a-f]{8,17}$",
            "aws_volume": r"^vol-[0-9a-f]{8,17}$",
            "aws_snapshot": r"^snap-[0-9a-f]{8,17}$",
            "aws_ami": r"^ami-[0-9a-f]{8,17}$",
            "aws_launch_template": r"^lt-[0-9a-f]{8,17}$",
            "aws_launch_configuration": r"^[a-zA-Z0-9\-_\.]{1,255}$",
            
            # Load Balancer Resources
            "aws_lb": r"^arn:aws:elasticloadbalancing:[^:]+:[^:]+:loadbalancer/.+$",
            "aws_lb_target_group": r"^arn:aws:elasticloadbalancing:[^:]+:[^:]+:targetgroup/.+$",
            "aws_lb_listener": r"^arn:aws:elasticloadbalancing:[^:]+:[^:]+:listener/.+$",
            
            # Auto Scaling Resources
            "aws_autoscaling_group": r"^[a-zA-Z0-9\-_\.]{1,255}$",
            "aws_autoscaling_policy": r"^arn:aws:autoscaling:[^:]+:[^:]+:scalingPolicy:.+$",
            
            # RDS Resources
            "aws_db_instance": r"^[a-zA-Z0-9\-]{1,63}$",
            "aws_db_subnet_group": r"^[a-zA-Z0-9\-]{1,255}$",
            "aws_db_parameter_group": r"^[a-zA-Z0-9\-]{1,255}$",
            "aws_rds_cluster": r"^[a-zA-Z0-9\-]{1,63}$",
            
            # IAM Resources
            "aws_iam_role": r"^[a-zA-Z0-9+=,.@\-_]{1,64}$",
            "aws_iam_policy": r"^arn:aws:iam::[^:]+:policy/.+$",
            "aws_iam_user": r"^[a-zA-Z0-9+=,.@\-_]{1,64}$",
            "aws_iam_group": r"^[a-zA-Z0-9+=,.@\-_]{1,128}$",
            "aws_iam_instance_profile": r"^[a-zA-Z0-9+=,.@\-_]{1,128}$",
            
            # S3 Resources
            "aws_s3_bucket": r"^[a-z0-9\-\.]{3,63}$",
            "aws_s3_bucket_policy": r"^[a-z0-9\-\.]{3,63}$",
            
            # Lambda Resources
            "aws_lambda_function": r"^[a-zA-Z0-9\-_]{1,64}$",
            "aws_lambda_layer_version": r"^arn:aws:lambda:[^:]+:[^:]+:layer:.+$",
            
            # EKS Resources
            "aws_eks_cluster": r"^[a-zA-Z0-9\-]{1,100}$",
            "aws_eks_node_group": r"^[a-zA-Z0-9\-]{1,63}$",
            
            # CloudWatch Resources
            "aws_cloudwatch_log_group": r"^[a-zA-Z0-9\-_/\.]{1,512}$",
            "aws_cloudwatch_metric_alarm": r"^[a-zA-Z0-9\-_]{1,255}$",
            
            # SNS/SQS Resources
            "aws_sns_topic": r"^arn:aws:sns:[^:]+:[^:]+:.+$",
            "aws_sqs_queue": r"^https://sqs\.[^/]+/[^/]+/.+$",
            
            # KMS Resources
            "aws_kms_key": r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
            "aws_kms_alias": r"^alias/[a-zA-Z0-9\-_/]{1,256}$",
        }
    
    def _initialize_resource_mappings(self) -> Dict[str, Dict[str, Any]]:
        """Initialize resource type mappings and special handling."""
        return {
            # Resources that need special ID transformation
            "aws_route_table_association": {
                "id_format": "subnet_id/route_table_id",
                "requires_lookup": True
            },
            "aws_security_group_rule": {
                "id_format": "sg_id_direction_protocol_from_port_to_port_cidr",
                "requires_lookup": True
            },
            "aws_lb_listener_rule": {
                "id_format": "listener_arn:priority",
                "requires_lookup": True
            },
            "aws_iam_role_policy_attachment": {
                "id_format": "role_name/policy_arn",
                "requires_lookup": True
            },
            
            # Resources with ARN-based IDs
            "aws_lb": {"id_type": "arn"},
            "aws_lb_target_group": {"id_type": "arn"},
            "aws_lb_listener": {"id_type": "arn"},
            "aws_sns_topic": {"id_type": "arn"},
            "aws_iam_policy": {"id_type": "arn"},
            
            # Resources with URL-based IDs
            "aws_sqs_queue": {"id_type": "url"},
        }
    
    def generate_import_command(self, resource_type: str, resource_name: str, 
                              aws_resource_id: str) -> ImportCommand:
        """
        Generate a terraform import command for a resource.
        
        Args:
            resource_type: Terraform resource type (e.g., 'aws_vpc')
            resource_name: Terraform resource name (e.g., 'main_vpc')
            aws_resource_id: AWS resource ID (e.g., 'vpc-123456')
            
        Returns:
            ImportCommand object with generated command and validation
        """
        terraform_address = f"{resource_type}.{resource_name}"
        
        # Validate resource type
        if not self._is_supported_resource_type(resource_type):
            return ImportCommand(
                resource_type=resource_type,
                resource_name=resource_name,
                terraform_address=terraform_address,
                aws_resource_id=aws_resource_id,
                import_command="",
                validation_result=ImportValidationResult.INVALID_RESOURCE_TYPE,
                validation_message=f"Unsupported resource type: {resource_type}"
            )
        
        # Validate resource ID format
        validation_result, validation_message = self._validate_resource_id(resource_type, aws_resource_id)
        if validation_result != ImportValidationResult.VALID:
            return ImportCommand(
                resource_type=resource_type,
                resource_name=resource_name,
                terraform_address=terraform_address,
                aws_resource_id=aws_resource_id,
                import_command="",
                validation_result=validation_result,
                validation_message=validation_message
            )
        
        # Transform resource ID if needed
        transformed_id = self._transform_resource_id(resource_type, aws_resource_id)
        
        # Generate import command
        import_command = f"terraform import {terraform_address} {transformed_id}"
        
        command = ImportCommand(
            resource_type=resource_type,
            resource_name=resource_name,
            terraform_address=terraform_address,
            aws_resource_id=aws_resource_id,
            import_command=import_command,
            validation_result=ImportValidationResult.VALID
        )
        
        return command
    
    def _is_supported_resource_type(self, resource_type: str) -> bool:
        """Check if resource type is supported for import."""
        # Check if we have a validation pattern for this resource type
        return resource_type in self.resource_id_patterns
    
    def _validate_resource_id(self, resource_type: str, resource_id: str) -> Tuple[ImportValidationResult, Optional[str]]:
        """Validate AWS resource ID format."""
        if not resource_id:
            return ImportValidationResult.INVALID_RESOURCE_ID, "Resource ID cannot be empty"
        
        # Get validation pattern
        pattern = self.resource_id_patterns.get(resource_type)
        if not pattern:
            return ImportValidationResult.INVALID_RESOURCE_TYPE, f"No validation pattern for {resource_type}"
        
        # Validate against pattern
        if not re.match(pattern, resource_id):
            return ImportValidationResult.INVALID_RESOURCE_ID, f"Resource ID '{resource_id}' does not match expected pattern for {resource_type}"
        
        return ImportValidationResult.VALID, None
    
    def _transform_resource_id(self, resource_type: str, resource_id: str) -> str:
        """Transform resource ID for terraform import if needed."""
        mapping = self.resource_type_mappings.get(resource_type, {})
        
        # Most resources use the ID as-is
        if not mapping or mapping.get("id_type") != "transformed":
            return resource_id
        
        # Handle special transformations here if needed
        return resource_id
    
    def add_import_command(self, resource_type: str, resource_name: str, 
                          aws_resource_id: str, dependencies: Optional[Set[str]] = None) -> str:
        """
        Add an import command to the batch.
        
        Args:
            resource_type: Terraform resource type
            resource_name: Terraform resource name
            aws_resource_id: AWS resource ID
            dependencies: Set of terraform addresses this import depends on
            
        Returns:
            Command ID for tracking
        """
        command = self.generate_import_command(resource_type, resource_name, aws_resource_id)
        
        if dependencies:
            command.dependencies = dependencies
        
        command_id = f"{resource_type}.{resource_name}"
        
        with self.lock:
            self.import_commands[command_id] = command
        
        if self.config.debug.enabled:
            print(f"Added import command: {command.import_command}")
        
        return command_id
    
    def validate_import_commands(self) -> Dict[str, List[ImportCommand]]:
        """
        Validate all import commands and categorize by validation result.
        
        Returns:
            Dictionary with validation results as keys and lists of commands as values
        """
        results = {result.value: [] for result in ImportValidationResult}
        
        for command in self.import_commands.values():
            results[command.validation_result.value].append(command)
        
        return results
    
    def get_import_order(self) -> List[List[str]]:
        """
        Get the order for executing import commands based on dependencies.
        
        Returns:
            List of lists, where each inner list contains command IDs that can be executed in parallel
        """
        # Build dependency graph
        remaining_commands = set(self.import_commands.keys())
        completed_commands = set()
        execution_levels = []
        
        while remaining_commands:
            current_level = []
            
            for command_id in list(remaining_commands):
                command = self.import_commands[command_id]
                
                # Check if all dependencies are satisfied
                if command.dependencies.issubset(completed_commands):
                    current_level.append(command_id)
                    remaining_commands.remove(command_id)
            
            if not current_level:
                # Circular dependency or missing dependency
                if self.config.debug.enabled:
                    print(f"Warning: Circular or missing dependencies. Remaining: {remaining_commands}")
                # Add remaining commands to avoid infinite loop
                current_level = list(remaining_commands)
                remaining_commands.clear()
            
            execution_levels.append(current_level)
            completed_commands.update(current_level)
        
        return execution_levels
    
    def execute_import_command(self, command_id: str, dry_run: bool = False) -> ImportResult:
        """
        Execute a single terraform import command.
        
        Args:
            command_id: ID of the command to execute
            dry_run: If True, don't actually execute the command
            
        Returns:
            ImportResult with execution details
        """
        if command_id not in self.import_commands:
            raise ValueError(f"Import command not found: {command_id}")
        
        command = self.import_commands[command_id]
        
        if not command.is_valid():
            return ImportResult(
                command=command,
                success=False,
                stderr=f"Invalid command: {command.validation_message}",
                return_code=-1
            )
        
        if dry_run:
            if self.config.debug.enabled:
                print(f"DRY RUN: {command.import_command}")
            
            return ImportResult(
                command=command,
                success=True,
                stdout="DRY RUN - Command not executed",
                execution_time=0.0
            )
        
        # Update status
        command.status = ImportStatus.IN_PROGRESS
        
        start_time = time.time()
        
        try:
            # Execute terraform import command
            result = subprocess.run(
                command.import_command.split(),
                cwd=self.terraform_dir,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            execution_time = time.time() - start_time
            command.execution_time = execution_time
            
            # Parse output for imported resources
            imported_resources = self._parse_import_output(result.stdout)
            
            success = result.returncode == 0
            command.status = ImportStatus.COMPLETED if success else ImportStatus.FAILED
            
            if not success:
                command.error_message = result.stderr
            
            import_result = ImportResult(
                command=command,
                success=success,
                stdout=result.stdout,
                stderr=result.stderr,
                return_code=result.returncode,
                execution_time=execution_time,
                imported_resources=imported_resources
            )
            
            with self.lock:
                self.import_results[command_id] = import_result
            
            if self.config.debug.enabled:
                status = "SUCCESS" if success else "FAILED"
                print(f"Import {status}: {command.terraform_address} ({execution_time:.2f}s)")
            
            return import_result
            
        except subprocess.TimeoutExpired:
            command.status = ImportStatus.FAILED
            command.error_message = "Import command timed out"
            
            return ImportResult(
                command=command,
                success=False,
                stderr="Command timed out after 5 minutes",
                return_code=-2,
                execution_time=time.time() - start_time
            )
            
        except Exception as e:
            command.status = ImportStatus.FAILED
            command.error_message = str(e)
            
            return ImportResult(
                command=command,
                success=False,
                stderr=str(e),
                return_code=-3,
                execution_time=time.time() - start_time
            )
    
    def _parse_import_output(self, stdout: str) -> List[str]:
        """Parse terraform import output to extract imported resource information."""
        imported_resources = []
        
        # Look for import success patterns in terraform output
        import_patterns = [
            r"Import successful!",
            r"Resource imported successfully",
            r"Imported (\S+)"
        ]
        
        for line in stdout.split('\n'):
            for pattern in import_patterns:
                match = re.search(pattern, line)
                if match:
                    if match.groups():
                        imported_resources.append(match.group(1))
                    else:
                        imported_resources.append(line.strip())
        
        return imported_resources
    
    def execute_batch_import(self, dry_run: bool = False, max_parallel: Optional[int] = None) -> Dict[str, ImportResult]:
        """
        Execute all import commands in dependency order with parallel execution.
        
        Args:
            dry_run: If True, don't actually execute commands
            max_parallel: Maximum number of parallel executions (defaults to config.cores)
            
        Returns:
            Dictionary of command_id -> ImportResult
        """
        if not self.import_commands:
            return {}
        
        self.config.set_tracking_message("Starting batch terraform import")
        
        # Get execution order
        execution_levels = self.get_import_order()
        
        # Determine parallelism
        if max_parallel is None:
            max_parallel = min(self.config.get_cores(), 4)  # Cap at 4 for terraform
        
        all_results = {}
        
        with ThreadPoolExecutor(max_workers=max_parallel) as executor:
            for level_index, command_ids in enumerate(execution_levels):
                if self.config.debug.enabled:
                    print(f"Executing import level {level_index + 1}/{len(execution_levels)} ({len(command_ids)} commands)")
                
                # Submit commands for this level
                futures = {}
                for command_id in command_ids:
                    future = executor.submit(self.execute_import_command, command_id, dry_run)
                    futures[future] = command_id
                
                # Wait for completion
                for future in as_completed(futures):
                    command_id = futures[future]
                    try:
                        result = future.result()
                        all_results[command_id] = result
                        
                        # Update progress
                        progress = len(all_results) / len(self.import_commands)
                        self.config.set_tracking_message(
                            f"Import progress: {progress:.1%} ({len(all_results)}/{len(self.import_commands)})"
                        )
                        
                    except Exception as e:
                        # Create error result
                        command = self.import_commands[command_id]
                        error_result = ImportResult(
                            command=command,
                            success=False,
                            stderr=str(e),
                            return_code=-4
                        )
                        all_results[command_id] = error_result
                        
                        if self.config.debug.enabled:
                            print(f"Import execution error for {command_id}: {e}")
        
        # Final status update
        successful = sum(1 for r in all_results.values() if r.success)
        failed = len(all_results) - successful
        
        self.config.set_tracking_message(
            f"Batch import complete: {successful} successful, {failed} failed"
        )
        
        return all_results
    
    def get_import_summary(self) -> Dict[str, Any]:
        """Get summary of import operations."""
        total_commands = len(self.import_commands)
        total_results = len(self.import_results)
        
        successful = sum(1 for r in self.import_results.values() if r.success)
        failed = total_results - successful
        
        # Calculate timing statistics
        execution_times = [r.execution_time for r in self.import_results.values() if r.execution_time > 0]
        avg_time = sum(execution_times) / len(execution_times) if execution_times else 0
        total_time = sum(execution_times)
        
        # Validation summary
        validation_summary = {}
        for command in self.import_commands.values():
            result = command.validation_result.value
            validation_summary[result] = validation_summary.get(result, 0) + 1
        
        return {
            "total_commands": total_commands,
            "executed_commands": total_results,
            "successful_imports": successful,
            "failed_imports": failed,
            "success_rate": successful / total_results if total_results > 0 else 0,
            "average_execution_time": avg_time,
            "total_execution_time": total_time,
            "validation_summary": validation_summary
        }
    
    def export_import_script(self, filename: str = "import_commands.sh") -> str:
        """
        Export all import commands as a shell script.
        
        Args:
            filename: Name of the script file to create
            
        Returns:
            Path to the created script file
        """
        script_path = self.terraform_dir / filename
        
        with open(script_path, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write("# Terraform import commands generated by aws2tf\n")
            f.write(f"# Generated at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("set -e  # Exit on any error\n\n")
            
            # Get execution order
            execution_levels = self.get_import_order()
            
            for level_index, command_ids in enumerate(execution_levels):
                f.write(f"# Import Level {level_index + 1}\n")
                f.write(f"echo \"Executing import level {level_index + 1}...\"\n\n")
                
                for command_id in command_ids:
                    command = self.import_commands[command_id]
                    if command.is_valid():
                        f.write(f"# Import {command.terraform_address}\n")
                        f.write(f"{command.import_command}\n")
                        f.write("if [ $? -ne 0 ]; then\n")
                        f.write(f"    echo \"Failed to import {command.terraform_address}\"\n")
                        f.write("    exit 1\n")
                        f.write("fi\n\n")
                    else:
                        f.write(f"# SKIPPED: {command.terraform_address} - {command.validation_message}\n\n")
                
                f.write("\n")
            
            f.write("echo \"All imports completed successfully!\"\n")
        
        # Make script executable
        os.chmod(script_path, 0o755)
        
        if self.config.debug.enabled:
            print(f"Export import script to: {script_path}")
        
        return str(script_path)
    
    def clear_commands(self) -> None:
        """Clear all import commands and results."""
        with self.lock:
            self.import_commands.clear()
            self.import_results.clear()


def create_terraform_importer(config: ConfigurationManager) -> TerraformImporter:
    """Factory function to create TerraformImporter."""
    return TerraformImporter(config)


def generate_import_commands_for_resources(config: ConfigurationManager, 
                                         discovered_resources: Dict[str, Any]) -> TerraformImporter:
    """
    Generate import commands for discovered resources.
    
    Args:
        config: Configuration manager
        discovered_resources: Dictionary of discovered resources from ResourceDiscovery
        
    Returns:
        TerraformImporter with generated commands
    """
    importer = create_terraform_importer(config)
    
    for resource_name, resource_info in discovered_resources.items():
        # Extract resource type and ID from resource name
        if '.' in resource_name:
            resource_type, resource_id = resource_name.split('.', 1)
            
            # Generate terraform resource name (sanitize for terraform)
            terraform_name = resource_id.replace('-', '_').replace(':', '_')
            
            # Add import command
            importer.add_import_command(
                resource_type=resource_type,
                resource_name=terraform_name,
                aws_resource_id=resource_id
            )
    
    return importer