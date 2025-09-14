#!/usr/bin/env python3
"""
Advanced Resource Dependency Mapping and Validation for aws2tf.

This module provides comprehensive dependency mapping, validation, and resolution
for AWS resources with sophisticated circular dependency detection and resolution.
"""

import json
import time
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, field
from enum import Enum
from collections import defaultdict, deque
import threading
from pathlib import Path

from .config import ConfigurationManager


class DependencyType(Enum):
    """Types of dependencies between resources."""
    REQUIRED = "required"          # Must exist before this resource
    OPTIONAL = "optional"          # May exist, but not required
    CREATES = "creates"           # This resource creates the dependency
    REFERENCES = "references"     # This resource references the dependency
    CONTAINS = "contains"         # This resource contains the dependency


class ValidationSeverity(Enum):
    """Severity levels for validation issues."""
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class DependencyRule:
    """Rule defining a dependency relationship between resource types."""
    source_type: str
    target_type: str
    dependency_type: DependencyType
    field_mappings: List[str] = field(default_factory=list)
    conditions: Dict[str, Any] = field(default_factory=dict)
    priority: int = 1
    description: str = ""
    
    def matches_condition(self, resource_data: Dict[str, Any]) -> bool:
        """Check if this rule applies based on conditions."""
        if not self.conditions:
            return True
        
        for field, expected_value in self.conditions.items():
            actual_value = self._get_nested_value(resource_data, field)
            if actual_value != expected_value:
                return False
        
        return True
    
    def _get_nested_value(self, data: Dict[str, Any], field_path: str) -> Any:
        """Get value from nested dictionary using dot notation."""
        keys = field_path.split('.')
        value = data
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        
        return value


@dataclass
class ValidationIssue:
    """Represents a validation issue found during dependency analysis."""
    severity: ValidationSeverity
    resource_name: str
    issue_type: str
    message: str
    suggested_fix: Optional[str] = None
    related_resources: List[str] = field(default_factory=list)


@dataclass
class DependencyPath:
    """Represents a path between two resources in the dependency graph."""
    source: str
    target: str
    path: List[str]
    path_length: int
    dependency_types: List[DependencyType]
    
    def __post_init__(self):
        self.path_length = len(self.path)


