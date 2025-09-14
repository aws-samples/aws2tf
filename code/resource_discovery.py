#!/usr/bin/env python3
"""
Resource Discovery Engine for aws2tf with dependency injection.

This module provides a comprehensive resource discovery system that:
1. Discovers AWS resources based on target type and ID
2. Maps resource dependencies automatically
3. Handles recursive dependency discovery
4. Uses ConfigurationManager for all state management
"""

import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import sys
import json
import time
from typing import Dict, List, Set, Optional, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from .config import ConfigurationManager
from .resources_migrated import resource_types, resource_data, is_resource_type_supported


class DiscoveryStatus(Enum):
    """Status of resource discovery operations."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class ResourceInfo:
    """Information about a discovered AWS resource."""
    resource_type: str
    resource_id: str
    aws_data: Dict[str, Any] = field(default_factory=dict)
    dependencies: Set[str] = field(default_factory=set)
    dependents: Set[str] = field(default_factory=set)
    status: DiscoveryStatus = DiscoveryStatus.PENDING
    error_message: Optional[str] = None
    discovery_time: Optional[float] = None
    
    def __post_init__(self):
        """Ensure sets are properly initialized."""
        if not isinstance(self.dependencies, set):
            self.dependencies = set(self.dependencies) if self.dependencies else set()
        if not isinstance(self.dependents, set):
            self.dependents = set(self.dependents) if self.dependents else set()
    
    @property
    def full_resource_name(self) -> str:
        """Get the full terraform resource name."""
        return f"{self.resource_type}.{self.resource_id}"
    
    def add_dependency(self, dependency: str) -> None:
        """Add a dependency to this resource."""
        self.dependencies.add(dependency)
    
    def add_dependent(self, dependent: str) -> None:
        """Add a dependent to this resource."""
        self.dependents.add(dependent)


class ResourceDependencyMapper:
    """Maps and manages resource dependencies."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.dependency_rules = self._initialize_dependency_rules()
    
    def _initialize_dependency_rules(self) -> Dict[str, Dict[str, List[str]]]:
        """Initialize dependency mapping rules."""
        return {
            # VPC dependencies
            "aws_vpc": {
                "depends_on": [],
                "creates": [
                    "aws_subnet", "aws_security_group", "aws_internet_gateway",
                    "aws_nat_gateway", "aws_route_table", "aws_vpc_endpoint",
                    "aws_network_acl", "aws_vpc_dhcp_options"
                ]
            },
            
            # Subnet dependencies
            "aws_subnet": {
                "depends_on": ["aws_vpc"],
                "creates": [
                    "aws_route_table_association", "aws_network_acl_association",
                    "aws_instance", "aws_nat_gateway"
                ]
            },
            
            # Security Group dependencies
            "aws_security_group": {
                "depends_on": ["aws_vpc"],
                "creates": ["aws_security_group_rule"]
            },
            
            # Internet Gateway dependencies
            "aws_internet_gateway": {
                "depends_on": ["aws_vpc"],
                "creates": ["aws_route"]
            },
            
            # NAT Gateway dependencies
            "aws_nat_gateway": {
                "depends_on": ["aws_subnet", "aws_internet_gateway"],
                "creates": ["aws_route"]
            },
            
            # Route Table dependencies
            "aws_route_table": {
                "depends_on": ["aws_vpc"],
                "creates": ["aws_route", "aws_route_table_association"]
            },
            
            # EC2 Instance dependencies
            "aws_instance": {
                "depends_on": ["aws_subnet", "aws_security_group", "aws_key_pair"],
                "creates": ["aws_eip_association", "aws_volume_attachment"]
            },
            
            # Load Balancer dependencies
            "aws_lb": {
                "depends_on": ["aws_subnet", "aws_security_group"],
                "creates": ["aws_lb_target_group", "aws_lb_listener"]
            },
            
            # RDS dependencies
            "aws_db_instance": {
                "depends_on": ["aws_db_subnet_group", "aws_security_group"],
                "creates": []
            },
            
            # EKS dependencies
            "aws_eks_cluster": {
                "depends_on": ["aws_subnet", "aws_security_group", "aws_iam_role"],
                "creates": ["aws_eks_node_group", "aws_eks_fargate_profile"]
            },
            
            # Lambda dependencies
            "aws_lambda_function": {
                "depends_on": ["aws_iam_role", "aws_subnet", "aws_security_group"],
                "creates": ["aws_lambda_permission", "aws_lambda_event_source_mapping"]
            },
            
            # Add more dependency rules as needed...
        }
    
    def get_dependencies(self, resource_type: str) -> List[str]:
        """Get list of resource types this resource depends on."""
        return self.dependency_rules.get(resource_type, {}).get("depends_on", [])
    
    def get_created_resources(self, resource_type: str) -> List[str]:
        """Get list of resource types this resource can create."""
        return self.dependency_rules.get(resource_type, {}).get("creates", [])
    
    def should_discover_dependency(self, parent_type: str, dependency_type: str) -> bool:
        """Check if a dependency should be automatically discovered."""
        dependencies = self.get_dependencies(parent_type)
        created_resources = self.get_created_resources(parent_type)
        
        return dependency_type in dependencies or dependency_type in created_resources


