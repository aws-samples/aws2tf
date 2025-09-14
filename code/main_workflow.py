#!/usr/bin/env python3
"""
Main Workflow Orchestrator for aws2tf with dependency injection.

This module provides the main workflow orchestrator that coordinates all aws2tf operations:
1. Resource discovery and dependency mapping
2. Terraform import command generation and execution
3. Terraform configuration file generation
4. Comprehensive error handling and recovery
5. Progress tracking and status reporting
6. Integration with all aws2tf components using dependency injection
"""

import os
import sys
import time
import json
import traceback
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

try:
    from .config import ConfigurationManager
    from .resource_discovery import ResourceDiscovery, ResourceInfo, DiscoveryStatus
    from .dependency_mapper import ResourceDependencyMapper, ValidationIssue, ValidationSeverity
    from .terraform_importer import TerraformImporter, ImportCommand, ImportStatus
    from .terraform_state_manager import TerraformStateManager, StateValidationResult
    from .terraform_config_generator import TerraformConfigGenerator, ConfigFileType
    from .resource_processor import ResourceProcessor, ProcessingTask, ProcessingStatus
except ImportError:
    # For standalone testing
    from config import ConfigurationManager
    from resource_discovery import ResourceDiscovery, ResourceInfo, DiscoveryStatus
    from dependency_mapper import ResourceDependencyMapper, ValidationIssue, ValidationSeverity
    from terraform_importer import TerraformImporter, ImportCommand, ImportStatus
    from terraform_state_manager import TerraformStateManager, StateValidationResult
    from terraform_config_generator import TerraformConfigGenerator, ConfigFileType
    from resource_processor import ResourceProcessor, ProcessingTask, ProcessingStatus


class WorkflowPhase(Enum):
    """Phases of the aws2tf workflow."""
    INITIALIZATION = "initialization"
    DISCOVERY = "discovery"
    VALIDATION = "validation"
    IMPORT = "import"
    GENERATION = "generation"
    FINALIZATION = "finalization"
    COMPLETED = "completed"
    FAILED = "failed"


class WorkflowMode(Enum):
    """Execution modes for the workflow."""
    FULL = "full"                    # Complete workflow
    DISCOVERY_ONLY = "discovery"     # Only discover resources
    VALIDATE_ONLY = "validate"       # Only validate dependencies
    IMPORT_ONLY = "import"          # Only import resources
    GENERATE_ONLY = "generate"      # Only generate configurations
    DRY_RUN = "dry_run"            # Show what would be done


class WorkflowResult(Enum):
    """Results of workflow execution."""
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMEOUT = "timeout"


@dataclass
class WorkflowMetrics:
    """Metrics collected during workflow execution."""
    start_time: float = field(default_factory=time.time)
    end_time: Optional[float] = None
    total_duration: Optional[float] = None
    resources_discovered: int = 0
    resources_validated: int = 0
    resources_imported: int = 0
    configs_generated: int = 0
    errors_encountered: int = 0
    warnings_generated: int = 0
    
    def finalize(self) -> None:
        """Finalize metrics calculation."""
        if self.end_time is None:
            self.end_time = time.time()
        self.total_duration = self.end_time - self.start_time