class ResourceDependencyMapper:
    """Advanced resource dependency mapper with validation and resolution."""
    
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.dependency_rules: List[DependencyRule] = []
        self.resource_graph: Dict[str, Set[str]] = defaultdict(set)
        self.reverse_graph: Dict[str, Set[str]] = defaultdict(set)
        self.validation_issues: List[ValidationIssue] = []
        self.lock = threading.Lock()
        
        self._initialize_dependency_rules()
    
    def _initialize_dependency_rules(self) -> None:
        """Initialize comprehensive dependency rules for AWS resources."""
        rules = [
            # VPC and Networking Dependencies
            DependencyRule(
                "aws_subnet", "aws_vpc", DependencyType.REQUIRED,
                field_mappings=["VpcId"],
                description="Subnets must belong to a VPC"
            ),
            DependencyRule(
                "aws_security_group", "aws_vpc", DependencyType.REQUIRED,
                field_mappings=["VpcId"],
                description="Security groups must belong to a VPC"
            ),
            DependencyRule(
                "aws_internet_gateway", "aws_vpc", DependencyType.CREATES,
                field_mappings=["Attachments.0.VpcId", ".Attachments.0.VpcId"],
                description="Internet gateways attach to VPCs"
            ),
            DependencyRule(
                "aws_nat_gateway", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["SubnetId"],
                description="NAT gateways must be in a subnet"
            ),
            DependencyRule(
                "aws_nat_gateway", "aws_internet_gateway", DependencyType.REQUIRED,
                field_mappings=["AllocationId"],
                description="NAT gateways require internet gateway for EIP"
            ),
            DependencyRule(
                "aws_route_table", "aws_vpc", DependencyType.REQUIRED,
                field_mappings=["VpcId"],
                description="Route tables belong to VPCs"
            ),
            DependencyRule(
                "aws_route_table_association", "aws_route_table", DependencyType.REQUIRED,
                field_mappings=["RouteTableId", ".Associations.0.RouteTableId"],
                description="Route table associations require route tables"
            ),
            DependencyRule(
                "aws_route_table_association", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["SubnetId", ".Associations.0.SubnetId"],
                description="Route table associations require subnets"
            ),
            DependencyRule(
                "aws_vpc_endpoint", "aws_vpc", DependencyType.REQUIRED,
                field_mappings=["VpcId"],
                description="VPC endpoints belong to VPCs"
            ),
            DependencyRule(
                "aws_network_acl", "aws_vpc", DependencyType.REQUIRED,
                field_mappings=["VpcId"],
                description="Network ACLs belong to VPCs"
            ),
            
            # EC2 Dependencies
            DependencyRule(
                "aws_instance", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["SubnetId"],
                description="EC2 instances must be in a subnet"
            ),
            DependencyRule(
                "aws_instance", "aws_security_group", DependencyType.REQUIRED,
                field_mappings=["SecurityGroups", "SecurityGroupIds"],
                description="EC2 instances require security groups"
            ),
            DependencyRule(
                "aws_instance", "aws_key_pair", DependencyType.OPTIONAL,
                field_mappings=["KeyName"],
                description="EC2 instances may use key pairs"
            ),
            DependencyRule(
                "aws_instance", "aws_iam_instance_profile", DependencyType.OPTIONAL,
                field_mappings=["IamInstanceProfile.Arn"],
                description="EC2 instances may have IAM instance profiles"
            ),
            
            # Load Balancer Dependencies
            DependencyRule(
                "aws_lb", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["Subnets", "SubnetIds"],
                description="Load balancers require subnets"
            ),
            DependencyRule(
                "aws_lb", "aws_security_group", DependencyType.REQUIRED,
                field_mappings=["SecurityGroups"],
                description="Load balancers require security groups"
            ),
            DependencyRule(
                "aws_lb_target_group", "aws_vpc", DependencyType.REQUIRED,
                field_mappings=["VpcId"],
                description="Target groups belong to VPCs"
            ),
            DependencyRule(
                "aws_lb_listener", "aws_lb", DependencyType.REQUIRED,
                field_mappings=["LoadBalancerArn"],
                description="Listeners belong to load balancers"
            ),
            
            # RDS Dependencies
            DependencyRule(
                "aws_db_instance", "aws_db_subnet_group", DependencyType.REQUIRED,
                field_mappings=["DBSubnetGroup"],
                description="RDS instances require DB subnet groups"
            ),
            DependencyRule(
                "aws_db_instance", "aws_security_group", DependencyType.REQUIRED,
                field_mappings=["VpcSecurityGroups"],
                description="RDS instances require security groups"
            ),
            DependencyRule(
                "aws_db_subnet_group", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["Subnets"],
                description="DB subnet groups require subnets"
            ),
            
            # EKS Dependencies
            DependencyRule(
                "aws_eks_cluster", "aws_iam_role", DependencyType.REQUIRED,
                field_mappings=["RoleArn"],
                description="EKS clusters require service roles"
            ),
            DependencyRule(
                "aws_eks_cluster", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["ResourcesVpcConfig.SubnetIds"],
                description="EKS clusters require subnets"
            ),
            DependencyRule(
                "aws_eks_node_group", "aws_eks_cluster", DependencyType.REQUIRED,
                field_mappings=["ClusterName"],
                description="EKS node groups belong to clusters"
            ),
            DependencyRule(
                "aws_eks_node_group", "aws_iam_role", DependencyType.REQUIRED,
                field_mappings=["NodeRole"],
                description="EKS node groups require node roles"
            ),
            
            # Lambda Dependencies
            DependencyRule(
                "aws_lambda_function", "aws_iam_role", DependencyType.REQUIRED,
                field_mappings=["Role"],
                description="Lambda functions require execution roles"
            ),
            DependencyRule(
                "aws_lambda_function", "aws_subnet", DependencyType.OPTIONAL,
                field_mappings=["VpcConfig.SubnetIds"],
                description="Lambda functions may be in VPC subnets"
            ),
            DependencyRule(
                "aws_lambda_function", "aws_security_group", DependencyType.OPTIONAL,
                field_mappings=["VpcConfig.SecurityGroupIds"],
                description="Lambda functions in VPC require security groups"
            ),
            
            # IAM Dependencies
            DependencyRule(
                "aws_iam_role_policy_attachment", "aws_iam_role", DependencyType.REQUIRED,
                field_mappings=["RoleName"],
                description="Policy attachments require roles"
            ),
            DependencyRule(
                "aws_iam_role_policy_attachment", "aws_iam_policy", DependencyType.REQUIRED,
                field_mappings=["PolicyArn"],
                description="Policy attachments require policies"
            ),
            DependencyRule(
                "aws_iam_instance_profile", "aws_iam_role", DependencyType.REQUIRED,
                field_mappings=["Roles"],
                description="Instance profiles require roles"
            ),
            
            # S3 Dependencies
            DependencyRule(
                "aws_s3_bucket_policy", "aws_s3_bucket", DependencyType.REQUIRED,
                field_mappings=["Bucket"],
                description="Bucket policies require buckets"
            ),
            DependencyRule(
                "aws_s3_bucket_notification", "aws_s3_bucket", DependencyType.REQUIRED,
                field_mappings=["Bucket"],
                description="Bucket notifications require buckets"
            ),
            
            # CloudWatch Dependencies
            DependencyRule(
                "aws_cloudwatch_metric_alarm", "aws_sns_topic", DependencyType.OPTIONAL,
                field_mappings=["AlarmActions", "OKActions"],
                description="CloudWatch alarms may reference SNS topics"
            ),
            
            # Auto Scaling Dependencies
            DependencyRule(
                "aws_autoscaling_group", "aws_launch_template", DependencyType.OPTIONAL,
                field_mappings=["LaunchTemplate.Id"],
                description="Auto Scaling groups may use launch templates"
            ),
            DependencyRule(
                "aws_autoscaling_group", "aws_launch_configuration", DependencyType.OPTIONAL,
                field_mappings=["LaunchConfigurationName"],
                description="Auto Scaling groups may use launch configurations"
            ),
            DependencyRule(
                "aws_autoscaling_group", "aws_subnet", DependencyType.REQUIRED,
                field_mappings=["VPCZoneIdentifier"],
                description="Auto Scaling groups require subnets"
            ),
        ]
        
        self.dependency_rules = rules
    
    def add_dependency_rule(self, rule: DependencyRule) -> None:
        """Add a custom dependency rule."""
        with self.lock:
            self.dependency_rules.append(rule)
    
    def get_dependencies_for_resource(self, resource_type: str, 
                                    resource_data: Dict[str, Any]) -> List[Tuple[str, str, DependencyType]]:
        """
        Get all dependencies for a specific resource based on its data.
        
        Returns:
            List of (dependency_type, dependency_id, dependency_relationship) tuples
        """
        dependencies = []
        
        for rule in self.dependency_rules:
            if rule.source_type == resource_type and rule.matches_condition(resource_data):
                # Extract dependency IDs from resource data
                dependency_ids = self._extract_dependency_ids(resource_data, rule.field_mappings)
                
                for dep_id in dependency_ids:
                    if dep_id:
                        dependencies.append((rule.target_type, dep_id, rule.dependency_type))
        
        return dependencies
    
    def _extract_dependency_ids(self, resource_data: Dict[str, Any], 
                               field_mappings: List[str]) -> List[str]:
        """Extract dependency IDs from resource data using field mappings."""
        ids = []
        
        for field_path in field_mappings:
            extracted_ids = self._extract_ids_from_field(resource_data, field_path)
            ids.extend(extracted_ids)
        
        return list(set(ids))  # Remove duplicates
    
    def _extract_ids_from_field(self, data: Any, field_path: str) -> List[str]:
        """Extract IDs from a specific field path."""
        if field_path.startswith('.'):
            # Handle special dot notation for nested searches
            return self._search_nested_field(data, field_path[1:])
        
        value = self._get_nested_value(data, field_path)
        
        if value is None:
            return []
        
        if isinstance(value, str):
            return [value] if value else []
        elif isinstance(value, list):
            result = []
            for item in value:
                if isinstance(item, str):
                    result.append(item)
                elif isinstance(item, dict):
                    # Handle complex objects like security groups
                    if 'GroupId' in item:
                        result.append(item['GroupId'])
                    elif 'Id' in item:
                        result.append(item['Id'])
            return result
        elif isinstance(value, dict):
            # Handle nested objects
            if 'Id' in value:
                return [value['Id']]
            elif 'Arn' in value:
                return [value['Arn']]
        
        return []
    
    def _search_nested_field(self, data: Any, field_path: str) -> List[str]:
        """Search for field in nested structures."""
        results = []
        
        def search_recursive(obj: Any, path: str) -> None:
            if isinstance(obj, dict):
                if path in obj:
                    value = obj[path]
                    if isinstance(value, str) and value:
                        results.append(value)
                    elif isinstance(value, list):
                        results.extend([v for v in value if isinstance(v, str) and v])
                
                # Search nested dictionaries
                for v in obj.values():
                    search_recursive(v, path)
            
            elif isinstance(obj, list):
                for item in obj:
                    search_recursive(item, path)
        
        search_recursive(data, field_path)
        return results
    
    def _get_nested_value(self, data: Any, field_path: str) -> Any:
        """Get value from nested dictionary using dot notation."""
        if not isinstance(data, dict):
            return None
        
        keys = field_path.split('.')
        value = data
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            elif isinstance(value, list) and key.isdigit():
                idx = int(key)
                if 0 <= idx < len(value):
                    value = value[idx]
                else:
                    return None
            else:
                return None
        
        return value
    
    def build_dependency_graph(self, resources: Dict[str, Dict[str, Any]]) -> None:
        """Build the complete dependency graph from discovered resources."""
        with self.lock:
            self.resource_graph.clear()
            self.reverse_graph.clear()
            
            for resource_name, resource_info in resources.items():
                resource_type = resource_info.get('resource_type', '')
                resource_data = resource_info.get('aws_data', {})
                
                # Get dependencies for this resource
                dependencies = self.get_dependencies_for_resource(resource_type, resource_data)
                
                for dep_type, dep_id, dep_relationship in dependencies:
                    dep_name = f"{dep_type}.{dep_id}"
                    
                    # Add to forward graph
                    self.resource_graph[resource_name].add(dep_name)
                    
                    # Add to reverse graph
                    self.reverse_graph[dep_name].add(resource_name)
    
    def validate_dependencies(self, resources: Dict[str, Dict[str, Any]]) -> List[ValidationIssue]:
        """Validate all dependencies and return issues."""
        self.validation_issues.clear()
        
        # Build dependency graph
        self.build_dependency_graph(resources)
        
        # Check for missing dependencies
        self._validate_missing_dependencies(resources)
        
        # Check for circular dependencies
        self._validate_circular_dependencies()
        
        # Check for orphaned resources
        self._validate_orphaned_resources(resources)
        
        # Check for invalid references
        self._validate_invalid_references(resources)
        
        return self.validation_issues
    
    def _validate_missing_dependencies(self, resources: Dict[str, Dict[str, Any]]) -> None:
        """Check for missing required dependencies."""
        for resource_name in self.resource_graph:
            for dependency in self.resource_graph[resource_name]:
                if dependency not in resources:
                    # Find the dependency rule to check if it's required
                    resource_type = resource_name.split('.')[0]
                    dep_type = dependency.split('.')[0]
                    
                    rule = self._find_dependency_rule(resource_type, dep_type)
                    if rule and rule.dependency_type == DependencyType.REQUIRED:
                        self.validation_issues.append(ValidationIssue(
                            severity=ValidationSeverity.ERROR,
                            resource_name=resource_name,
                            issue_type="missing_required_dependency",
                            message=f"Required dependency {dependency} not found",
                            suggested_fix=f"Discover or import {dependency}",
                            related_resources=[dependency]
                        ))
                    elif rule and rule.dependency_type in [DependencyType.OPTIONAL, DependencyType.REFERENCES]:
                        self.validation_issues.append(ValidationIssue(
                            severity=ValidationSeverity.WARNING,
                            resource_name=resource_name,
                            issue_type="missing_optional_dependency",
                            message=f"Optional dependency {dependency} not found",
                            suggested_fix=f"Consider discovering {dependency} if needed",
                            related_resources=[dependency]
                        ))
    
    def _validate_circular_dependencies(self) -> None:
        """Check for circular dependencies."""
        cycles = self.detect_circular_dependencies()
        
        for cycle in cycles:
            cycle_str = " -> ".join(cycle)
            
            self.validation_issues.append(ValidationIssue(
                severity=ValidationSeverity.ERROR,
                resource_name=cycle[0],
                issue_type="circular_dependency",
                message=f"Circular dependency detected: {cycle_str}",
                suggested_fix="Review resource relationships and break the cycle",
                related_resources=cycle
            ))
    
    def _validate_orphaned_resources(self, resources: Dict[str, Dict[str, Any]]) -> None:
        """Check for resources with no dependencies or dependents."""
        for resource_name in resources:
            has_dependencies = resource_name in self.resource_graph and self.resource_graph[resource_name]
            has_dependents = resource_name in self.reverse_graph and self.reverse_graph[resource_name]
            
            if not has_dependencies and not has_dependents:
                self.validation_issues.append(ValidationIssue(
                    severity=ValidationSeverity.INFO,
                    resource_name=resource_name,
                    issue_type="orphaned_resource",
                    message=f"Resource {resource_name} has no dependencies or dependents",
                    suggested_fix="Verify this resource is needed or check for missing relationships"
                ))
    
    def _validate_invalid_references(self, resources: Dict[str, Dict[str, Any]]) -> None:
        """Check for invalid resource references."""
        for resource_name, resource_info in resources.items():
            resource_type = resource_info.get('resource_type', '')
            resource_data = resource_info.get('aws_data', {})
            
            # Check if resource data contains references to non-existent resources
            self._check_resource_references(resource_name, resource_data, resources)
    
    def _check_resource_references(self, resource_name: str, resource_data: Dict[str, Any], 
                                 all_resources: Dict[str, Dict[str, Any]]) -> None:
        """Check for invalid references in resource data."""
        # This is a simplified check - could be expanded based on specific AWS resource patterns
        common_id_patterns = {
            'vpc-': 'aws_vpc',
            'subnet-': 'aws_subnet',
            'sg-': 'aws_security_group',
            'igw-': 'aws_internet_gateway',
            'nat-': 'aws_nat_gateway',
            'rtb-': 'aws_route_table',
            'i-': 'aws_instance'
        }
        
        def check_value(value: Any, path: str = "") -> None:
            if isinstance(value, str):
                for prefix, resource_type in common_id_patterns.items():
                    if value.startswith(prefix):
                        expected_name = f"{resource_type}.{value}"
                        if expected_name not in all_resources:
                            self.validation_issues.append(ValidationIssue(
                                severity=ValidationSeverity.WARNING,
                                resource_name=resource_name,
                                issue_type="invalid_reference",
                                message=f"References {expected_name} which is not discovered",
                                suggested_fix=f"Discover {expected_name} or verify the reference",
                                related_resources=[expected_name]
                            ))
            elif isinstance(value, dict):
                for k, v in value.items():
                    check_value(v, f"{path}.{k}" if path else k)
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    check_value(item, f"{path}[{i}]" if path else f"[{i}]")
        
        check_value(resource_data)
    
    def _find_dependency_rule(self, source_type: str, target_type: str) -> Optional[DependencyRule]:
        """Find a dependency rule for the given resource types."""
        for rule in self.dependency_rules:
            if rule.source_type == source_type and rule.target_type == target_type:
                return rule
        return None
    
    def detect_circular_dependencies(self) -> List[List[str]]:
        """Detect circular dependencies using DFS."""
        def dfs(node: str, path: List[str], visited: Set[str], rec_stack: Set[str]) -> List[List[str]]:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            cycles = []
            
            for neighbor in self.resource_graph.get(node, set()):
                if neighbor in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
                elif neighbor not in visited:
                    cycles.extend(dfs(neighbor, path.copy(), visited, rec_stack))
            
            rec_stack.remove(node)
            return cycles
        
        all_cycles = []
        visited = set()
        
        for node in self.resource_graph:
            if node not in visited:
                cycles = dfs(node, [], visited, set())
                all_cycles.extend(cycles)
        
        return all_cycles
    
    def get_dependency_order(self) -> List[str]:
        """Get topological order for resource creation (resolves dependencies)."""
        # Kahn's algorithm for topological sorting
        in_degree = defaultdict(int)
        
        # Calculate in-degrees
        for node in self.resource_graph:
            for neighbor in self.resource_graph[node]:
                in_degree[neighbor] += 1
        
        # Initialize queue with nodes having no dependencies
        queue = deque([node for node in self.resource_graph if in_degree[node] == 0])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Remove this node and update in-degrees
            for neighbor in self.resource_graph.get(node, set()):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
    
    def find_dependency_path(self, source: str, target: str) -> Optional[DependencyPath]:
        """Find the shortest dependency path between two resources."""
        if source == target:
            return DependencyPath(source, target, [source], 0, [])
        
        queue = deque([(source, [source], [])])
        visited = {source}
        
        while queue:
            current, path, dep_types = queue.popleft()
            
            for neighbor in self.resource_graph.get(current, set()):
                if neighbor == target:
                    # Found target
                    final_path = path + [neighbor]
                    rule = self._find_dependency_rule(
                        current.split('.')[0], 
                        neighbor.split('.')[0]
                    )
                    final_dep_types = dep_types + ([rule.dependency_type] if rule else [DependencyType.REFERENCES])
                    
                    return DependencyPath(
                        source, target, final_path, 
                        len(final_path) - 1, final_dep_types
                    )
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    rule = self._find_dependency_rule(
                        current.split('.')[0], 
                        neighbor.split('.')[0]
                    )
                    new_dep_types = dep_types + ([rule.dependency_type] if rule else [DependencyType.REFERENCES])
                    queue.append((neighbor, new_path, new_dep_types))
        
        return None
    
    def get_dependency_statistics(self) -> Dict[str, Any]:
        """Get statistics about the dependency graph."""
        total_resources = len(self.resource_graph)
        total_dependencies = sum(len(deps) for deps in self.resource_graph.values())
        
        # Count by dependency type
        type_counts = defaultdict(int)
        for resource_name in self.resource_graph:
            resource_type = resource_name.split('.')[0]
            type_counts[resource_type] += 1
        
        # Find resources with most dependencies
        most_dependencies = sorted(
            [(name, len(deps)) for name, deps in self.resource_graph.items()],
            key=lambda x: x[1], reverse=True
        )[:5]
        
        # Find most referenced resources
        most_referenced = sorted(
            [(name, len(refs)) for name, refs in self.reverse_graph.items()],
            key=lambda x: x[1], reverse=True
        )[:5]
        
        return {
            "total_resources": total_resources,
            "total_dependencies": total_dependencies,
            "average_dependencies": total_dependencies / total_resources if total_resources > 0 else 0,
            "resource_type_counts": dict(type_counts),
            "most_dependencies": most_dependencies,
            "most_referenced": most_referenced,
            "validation_issues": len(self.validation_issues),
            "circular_dependencies": len(self.detect_circular_dependencies())
        }
    
    def export_dependency_graph(self, format_type: str = "json") -> str:
        """Export dependency graph in various formats."""
        if format_type == "json":
            graph_data = {
                "nodes": list(self.resource_graph.keys()),
                "edges": [
                    {"source": source, "target": target}
                    for source, targets in self.resource_graph.items()
                    for target in targets
                ]
            }
            return json.dumps(graph_data, indent=2)
        
        elif format_type == "dot":
            # Graphviz DOT format
            lines = ["digraph dependencies {"]
            lines.append("  rankdir=TB;")
            lines.append("  node [shape=box];")
            
            for source, targets in self.resource_graph.items():
                for target in targets:
                    lines.append(f'  "{source}" -> "{target}";')
            
            lines.append("}")
            return "\n".join(lines)
        
        else:
            raise ValueError(f"Unsupported format: {format_type}")


def create_dependency_mapper(config: ConfigurationManager) -> ResourceDependencyMapper:
    """Factory function to create ResourceDependencyMapper."""
    return ResourceDependencyMapper(config)


def validate_resource_dependencies(config: ConfigurationManager, 
                                 resources: Dict[str, Dict[str, Any]]) -> List[ValidationIssue]:
    """
    Convenience function to validate resource dependencies.
    
    Args:
        config: Configuration manager
        resources: Dictionary of discovered resources
        
    Returns:
        List of validation issues
    """
    mapper = create_dependency_mapper(config)
    return mapper.validate_dependencies(resources)