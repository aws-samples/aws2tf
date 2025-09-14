#!/usr/bin/env python3
"""
Terraform State Management and Validation for aws2tf.

This module provides comprehensive terraform state management including:
1. State file validation and analysis
2. State backup and recovery mechanisms
3. Import validation against existing state
4. State drift detection and remediation
5. Rollback capabilities for failed operations
6. Integration with configuration management system
"""

import os
import json
import shutil
import subprocess
import time
import hashlib
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import threading
from datetime import datetime, timezone

from .config import ConfigurationManager


class StateValidationResult(Enum):
    """Result of state validation operations."""
    VALID = "valid"
    INVALID_FORMAT = "invalid_format"
    MISSING_RESOURCES = "missing_resources"
    DUPLICATE_RESOURCES = "duplicate_resources"
    CORRUPTED_STATE = "corrupted_state"
    VERSION_MISMATCH = "version_mismatch"
    BACKEND_ERROR = "backend_error"


class StateBackupType(Enum):
    """Types of state backups."""
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    PRE_IMPORT = "pre_import"
    PRE_OPERATION = "pre_operation"


class StateDriftType(Enum):
    """Types of state drift."""
    RESOURCE_ADDED = "resource_added"
    RESOURCE_REMOVED = "resource_removed"
    RESOURCE_MODIFIED = "resource_modified"
    ATTRIBUTE_CHANGED = "attribute_changed"
    DEPENDENCY_CHANGED = "dependency_changed"


@dataclass
class StateResource:
    """Represents a resource in terraform state."""
    address: str
    type: str
    name: str
    provider: str
    instances: List[Dict[str, Any]] = field(default_factory=list)
    dependencies: Set[str] = field(default_factory=set)
    attributes: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def full_address(self) -> str:
        """Get the full terraform address."""
        return f"{self.type}.{self.name}"
    
    @property
    def resource_id(self) -> Optional[str]:
        """Get the AWS resource ID from state."""
        if self.instances:
            return self.instances[0].get("attributes", {}).get("id")
        return None


@dataclass
class StateValidationIssue:
    """Represents a state validation issue."""
    severity: str  # "error", "warning", "info"
    issue_type: str
    resource_address: Optional[str]
    message: str
    suggested_fix: Optional[str] = None
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class StateBackup:
    """Represents a terraform state backup."""
    backup_id: str
    backup_type: StateBackupType
    timestamp: datetime
    file_path: Path
    checksum: str
    size_bytes: int
    description: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class StateDrift:
    """Represents detected state drift."""
    resource_address: str
    drift_type: StateDriftType
    expected_value: Any
    actual_value: Any
    attribute_path: str = ""
    severity: str = "warning"
    description: str = ""