class ResourceDiscovery:
    """Main resource discovery engine with dependency injection."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.dependency_mapper = ResourceDependencyMapper(config)
        self.discovered_resources: Dict[str, ResourceInfo] = {}
        self.discovery_queue: Set[Tuple[str, str]] = set()  # (resource_type, resource_id)
        self.processing_lock = threading.Lock()
        self.aws_clients: Dict[str, Any] = {}
        
    def _get_aws_client(self, service_name: str):
        """Get or create AWS client for a service."""
        if service_name not in self.aws_clients:
            session = self.config.aws.get_session()
            self.aws_clients[service_name] = session.client(service_name)
        return self.aws_clients[service_name]
    
    def discover_resource(self, resource_type: str, resource_id: str, 
                         recursive: bool = True) -> ResourceInfo:
        """
        Discover a single AWS resource and optionally its dependencies.
        
        Args:
            resource_type: AWS resource type (e.g., 'aws_vpc')
            resource_id: AWS resource ID (e.g., 'vpc-123456')
            recursive: Whether to discover dependencies recursively
            
        Returns:
            ResourceInfo object with discovery results
        """
        full_name = f"{resource_type}.{resource_id}"
        
        if self.config.debug.enabled:
            print(f"Discovering resource: {full_name}")
        
        # Check if already discovered
        if full_name in self.discovered_resources:
            return self.discovered_resources[full_name]
        
        # Create resource info
        resource_info = ResourceInfo(
            resource_type=resource_type,
            resource_id=resource_id,
            status=DiscoveryStatus.IN_PROGRESS
        )
        
        self.discovered_resources[full_name] = resource_info
        
        try:
            start_time = time.time()
            
            # Get AWS API metadata
            clfn, descfn, topkey, key, filterid = resource_data(
                self.config, resource_type, resource_id
            )
            
            if not clfn or not descfn:
                resource_info.status = DiscoveryStatus.SKIPPED
                resource_info.error_message = f"No AWS API metadata for {resource_type}"
                return resource_info
            
            # Discover the resource from AWS
            aws_data = self._discover_aws_resource(
                clfn, descfn, topkey, key, filterid, resource_id
            )
            
            if aws_data:
                resource_info.aws_data = aws_data
                resource_info.status = DiscoveryStatus.COMPLETED
                resource_info.discovery_time = time.time() - start_time
                
                # Mark as processed in configuration
                self.config.mark_resource_processed(full_name)
                
                # Discover dependencies if requested
                if recursive:
                    self._discover_dependencies(resource_info)
                
                if self.config.debug.enabled:
                    print(f"Successfully discovered {full_name} in {resource_info.discovery_time:.3f}s")
            else:
                resource_info.status = DiscoveryStatus.FAILED
                resource_info.error_message = "Resource not found in AWS"
                
        except Exception as e:
            resource_info.status = DiscoveryStatus.FAILED
            resource_info.error_message = str(e)
            
            if self.config.debug.enabled:
                print(f"Error discovering {full_name}: {e}")
        
        return resource_info
    
    def _discover_aws_resource(self, clfn: str, descfn: str, topkey: str, 
                              key: str, filterid: str, resource_id: str) -> Optional[Dict]:
        """Discover resource from AWS API."""
        try:
            client = self._get_aws_client(clfn)
            
            # Build API call parameters
            params = {}
            
            # Handle different filtering strategies
            if filterid and resource_id:
                if filterid == "VpcId" and resource_id.startswith("vpc-"):
                    params["Filters"] = [{"Name": "vpc-id", "Values": [resource_id]}]
                elif filterid == "SubnetId" and resource_id.startswith("subnet-"):
                    params["Filters"] = [{"Name": "subnet-id", "Values": [resource_id]}]
                elif filterid.endswith("Ids"):
                    # Direct ID parameter (e.g., VpcIds, SubnetIds)
                    params[filterid] = [resource_id]
                elif "." not in filterid:
                    # Simple filter
                    params["Filters"] = [{"Name": filterid.lower(), "Values": [resource_id]}]
            
            # Make AWS API call
            describe_method = getattr(client, descfn)
            response = describe_method(**params)
            
            # Extract resource data
            if topkey and topkey in response:
                resources = response[topkey]
                
                if resources:
                    # Find the specific resource if key is provided
                    if key and resource_id:
                        for resource in resources:
                            if resource.get(key) == resource_id:
                                return resource
                    else:
                        # Return first resource if no specific key matching
                        return resources[0] if isinstance(resources, list) else resources
            
            return None
            
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code', 'Unknown')
            if error_code in ['ResourceNotFound', 'InvalidResourceId', 'InvalidVpcID']:
                return None  # Resource doesn't exist
            else:
                raise  # Re-raise other errors
        
        except Exception as e:
            if self.config.debug.enabled:
                print(f"AWS API error in _discover_aws_resource: {e}")
            raise
    
    def _discover_dependencies(self, resource_info: ResourceInfo) -> None:
        """Discover dependencies for a resource."""
        resource_type = resource_info.resource_type
        resource_id = resource_info.resource_id
        
        # Get dependency types for this resource
        dependency_types = self.dependency_mapper.get_dependencies(resource_type)
        created_types = self.dependency_mapper.get_created_resources(resource_type)
        
        # Discover dependencies based on resource data
        if resource_info.aws_data:
            self._discover_dependencies_from_data(
                resource_info, dependency_types + created_types
            )
    
    def _discover_dependencies_from_data(self, resource_info: ResourceInfo, 
                                       dependency_types: List[str]) -> None:
        """Discover dependencies based on AWS resource data."""
        aws_data = resource_info.aws_data
        
        # Common dependency patterns
        dependency_mappings = {
            "VpcId": "aws_vpc",
            "SubnetId": "aws_subnet", 
            "SubnetIds": "aws_subnet",
            "SecurityGroupIds": "aws_security_group",
            "SecurityGroups": "aws_security_group",
            "InternetGatewayId": "aws_internet_gateway",
            "NatGatewayId": "aws_nat_gateway",
            "RouteTableId": "aws_route_table",
            "KeyName": "aws_key_pair",
            "IamInstanceProfile": "aws_iam_instance_profile",
            "Role": "aws_iam_role",
            "RoleArn": "aws_iam_role"
        }
        
        # Extract dependencies from AWS data
        for field, resource_type in dependency_mappings.items():
            if resource_type in dependency_types:
                self._extract_dependency_ids(resource_info, aws_data, field, resource_type)
    
    def _extract_dependency_ids(self, resource_info: ResourceInfo, data: Dict, 
                               field: str, dependency_type: str) -> None:
        """Extract dependency IDs from AWS data."""
        if isinstance(data, dict):
            if field in data:
                value = data[field]
                if isinstance(value, str) and value:
                    # Single ID
                    dependency_name = f"{dependency_type}.{value}"
                    resource_info.add_dependency(dependency_name)
                    self._queue_dependency_discovery(dependency_type, value)
                    
                elif isinstance(value, list):
                    # List of IDs
                    for item in value:
                        if isinstance(item, str) and item:
                            dependency_name = f"{dependency_type}.{item}"
                            resource_info.add_dependency(dependency_name)
                            self._queue_dependency_discovery(dependency_type, item)
                        elif isinstance(item, dict) and 'GroupId' in item:
                            # Security group format
                            group_id = item['GroupId']
                            dependency_name = f"{dependency_type}.{group_id}"
                            resource_info.add_dependency(dependency_name)
                            self._queue_dependency_discovery(dependency_type, group_id)
            
            # Recursively search nested structures
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    self._extract_dependency_ids(resource_info, value, field, dependency_type)
                    
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    self._extract_dependency_ids(resource_info, item, field, dependency_type)
    
    def _queue_dependency_discovery(self, resource_type: str, resource_id: str) -> None:
        """Queue a dependency for discovery."""
        with self.processing_lock:
            self.discovery_queue.add((resource_type, resource_id))
    
    def discover_all_queued(self) -> Dict[str, ResourceInfo]:
        """Discover all queued dependencies."""
        max_iterations = 10  # Prevent infinite loops
        iteration = 0
        
        while self.discovery_queue and iteration < max_iterations:
            iteration += 1
            
            if self.config.debug.enabled:
                print(f"Discovery iteration {iteration}, queue size: {len(self.discovery_queue)}")
            
            # Get current queue and clear it
            with self.processing_lock:
                current_queue = list(self.discovery_queue)
                self.discovery_queue.clear()
            
            # Process queued discoveries
            for resource_type, resource_id in current_queue:
                full_name = f"{resource_type}.{resource_id}"
                
                if full_name not in self.discovered_resources:
                    self.discover_resource(resource_type, resource_id, recursive=True)
        
        if self.discovery_queue:
            print(f"Warning: Discovery queue not empty after {max_iterations} iterations")
        
        return self.discovered_resources
    
    def discover_by_category(self, category: str, target_id: Optional[str] = None) -> Dict[str, ResourceInfo]:
        """
        Discover resources by category (e.g., 'vpc', 'subnet', 'ec2').
        
        Args:
            category: Resource category from resources_migrated.resource_types()
            target_id: Optional specific resource ID to target
            
        Returns:
            Dictionary of discovered resources
        """
        if self.config.debug.enabled:
            print(f"Discovering resources for category: {category}")
        
        # Get resource types for category
        resource_type_list = resource_types(self.config, category)
        
        if not resource_type_list:
            print(f"Warning: No resource types found for category '{category}'")
            return {}
        
        discovered = {}
        
        for resource_type in resource_type_list:
            if target_id:
                # Discover specific resource
                resource_info = self.discover_resource(resource_type, target_id, recursive=True)
                discovered[resource_info.full_resource_name] = resource_info
            else:
                # Discover all resources of this type (implementation depends on AWS API)
                resources = self._discover_all_resources_of_type(resource_type)
                discovered.update(resources)
        
        # Process any queued dependencies
        discovered.update(self.discover_all_queued())
        
        return discovered
    
    def _discover_all_resources_of_type(self, resource_type: str) -> Dict[str, ResourceInfo]:
        """Discover all resources of a specific type."""
        # This would implement listing all resources of a type
        # For now, return empty dict - this would be expanded based on specific needs
        if self.config.debug.enabled:
            print(f"Discovering all resources of type: {resource_type}")
        
        return {}
    
    def get_discovery_summary(self) -> Dict[str, Any]:
        """Get summary of discovery results."""
        summary = {
            "total_resources": len(self.discovered_resources),
            "by_status": {},
            "by_type": {},
            "total_dependencies": 0,
            "discovery_errors": []
        }
        
        for resource_info in self.discovered_resources.values():
            # Count by status
            status = resource_info.status.value
            summary["by_status"][status] = summary["by_status"].get(status, 0) + 1
            
            # Count by type
            resource_type = resource_info.resource_type
            summary["by_type"][resource_type] = summary["by_type"].get(resource_type, 0) + 1
            
            # Count dependencies
            summary["total_dependencies"] += len(resource_info.dependencies)
            
            # Collect errors
            if resource_info.status == DiscoveryStatus.FAILED and resource_info.error_message:
                summary["discovery_errors"].append({
                    "resource": resource_info.full_resource_name,
                    "error": resource_info.error_message
                })
        
        return summary
    
    def validate_dependencies(self) -> List[str]:
        """Validate that all dependencies are satisfied."""
        errors = []
        
        for resource_info in self.discovered_resources.values():
            for dependency in resource_info.dependencies:
                if dependency not in self.discovered_resources:
                    errors.append(f"{resource_info.full_resource_name} depends on {dependency} which was not discovered")
        
        return errors
    
    def get_dependency_graph(self) -> Dict[str, Dict[str, List[str]]]:
        """Get the complete dependency graph."""
        graph = {}
        
        for resource_name, resource_info in self.discovered_resources.items():
            graph[resource_name] = {
                "dependencies": list(resource_info.dependencies),
                "dependents": list(resource_info.dependents)
            }
        
        return graph
    
    def detect_circular_dependencies(self) -> List[List[str]]:
        """Detect circular dependencies in the discovered resources."""
        def dfs(node: str, path: List[str], visited: Set[str]) -> List[List[str]]:
            if node in path:
                # Found a cycle
                cycle_start = path.index(node)
                return [path[cycle_start:] + [node]]
            
            if node in visited:
                return []
            
            visited.add(node)
            path.append(node)
            
            cycles = []
            resource_info = self.discovered_resources.get(node)
            if resource_info:
                for dependency in resource_info.dependencies:
                    cycles.extend(dfs(dependency, path.copy(), visited))
            
            return cycles
        
        all_cycles = []
        visited = set()
        
        for resource_name in self.discovered_resources:
            if resource_name not in visited:
                cycles = dfs(resource_name, [], visited)
                all_cycles.extend(cycles)
        
        return all_cycles


# Utility functions for resource discovery

def create_resource_discovery(config: ConfigurationManager) -> ResourceDiscovery:
    """Factory function to create ResourceDiscovery instance."""
    return ResourceDiscovery(config)


def discover_target_resource(config: ConfigurationManager, target_type: str, 
                           target_id: str) -> Dict[str, ResourceInfo]:
    """
    Convenience function to discover a target resource and its dependencies.
    
    Args:
        config: Configuration manager
        target_type: Target resource type category
        target_id: Target resource ID
        
    Returns:
        Dictionary of discovered resources
    """
    discovery = create_resource_discovery(config)
    
    # Update configuration with discovery progress
    config.set_tracking_message(f"Discovering {target_type} resources for {target_id}")
    
    # Discover by category
    discovered = discovery.discover_by_category(target_type, target_id)
    
    # Validate dependencies
    errors = discovery.validate_dependencies()
    if errors and config.debug.enabled:
        print("Dependency validation errors:")
        for error in errors:
            print(f"  - {error}")
    
    # Check for circular dependencies
    cycles = discovery.detect_circular_dependencies()
    if cycles and config.debug.enabled:
        print("Circular dependencies detected:")
        for cycle in cycles:
            print(f"  - {' -> '.join(cycle)}")
    
    # Update configuration with results
    summary = discovery.get_discovery_summary()
    config.set_tracking_message(
        f"Discovery complete: {summary['total_resources']} resources, "
        f"{summary['total_dependencies']} dependencies"
    )
    
    return discovered