@dataclass
class WorkflowSummary:
    """Summary of workflow execution results."""
    result: WorkflowResult
    phase_completed: WorkflowPhase
    metrics: WorkflowMetrics
    discovered_resources: Dict[str, ResourceInfo] = field(default_factory=dict)
    validation_issues: List[ValidationIssue] = field(default_factory=list)
    import_results: List[ImportCommand] = field(default_factory=list)
    generated_files: List[Path] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class MainWorkflow:
    """
    Main workflow orchestrator for aws2tf operations.
    
    Coordinates all aws2tf components to provide a complete infrastructure
    import workflow with comprehensive error handling and progress tracking.
    """
    
    def __init__(self, config: ConfigurationManager):
        """Initialize the main workflow orchestrator."""
        self.config = config
        self._lock = threading.RLock()
        
        # Initialize component instances
        self.resource_discovery = ResourceDiscovery(config)
        self.dependency_mapper = ResourceDependencyMapper(config)
        self.terraform_importer = TerraformImporter(config)
        self.state_manager = TerraformStateManager(config)
        self.config_generator = TerraformConfigGenerator(config)
        self.resource_processor = ResourceProcessor(config)
        
        # Workflow state
        self.current_phase = WorkflowPhase.INITIALIZATION
        self.workflow_mode = WorkflowMode.FULL
        self.is_running = False
        self.is_cancelled = False
        self.metrics = WorkflowMetrics()
        
        # Progress callbacks
        self.progress_callbacks: List[Callable[[str, float], None]] = []
        self.status_callbacks: List[Callable[[WorkflowPhase, str], None]] = []
        
        # Results storage
        self.discovered_resources: Dict[str, ResourceInfo] = {}
        self.validation_issues: List[ValidationIssue] = []
        self.import_results: List[ImportCommand] = []
        self.generated_files: List[Path] = []
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def add_progress_callback(self, callback: Callable[[str, float], None]) -> None:
        """Add a progress callback function."""
        with self._lock:
            self.progress_callbacks.append(callback)
    
    def add_status_callback(self, callback: Callable[[WorkflowPhase, str], None]) -> None:
        """Add a status callback function."""
        with self._lock:
            self.status_callbacks.append(callback)
    
    def _notify_progress(self, message: str, progress: float) -> None:
        """Notify all progress callbacks."""
        with self._lock:
            for callback in self.progress_callbacks:
                try:
                    callback(message, progress)
                except Exception as e:
                    self.warnings.append(f"Progress callback error: {e}")
    
    def _notify_status(self, phase: WorkflowPhase, message: str) -> None:
        """Notify all status callbacks."""
        with self._lock:
            for callback in self.status_callbacks:
                try:
                    callback(phase, message)
                except Exception as e:
                    self.warnings.append(f"Status callback error: {e}")
    
    def _update_phase(self, phase: WorkflowPhase, message: str = "") -> None:
        """Update the current workflow phase."""
        with self._lock:
            self.current_phase = phase
            if message:
                self.config.set_tracking_message(message)
            self._notify_status(phase, message)
    
    def execute_workflow(
        self,
        target_type: str,
        target_id: str,
        mode: WorkflowMode = WorkflowMode.FULL,
        output_dir: Optional[Path] = None
    ) -> WorkflowSummary:
        """
        Execute the complete aws2tf workflow.
        
        Args:
            target_type: AWS resource type to import (e.g., 'vpc', 'subnet')
            target_id: AWS resource ID to import
            mode: Workflow execution mode
            output_dir: Directory for generated terraform files
            
        Returns:
            WorkflowSummary with complete execution results
        """
        self.workflow_mode = mode
        self.is_running = True
        self.is_cancelled = False
        self.metrics = WorkflowMetrics()
        
        try:
            # Phase 1: Initialization
            self._update_phase(WorkflowPhase.INITIALIZATION, "Initializing aws2tf workflow")
            self._initialize_workflow(target_type, target_id, output_dir)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 2: Resource Discovery
            if mode in [WorkflowMode.FULL, WorkflowMode.DISCOVERY_ONLY]:
                self._update_phase(WorkflowPhase.DISCOVERY, "Discovering AWS resources and dependencies")
                self._execute_discovery_phase(target_type, target_id)
                
                if mode == WorkflowMode.DISCOVERY_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 3: Dependency Validation
            if mode in [WorkflowMode.FULL, WorkflowMode.VALIDATE_ONLY]:
                self._update_phase(WorkflowPhase.VALIDATION, "Validating resource dependencies")
                self._execute_validation_phase()
                
                if mode == WorkflowMode.VALIDATE_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 4: Terraform Import
            if mode in [WorkflowMode.FULL, WorkflowMode.IMPORT_ONLY] and mode != WorkflowMode.DRY_RUN:
                self._update_phase(WorkflowPhase.IMPORT, "Importing resources into terraform")
                self._execute_import_phase()
                
                if mode == WorkflowMode.IMPORT_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 5: Configuration Generation
            if mode in [WorkflowMode.FULL, WorkflowMode.GENERATE_ONLY]:
                self._update_phase(WorkflowPhase.GENERATION, "Generating terraform configuration files")
                self._execute_generation_phase(output_dir)
                
                if mode == WorkflowMode.GENERATE_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 6: Finalization
            self._update_phase(WorkflowPhase.FINALIZATION, "Finalizing workflow and cleanup")
            self._execute_finalization_phase()
            
            # Complete
            self._update_phase(WorkflowPhase.COMPLETED, "Workflow completed successfully")
            return self._create_summary(WorkflowResult.SUCCESS)
            
        except Exception as e:
            error_msg = f"Workflow failed: {str(e)}"
            self.errors.append(error_msg)
            self._update_phase(WorkflowPhase.FAILED, error_msg)
            
            if self.config.debug.enabled:
                self.errors.append(f"Traceback: {traceback.format_exc()}")
            
            return self._create_summary(WorkflowResult.FAILED)
        
        finally:
            self.is_running = False
            self.metrics.finalize() 
   
    def _initialize_workflow(self, target_type: str, target_id: str, output_dir: Optional[Path]) -> None:
        """Initialize the workflow with validation and setup."""
        self._notify_progress("Validating configuration and setup", 0.0)
        
        # Validate configuration
        config_errors = []
        config_errors.extend(self.config.aws.validate())
        config_errors.extend(self.config.runtime.validate())
        
        if config_errors:
            raise ValueError(f"Configuration validation failed: {'; '.join(config_errors)}")
        
        # Validate target resource
        if not target_type or not target_id:
            raise ValueError("Target resource type and ID must be specified")
        
        # Setup output directory
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            self.config.runtime.output_dir = str(output_dir)
        
        # Initialize terraform state manager
        if self.workflow_mode != WorkflowMode.DRY_RUN:
            state_validation = self.state_manager.validate_state()
            if state_validation != StateValidationResult.VALID:
                self.warnings.append(f"Terraform state validation: {state_validation.value}")
        
        self._notify_progress("Initialization completed", 0.1)
    
    def _execute_discovery_phase(self, target_type: str, target_id: str) -> None:
        """Execute the resource discovery phase."""
        self._notify_progress("Starting resource discovery", 0.1)
        
        try:
            # Discover target resource and dependencies
            target_resource = self.resource_discovery.discover_target_resource(target_type, target_id)
            
            if not target_resource:
                raise ValueError(f"Target resource {target_type}:{target_id} not found")
            
            # Get all discovered resources
            self.discovered_resources = self.resource_discovery.get_discovered_resources()
            self.metrics.resources_discovered = len(self.discovered_resources)
            
            # Update progress
            discovery_summary = self.resource_discovery.get_discovery_summary()
            completed_count = discovery_summary.get('by_status', {}).get('completed', 0)
            total_count = discovery_summary.get('total_resources', 1)
            progress = 0.1 + (completed_count / total_count) * 0.3  # 10% to 40%
            
            self._notify_progress(
                f"Discovered {completed_count}/{total_count} resources", 
                progress
            )
            
            # Check for discovery errors
            failed_resources = [
                res for res in self.discovered_resources.values() 
                if res.status == DiscoveryStatus.FAILED
            ]
            
            if failed_resources:
                error_messages = [f"{res.resource_type}:{res.resource_id} - {res.error_message}" 
                                for res in failed_resources]
                self.warnings.extend([f"Discovery failed: {msg}" for msg in error_messages])
            
        except Exception as e:
            raise RuntimeError(f"Resource discovery failed: {str(e)}")
    
    def _execute_validation_phase(self) -> None:
        """Execute the dependency validation phase."""
        self._notify_progress("Starting dependency validation", 0.4)
        
        try:
            # Validate dependencies for all discovered resources
            self.validation_issues = self.dependency_mapper.validate_resource_dependencies(
                list(self.discovered_resources.values())
            )
            
            self.metrics.resources_validated = len(self.discovered_resources)
            
            # Count validation issues by severity
            error_count = sum(1 for issue in self.validation_issues 
                            if issue.severity == ValidationSeverity.ERROR)
            warning_count = sum(1 for issue in self.validation_issues 
                              if issue.severity == ValidationSeverity.WARNING)
            
            self.metrics.errors_encountered += error_count
            self.metrics.warnings_generated += warning_count
            
            # Add validation issues to results
            for issue in self.validation_issues:
                if issue.severity == ValidationSeverity.ERROR:
                    self.errors.append(f"Validation error: {issue.message}")
                elif issue.severity == ValidationSeverity.WARNING:
                    self.warnings.append(f"Validation warning: {issue.message}")
            
            # Check for circular dependencies
            circular_deps = self.dependency_mapper.detect_circular_dependencies(
                list(self.discovered_resources.values())
            )
            
            if circular_deps:
                self.warnings.append(f"Detected {len(circular_deps)} circular dependencies")
                for cycle in circular_deps:
                    self.warnings.append(f"Circular dependency: {' -> '.join(cycle)}")
            
            self._notify_progress(
                f"Validated {len(self.discovered_resources)} resources "
                f"({error_count} errors, {warning_count} warnings)", 
                0.5
            )
            
            # Fail if critical validation errors
            if error_count > 0 and not self.config.runtime.ignore_validation_errors:
                raise RuntimeError(f"Validation failed with {error_count} critical errors")
            
        except Exception as e:
            raise RuntimeError(f"Dependency validation failed: {str(e)}")
    
    def _execute_import_phase(self) -> None:
        """Execute the terraform import phase."""
        self._notify_progress("Starting terraform import", 0.5)
        
        try:
            # Create backup of current state
            if self.config.runtime.create_backups:
                backup_path = self.state_manager.create_backup("pre_import")
                if backup_path:
                    self.warnings.append(f"Created state backup: {backup_path}")
            
            # Generate import commands for all discovered resources
            for resource_info in self.discovered_resources.values():
                if resource_info.status == DiscoveryStatus.COMPLETED:
                    import_cmd = self.terraform_importer.generate_import_command(
                        resource_info.resource_type,
                        resource_info.resource_id,
                        resource_info.aws_data
                    )
                    
                    if import_cmd:
                        self.terraform_importer.add_import_command(import_cmd)
            
            # Get import order based on dependencies
            import_order = self.terraform_importer.get_import_order()
            
            # Execute imports in dependency order
            imported_count = 0
            total_imports = len(import_order)
            
            for import_cmd in import_order:
                if self.is_cancelled:
                    break
                
                # Execute import command
                result = self.terraform_importer.execute_import_command(
                    import_cmd, 
                    dry_run=(self.workflow_mode == WorkflowMode.DRY_RUN)
                )
                
                self.import_results.append(result)
                
                if result.status == ImportStatus.COMPLETED:
                    imported_count += 1
                elif result.status == ImportStatus.FAILED:
                    self.errors.append(f"Import failed: {result.error_message}")
                
                # Update progress
                progress = 0.5 + (imported_count / total_imports) * 0.2  # 50% to 70%
                self._notify_progress(
                    f"Imported {imported_count}/{total_imports} resources", 
                    progress
                )
            
            self.metrics.resources_imported = imported_count
            
            # Validate state after imports
            if imported_count > 0 and self.workflow_mode != WorkflowMode.DRY_RUN:
                state_validation = self.state_manager.validate_state()
                if state_validation != StateValidationResult.VALID:
                    self.warnings.append(f"Post-import state validation: {state_validation.value}")
            
        except Exception as e:
            raise RuntimeError(f"Terraform import failed: {str(e)}")
    
    def _execute_generation_phase(self, output_dir: Optional[Path]) -> None:
        """Execute the terraform configuration generation phase."""
        self._notify_progress("Starting configuration generation", 0.7)
        
        try:
            # Add resources to config generator
            for resource_info in self.discovered_resources.values():
                if resource_info.status == DiscoveryStatus.COMPLETED:
                    self.config_generator.add_resource_from_aws_data(
                        resource_info.resource_type,
                        resource_info.resource_id,
                        resource_info.aws_data
                    )
            
            # Add common variables and outputs
            self.config_generator.add_common_variables()
            self.config_generator.add_common_outputs()
            
            # Generate all configuration files
            generated_files = self.config_generator.generate_all_files()
            
            # Write files to disk if output directory specified
            if output_dir:
                written_files = self.config_generator.write_files_to_disk(output_dir)
                self.generated_files.extend(written_files)
                self.metrics.configs_generated = len(written_files)
            else:
                self.metrics.configs_generated = len(generated_files)
            
            self._notify_progress(
                f"Generated {self.metrics.configs_generated} configuration files", 
                0.9
            )
            
        except Exception as e:
            raise RuntimeError(f"Configuration generation failed: {str(e)}")
    
    def _execute_finalization_phase(self) -> None:
        """Execute the workflow finalization phase."""
        self._notify_progress("Finalizing workflow", 0.9)
        
        try:
            # Generate workflow summary report
            summary_data = {
                'workflow_mode': self.workflow_mode.value,
                'execution_time': self.metrics.total_duration,
                'resources_discovered': self.metrics.resources_discovered,
                'resources_validated': self.metrics.resources_validated,
                'resources_imported': self.metrics.resources_imported,
                'configs_generated': self.metrics.configs_generated,
                'errors': len(self.errors),
                'warnings': len(self.warnings)
            }
            
            # Save summary if output directory exists
            if hasattr(self.config.runtime, 'output_dir') and self.config.runtime.output_dir:
                summary_path = Path(self.config.runtime.output_dir) / 'aws2tf_summary.json'
                with open(summary_path, 'w') as f:
                    json.dump(summary_data, f, indent=2)
                self.generated_files.append(summary_path)
            
            # Cleanup temporary resources
            if hasattr(self.resource_processor, 'cleanup'):
                self.resource_processor.cleanup()
            
            self._notify_progress("Workflow finalization completed", 1.0)
            
        except Exception as e:
            self.warnings.append(f"Finalization warning: {str(e)}")
    
    def _create_summary(self, result: WorkflowResult) -> WorkflowSummary:
        """Create a workflow summary with current state."""
        return WorkflowSummary(
            result=result,
            phase_completed=self.current_phase,
            metrics=self.metrics,
            discovered_resources=self.discovered_resources.copy(),
            validation_issues=self.validation_issues.copy(),
            import_results=self.import_results.copy(),
            generated_files=self.generated_files.copy(),
            errors=self.errors.copy(),
            warnings=self.warnings.copy()
        )
    
    def cancel_workflow(self) -> None:
        """Cancel the currently running workflow."""
        with self._lock:
            self.is_cancelled = True
            if hasattr(self.resource_processor, 'cancel_processing'):
                self.resource_processor.cancel_processing()
    
    def get_current_status(self) -> Dict[str, Any]:
        """Get the current workflow status."""
        with self._lock:
            return {
                'phase': self.current_phase.value,
                'mode': self.workflow_mode.value,
                'is_running': self.is_running,
                'is_cancelled': self.is_cancelled,
                'progress': {
                    'resources_discovered': self.metrics.resources_discovered,
                    'resources_validated': self.metrics.resources_validated,
                    'resources_imported': self.metrics.resources_imported,
                    'configs_generated': self.metrics.configs_generated
                },
                'issues': {
                    'errors': len(self.errors),
                    'warnings': len(self.warnings)
                },
                'elapsed_time': time.time() - self.metrics.start_time if self.is_running else self.metrics.total_duration
            }
    
    def get_detailed_report(self) -> Dict[str, Any]:
        """Get a detailed workflow execution report."""
        with self._lock:
            return {
                'workflow_info': {
                    'phase': self.current_phase.value,
                    'mode': self.workflow_mode.value,
                    'status': 'running' if self.is_running else 'completed'
                },
                'metrics': {
                    'execution_time': self.metrics.total_duration or (time.time() - self.metrics.start_time),
                    'resources_discovered': self.metrics.resources_discovered,
                    'resources_validated': self.metrics.resources_validated,
                    'resources_imported': self.metrics.resources_imported,
                    'configs_generated': self.metrics.configs_generated,
                    'errors_encountered': self.metrics.errors_encountered,
                    'warnings_generated': self.metrics.warnings_generated
                },
                'discovered_resources': {
                    res_id: {
                        'type': res.resource_type,
                        'status': res.status.value,
                        'dependencies': len(res.dependencies),
                        'error': res.error_message
                    }
                    for res_id, res in self.discovered_resources.items()
                },
                'validation_issues': [
                    {
                        'severity': issue.severity.value,
                        'message': issue.message,
                        'resource_id': issue.resource_id
                    }
                    for issue in self.validation_issues
                ],
                'import_results': [
                    {
                        'resource_type': cmd.resource_type,
                        'resource_name': cmd.resource_name,
                        'status': cmd.status.value,
                        'error': cmd.error_message
                    }
                    for cmd in self.import_results
                ],
                'generated_files': [str(path) for path in self.generated_files],
                'errors': self.errors.copy(),
                'warnings': self.warnings.copy()
            }


