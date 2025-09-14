"""
Configuration category classes for aws2tf.

This module defines the base ConfigCategory class and all specific configuration
categories that organize related settings into logical groups.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import threading


class ConfigCategory(ABC):
    """Base class for all configuration categories."""
    
    @abstractmethod
    def validate(self) -> List[str]:
        """
        Validate the configuration category.
        
        Returns:
            List of validation error messages. Empty list if valid.
        """
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert configuration to dictionary.
        
        Returns:
            Dictionary representation of the configuration.
        """
        if hasattr(self, '__dataclass_fields__'):
            return {field.name: getattr(self, field.name) 
                   for field in self.__dataclass_fields__.values()}
        return {}
    
    def from_dict(self, data: Dict[str, Any]) -> None:
        """
        Update configuration from dictionary.
        
        Args:
            data: Dictionary containing configuration values.
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)


@dataclass
class AWSConfig(ConfigCategory):
    """AWS-specific configuration settings."""
    
    # Core AWS configuration
    version: str = "v1010"
    tf_version: str = "5.100.0"
    profile: str = "default"
    region: str = "xx-xxxx-x"
    account_id: str = "xxxxxxxxxxxx"
    credential_type: str = "invalid"
    is_sso: bool = False
    sso_instance: Optional[str] = None
    
    def validate(self) -> List[str]:
        """Validate AWS configuration."""
        errors = []
        
        if not self.region or self.region == "xx-xxxx-x":
            errors.append("Invalid AWS region specified")
        
        if not self.account_id or self.account_id == "xxxxxxxxxxxx":
            errors.append("AWS account ID not set")
        
        if self.credential_type == "invalid":
            errors.append("Invalid AWS credential type")
        
        if not self.profile:
            errors.append("AWS profile not specified")
        
        # Validate region format (basic check)
        if self.region and not self._is_valid_region_format(self.region):
            errors.append(f"Invalid AWS region format: {self.region}")
        
        # Validate account ID format
        if self.account_id and self.account_id != "xxxxxxxxxxxx":
            if not self._is_valid_account_id(self.account_id):
                errors.append(f"Invalid AWS account ID format: {self.account_id}")
        
        # Validate Terraform version format
        if not self._is_valid_tf_version(self.tf_version):
            errors.append(f"Invalid Terraform version format: {self.tf_version}")
        
        return errors
    
    def _is_valid_region_format(self, region: str) -> bool:
        """
        Validate AWS region format.
        
        Args:
            region: AWS region string to validate.
            
        Returns:
            True if region format is valid.
        """
        import re
        # AWS regions follow pattern: us-east-1, eu-west-2, ap-southeast-1, etc.
        pattern = r'^[a-z]{2,3}-[a-z]+-\d+$'
        return bool(re.match(pattern, region))
    
    def _is_valid_account_id(self, account_id: str) -> bool:
        """
        Validate AWS account ID format.
        
        Args:
            account_id: AWS account ID to validate.
            
        Returns:
            True if account ID format is valid.
        """
        # AWS account IDs are 12-digit numbers
        return account_id.isdigit() and len(account_id) == 12
    
    def _is_valid_tf_version(self, version: str) -> bool:
        """
        Validate Terraform version format.
        
        Args:
            version: Terraform version string to validate.
            
        Returns:
            True if version format is valid.
        """
        import re
        # Terraform versions follow semantic versioning: X.Y.Z
        pattern = r'^\d+\.\d+\.\d+$'
        return bool(re.match(pattern, version))
    
    def get_session_kwargs(self) -> Dict[str, Any]:
        """
        Get kwargs for creating a boto3 session.
        
        Returns:
            Dictionary of kwargs for boto3.Session().
        """
        kwargs = {'region_name': self.region}
        
        if self.profile != "default":
            kwargs['profile_name'] = self.profile
        
        return kwargs
    
    def is_valid_for_aws_operations(self) -> bool:
        """
        Check if configuration is valid for AWS operations.
        
        Returns:
            True if configuration can be used for AWS API calls.
        """
        return (
            self.credential_type != "invalid" and
            self.region != "xx-xxxx-x" and
            self.account_id != "xxxxxxxxxxxx" and
            len(self.validate()) == 0
        )


@dataclass
class DebugConfig(ConfigCategory):
    """Debug and logging configuration settings."""
    
    # Core debug flags
    enabled: bool = False
    debug5: bool = False
    validate_mode: bool = False
    fast: bool = False
    
    # Logging configuration
    log_level: str = "INFO"
    log_to_file: bool = False
    log_file_path: Optional[str] = None
    
    # Debug output options
    verbose_output: bool = False
    show_timestamps: bool = True
    show_thread_info: bool = False
    
    def validate(self) -> List[str]:
        """Validate debug configuration."""
        errors = []
        
        # Validate log level
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if self.log_level not in valid_log_levels:
            errors.append(f"Invalid log level: {self.log_level}. Must be one of {valid_log_levels}")
        
        # Validate log file configuration
        if self.log_to_file and not self.log_file_path:
            errors.append("Log file path must be specified when log_to_file is True")
        
        # Validate conflicting settings
        if self.enabled and self.fast:
            errors.append("Debug mode and fast mode cannot both be enabled")
        
        return errors
    
    def should_log_debug(self) -> bool:
        """
        Check if debug logging should be enabled.
        
        Returns:
            True if debug logging should be enabled.
        """
        return self.enabled or self.debug5 or self.log_level == "DEBUG"
    
    def get_effective_log_level(self) -> str:
        """
        Get the effective log level based on debug settings.
        
        Returns:
            Effective log level string.
        """
        if self.enabled or self.debug5:
            return "DEBUG"
        return self.log_level
    
    def is_verbose_mode(self) -> bool:
        """
        Check if verbose output mode is enabled.
        
        Returns:
            True if verbose output should be shown.
        """
        return self.verbose_output or self.enabled or self.debug5
    
    def get_debug_context(self) -> Dict[str, Any]:
        """
        Get debug context information for logging.
        
        Returns:
            Dictionary containing debug context.
        """
        context = {
            'debug_enabled': self.enabled,
            'debug5_enabled': self.debug5,
            'log_level': self.get_effective_log_level(),
            'verbose': self.is_verbose_mode()
        }
        
        if self.show_timestamps:
            import datetime
            context['timestamp'] = datetime.datetime.now().isoformat()
        
        if self.show_thread_info:
            import threading
            context['thread_id'] = threading.current_thread().ident
            context['thread_name'] = threading.current_thread().name
        
        return context


@dataclass
class ProcessingConfig(ConfigCategory):
    """Processing state and tracking configuration."""
    
    # Core processing settings
    tracking_message: str = "aws2tf: Starting, update messages every 20 seconds"
    estimated_time: float = 120.0
    cores: int = 2
    
    # Processing lists
    processed: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    types: List[str] = field(default_factory=list)
    
    # Processing state dictionaries
    rproc: Dict[str, bool] = field(default_factory=dict)
    rdep: Dict[str, bool] = field(default_factory=dict)
    trdep: Dict[str, bool] = field(default_factory=dict)
    
    # Processing flags and counters
    lbc: int = 0
    rbc: int = 0
    plan2: bool = False
    
    # Progress tracking
    total_resources: int = 0
    processed_resources: int = 0
    failed_resources: int = 0
    start_time: Optional[float] = None
    
    def validate(self) -> List[str]:
        """Validate processing configuration."""
        errors = []
        
        if self.cores < 1:
            errors.append("Number of cores must be at least 1")
        
        if self.cores > 64:  # Reasonable upper limit
            errors.append("Number of cores cannot exceed 64")
        
        if self.estimated_time < 0:
            errors.append("Estimated time cannot be negative")
        
        if self.total_resources < 0:
            errors.append("Total resources cannot be negative")
        
        if self.processed_resources < 0:
            errors.append("Processed resources cannot be negative")
        
        if self.failed_resources < 0:
            errors.append("Failed resources cannot be negative")
        
        if self.processed_resources > self.total_resources:
            errors.append("Processed resources cannot exceed total resources")
        
        return errors
    
    def add_processed_item(self, item: str) -> None:
        """
        Add an item to the processed list.
        
        Args:
            item: Item identifier to add.
        """
        if item not in self.processed:
            self.processed.append(item)
            self.processed_resources += 1
    
    def add_dependency(self, dependency: str) -> None:
        """
        Add a dependency to the dependencies list.
        
        Args:
            dependency: Dependency identifier to add.
        """
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)
    
    def mark_resource_processed(self, resource_id: str) -> None:
        """
        Mark a resource as processed.
        
        Args:
            resource_id: Resource identifier.
        """
        self.rproc[resource_id] = True
    
    def is_resource_processed(self, resource_id: str) -> bool:
        """
        Check if a resource has been processed.
        
        Args:
            resource_id: Resource identifier.
            
        Returns:
            True if resource has been processed.
        """
        return self.rproc.get(resource_id, False)
    
    def mark_dependency_resolved(self, dependency_id: str) -> None:
        """
        Mark a dependency as resolved.
        
        Args:
            dependency_id: Dependency identifier.
        """
        self.rdep[dependency_id] = True
    
    def is_dependency_resolved(self, dependency_id: str) -> bool:
        """
        Check if a dependency has been resolved.
        
        Args:
            dependency_id: Dependency identifier.
            
        Returns:
            True if dependency has been resolved.
        """
        return self.rdep.get(dependency_id, False)
    
    def get_progress_percentage(self) -> float:
        """
        Get processing progress as a percentage.
        
        Returns:
            Progress percentage (0.0 to 100.0).
        """
        if self.total_resources == 0:
            return 0.0
        return (self.processed_resources / self.total_resources) * 100.0
    
    def get_failure_rate(self) -> float:
        """
        Get failure rate as a percentage.
        
        Returns:
            Failure rate percentage (0.0 to 100.0).
        """
        total_attempted = self.processed_resources + self.failed_resources
        if total_attempted == 0:
            return 0.0
        return (self.failed_resources / total_attempted) * 100.0
    
    def start_processing(self) -> None:
        """Mark the start of processing."""
        import time
        self.start_time = time.time()
    
    def get_elapsed_time(self) -> float:
        """
        Get elapsed processing time in seconds.
        
        Returns:
            Elapsed time in seconds, or 0.0 if not started.
        """
        if self.start_time is None:
            return 0.0
        import time
        return time.time() - self.start_time
    
    def get_estimated_remaining_time(self) -> float:
        """
        Get estimated remaining processing time.
        
        Returns:
            Estimated remaining time in seconds.
        """
        if self.processed_resources == 0 or self.start_time is None:
            return self.estimated_time
        
        elapsed = self.get_elapsed_time()
        rate = self.processed_resources / elapsed
        remaining_resources = self.total_resources - self.processed_resources
        
        if rate > 0:
            return remaining_resources / rate
        return self.estimated_time
    
    def get_processing_stats(self) -> Dict[str, Any]:
        """
        Get comprehensive processing statistics.
        
        Returns:
            Dictionary containing processing statistics.
        """
        return {
            'total_resources': self.total_resources,
            'processed_resources': self.processed_resources,
            'failed_resources': self.failed_resources,
            'progress_percentage': self.get_progress_percentage(),
            'failure_rate': self.get_failure_rate(),
            'elapsed_time': self.get_elapsed_time(),
            'estimated_remaining_time': self.get_estimated_remaining_time(),
            'cores': self.cores,
            'tracking_message': self.tracking_message
        }


@dataclass
class RuntimeConfig(ConfigCategory):
    """Runtime behavior and flag configuration."""
    
    merge: bool = False
    fast: bool = False
    apionly: bool = False
    serverless: bool = False
    expected: bool = False
    
    # Data source flags
    dnet: bool = False
    dkms: bool = False
    dkey: bool = False
    dsgs: bool = False
    
    # EC2 tag filtering
    ec2tag: Optional[str] = None
    ec2tagv: Optional[str] = None
    ec2tagk: Optional[str] = None
    
    # Path configuration
    cwd: str = ""
    path1: str = ""
    path2: str = ""
    path3: str = ""
    pathadd: str = ""
    
    # Various runtime flags
    asg_azs: bool = False
    lbskipaacl: bool = False
    lbskipcnxl: bool = False
    mskcfg: bool = False
    repdbin: bool = False
    gulejobmaxcap: bool = False
    levsmap: bool = False
    ec2ignore: bool = False
    emrsubnetid: bool = False
    
    # Processing flags
    elastirep: bool = False
    elastigrep: bool = False
    elasticc: bool = False
    kinesismsk: bool = False
    destbuck: bool = False
    
    # Exclusion types
    all_extypes: List[str] = field(default_factory=list)
    exclude_types: List[str] = field(default_factory=list)
    
    # Target resource configuration
    target_type: Optional[str] = None
    target_id: Optional[str] = None
    
    # Output configuration
    singlefile: bool = False
    
    def validate(self) -> List[str]:
        """Validate runtime configuration."""
        errors = []
        
        if self.ec2tag and ":" not in self.ec2tag:
            errors.append("EC2 tag must be in format 'key:value'")
        
        # Validate path configurations
        if self.serverless and not self.path1.startswith("/tmp"):
            errors.append("Serverless mode requires paths to start with /tmp")
        
        return errors
    
    def set_ec2_tag_filter(self, tag_string: str) -> None:
        """
        Set EC2 tag filter from a tag string.
        
        Args:
            tag_string: Tag in format "key:value".
            
        Raises:
            ValueError: If tag format is invalid.
        """
        if ":" not in tag_string:
            raise ValueError("EC2 tag must be in format 'key:value'")
        
        self.ec2tag = tag_string
        self.ec2tagk, self.ec2tagv = tag_string.split(":", 1)
    
    def has_ec2_tag_filter(self) -> bool:
        """
        Check if EC2 tag filtering is enabled.
        
        Returns:
            True if EC2 tag filtering is configured.
        """
        return self.ec2tag is not None and self.ec2tagk is not None and self.ec2tagv is not None
    
    def get_data_source_flags(self) -> Dict[str, bool]:
        """
        Get all data source flags.
        
        Returns:
            Dictionary of data source flag names and values.
        """
        return {
            'dnet': self.dnet,
            'dkms': self.dkms,
            'dkey': self.dkey,
            'dsgs': self.dsgs
        }
    
    def is_any_data_source_enabled(self) -> bool:
        """
        Check if any data source flags are enabled.
        
        Returns:
            True if any data source flag is enabled.
        """
        return any(self.get_data_source_flags().values())
    
    def get_processing_flags(self) -> Dict[str, bool]:
        """
        Get all processing flags.
        
        Returns:
            Dictionary of processing flag names and values.
        """
        return {
            'elastirep': self.elastirep,
            'elastigrep': self.elastigrep,
            'elasticc': self.elasticc,
            'kinesismsk': self.kinesismsk,
            'destbuck': self.destbuck,
            'asg_azs': self.asg_azs,
            'lbskipaacl': self.lbskipaacl,
            'lbskipcnxl': self.lbskipcnxl,
            'mskcfg': self.mskcfg,
            'repdbin': self.repdbin,
            'gulejobmaxcap': self.gulejobmaxcap,
            'levsmap': self.levsmap,
            'ec2ignore': self.ec2ignore,
            'emrsubnetid': self.emrsubnetid
        }
    
    def get_runtime_mode(self) -> str:
        """
        Get the current runtime mode description.
        
        Returns:
            String describing the runtime mode.
        """
        modes = []
        
        if self.fast:
            modes.append("fast")
        if self.serverless:
            modes.append("serverless")
        if self.merge:
            modes.append("merge")
        if self.apionly:
            modes.append("api-only")
        if self.expected:
            modes.append("expected")
        
        return ", ".join(modes) if modes else "standard"


@dataclass
class ResourceConfig(ConfigCategory):
    """Resource lists and caches configuration."""
    
    # AWS resource response caches
    aws_subnet_resp: List[Dict] = field(default_factory=list)
    aws_route_table_resp: List[Dict] = field(default_factory=list)
    aws_kms_alias_resp: List[Dict] = field(default_factory=list)
    aws_vpc_resp: List[Dict] = field(default_factory=list)
    aws_iam_role_resp: List[Dict] = field(default_factory=list)
    aws_instance_resp: List[Dict] = field(default_factory=list)
    
    # Resource lists
    policies: List[str] = field(default_factory=list)
    policyarns: List[str] = field(default_factory=list)
    roles: List[str] = field(default_factory=list)
    badlist: List[str] = field(default_factory=list)
    
    # Resource dictionaries
    subnets: Dict[str, Any] = field(default_factory=dict)
    vpcs: Dict[str, Any] = field(default_factory=dict)
    subnetlist: Dict[str, bool] = field(default_factory=dict)
    sglist: Dict[str, bool] = field(default_factory=dict)
    vpclist: Dict[str, bool] = field(default_factory=dict)
    lambdalist: Dict[str, bool] = field(default_factory=dict)
    s3list: Dict[str, bool] = field(default_factory=dict)
    rolelist: Dict[str, bool] = field(default_factory=dict)
    policylist: Dict[str, bool] = field(default_factory=dict)
    bucketlist: Dict[str, bool] = field(default_factory=dict)
    tgwlist: Dict[str, bool] = field(default_factory=dict)
    gluedbs: Dict[str, Any] = field(default_factory=dict)
    attached_role_policies_list: Dict[str, Any] = field(default_factory=dict)
    role_policies_list: Dict[str, Any] = field(default_factory=dict)
    
    # Special dictionaries
    mopup: Dict[str, str] = field(default_factory=lambda: {
        "aws_service_discovery_http_namespace": "ns-"
    })
    
    noimport: Dict[str, bool] = field(default_factory=lambda: {
        "aws_iam_user_group_membership": True,
        "aws_iam_security_token_service_preferences": True,
        "aws_ebs_snapshot_copy": True,
        "aws_ebs_snapshot_import": True,
        "aws_vpclattice_target_group_attachment": True
    })
    
    tested: Dict[str, Any] = field(default_factory=dict)
    
    # Various ID fields
    regionl: int = 0
    api_id: str = ""
    stripblock: str = ""
    stripstart: str = ""
    stripend: str = ""
    apigwrestapiid: str = ""
    secid: str = ""
    secvid: str = ""
    meshname: str = ""
    workaround: str = ""
    dzd: str = ""
    dzgid: str = ""
    dzpid: str = ""
    connectinid: str = ""
    waf2id: str = ""
    waf2nm: str = ""
    waf2sc: str = ""
    subnetid: str = ""
    ssmparamn: str = ""
    
    def validate(self) -> List[str]:
        """Validate resource configuration."""
        # Resource configuration is generally always valid
        return []
    
    def add_resource_to_list(self, resource_type: str, resource_id: str) -> None:
        """
        Add a resource to the appropriate resource list.
        
        Args:
            resource_type: Type of resource (vpc, subnet, sg, etc.).
            resource_id: Resource identifier.
        """
        list_map = {
            'vpc': self.vpclist,
            'subnet': self.subnetlist,
            'sg': self.sglist,
            'lambda': self.lambdalist,
            's3': self.s3list,
            'role': self.rolelist,
            'policy': self.policylist,
            'bucket': self.bucketlist,
            'tgw': self.tgwlist
        }
        
        if resource_type in list_map:
            list_map[resource_type][resource_id] = True
    
    def is_resource_in_list(self, resource_type: str, resource_id: str) -> bool:
        """
        Check if a resource is in the appropriate resource list.
        
        Args:
            resource_type: Type of resource.
            resource_id: Resource identifier.
            
        Returns:
            True if resource is in the list.
        """
        list_map = {
            'vpc': self.vpclist,
            'subnet': self.subnetlist,
            'sg': self.sglist,
            'lambda': self.lambdalist,
            's3': self.s3list,
            'role': self.rolelist,
            'policy': self.policylist,
            'bucket': self.bucketlist,
            'tgw': self.tgwlist
        }
        
        if resource_type in list_map:
            return list_map[resource_type].get(resource_id, False)
        return False
    
    def get_resource_count(self, resource_type: str) -> int:
        """
        Get the count of resources in a specific list.
        
        Args:
            resource_type: Type of resource.
            
        Returns:
            Number of resources in the list.
        """
        list_map = {
            'vpc': self.vpclist,
            'subnet': self.subnetlist,
            'sg': self.sglist,
            'lambda': self.lambdalist,
            's3': self.s3list,
            'role': self.rolelist,
            'policy': self.policylist,
            'bucket': self.bucketlist,
            'tgw': self.tgwlist
        }
        
        if resource_type in list_map:
            return len(list_map[resource_type])
        return 0
    
    def get_all_resource_counts(self) -> Dict[str, int]:
        """
        Get counts for all resource types.
        
        Returns:
            Dictionary mapping resource types to counts.
        """
        return {
            'vpc': len(self.vpclist),
            'subnet': len(self.subnetlist),
            'sg': len(self.sglist),
            'lambda': len(self.lambdalist),
            's3': len(self.s3list),
            'role': len(self.rolelist),
            'policy': len(self.policylist),
            'bucket': len(self.bucketlist),
            'tgw': len(self.tgwlist)
        }
    
    def clear_resource_list(self, resource_type: str) -> None:
        """
        Clear a specific resource list.
        
        Args:
            resource_type: Type of resource list to clear.
        """
        list_map = {
            'vpc': self.vpclist,
            'subnet': self.subnetlist,
            'sg': self.sglist,
            'lambda': self.lambdalist,
            's3': self.s3list,
            'role': self.rolelist,
            'policy': self.policylist,
            'bucket': self.bucketlist,
            'tgw': self.tgwlist
        }
        
        if resource_type in list_map:
            list_map[resource_type].clear()
    
    def clear_all_resource_lists(self) -> None:
        """Clear all resource lists."""
        self.vpclist.clear()
        self.subnetlist.clear()
        self.sglist.clear()
        self.lambdalist.clear()
        self.s3list.clear()
        self.rolelist.clear()
        self.policylist.clear()
        self.bucketlist.clear()
        self.tgwlist.clear()
    
    def is_resource_skipped(self, resource_type: str) -> bool:
        """
        Check if a resource type should be skipped for import.
        
        Args:
            resource_type: AWS resource type.
            
        Returns:
            True if resource should be skipped.
        """
        return self.noimport.get(resource_type, False)
    
    def add_bad_resource(self, resource_id: str) -> None:
        """
        Add a resource to the bad list.
        
        Args:
            resource_id: Resource identifier that failed processing.
        """
        if resource_id not in self.badlist:
            self.badlist.append(resource_id)
    
    def is_bad_resource(self, resource_id: str) -> bool:
        """
        Check if a resource is in the bad list.
        
        Args:
            resource_id: Resource identifier.
            
        Returns:
            True if resource is in the bad list.
        """
        return resource_id in self.badlist
    
    def get_cache_stats(self) -> Dict[str, int]:
        """
        Get statistics about cached AWS responses.
        
        Returns:
            Dictionary with cache statistics.
        """
        return {
            'subnets': len(self.aws_subnet_resp),
            'route_tables': len(self.aws_route_table_resp),
            'kms_aliases': len(self.aws_kms_alias_resp),
            'vpcs': len(self.aws_vpc_resp),
            'iam_roles': len(self.aws_iam_role_resp),
            'instances': len(self.aws_instance_resp)
        }