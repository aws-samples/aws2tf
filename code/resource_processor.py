#!/usr/bin/env python3
"""
Resource Processing Pipeline for aws2tf with configuration management.

This module provides a comprehensive pipeline for processing AWS resources including:
1. Orchestrated resource discovery and processing
2. Parallel processing of independent resources
3. Progress tracking and status reporting
4. Error handling and recovery mechanisms
5. Integration with configuration management system
"""

import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from typing import Dict, List, Set, Optional, Tuple, Any, Callable, Union
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
import json
import traceback
from pathlib import Path

from .config import ConfigurationManager
from .resource_discovery import ResourceDiscovery, ResourceInfo, DiscoveryStatus
from .dependency_mapper import ResourceDependencyMapper, ValidationIssue, ValidationSeverity


class ProcessingStatus(Enum):
    """Status of resource processing operations."""
    PENDING = "pending"
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    CANCELLED = "cancelled"


class ProcessingPriority(Enum):
    """Priority levels for resource processing."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class ProcessingTask:
    """Represents a resource processing task."""
    resource_name: str
    resource_type: str
    resource_id: str
    task_type: str  # 'discover', 'validate', 'import', 'generate'
    priority: ProcessingPriority = ProcessingPriority.NORMAL
    dependencies: Set[str] = field(default_factory=set)
    status: ProcessingStatus = ProcessingStatus.PENDING
    error_message: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    retry_count: int = 0
    max_retries: int = 3
    
    @property
    def processing_time(self) -> Optional[float]:
        """Get processing time in seconds."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return None
    
    @property
    def is_ready(self) -> bool:
        """Check if task is ready to be processed (all dependencies completed)."""
        return self.status == ProcessingStatus.PENDING
    
    def can_retry(self) -> bool:
        """Check if task can be retried."""
        return self.retry_count < self.max_retries and self.status == ProcessingStatus.FAILED


@dataclass
class ProcessingResult:
    """Result of a processing operation."""
    task: ProcessingTask
    success: bool
    result_data: Any = None
    error_message: Optional[str] = None
    warnings: List[str] = field(default_factory=list)
    processing_time: Optional[float] = None


@dataclass
class PipelineMetrics:
    """Metrics for the processing pipeline."""
    total_tasks: int = 0
    completed_tasks: int = 0
    failed_tasks: int = 0
    skipped_tasks: int = 0
    cancelled_tasks: int = 0
    total_processing_time: float = 0.0
    average_processing_time: float = 0.0
    throughput_per_second: float = 0.0
    error_rate: float = 0.0
    
    def update_from_results(self, results: List[ProcessingResult]) -> None:
        """Update metrics from processing results."""
        self.total_tasks = len(results)
        self.completed_tasks = sum(1 for r in results if r.success)
        self.failed_tasks = sum(1 for r in results if not r.success)
        
        processing_times = [r.processing_time for r in results if r.processing_time]
        if processing_times:
            self.total_processing_time = sum(processing_times)
            self.average_processing_time = self.total_processing_time / len(processing_times)
            self.throughput_per_second = len(processing_times) / self.total_processing_time
        
        self.error_rate = self.failed_tasks / self.total_tasks if self.total_tasks > 0 else 0.0