class TerraformStateManager:
    """Main terraform state management and validation system."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.terraform_dir = Path(config.runtime.path1) if config.runtime.path1 else Path(".")
        self.state_file = self.terraform_dir / "terraform.tfstate"
        self.backup_dir = self.terraform_dir / ".terraform" / "backups"
        self.lock = threading.Lock()
        
        # State cache
        self._state_cache: Optional[Dict[str, Any]] = None
        self._cache_timestamp: Optional[float] = None
        self._cache_ttl = 30  # Cache TTL in seconds
        
        # Backup management
        self.backups: Dict[str, StateBackup] = {}
        self._load_existing_backups()
        
        # Validation rules
        self.validation_rules = self._initialize_validation_rules()
    
    def _initialize_validation_rules(self) -> Dict[str, Any]:
        """Initialize state validation rules."""
        return {
            "required_terraform_version": ">=0.12.0",
            "max_resources_per_state": 1000,
            "required_providers": ["aws"],
            "forbidden_resource_types": [],
            "required_attributes": {
                "aws_vpc": ["id", "cidr_block"],
                "aws_subnet": ["id", "vpc_id", "cidr_block"],
                "aws_instance": ["id", "instance_type", "subnet_id"],
                "aws_security_group": ["id", "vpc_id"],
            }
        }
    
    def _load_existing_backups(self) -> None:
        """Load information about existing backups."""
        if not self.backup_dir.exists():
            return
        
        for backup_file in self.backup_dir.glob("*.tfstate"):
            try:
                backup_info = self._analyze_backup_file(backup_file)
                if backup_info:
                    self.backups[backup_info.backup_id] = backup_info
            except Exception as e:
                if self.config.debug.enabled:
                    print(f"Error loading backup {backup_file}: {e}")
    
    def _analyze_backup_file(self, backup_file: Path) -> Optional[StateBackup]:
        """Analyze a backup file and extract metadata."""
        try:
            stat = backup_file.stat()
            
            # Generate backup ID from filename and timestamp
            backup_id = f"{backup_file.stem}_{int(stat.st_mtime)}"
            
            # Calculate checksum
            checksum = self._calculate_file_checksum(backup_file)
            
            # Determine backup type from filename
            backup_type = StateBackupType.MANUAL
            if "auto" in backup_file.name:
                backup_type = StateBackupType.AUTOMATIC
            elif "pre_import" in backup_file.name:
                backup_type = StateBackupType.PRE_IMPORT
            elif "pre_op" in backup_file.name:
                backup_type = StateBackupType.PRE_OPERATION
            
            return StateBackup(
                backup_id=backup_id,
                backup_type=backup_type,
                timestamp=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc),
                file_path=backup_file,
                checksum=checksum,
                size_bytes=stat.st_size
            )
        except Exception:
            return None
    
    def _calculate_file_checksum(self, file_path: Path) -> str:
        """Calculate SHA256 checksum of a file."""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    
    def get_current_state(self, force_refresh: bool = False) -> Optional[Dict[str, Any]]:
        """
        Get the current terraform state with caching.
        
        Args:
            force_refresh: Force refresh of cached state
            
        Returns:
            Parsed terraform state or None if not available
        """
        current_time = time.time()
        
        # Check cache validity
        if (not force_refresh and 
            self._state_cache is not None and 
            self._cache_timestamp is not None and
            current_time - self._cache_timestamp < self._cache_ttl):
            return self._state_cache
        
        # Load state from file
        if not self.state_file.exists():
            self._state_cache = None
            self._cache_timestamp = current_time
            return None
        
        try:
            with open(self.state_file, 'r') as f:
                state_data = json.load(f)
            
            self._state_cache = state_data
            self._cache_timestamp = current_time
            
            return state_data
            
        except (json.JSONDecodeError, IOError) as e:
            if self.config.debug.enabled:
                print(f"Error reading state file: {e}")
            self._state_cache = None
            self._cache_timestamp = current_time
            return None
    
    def validate_state(self, state_data: Optional[Dict[str, Any]] = None) -> List[StateValidationIssue]:
        """
        Validate terraform state against validation rules.
        
        Args:
            state_data: State data to validate (uses current state if None)
            
        Returns:
            List of validation issues
        """
        if state_data is None:
            state_data = self.get_current_state()
        
        if state_data is None:
            return [StateValidationIssue(
                severity="error",
                issue_type="missing_state",
                resource_address=None,
                message="No terraform state file found",
                suggested_fix="Initialize terraform or import resources"
            )]
        
        issues = []
        
        # Validate state format
        issues.extend(self._validate_state_format(state_data))
        
        # Validate terraform version
        issues.extend(self._validate_terraform_version(state_data))
        
        # Validate resources
        issues.extend(self._validate_resources(state_data))
        
        # Validate providers
        issues.extend(self._validate_providers(state_data))
        
        # Validate resource count
        issues.extend(self._validate_resource_count(state_data))
        
        return issues
    
    def _validate_state_format(self, state_data: Dict[str, Any]) -> List[StateValidationIssue]:
        """Validate basic state file format."""
        issues = []
        
        # Check required top-level keys
        required_keys = ["version", "terraform_version", "resources"]
        for key in required_keys:
            if key not in state_data:
                issues.append(StateValidationIssue(
                    severity="error",
                    issue_type="invalid_format",
                    resource_address=None,
                    message=f"Missing required key: {key}",
                    suggested_fix=f"Ensure state file contains '{key}' field"
                ))
        
        # Validate version format
        if "version" in state_data:
            version = state_data["version"]
            if not isinstance(version, int) or version < 3:
                issues.append(StateValidationIssue(
                    severity="warning",
                    issue_type="version_mismatch",
                    resource_address=None,
                    message=f"Unsupported state version: {version}",
                    suggested_fix="Consider upgrading terraform version"
                ))
        
        return issues
    
    def _validate_terraform_version(self, state_data: Dict[str, Any]) -> List[StateValidationIssue]:
        """Validate terraform version compatibility."""
        issues = []
        
        tf_version = state_data.get("terraform_version")
        if tf_version:
            # Parse version (simplified)
            try:
                version_parts = tf_version.split(".")
                major = int(version_parts[0])
                minor = int(version_parts[1]) if len(version_parts) > 1 else 0
                
                if major == 0 and minor < 12:
                    issues.append(StateValidationIssue(
                        severity="warning",
                        issue_type="version_mismatch",
                        resource_address=None,
                        message=f"Old terraform version: {tf_version}",
                        suggested_fix="Consider upgrading to terraform >= 0.12"
                    ))
            except (ValueError, IndexError):
                issues.append(StateValidationIssue(
                    severity="warning",
                    issue_type="invalid_format",
                    resource_address=None,
                    message=f"Invalid terraform version format: {tf_version}"
                ))
        
        return issues
    
    def _validate_resources(self, state_data: Dict[str, Any]) -> List[StateValidationIssue]:
        """Validate resources in state."""
        issues = []
        
        resources = state_data.get("resources", [])
        resource_addresses = set()
        
        for resource in resources:
            # Check for duplicate addresses
            address = f"{resource.get('type', '')}.{resource.get('name', '')}"
            if address in resource_addresses:
                issues.append(StateValidationIssue(
                    severity="error",
                    issue_type="duplicate_resources",
                    resource_address=address,
                    message=f"Duplicate resource address: {address}",
                    suggested_fix="Remove duplicate resource definitions"
                ))
            resource_addresses.add(address)
            
            # Validate resource structure
            issues.extend(self._validate_single_resource(resource))
        
        return issues
    
    def _validate_single_resource(self, resource: Dict[str, Any]) -> List[StateValidationIssue]:
        """Validate a single resource in state."""
        issues = []
        
        resource_type = resource.get("type", "")
        resource_name = resource.get("name", "")
        address = f"{resource_type}.{resource_name}"
        
        # Check required fields
        required_fields = ["type", "name", "provider", "instances"]
        for field in required_fields:
            if field not in resource:
                issues.append(StateValidationIssue(
                    severity="error",
                    issue_type="invalid_format",
                    resource_address=address,
                    message=f"Missing required field: {field}",
                    suggested_fix=f"Ensure resource has '{field}' field"
                ))
        
        # Validate instances
        instances = resource.get("instances", [])
        if not instances:
            issues.append(StateValidationIssue(
                severity="warning",
                issue_type="missing_resources",
                resource_address=address,
                message="Resource has no instances",
                suggested_fix="Check if resource was properly imported"
            ))
        
        # Validate required attributes for known resource types
        if resource_type in self.validation_rules["required_attributes"]:
            required_attrs = self.validation_rules["required_attributes"][resource_type]
            
            for instance in instances:
                attributes = instance.get("attributes", {})
                for attr in required_attrs:
                    if attr not in attributes:
                        issues.append(StateValidationIssue(
                            severity="warning",
                            issue_type="missing_resources",
                            resource_address=address,
                            message=f"Missing required attribute: {attr}",
                            suggested_fix=f"Ensure resource has '{attr}' attribute"
                        ))
        
        return issues
    
    def _validate_providers(self, state_data: Dict[str, Any]) -> List[StateValidationIssue]:
        """Validate provider configuration."""
        issues = []
        
        # Check for required providers
        resources = state_data.get("resources", [])
        used_providers = set()
        
        for resource in resources:
            provider = resource.get("provider", "")
            if provider:
                # Extract provider name (remove version info)
                provider_name = provider.split("[")[0].strip()
                used_providers.add(provider_name)
        
        required_providers = self.validation_rules["required_providers"]
        for required_provider in required_providers:
            provider_found = any(
                provider.startswith(f"provider[\"{required_provider}\"]") or 
                provider.startswith(required_provider)
                for provider in used_providers
            )
            
            if not provider_found and resources:  # Only check if we have resources
                issues.append(StateValidationIssue(
                    severity="warning",
                    issue_type="missing_resources",
                    resource_address=None,
                    message=f"Required provider not found: {required_provider}",
                    suggested_fix=f"Ensure {required_provider} provider is configured"
                ))
        
        return issues
    
    def _validate_resource_count(self, state_data: Dict[str, Any]) -> List[StateValidationIssue]:
        """Validate resource count limits."""
        issues = []
        
        resources = state_data.get("resources", [])
        resource_count = len(resources)
        max_resources = self.validation_rules["max_resources_per_state"]
        
        if resource_count > max_resources:
            issues.append(StateValidationIssue(
                severity="warning",
                issue_type="invalid_format",
                resource_address=None,
                message=f"Too many resources in state: {resource_count} > {max_resources}",
                suggested_fix="Consider splitting state into multiple files"
            ))
        
        return issues
    
    def create_backup(self, backup_type: StateBackupType = StateBackupType.MANUAL,
                     description: str = "") -> Optional[StateBackup]:
        """
        Create a backup of the current terraform state.
        
        Args:
            backup_type: Type of backup to create
            description: Optional description for the backup
            
        Returns:
            StateBackup object or None if backup failed
        """
        if not self.state_file.exists():
            if self.config.debug.enabled:
                print("No state file to backup")
            return None
        
        # Ensure backup directory exists
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate backup filename
        timestamp = datetime.now(timezone.utc)
        timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")
        backup_filename = f"terraform.tfstate.{backup_type.value}.{timestamp_str}"
        backup_path = self.backup_dir / backup_filename
        
        try:
            # Copy state file to backup location
            shutil.copy2(self.state_file, backup_path)
            
            # Calculate checksum
            checksum = self._calculate_file_checksum(backup_path)
            
            # Get file size
            size_bytes = backup_path.stat().st_size
            
            # Generate backup ID
            backup_id = f"{backup_type.value}_{timestamp_str}"
            
            # Create backup object
            backup = StateBackup(
                backup_id=backup_id,
                backup_type=backup_type,
                timestamp=timestamp,
                file_path=backup_path,
                checksum=checksum,
                size_bytes=size_bytes,
                description=description
            )
            
            # Store backup info
            with self.lock:
                self.backups[backup_id] = backup
            
            if self.config.debug.enabled:
                print(f"Created state backup: {backup_path}")
            
            return backup
            
        except Exception as e:
            if self.config.debug.enabled:
                print(f"Failed to create backup: {e}")
            return None
    
    def restore_backup(self, backup_id: str) -> bool:
        """
        Restore terraform state from a backup.
        
        Args:
            backup_id: ID of the backup to restore
            
        Returns:
            True if restore was successful
        """
        if backup_id not in self.backups:
            if self.config.debug.enabled:
                print(f"Backup not found: {backup_id}")
            return False
        
        backup = self.backups[backup_id]
        
        if not backup.file_path.exists():
            if self.config.debug.enabled:
                print(f"Backup file not found: {backup.file_path}")
            return False
        
        try:
            # Verify backup integrity
            current_checksum = self._calculate_file_checksum(backup.file_path)
            if current_checksum != backup.checksum:
                if self.config.debug.enabled:
                    print(f"Backup checksum mismatch: {backup_id}")
                return False
            
            # Create backup of current state before restore
            self.create_backup(StateBackupType.PRE_OPERATION, f"Before restore of {backup_id}")
            
            # Restore backup
            shutil.copy2(backup.file_path, self.state_file)
            
            # Clear state cache
            self._state_cache = None
            self._cache_timestamp = None
            
            if self.config.debug.enabled:
                print(f"Restored state from backup: {backup_id}")
            
            return True
            
        except Exception as e:
            if self.config.debug.enabled:
                print(f"Failed to restore backup {backup_id}: {e}")
            return False
    
    def list_backups(self, backup_type: Optional[StateBackupType] = None) -> List[StateBackup]:
        """
        List available state backups.
        
        Args:
            backup_type: Filter by backup type (optional)
            
        Returns:
            List of StateBackup objects
        """
        backups = list(self.backups.values())
        
        if backup_type:
            backups = [b for b in backups if b.backup_type == backup_type]
        
        # Sort by timestamp (newest first)
        backups.sort(key=lambda b: b.timestamp, reverse=True)
        
        return backups
    
    def cleanup_old_backups(self, keep_count: int = 10) -> int:
        """
        Clean up old backups, keeping only the most recent ones.
        
        Args:
            keep_count: Number of backups to keep per type
            
        Returns:
            Number of backups deleted
        """
        deleted_count = 0
        
        # Group backups by type
        backups_by_type = {}
        for backup in self.backups.values():
            backup_type = backup.backup_type
            if backup_type not in backups_by_type:
                backups_by_type[backup_type] = []
            backups_by_type[backup_type].append(backup)
        
        # Clean up each type
        for backup_type, type_backups in backups_by_type.items():
            # Sort by timestamp (newest first)
            type_backups.sort(key=lambda b: b.timestamp, reverse=True)
            
            # Delete old backups
            for backup in type_backups[keep_count:]:
                try:
                    if backup.file_path.exists():
                        backup.file_path.unlink()
                    
                    with self.lock:
                        if backup.backup_id in self.backups:
                            del self.backups[backup.backup_id]
                    
                    deleted_count += 1
                    
                    if self.config.debug.enabled:
                        print(f"Deleted old backup: {backup.backup_id}")
                        
                except Exception as e:
                    if self.config.debug.enabled:
                        print(f"Failed to delete backup {backup.backup_id}: {e}")
        
        return deleted_count
    
    def detect_state_drift(self, expected_resources: Dict[str, Any]) -> List[StateDrift]:
        """
        Detect drift between expected resources and current state.
        
        Args:
            expected_resources: Expected resource configuration
            
        Returns:
            List of detected drift issues
        """
        current_state = self.get_current_state()
        if not current_state:
            return []
        
        drift_issues = []
        current_resources = {
            f"{r['type']}.{r['name']}": r 
            for r in current_state.get("resources", [])
        }
        
        # Check for missing resources
        for expected_addr, expected_config in expected_resources.items():
            if expected_addr not in current_resources:
                drift_issues.append(StateDrift(
                    resource_address=expected_addr,
                    drift_type=StateDriftType.RESOURCE_REMOVED,
                    expected_value=expected_config,
                    actual_value=None,
                    severity="error",
                    description=f"Resource {expected_addr} missing from state"
                ))
        
        # Check for unexpected resources
        for current_addr in current_resources:
            if current_addr not in expected_resources:
                drift_issues.append(StateDrift(
                    resource_address=current_addr,
                    drift_type=StateDriftType.RESOURCE_ADDED,
                    expected_value=None,
                    actual_value=current_resources[current_addr],
                    severity="warning",
                    description=f"Unexpected resource {current_addr} in state"
                ))
        
        # Check for attribute differences
        for addr in set(expected_resources.keys()) & set(current_resources.keys()):
            expected = expected_resources[addr]
            current = current_resources[addr]
            
            # Compare key attributes
            drift_issues.extend(self._compare_resource_attributes(addr, expected, current))
        
        return drift_issues
    
    def _compare_resource_attributes(self, address: str, expected: Dict[str, Any], 
                                   current: Dict[str, Any]) -> List[StateDrift]:
        """Compare attributes between expected and current resource."""
        drift_issues = []
        
        # Get current attributes
        current_instances = current.get("instances", [])
        if not current_instances:
            return drift_issues
        
        current_attrs = current_instances[0].get("attributes", {})
        expected_attrs = expected.get("attributes", {})
        
        # Compare important attributes
        important_attrs = ["id", "type", "vpc_id", "subnet_id", "security_groups"]
        
        for attr in important_attrs:
            if attr in expected_attrs and attr in current_attrs:
                if expected_attrs[attr] != current_attrs[attr]:
                    drift_issues.append(StateDrift(
                        resource_address=address,
                        drift_type=StateDriftType.ATTRIBUTE_CHANGED,
                        expected_value=expected_attrs[attr],
                        actual_value=current_attrs[attr],
                        attribute_path=attr,
                        severity="warning",
                        description=f"Attribute {attr} changed in {address}"
                    ))
        
        return drift_issues
    
    def get_state_resources(self) -> List[StateResource]:
        """
        Get all resources from current state as StateResource objects.
        
        Returns:
            List of StateResource objects
        """
        state_data = self.get_current_state()
        if not state_data:
            return []
        
        resources = []
        
        for resource_data in state_data.get("resources", []):
            resource = StateResource(
                address=f"{resource_data.get('type', '')}.{resource_data.get('name', '')}",
                type=resource_data.get("type", ""),
                name=resource_data.get("name", ""),
                provider=resource_data.get("provider", ""),
                instances=resource_data.get("instances", [])
            )
            
            # Extract attributes from first instance
            if resource.instances:
                resource.attributes = resource.instances[0].get("attributes", {})
            
            resources.append(resource)
        
        return resources
    
    def check_resource_exists(self, resource_address: str) -> bool:
        """
        Check if a resource exists in current state.
        
        Args:
            resource_address: Terraform resource address (e.g., "aws_vpc.main")
            
        Returns:
            True if resource exists in state
        """
        resources = self.get_state_resources()
        return any(r.address == resource_address for r in resources)
    
    def get_state_summary(self) -> Dict[str, Any]:
        """Get summary information about current state."""
        state_data = self.get_current_state()
        if not state_data:
            return {
                "state_exists": False,
                "resource_count": 0,
                "provider_count": 0,
                "terraform_version": None
            }
        
        resources = state_data.get("resources", [])
        providers = set()
        
        for resource in resources:
            provider = resource.get("provider", "")
            if provider:
                providers.add(provider)
        
        # Count resources by type
        resource_types = {}
        for resource in resources:
            resource_type = resource.get("type", "unknown")
            resource_types[resource_type] = resource_types.get(resource_type, 0) + 1
        
        return {
            "state_exists": True,
            "resource_count": len(resources),
            "provider_count": len(providers),
            "terraform_version": state_data.get("terraform_version"),
            "state_version": state_data.get("version"),
            "resource_types": resource_types,
            "providers": list(providers),
            "backup_count": len(self.backups)
        }


def create_terraform_state_manager(config: ConfigurationManager) -> TerraformStateManager:
    """Factory function to create TerraformStateManager."""
    return TerraformStateManager(config)


def validate_state_before_import(config: ConfigurationManager, 
                                import_commands: List[str]) -> List[StateValidationIssue]:
    """
    Validate terraform state before executing import commands.
    
    Args:
        config: Configuration manager
        import_commands: List of import commands to validate
        
    Returns:
        List of validation issues
    """
    state_manager = create_terraform_state_manager(config)
    
    # Validate current state
    issues = state_manager.validate_state()
    
    # Check for conflicts with planned imports
    existing_resources = {r.address for r in state_manager.get_state_resources()}
    
    for command in import_commands:
        # Extract resource address from import command
        # Format: "terraform import aws_vpc.main vpc-123456"
        parts = command.split()
        if len(parts) >= 3 and parts[0] == "terraform" and parts[1] == "import":
            resource_address = parts[2]
            
            if resource_address in existing_resources:
                issues.append(StateValidationIssue(
                    severity="error",
                    issue_type="duplicate_resources",
                    resource_address=resource_address,
                    message=f"Resource already exists in state: {resource_address}",
                    suggested_fix="Remove existing resource or use different name"
                ))
    
    return issues