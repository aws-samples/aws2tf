"""
Base handler for AWS resource transformations.

This module provides common utilities and patterns used across all fixtf_*.py files
to reduce code duplication and standardize resource handling.
"""

import common
import fixtf
import logging
import context

log = logging.getLogger('aws2tf')


class BaseResourceHandler:
    """
    Base class providing common resource transformation utilities.
    
    All handler functions follow the signature:
        handler(t1, tt1, tt2, flag1, flag2) -> (skip, t1, flag1, flag2)
    
    Where:
        t1: Current line being processed
        tt1: Terraform attribute name
        tt2: Terraform attribute value
        flag1: General purpose flag (usage varies by resource)
        flag2: General purpose flag (usage varies by resource)
        skip: 1 to skip this line, 0 to include it
    """
    
    @staticmethod
    def default_handler(t1, tt1, tt2, flag1, flag2):
        """
        Default handler for resources with no custom logic.
        Simply returns skip=0 to include all attributes.
        
        This replaces 86% of boilerplate functions that just do:
            skip=0
            return skip,t1,flag1,flag2
        """
        skip = 0
        return skip, t1, flag1, flag2
    
    @staticmethod
    def skip_if_zero(t1, tt1, tt2, flag1, flag2, fields):
        """
        Skip attribute if its value is "0".
        
        Args:
            fields: List of field names to check
            
        Example:
            skip, t1, flag1, flag2 = BaseResourceHandler.skip_if_zero(
                t1, tt1, tt2, flag1, flag2, 
                ['throughput', 'max_entries', 'days']
            )
        """
        skip = 0
        if tt1 in fields and tt2 == "0":
            skip = 1
        return skip, t1, flag1, flag2
    
    @staticmethod
    def skip_if_empty_array(t1, tt1, tt2, flag1, flag2, fields):
        """
        Skip attribute if its value is "[]" (empty array).
        
        Args:
            fields: List of field names to check
            
        Example:
            skip, t1, flag1, flag2 = BaseResourceHandler.skip_if_empty_array(
                t1, tt1, tt2, flag1, flag2,
                ['security_group_names', 'ipv6_addresses']
            )
        """
        skip = 0
        if tt1 in fields and tt2 == "[]":
            skip = 1
        return skip, t1, flag1, flag2
    
    @staticmethod
    def skip_if_null(t1, tt1, tt2, flag1, flag2, fields):
        """
        Skip attribute if its value is "null".
        
        Args:
            fields: List of field names to check
        """
        skip = 0
        if tt1 in fields and tt2 == "null":
            skip = 1
        return skip, t1, flag1, flag2
    
    @staticmethod
    def skip_if_false(t1, tt1, tt2, flag1, flag2, fields):
        """
        Skip attribute if its value is "false".
        
        Args:
            fields: List of field names to check
        """
        skip = 0
        if tt1 in fields and tt2 == "false":
            skip = 1
        return skip, t1, flag1, flag2
    
    @staticmethod
    def add_resource_reference(t1, tt1, tt2, resource_type, id_field="id"):
        """
        Create a reference to another Terraform resource.
        
        Args:
            resource_type: The AWS resource type (e.g., "ec2_transit_gateway")
            id_field: The field to reference (default: "id")
            
        Example:
            t1 = BaseResourceHandler.add_resource_reference(
                t1, tt1, tt2, "ec2_transit_gateway", "id"
            )
            # Generates: transit_gateway_id = aws_ec2_transit_gateway.tgw-123.id
        """
        t1 = f'{tt1} = aws_{resource_type}.{tt2}.{id_field}\n'
        common.add_dependancy(f"aws_{resource_type}", tt2)
        return t1
    
    @staticmethod
    def add_lifecycle_ignore(t1, fields):
        """
        Add lifecycle ignore_changes block.
        
        Args:
            fields: List of field names to ignore
            
        Example:
            t1 = BaseResourceHandler.add_lifecycle_ignore(
                t1, ['user_data', 'user_data_base64']
            )
        """
        fields_str = ','.join(fields)
        t1 = t1 + f"\n lifecycle {{\n   ignore_changes = [{fields_str}]\n}}\n"
        return t1
    
    @staticmethod
    def handle_arn_reference(t1, tt1, tt2, resource_type):
        """
        Handle ARN-based resource references.
        
        Extracts resource ID from ARN and creates Terraform reference.
        """
        if "arn:aws:" in tt2:
            resource_id = tt2.split(":")[-1]
            t1 = f'{tt1} = aws_{resource_type}.{resource_id}.arn\n'
            common.add_dependancy(f"aws_{resource_type}", resource_id)
        return t1
    
    @staticmethod
    def sanitize_resource_name(name):
        """
        Sanitize resource name for use in Terraform identifiers.
        
        Replaces special characters with underscores.
        """
        return name.replace("/", "_").replace(".", "_").replace(":", "_") \
                   .replace("|", "_").replace("$", "_").replace(",", "_") \
                   .replace("&", "_").replace("#", "_").replace("[", "_") \
                   .replace("]", "_").replace("=", "_").replace("!", "_") \
                   .replace(";", "_")
    
    @staticmethod
    def handle_name_prefix(t1, tt1, tt2, flag1, flag2):
        """
        Handle name_prefix attribute - skip if name is already set.
        
        Common pattern: if name is set (flag1=True), skip name_prefix
        """
        skip = 0
        if tt1 == "name_prefix" and flag1 is True:
            skip = 1
        return skip, t1, flag1, flag2
    
    @staticmethod
    def handle_array_block(t1, tt1, tt2, flag1, flag2, block_name):
        """
        Handle array blocks (ingress, egress, etc.) that span multiple lines.
        
        Uses context.lbc (line bracket counter) to track nested brackets.
        """
        skip = 0
        
        if tt1 == block_name or context.lbc > 0:
            if tt2 == "[]":
                skip = 1
            if "[" in t1:
                context.lbc = context.lbc + 1
            if "]" in t1:
                context.lbc = context.lbc - 1
            
            if context.lbc > 0:
                skip = 1
            if context.lbc == 0:
                if "]" in t1.strip():
                    skip = 1
        
        return skip, t1, flag1, flag2


# Convenience functions for common patterns
def skip_zero_fields(fields):
    """Decorator to skip fields with zero values"""
    def handler(t1, tt1, tt2, flag1, flag2):
        return BaseResourceHandler.skip_if_zero(t1, tt1, tt2, flag1, flag2, fields)
    return handler


def skip_empty_arrays(fields):
    """Decorator to skip fields with empty arrays"""
    def handler(t1, tt1, tt2, flag1, flag2):
        return BaseResourceHandler.skip_if_empty_array(t1, tt1, tt2, flag1, flag2, fields)
    return handler


def skip_null_fields(fields):
    """Decorator to skip fields with null values"""
    def handler(t1, tt1, tt2, flag1, flag2):
        return BaseResourceHandler.skip_if_null(t1, tt1, tt2, flag1, flag2, fields)
    return handler
