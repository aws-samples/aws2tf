# New Optimization Approach - Backward Compatible

## Problem with Previous Approach

The previous refactoring removed boilerplate functions entirely, but the calling code uses `getattr(module, function_name)` which requires functions to exist as module attributes. Removing functions broke the application.

## New Approach: Keep Functions, Reduce Duplication

Instead of removing functions, we'll:
1. Keep ALL function definitions (for backward compatibility)
2. Make boilerplate functions delegate to base handler
3. Extract common logic into utilities
4. Reduce code through delegation, not removal

## Implementation Strategy

### Option 1: Delegation Pattern (Recommended)

Keep all functions but make simple ones delegate to base handler:

**Before:**
```python
def aws_ami(t1, tt1, tt2, flag1, flag2):
    skip = 0
    return skip, t1, flag1, flag2

def aws_ami_copy(t1, tt1, tt2, flag1, flag2):
    skip = 0
    return skip, t1, flag1, flag2

# ... 100+ more identical functions
```

**After:**
```python
from base_handler import BaseResourceHandler

# Simple resources delegate to base handler
def aws_ami(t1, tt1, tt2, flag1, flag2):
    return BaseResourceHandler.default_handler(t1, tt1, tt2, flag1, flag2)

def aws_ami_copy(t1, tt1, tt2, flag1, flag2):
    return BaseResourceHandler.default_handler(t1, tt1, tt2, flag1, flag2)

# Or even simpler with lambda:
aws_ami = lambda t1, tt1, tt2, flag1, flag2: BaseResourceHandler.default_handler(t1, tt1, tt2, flag1, flag2)
aws_ami_copy = lambda t1, tt1, tt2, flag1, flag2: BaseResourceHandler.default_handler(t1, tt1, tt2, flag1, flag2)

# Custom logic functions stay as-is
def aws_instance(t1, tt1, tt2, flag1, flag2):
    skip = 0
    # Custom logic here
    return skip, t1, flag1, flag2
```

**Benefits:**
- ✅ All functions still exist (backward compatible)
- ✅ Boilerplate reduced to one-liners
- ✅ Clear which functions have custom logic
- ✅ No changes to calling code needed
- ✅ ~70% code reduction (not 86%, but safer)

### Option 2: Module __getattr__ Magic Method

Use Python's `__getattr__` to dynamically provide functions:

```python
# At end of fixtf_ec2.py

def __getattr__(name):
    """
    Dynamically provide handler functions for resources without explicit definitions.
    
    This allows the module to respond to getattr(module, 'aws_ami') even if
    aws_ami function doesn't exist, by returning the default handler.
    """
    if name.startswith('aws_'):
        # Return default handler for any aws_* function not explicitly defined
        return BaseResourceHandler.default_handler
    raise AttributeError(f"module has no attribute '{name}'")
```

**Benefits:**
- ✅ Can remove boilerplate functions entirely
- ✅ Backward compatible with getattr()
- ✅ 86% code reduction achieved
- ✅ No changes to calling code needed
- ⚠️ Slightly more "magic" (less explicit)

### Option 3: Hybrid Approach

Combine both approaches:

```python
# Use __getattr__ for truly simple resources
def __getattr__(name):
    if name.startswith('aws_'):
        return BaseResourceHandler.default_handler
    raise AttributeError(f"module has no attribute '{name}'")

# Keep explicit functions for resources with ANY logic
def aws_instance(t1, tt1, tt2, flag1, flag2):
    # Custom logic
    pass

def aws_launch_template(t1, tt1, tt2, flag1, flag2):
    # Uses base handler utilities
    return BaseResourceHandler.skip_if_zero(t1, tt1, tt2, flag1, flag2, ['throughput'])
```

## Recommended: Option 2 (__getattr__)

This is the cleanest approach that achieves maximum code reduction while maintaining backward compatibility.

### Implementation Steps

1. **Add __getattr__ to each fixtf_*.py file**
2. **Keep only functions with custom logic**
3. **Test thoroughly**
4. **No changes to calling code needed**

### Example: fixtf_ec2.py Refactored

```python
"""
EC2 Resource Handlers

This file contains EC2 resources with custom transformation logic.
All other EC2 resources automatically use the default handler via __getattr__.
"""

import common
import fixtf
import logging
import base64
import boto3
import context
import inspect
from .base_handler import BaseResourceHandler

log = logging.getLogger('aws2tf')

# Only define functions with custom logic (24 functions)

def aws_instance(t1, tt1, tt2, flag1, flag2):
    skip = 0
    # Custom logic...
    return skip, t1, flag1, flag2

def aws_vpc(t1, tt1, tt2, skipipv6, flag2):
    skip = 0
    # Custom logic...
    return skip, t1, skipipv6, flag2

# ... 22 more custom functions

# Magic method to provide default handler for all other resources
def __getattr__(name):
    """
    Dynamically provide default handler for resources without custom logic.
    
    This allows getattr(module, 'aws_ami') to work even though aws_ami
    function doesn't exist, by returning the default handler.
    """
    if name.startswith('aws_'):
        return BaseResourceHandler.default_handler
    raise AttributeError(f"module 'fixtf_ec2' has no attribute '{name}'")
```

### Benefits of __getattr__ Approach

1. **Maximum code reduction**: 86% (remove all boilerplate)
2. **Backward compatible**: getattr() still works
3. **No calling code changes**: Works with existing code
4. **Clear intent**: Only custom logic functions visible
5. **Easy maintenance**: Add function only if custom logic needed
6. **Safe**: Falls back to default for unknown resources

### Testing Strategy

1. Test that getattr() works for simple resources
2. Test that custom functions work correctly
3. Test with actual application (./aws2tf.py -t vpc)
4. Verify output matches original code

## Next Steps

1. Implement __getattr__ in base_handler.py as a utility
2. Update migration script to add __getattr__ to each file
3. Re-run migration
4. Test thoroughly
5. Deploy

This approach achieves the same 86% code reduction while maintaining full backward compatibility!