def create_main_workflow(config: ConfigurationManager) -> MainWorkflow:
    """
    Factory function to create a MainWorkflow instance.
    
    Args:
        config: ConfigurationManager instance
        
    Returns:
        MainWorkflow instance ready for execution
    """
    return MainWorkflow(config)


def execute_aws2tf_workflow(
    config: ConfigurationManager,
    target_type: str,
    target_id: str,
    mode: WorkflowMode = WorkflowMode.FULL,
    output_dir: Optional[Path] = None,
    progress_callback: Optional[Callable[[str, float], None]] = None,
    status_callback: Optional[Callable[[WorkflowPhase, str], None]] = None
) -> WorkflowSummary:
    """
    Convenience function to execute the complete aws2tf workflow.
    
    Args:
        config: ConfigurationManager instance
        target_type: AWS resource type to import
        target_id: AWS resource ID to import
        mode: Workflow execution mode
        output_dir: Directory for generated terraform files
        progress_callback: Optional progress callback function
        status_callback: Optional status callback function
        
    Returns:
        WorkflowSummary with execution results
    """
    workflow = create_main_workflow(config)
    
    if progress_callback:
        workflow.add_progress_callback(progress_callback)
    
    if status_callback:
        workflow.add_status_callback(status_callback)
    
    return workflow.execute_workflow(target_type, target_id, mode, output_dir)