class ResourceProcessor:
    """Main resource processing pipeline orchestrator."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.discovery = ResourceDiscovery(config)
        self.dependency_mapper = ResourceDependencyMapper(config)
        
        # Processing state
        self.tasks: Dict[str, ProcessingTask] = {}
        self.results: Dict[str, ProcessingResult] = {}
        self.processing_queue: deque = deque()
        self.completed_tasks: Set[str] = set()
        self.failed_tasks: Set[str] = set()
        
        # Threading and synchronization
        self.lock = threading.Lock()
        self.executor: Optional[ThreadPoolExecutor] = None
        self.active_futures: Dict[str, Future] = {}
        self.shutdown_requested = False
        
        # Progress tracking
        self.progress_callbacks: List[Callable[[str, float, str], None]] = []
        self.start_time: Optional[float] = None
        self.metrics = PipelineMetrics()
        
        # Task processors
        self.task_processors = {
            'discover': self._process_discovery_task,
            'validate': self._process_validation_task,
            'import': self._process_import_task,
            'generate': self._process_generation_task
        }
    
    def add_progress_callback(self, callback: Callable[[str, float, str], None]) -> None:
        """Add a progress callback function."""
        self.progress_callbacks.append(callback)
    
    def _notify_progress(self, task_name: str, progress: float, message: str) -> None:
        """Notify progress callbacks."""
        for callback in self.progress_callbacks:
            try:
                callback(task_name, progress, message)
            except Exception as e:
                if self.config.debug.enabled:
                    print(f"Error in progress callback: {e}")
    
    def add_discovery_task(self, resource_type: str, resource_id: str, 
                          priority: ProcessingPriority = ProcessingPriority.NORMAL) -> str:
        """Add a resource discovery task."""
        task_name = f"discover_{resource_type}.{resource_id}"
        
        task = ProcessingTask(
            resource_name=f"{resource_type}.{resource_id}",
            resource_type=resource_type,
            resource_id=resource_id,
            task_type="discover",
            priority=priority
        )
        
        with self.lock:
            self.tasks[task_name] = task
        
        return task_name
    
    def add_validation_task(self, resources: Dict[str, ResourceInfo],
                           priority: ProcessingPriority = ProcessingPriority.NORMAL) -> str:
        """Add a resource validation task."""
        task_name = f"validate_dependencies_{int(time.time())}"
        
        task = ProcessingTask(
            resource_name="validation",
            resource_type="validation",
            resource_id="dependencies",
            task_type="validate",
            priority=priority
        )
        
        with self.lock:
            self.tasks[task_name] = task
        
        return task_name
    
    def add_import_task(self, resource_name: str, 
                       priority: ProcessingPriority = ProcessingPriority.NORMAL) -> str:
        """Add a terraform import task."""
        resource_type, resource_id = resource_name.split('.', 1)
        task_name = f"import_{resource_name}"
        
        task = ProcessingTask(
            resource_name=resource_name,
            resource_type=resource_type,
            resource_id=resource_id,
            task_type="import",
            priority=priority
        )
        
        with self.lock:
            self.tasks[task_name] = task
        
        return task_name
    
    def add_generation_task(self, resource_name: str,
                           priority: ProcessingPriority = ProcessingPriority.NORMAL) -> str:
        """Add a terraform configuration generation task."""
        resource_type, resource_id = resource_name.split('.', 1)
        task_name = f"generate_{resource_name}"
        
        task = ProcessingTask(
            resource_name=resource_name,
            resource_type=resource_type,
            resource_id=resource_id,
            task_type="generate",
            priority=priority
        )
        
        with self.lock:
            self.tasks[task_name] = task
        
        return task_name
    
    def set_task_dependencies(self, task_name: str, dependencies: List[str]) -> None:
        """Set dependencies for a task."""
        with self.lock:
            if task_name in self.tasks:
                self.tasks[task_name].dependencies = set(dependencies)
    
    def process_resources(self, target_type: str, target_id: str, 
                         include_validation: bool = True,
                         include_import: bool = False,
                         include_generation: bool = False) -> Dict[str, ProcessingResult]:
        """
        Process resources with the complete pipeline.
        
        Args:
            target_type: Target resource type category
            target_id: Target resource ID
            include_validation: Whether to include dependency validation
            include_import: Whether to include terraform import
            include_generation: Whether to include terraform config generation
            
        Returns:
            Dictionary of processing results
        """
        self.start_time = time.time()
        self.config.start_processing()
        self.config.set_tracking_message(f"Starting resource processing for {target_type}:{target_id}")
        
        try:
            # Phase 1: Discovery
            self._phase_discovery(target_type, target_id)
            
            # Phase 2: Validation (optional)
            if include_validation:
                self._phase_validation()
            
            # Phase 3: Import (optional)
            if include_import:
                self._phase_import()
            
            # Phase 4: Generation (optional)
            if include_generation:
                self._phase_generation()
            
            # Execute all tasks
            results = self._execute_pipeline()
            
            # Update metrics
            self.metrics.update_from_results(list(results.values()))
            
            # Final status update
            elapsed = time.time() - self.start_time
            self.config.set_tracking_message(
                f"Processing complete: {self.metrics.completed_tasks}/{self.metrics.total_tasks} "
                f"tasks completed in {elapsed:.2f}s"
            )
            
            return results
            
        except Exception as e:
            error_msg = f"Pipeline processing failed: {str(e)}"
            self.config.set_tracking_message(error_msg)
            if self.config.debug.enabled:
                print(f"Pipeline error: {traceback.format_exc()}")
            raise
    
    def _phase_discovery(self, target_type: str, target_id: str) -> None:
        """Phase 1: Resource discovery."""
        self.config.set_tracking_message("Phase 1: Discovering resources and dependencies")
        
        # Add initial discovery task
        initial_task = self.add_discovery_task(target_type, target_id, ProcessingPriority.HIGH)
        
        # Discover resources by category
        discovered = self.discovery.discover_by_category(target_type, target_id)
        
        # Add discovery tasks for all found resources
        for resource_name, resource_info in discovered.items():
            if resource_info.status == DiscoveryStatus.COMPLETED:
                # Add tasks for dependencies if they weren't discovered
                for dependency in resource_info.dependencies:
                    if dependency not in discovered:
                        dep_type, dep_id = dependency.split('.', 1)
                        self.add_discovery_task(dep_type, dep_id, ProcessingPriority.NORMAL)
    
    def _phase_validation(self) -> None:
        """Phase 2: Dependency validation."""
        self.config.set_tracking_message("Phase 2: Validating dependencies")
        
        # Convert discovered resources to format expected by dependency mapper
        resources = {}
        for resource_name, resource_info in self.discovery.discovered_resources.items():
            resources[resource_name] = {
                'resource_type': resource_info.resource_type,
                'aws_data': resource_info.aws_data
            }
        
        # Add validation task
        self.add_validation_task(resources, ProcessingPriority.HIGH)
    
    def _phase_import(self) -> None:
        """Phase 3: Terraform import."""
        self.config.set_tracking_message("Phase 3: Planning terraform imports")
        
        # Add import tasks for all discovered resources
        for resource_name in self.discovery.discovered_resources:
            import_task = self.add_import_task(resource_name, ProcessingPriority.NORMAL)
            
            # Set dependencies based on resource dependencies
            resource_info = self.discovery.discovered_resources[resource_name]
            import_dependencies = [f"import_{dep}" for dep in resource_info.dependencies 
                                 if dep in self.discovery.discovered_resources]
            self.set_task_dependencies(import_task, import_dependencies)
    
    def _phase_generation(self) -> None:
        """Phase 4: Terraform configuration generation."""
        self.config.set_tracking_message("Phase 4: Planning terraform configuration generation")
        
        # Add generation tasks for all discovered resources
        for resource_name in self.discovery.discovered_resources:
            gen_task = self.add_generation_task(resource_name, ProcessingPriority.NORMAL)
            
            # Generation depends on import completion
            import_task = f"import_{resource_name}"
            if import_task in self.tasks:
                self.set_task_dependencies(gen_task, [import_task])
    
    def _execute_pipeline(self) -> Dict[str, ProcessingResult]:
        """Execute the complete processing pipeline."""
        self.config.set_tracking_message("Executing processing pipeline")
        
        # Build execution order based on dependencies
        execution_order = self._build_execution_order()
        
        # Initialize thread pool
        max_workers = min(self.config.get_cores(), len(self.tasks))
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
        
        try:
            # Execute tasks in dependency order with parallelization
            return self._execute_tasks_parallel(execution_order)
        finally:
            if self.executor:
                self.executor.shutdown(wait=True)
                self.executor = None
    
    def _build_execution_order(self) -> List[List[str]]:
        """Build execution order respecting dependencies."""
        # Group tasks by dependency level
        levels = []
        remaining_tasks = set(self.tasks.keys())
        completed_dependencies = set()
        
        while remaining_tasks:
            current_level = []
            
            for task_name in list(remaining_tasks):
                task = self.tasks[task_name]
                
                # Check if all dependencies are satisfied
                if task.dependencies.issubset(completed_dependencies):
                    current_level.append(task_name)
                    remaining_tasks.remove(task_name)
            
            if not current_level:
                # Circular dependency or missing dependency
                if self.config.debug.enabled:
                    print(f"Warning: Circular or missing dependencies detected. "
                          f"Remaining tasks: {remaining_tasks}")
                # Add remaining tasks to current level to avoid infinite loop
                current_level = list(remaining_tasks)
                remaining_tasks.clear()
            
            levels.append(current_level)
            completed_dependencies.update(current_level)
        
        return levels
    
    def _execute_tasks_parallel(self, execution_order: List[List[str]]) -> Dict[str, ProcessingResult]:
        """Execute tasks in parallel within each dependency level."""
        all_results = {}
        
        for level_index, task_names in enumerate(execution_order):
            if self.shutdown_requested:
                break
            
            self.config.set_tracking_message(
                f"Executing level {level_index + 1}/{len(execution_order)} "
                f"({len(task_names)} tasks)"
            )
            
            # Submit tasks for this level
            futures = {}
            for task_name in task_names:
                if task_name in self.tasks:
                    future = self.executor.submit(self._execute_single_task, task_name)
                    futures[future] = task_name
                    self.active_futures[task_name] = future
            
            # Wait for completion and collect results
            level_results = {}
            for future in as_completed(futures):
                task_name = futures[future]
                try:
                    result = future.result()
                    level_results[task_name] = result
                    all_results[task_name] = result
                    
                    # Update progress
                    progress = len(all_results) / len(self.tasks)
                    self._notify_progress(task_name, progress, f"Completed {task_name}")
                    
                except Exception as e:
                    error_result = ProcessingResult(
                        task=self.tasks[task_name],
                        success=False,
                        error_message=str(e)
                    )
                    level_results[task_name] = error_result
                    all_results[task_name] = error_result
                    
                    if self.config.debug.enabled:
                        print(f"Task {task_name} failed: {e}")
                
                # Clean up future reference
                if task_name in self.active_futures:
                    del self.active_futures[task_name]
            
            # Check for failures that should stop the pipeline
            failed_critical_tasks = [
                name for name, result in level_results.items()
                if not result.success and self.tasks[name].priority == ProcessingPriority.CRITICAL
            ]
            
            if failed_critical_tasks:
                self.config.set_tracking_message(
                    f"Critical tasks failed: {failed_critical_tasks}. Stopping pipeline."
                )
                self.shutdown_requested = True
                break
        
        return all_results
    
    def _execute_single_task(self, task_name: str) -> ProcessingResult:
        """Execute a single processing task."""
        task = self.tasks[task_name]
        task.status = ProcessingStatus.IN_PROGRESS
        task.start_time = time.time()
        
        try:
            # Get the appropriate processor
            processor = self.task_processors.get(task.task_type)
            if not processor:
                raise ValueError(f"Unknown task type: {task.task_type}")
            
            # Execute the task
            result_data = processor(task)
            
            # Create successful result
            task.status = ProcessingStatus.COMPLETED
            task.end_time = time.time()
            
            result = ProcessingResult(
                task=task,
                success=True,
                result_data=result_data,
                processing_time=task.processing_time
            )
            
            with self.lock:
                self.completed_tasks.add(task_name)
                self.results[task_name] = result
            
            return result
            
        except Exception as e:
            task.status = ProcessingStatus.FAILED
            task.end_time = time.time()
            task.error_message = str(e)
            
            result = ProcessingResult(
                task=task,
                success=False,
                error_message=str(e),
                processing_time=task.processing_time
            )
            
            with self.lock:
                self.failed_tasks.add(task_name)
                self.results[task_name] = result
            
            # Check if task can be retried
            if task.can_retry():
                task.retry_count += 1
                task.status = ProcessingStatus.PENDING
                if self.config.debug.enabled:
                    print(f"Task {task_name} will be retried (attempt {task.retry_count})")
            
            return result
    
    def _process_discovery_task(self, task: ProcessingTask) -> Dict[str, Any]:
        """Process a resource discovery task."""
        if self.config.debug.enabled:
            print(f"Discovering resource: {task.resource_name}")
        
        resource_info = self.discovery.discover_resource(
            task.resource_type, 
            task.resource_id, 
            recursive=True
        )
        
        return {
            'resource_info': resource_info,
            'status': resource_info.status.value,
            'dependencies_found': len(resource_info.dependencies)
        }
    
    def _process_validation_task(self, task: ProcessingTask) -> Dict[str, Any]:
        """Process a dependency validation task."""
        if self.config.debug.enabled:
            print("Validating resource dependencies")
        
        # Convert discovered resources for validation
        resources = {}
        for resource_name, resource_info in self.discovery.discovered_resources.items():
            resources[resource_name] = {
                'resource_type': resource_info.resource_type,
                'aws_data': resource_info.aws_data
            }
        
        # Validate dependencies
        issues = self.dependency_mapper.validate_dependencies(resources)
        
        # Categorize issues by severity
        errors = [issue for issue in issues if issue.severity == ValidationSeverity.ERROR]
        warnings = [issue for issue in issues if issue.severity == ValidationSeverity.WARNING]
        info = [issue for issue in issues if issue.severity == ValidationSeverity.INFO]
        
        return {
            'total_issues': len(issues),
            'errors': len(errors),
            'warnings': len(warnings),
            'info': len(info),
            'validation_issues': issues
        }
    
    def _process_import_task(self, task: ProcessingTask) -> Dict[str, Any]:
        """Process a terraform import task."""
        if self.config.debug.enabled:
            print(f"Processing terraform import for: {task.resource_name}")
        
        # This is a placeholder - actual terraform import would be implemented here
        # For now, simulate the import process
        time.sleep(0.1)  # Simulate processing time
        
        return {
            'resource_name': task.resource_name,
            'import_command': f"terraform import {task.resource_name} {task.resource_id}",
            'status': 'simulated'
        }
    
    def _process_generation_task(self, task: ProcessingTask) -> Dict[str, Any]:
        """Process a terraform configuration generation task."""
        if self.config.debug.enabled:
            print(f"Generating terraform configuration for: {task.resource_name}")
        
        # This is a placeholder - actual terraform config generation would be implemented here
        # For now, simulate the generation process
        time.sleep(0.05)  # Simulate processing time
        
        return {
            'resource_name': task.resource_name,
            'config_file': f"{task.resource_name.replace('.', '_')}.tf",
            'status': 'simulated'
        }
    
    def get_processing_status(self) -> Dict[str, Any]:
        """Get current processing status."""
        with self.lock:
            total_tasks = len(self.tasks)
            completed = len(self.completed_tasks)
            failed = len(self.failed_tasks)
            in_progress = len(self.active_futures)
            pending = total_tasks - completed - failed - in_progress
            
            progress = completed / total_tasks if total_tasks > 0 else 0.0
            
            return {
                'total_tasks': total_tasks,
                'completed': completed,
                'failed': failed,
                'in_progress': in_progress,
                'pending': pending,
                'progress': progress,
                'elapsed_time': time.time() - self.start_time if self.start_time else 0,
                'metrics': self.metrics
            }
    
    def cancel_processing(self) -> None:
        """Cancel ongoing processing."""
        self.shutdown_requested = True
        
        # Cancel active futures
        for future in self.active_futures.values():
            future.cancel()
        
        # Shutdown executor
        if self.executor:
            self.executor.shutdown(wait=False)
    
    def get_task_results(self, task_type: Optional[str] = None) -> Dict[str, ProcessingResult]:
        """Get results for specific task type or all tasks."""
        if task_type:
            return {
                name: result for name, result in self.results.items()
                if self.tasks[name].task_type == task_type
            }
        return self.results.copy()
    
    def export_processing_report(self, format_type: str = "json") -> str:
        """Export processing report in various formats."""
        report_data = {
            'pipeline_metrics': {
                'total_tasks': self.metrics.total_tasks,
                'completed_tasks': self.metrics.completed_tasks,
                'failed_tasks': self.metrics.failed_tasks,
                'error_rate': self.metrics.error_rate,
                'total_processing_time': self.metrics.total_processing_time,
                'average_processing_time': self.metrics.average_processing_time,
                'throughput_per_second': self.metrics.throughput_per_second
            },
            'task_results': {},
            'discovered_resources': len(self.discovery.discovered_resources),
            'dependency_statistics': self.dependency_mapper.get_dependency_statistics()
        }
        
        # Add task results
        for task_name, result in self.results.items():
            report_data['task_results'][task_name] = {
                'success': result.success,
                'processing_time': result.processing_time,
                'error_message': result.error_message,
                'task_type': result.task.task_type,
                'priority': result.task.priority.value,
                'retry_count': result.task.retry_count
            }
        
        if format_type == "json":
            return json.dumps(report_data, indent=2, default=str)
        else:
            raise ValueError(f"Unsupported format: {format_type}")


def create_resource_processor(config: ConfigurationManager) -> ResourceProcessor:
    """Factory function to create ResourceProcessor."""
    return ResourceProcessor(config)


def process_target_resources(config: ConfigurationManager, target_type: str, target_id: str,
                           include_validation: bool = True, include_import: bool = False,
                           include_generation: bool = False) -> Dict[str, ProcessingResult]:
    """
    Convenience function to process target resources with the complete pipeline.
    
    Args:
        config: Configuration manager
        target_type: Target resource type category
        target_id: Target resource ID
        include_validation: Whether to include dependency validation
        include_import: Whether to include terraform import
        include_generation: Whether to include terraform config generation
        
    Returns:
        Dictionary of processing results
    """
    processor = create_resource_processor(config)
    
    # Add progress callback to update configuration
    def progress_callback(task_name: str, progress: float, message: str):
        config.set_tracking_message(f"Progress: {progress:.1%} - {message}")
    
    processor.add_progress_callback(progress_callback)
    
    return processor.process_resources(
        target_type, target_id, include_validation, include_import, include_generation
    )