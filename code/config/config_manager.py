"""
Configuration manager for aws2tf.

This module provides the main ConfigurationManager class that coordinates
all configuration categories and provides thread-safe access to configuration data.
"""

import threading
import argparse
from typing import List, Optional, Dict, Any
import boto3

from .config_categories import (
    AWSConfig,
    DebugConfig,
    ProcessingConfig,
    RuntimeConfig,
    ResourceConfig
)


class ConfigurationManager:
    """
    Central configuration manager that replaces global variables.
    
    This class provides thread-safe access to all configuration categories
    and coordinates configuration updates throughout the application lifecycle.
    """
    
    def __init__(self):
        """Initialize the configuration manager with default values."""
        self.aws = AWSConfig()
        self.debug = DebugConfig()
        self.processing = ProcessingConfig()
        self.runtime = RuntimeConfig()
        self.resources = ResourceConfig()
        
        # Thread safety lock
        self._lock = threading.RLock()
    
    def update_from_args(self, args: argparse.Namespace) -> None:
        """
        Update configuration from command-line arguments.
        
        Args:
            args: Parsed command-line arguments from argparse.
        """
        with self._lock:
            # AWS configuration
            if hasattr(args, 'profile') and args.profile:
                self.aws.profile = args.profile
            
            if hasattr(args, 'region') and args.region:
                self.aws.region = args.region
            
            if hasattr(args, 'tv') and args.tv:
                self.aws.tf_version = args.tv
            
            # Debug configuration
            debug_enabled = False
            if hasattr(args, 'debug') and args.debug:
                self.debug.enabled = True
                debug_enabled = True
            
            if hasattr(args, 'debug5') and args.debug5:
                self.debug.debug5 = True
                debug_enabled = True
            
            if hasattr(args, 'validate') and args.validate:
                self.debug.validate_mode = True
            
            if hasattr(args, 'boto3error') and args.boto3error:
                # Enable debug mode for boto3 errors
                self.debug.enabled = True
                debug_enabled = True
            
            # Fast mode - but debug takes precedence
            if hasattr(args, 'fast') and args.fast and not debug_enabled:
                self.runtime.fast = True
            elif debug_enabled:
                self.runtime.fast = False  # Debug disables fast mode
            
            # Runtime configuration
            if hasattr(args, 'merge') and args.merge:
                self.runtime.merge = True
            
            if hasattr(args, 'serverless') and args.serverless:
                self.runtime.serverless = True
            
            if hasattr(args, 'accept') and args.accept:
                self.runtime.expected = True
            
            if hasattr(args, 'singlefile') and args.singlefile:
                # Store singlefile flag in runtime config
                self.runtime.singlefile = True
            
            # Resource type and ID for targeted operations
            if hasattr(args, 'type') and args.type:
                self.runtime.target_type = args.type
            
            if hasattr(args, 'id') and args.id:
                self.runtime.target_id = args.id
            
            if hasattr(args, 'exclude') and args.exclude:
                # Handle exclusion types
                if isinstance(args.exclude, str):
                    self.runtime.exclude_types = [t.strip() for t in args.exclude.split(',')]
                elif isinstance(args.exclude, list):
                    self.runtime.exclude_types = args.exclude
            
            # Data source flags
            if hasattr(args, 'datanet') and args.datanet:
                self.runtime.dnet = True
            
            if hasattr(args, 'datasgs') and args.datasgs:
                self.runtime.dsgs = True
            
            if hasattr(args, 'datakms') and args.datakms:
                self.runtime.dkms = True
            
            if hasattr(args, 'datakey') and args.datakey:
                self.runtime.dkey = True
            
            # EC2 tag configuration
            if hasattr(args, 'ec2tag') and args.ec2tag:
                try:
                    self.runtime.set_ec2_tag_filter(args.ec2tag)
                except ValueError as e:
                    # Let validation catch this later
                    self.runtime.ec2tag = args.ec2tag
            
            # Output path modifier
            if hasattr(args, 'output') and args.output:
                if isinstance(args.output, str):
                    self.runtime.pathadd = args.output + "-"
    
    def get_aws_session(self) -> boto3.Session:
        """
        Create and return a boto3 session with current configuration.
        
        Returns:
            Configured boto3 session.
            
        Raises:
            ValueError: If AWS configuration is not valid for operations.
        """
        with self._lock:
            if not self.aws.is_valid_for_aws_operations():
                raise ValueError("AWS configuration is not valid for operations")
            
            kwargs = self.aws.get_session_kwargs()
            return boto3.Session(**kwargs)
    
    def is_debug_enabled(self) -> bool:
        """
        Check if debug mode is enabled.
        
        Returns:
            True if debug mode is enabled.
        """
        with self._lock:
            return self.debug.enabled
    
    def should_log_debug(self) -> bool:
        """
        Check if debug logging should be enabled.
        
        Returns:
            True if debug logging should be enabled.
        """
        with self._lock:
            return self.debug.should_log_debug()
    
    def get_effective_log_level(self) -> str:
        """
        Get the effective log level.
        
        Returns:
            Effective log level string.
        """
        with self._lock:
            return self.debug.get_effective_log_level()
    
    def is_verbose_mode(self) -> bool:
        """
        Check if verbose output mode is enabled.
        
        Returns:
            True if verbose output should be shown.
        """
        with self._lock:
            return self.debug.is_verbose_mode()
    
    def get_debug_context(self) -> Dict[str, Any]:
        """
        Get debug context information for logging.
        
        Returns:
            Dictionary containing debug context.
        """
        with self._lock:
            return self.debug.get_debug_context()
    
    def get_tracking_message(self) -> str:
        """
        Get the current tracking message.
        
        Returns:
            Current tracking message.
        """
        with self._lock:
            return self.processing.tracking_message
    
    def set_tracking_message(self, message: str) -> None:
        """
        Set the tracking message in a thread-safe manner.
        
        Args:
            message: New tracking message.
        """
        with self._lock:
            self.processing.tracking_message = message
    
    def validate_all(self) -> List[str]:
        """
        Validate all configuration categories.
        
        Returns:
            List of all validation errors across all categories.
        """
        with self._lock:
            all_errors = []
            
            all_errors.extend(self.aws.validate())
            all_errors.extend(self.debug.validate())
            all_errors.extend(self.processing.validate())
            all_errors.extend(self.runtime.validate())
            all_errors.extend(self.resources.validate())
            
            return all_errors
    
    def get_cores(self) -> int:
        """
        Get the number of cores for processing.
        
        Returns:
            Number of cores to use.
        """
        with self._lock:
            return self.processing.cores
    
    def set_cores(self, cores: int) -> None:
        """
        Set the number of cores for processing.
        
        Args:
            cores: Number of cores to use.
        """
        with self._lock:
            self.processing.cores = cores
    
    def is_fast_mode(self) -> bool:
        """
        Check if fast mode is enabled.
        
        Returns:
            True if fast mode is enabled.
        """
        with self._lock:
            return self.runtime.fast
    
    def get_estimated_time(self) -> float:
        """
        Get the estimated processing time.
        
        Returns:
            Estimated time in seconds.
        """
        with self._lock:
            return self.processing.estimated_time
    
    def set_estimated_time(self, time: float) -> None:
        """
        Set the estimated processing time.
        
        Args:
            time: Estimated time in seconds.
        """
        with self._lock:
            self.processing.estimated_time = time
    
    def start_processing(self) -> None:
        """Start processing and begin time tracking."""
        with self._lock:
            self.processing.start_processing()
    
    def get_processing_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive processing statistics.
        
        Returns:
            Dictionary containing processing statistics.
        """
        with self._lock:
            return self.processing.get_processing_stats()
    
    def get_progress_percentage(self) -> float:
        """
        Get processing progress as a percentage.
        
        Returns:
            Progress percentage (0.0 to 100.0).
        """
        with self._lock:
            return self.processing.get_progress_percentage()
    
    def mark_resource_processed(self, resource_id: str) -> None:
        """
        Mark a resource as processed.
        
        Args:
            resource_id: Resource identifier.
        """
        with self._lock:
            self.processing.mark_resource_processed(resource_id)
    
    def is_resource_processed(self, resource_id: str) -> bool:
        """
        Check if a resource has been processed.
        
        Args:
            resource_id: Resource identifier.
            
        Returns:
            True if resource has been processed.
        """
        with self._lock:
            return self.processing.is_resource_processed(resource_id)
    
    def set_total_resources(self, total: int) -> None:
        """
        Set the total number of resources to process.
        
        Args:
            total: Total number of resources.
        """
        with self._lock:
            self.processing.total_resources = total
    
    def update_aws_credentials(self, credential_type: str, is_sso: bool) -> None:
        """
        Update AWS credential information.
        
        Args:
            credential_type: Type of AWS credentials detected.
            is_sso: Whether SSO is being used.
        """
        with self._lock:
            self.aws.credential_type = credential_type
            self.aws.is_sso = is_sso
    
    def set_account_id(self, account_id: str) -> None:
        """
        Set the AWS account ID.
        
        Args:
            account_id: AWS account ID.
        """
        with self._lock:
            self.aws.account_id = account_id
    
    def get_region_length(self) -> int:
        """
        Get the length of the region string.
        
        Returns:
            Length of the region string.
        """
        with self._lock:
            return len(self.aws.region)
    
    def setup_paths(self) -> None:
        """Set up the processing paths based on current configuration."""
        with self._lock:
            if self.runtime.serverless:
                self.runtime.path1 = f"/tmp/aws2tf/generated/tf-{self.runtime.pathadd}{self.aws.account_id}-{self.aws.region}"
            else:
                self.runtime.path1 = f"generated/tf-{self.runtime.pathadd}{self.aws.account_id}-{self.aws.region}"
            
            self.runtime.path2 = f"{self.runtime.path1}/imported"
            self.runtime.path3 = f"{self.runtime.path1}/notimported"
            
            # Update resource config region length
            self.resources.regionl = len(self.aws.region)