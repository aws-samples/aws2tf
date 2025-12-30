"""
Handler registry for AWS resource transformations.

This module provides a centralized registry for resource handlers,
allowing dynamic lookup of custom handlers while providing a default
for resources without special logic.
"""

import logging
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')


class HandlerRegistry:
    """
    Registry for resource transformation handlers.
    
    The registry maintains a mapping of resource names to their handler functions.
    Resources without custom handlers automatically use the default handler.
    
    Usage:
        # In fixtf_ec2.py:
        from handler_registry import registry
        
        def aws_instance(t1, tt1, tt2, flag1, flag2):
            # Custom logic here
            return skip, t1, flag1, flag2
        
        registry.register('aws_instance', aws_instance)
        
        # In calling code:
        handler = registry.get_handler('aws_instance')
        skip, t1, flag1, flag2 = handler(t1, tt1, tt2, flag1, flag2)
    """
    
    def __init__(self):
        """Initialize the registry with empty handlers dict."""
        self.handlers = {}
        self.default_handler = BaseResourceHandler.default_handler
        self._stats = {
            'custom_handlers': 0,
            'default_calls': 0,
            'custom_calls': 0
        }
    
    def register(self, resource_name, handler_func):
        """
        Register a custom handler for a resource.
        
        Args:
            resource_name: AWS resource name (e.g., 'aws_instance')
            handler_func: Function with signature (t1, tt1, tt2, flag1, flag2)
        
        Example:
            registry.register('aws_instance', aws_instance)
        """
        if resource_name in self.handlers:
            log.warning(f"Overwriting existing handler for {resource_name}")
        
        self.handlers[resource_name] = handler_func
        self._stats['custom_handlers'] = len(self.handlers)
        log.debug(f"Registered custom handler for {resource_name}")
    
    def register_multiple(self, handlers_dict):
        """
        Register multiple handlers at once.
        
        Args:
            handlers_dict: Dictionary mapping resource names to handler functions
            
        Example:
            registry.register_multiple({
                'aws_instance': aws_instance,
                'aws_security_group': aws_security_group,
            })
        """
        for resource_name, handler_func in handlers_dict.items():
            self.register(resource_name, handler_func)
    
    def get_handler(self, resource_name):
        """
        Get handler for a resource.
        
        Returns custom handler if registered, otherwise returns default handler.
        
        Args:
            resource_name: AWS resource name (e.g., 'aws_instance')
            
        Returns:
            Handler function
        """
        if resource_name in self.handlers:
            self._stats['custom_calls'] += 1
            return self.handlers[resource_name]
        else:
            self._stats['default_calls'] += 1
            return self.default_handler
    
    def has_custom_handler(self, resource_name):
        """
        Check if a resource has a custom handler registered.
        
        Args:
            resource_name: AWS resource name
            
        Returns:
            bool: True if custom handler exists
        """
        return resource_name in self.handlers
    
    def list_custom_handlers(self):
        """
        Get list of all resources with custom handlers.
        
        Returns:
            List of resource names with custom handlers
        """
        return sorted(self.handlers.keys())
    
    def get_stats(self):
        """
        Get registry usage statistics.
        
        Returns:
            dict: Statistics about handler usage
        """
        return {
            'custom_handlers_registered': self._stats['custom_handlers'],
            'custom_handler_calls': self._stats['custom_calls'],
            'default_handler_calls': self._stats['default_calls'],
            'total_calls': self._stats['custom_calls'] + self._stats['default_calls']
        }
    
    def print_stats(self):
        """Print registry usage statistics."""
        stats = self.get_stats()
        print(f"Handler Registry Statistics:")
        print(f"  Custom handlers registered: {stats['custom_handlers_registered']}")
        print(f"  Custom handler calls: {stats['custom_handler_calls']}")
        print(f"  Default handler calls: {stats['default_handler_calls']}")
        print(f"  Total calls: {stats['total_calls']}")
        if stats['total_calls'] > 0:
            custom_pct = stats['custom_handler_calls'] / stats['total_calls'] * 100
            print(f"  Custom handler usage: {custom_pct:.1f}%")
    
    def unregister(self, resource_name):
        """
        Remove a custom handler from the registry.
        
        Args:
            resource_name: AWS resource name to unregister
        """
        if resource_name in self.handlers:
            del self.handlers[resource_name]
            self._stats['custom_handlers'] = len(self.handlers)
            log.debug(f"Unregistered handler for {resource_name}")
    
    def clear(self):
        """Clear all registered handlers."""
        self.handlers.clear()
        self._stats['custom_handlers'] = 0
        log.debug("Cleared all registered handlers")


# Global registry instance
# Import this in fixtf_*.py files to register handlers
registry = HandlerRegistry()


# Convenience function for getting handlers
def get_handler(resource_name):
    """
    Convenience function to get a handler from the global registry.
    
    Args:
        resource_name: AWS resource name
        
    Returns:
        Handler function
    """
    return registry.get_handler(resource_name)
