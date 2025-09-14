#!/usr/bin/env python3
"""
Standalone Main Workflow Orchestrator for aws2tf.

This is a standalone version for testing that doesn't require complex imports.
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
from datetime import datetime, timezone

# Add the code directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'code'))

from config import ConfigurationManager


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
    discovered_resources: Dict[str, Any] = field(default_factory=dict)
    validation_issues: List[Any] = field(default_factory=list)
    import_results: List[Any] = field(default_factory=list)
    generated_files: List[Path] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class MainWorkflowStandalone:
    """
    Standalone main workflow orchestrator for testing.
    
    This version doesn't require all the AWS component dependencies.
    """
    
    def __init__(self, config: ConfigurationManager):
        """Initialize the main workflow orchestrator."""
        self.config = config
        self._lock = threading.RLock()
        
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
        self.discovered_resources: Dict[str, Any] = {}
        self.validation_issues: List[Any] = []
        self.import_results: List[Any] = []
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
        Execute the complete aws2tf workflow (standalone version).
        
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
            self._initialize_workflow_standalone(target_type, target_id, output_dir)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 2: Resource Discovery (simulated)
            if mode in [WorkflowMode.FULL, WorkflowMode.DISCOVERY_ONLY]:
                self._update_phase(WorkflowPhase.DISCOVERY, "Discovering AWS resources and dependencies")
                self._execute_discovery_phase_standalone(target_type, target_id)
                
                if mode == WorkflowMode.DISCOVERY_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 3: Dependency Validation (simulated)
            if mode in [WorkflowMode.FULL, WorkflowMode.VALIDATE_ONLY]:
                self._update_phase(WorkflowPhase.VALIDATION, "Validating resource dependencies")
                self._execute_validation_phase_standalone()
                
                if mode == WorkflowMode.VALIDATE_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 4: Terraform Import (simulated)
            if mode in [WorkflowMode.FULL, WorkflowMode.IMPORT_ONLY] and mode != WorkflowMode.DRY_RUN:
                self._update_phase(WorkflowPhase.IMPORT, "Importing resources into terraform")
                self._execute_import_phase_standalone()
                
                if mode == WorkflowMode.IMPORT_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 5: Configuration Generation (simulated)
            if mode in [WorkflowMode.FULL, WorkflowMode.GENERATE_ONLY]:
                self._update_phase(WorkflowPhase.GENERATION, "Generating terraform configuration files")
                self._execute_generation_phase_standalone(output_dir)
                
                if mode == WorkflowMode.GENERATE_ONLY:
                    return self._create_summary(WorkflowResult.SUCCESS)
            
            if self.is_cancelled:
                return self._create_summary(WorkflowResult.CANCELLED)
            
            # Phase 6: Finalization
            self._update_phase(WorkflowPhase.FINALIZATION, "Finalizing workflow and cleanup")
            self._execute_finalization_phase_standalone()
            
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
    
    def _initialize_workflow_standalone(self, target_type: str, target_id: str, output_dir: Optional[Path]) -> None:
        """Initialize the workflow with validation and setup (standalone version)."""
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
        
        self._notify_progress("Initialization completed", 0.1)
    
    def _execute_discovery_phase_standalone(self, target_type: str, target_id: str) -> None:
        """Execute the resource discovery phase (standalone simulation)."""
        self._notify_progress("Starting resource discovery", 0.1)
        
        # Simulate resource discovery
        time.sleep(0.1)  # Simulate discovery time
        
        # Create mock discovered resources
        self.discovered_resources = {
            target_id: {
                'resource_type': f'aws_{target_type}',
                'resource_id': target_id,
                'status': 'completed',
                'aws_data': {'mock': 'data'}
            }
        }
        
        # Add some dependencies based on resource type
        if target_type == 'vpc':
            self.discovered_resources['subnet-12345'] = {
                'resource_type': 'aws_subnet',
                'resource_id': 'subnet-12345',
                'status': 'completed',
                'aws_data': {'VpcId': target_id}
            }
        
        self.metrics.resources_discovered = len(self.discovered_resources)
        
        self._notify_progress(
            f"Discovered {self.metrics.resources_discovered} resources", 
            0.4
        )
    
    def _execute_validation_phase_standalone(self) -> None:
        """Execute the dependency validation phase (standalone simulation)."""
        self._notify_progress("Starting dependency validation", 0.4)
        
        # Simulate validation
        time.sleep(0.05)
        
        # Create mock validation issues
        self.validation_issues = [
            {'severity': 'info', 'message': 'Resource validation completed', 'resource_id': list(self.discovered_resources.keys())[0]}
        ]
        
        self.metrics.resources_validated = len(self.discovered_resources)
        
        self._notify_progress(
            f"Validated {len(self.discovered_resources)} resources", 
            0.5
        )
    
    def _execute_import_phase_standalone(self) -> None:
        """Execute the terraform import phase (standalone simulation)."""
        self._notify_progress("Starting terraform import", 0.5)
        
        # Simulate import
        time.sleep(0.1)
        
        # Create mock import results
        self.import_results = [
            {'resource_type': res['resource_type'], 'resource_id': res['resource_id'], 'status': 'completed'}
            for res in self.discovered_resources.values()
        ]
        
        self.metrics.resources_imported = len(self.import_results)
        
        self._notify_progress(
            f"Imported {self.metrics.resources_imported} resources", 
            0.7
        )
    
    def _execute_generation_phase_standalone(self, output_dir: Optional[Path]) -> None:
        """Execute the terraform configuration generation phase (standalone simulation)."""
        self._notify_progress("Starting configuration generation", 0.7)
        
        # Simulate generation
        time.sleep(0.05)
        
        # Create mock generated files
        if output_dir:
            self.generated_files = [
                output_dir / 'main.tf',
                output_dir / 'variables.tf',
                output_dir / 'outputs.tf'
            ]
        else:
            self.generated_files = [
                Path('main.tf'),
                Path('variables.tf'),
                Path('outputs.tf')
            ]
        
        self.metrics.configs_generated = len(self.generated_files)
        
        self._notify_progress(
            f"Generated {self.metrics.configs_generated} configuration files", 
            0.9
        )
    
    def _execute_finalization_phase_standalone(self) -> None:
        """Execute the workflow finalization phase (standalone simulation)."""
        self._notify_progress("Finalizing workflow", 0.9)
        
        # Simulate finalization
        time.sleep(0.02)
        
        self._notify_progress("Workflow finalization completed", 1.0)
    
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
                'discovered_resources': self.discovered_resources,
                'validation_issues': self.validation_issues,
                'import_results': self.import_results,
                'generated_files': [str(path) for path in self.generated_files],
                'errors': self.errors.copy(),
                'warnings': self.warnings.copy()
            }


def create_main_workflow_standalone(config: ConfigurationManager) -> MainWorkflowStandalone:
    """
    Factory function to create a MainWorkflowStandalone instance.
    
    Args:
        config: ConfigurationManager instance
        
    Returns:
        MainWorkflowStandalone instance ready for execution
    """
    return MainWorkflowStandalone(config)


if __name__ == '__main__':
    # Demo the standalone workflow
    from config import create_test_config
    
    print("AWS2TF Main Workflow Orchestrator (Standalone)")
    print("=" * 60)
    
    # Create test configuration
    config = create_test_config(
        region='us-east-1',
        account_id='123456789012',
        debug=False
    )
    
    # Create workflow
    workflow = create_main_workflow_standalone(config)
    
    # Add callbacks
    def progress_callback(message: str, progress: float):
        bar_length = 40
        filled_length = int(bar_length * progress)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"\rProgress: |{bar}| {progress:.1%} - {message}", end='', flush=True)
        if progress >= 1.0:
            print()
    
    def status_callback(phase: WorkflowPhase, message: str):
        print(f"\nPhase: {phase.value.upper()} - {message}")
    
    workflow.add_progress_callback(progress_callback)
    workflow.add_status_callback(status_callback)
    
    # Execute workflow
    print("\nExecuting full workflow...")
    summary = workflow.execute_workflow("vpc", "vpc-demo", WorkflowMode.FULL)
    
    print(f"\nWorkflow Result: {summary.result.value}")
    print(f"Phase Completed: {summary.phase_completed.value}")
    print(f"Execution Time: {summary.metrics.total_duration:.3f}s")
    print(f"Resources Discovered: {summary.metrics.resources_discovered}")
    print(f"Resources Validated: {summary.metrics.resources_validated}")
    print(f"Resources Imported: {summary.metrics.resources_imported}")
    print(f"Configs Generated: {summary.metrics.configs_generated}")
    
    print("\nStandalone workflow orchestrator working correctly!")