# fixtf_aws_resources - Resource Handler System

## Overview

This directory contains resource-specific transformation handlers for converting AWS resources to Terraform format. The system uses a **handler registry pattern** to eliminate code duplication while maintaining clear file organization.

## Architecture

### Core Components

1. **base_handler.py** - Common utilities and base handler class
2. **handler_registry.py** - Central registry for resource handlers
3. **fixtf_*.py files** - Service-specific handler implementations (201 files)
4. **aws_dict.py** - Resource metadata (boto3 client, API methods, keys)
5. **aws_not_implemented.py** - Resources not yet implemented

### Handler Function Signature

All handler functions follow this signature:

```python
def aws_resource_name(t1, tt1, tt2, flag1, flag2):
    skip = 0
    # Custom logic here
    return skip, t1, flag1, flag2
```

**Parameters:**
- `t1`: Current line being processed (string)
- `tt1`: Terraform attribute name (string)
- `tt2`: Terraform attribute value (string)
- `flag1`: General purpose flag (varies by resource)
- `flag2`: General purpose flag (varies by resource)

**Returns:**
- `skip`: 1 to skip this line, 0 to include it
- `t1`: Modified line (if changed)
- `flag1`: Updated flag1
- `flag2`: Updated flag2

## How It Works

### Default Behavior (86% of resources)

Most resources (1,241 out of 1,443) have no custom logic and simply return `skip=0`. These automatically use the **default handler**:

```python
# No need to define this function anymore!
# def aws_ami(t1, tt1, tt2, flag1, flag2):
#     skip = 0
#     return skip, t1, flag1, flag2
```

The registry automatically provides the default handler for any resource without custom logic.

### Custom Handlers (14% of resources)

Resources with special logic are registered in their respective fixtf_*.py files:

```python
# In fixtf_ec2.py
from handler_registry import registry

def aws_instance(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Custom logic for EC2 instances
    if tt1 == "user_data":
        # Special handling for user data
        pass
    elif tt1 == "iam_instance_profile":
        # Reference IAM instance profile
        t1 = BaseResourceHandler.add_resource_reference(
            t1, tt1, tt2, "iam_instance_profile", "name"
        )
    
    return skip, t1, flag1, flag2

# Register the custom handler
registry.register('aws_instance', aws_instance)
```

### Using the Registry

In the calling code (e.g., `fixtf.py`):

```python
from handler_registry import registry

# Get handler for any resource
handler = registry.get_handler('aws_instance')  # Returns custom handler
handler = registry.get_handler('aws_ami')       # Returns default handler

# Call the handler
skip, t1, flag1, flag2 = handler(t1, tt1, tt2, flag1, flag2)
```

## Common Patterns

### 1. Skip Zero Values

```python
from base_handler import BaseResourceHandler

def aws_launch_template(t1, tt1, tt2, flag1, flag2):
    skip, t1, flag1, flag2 = BaseResourceHandler.skip_if_zero(
        t1, tt1, tt2, flag1, flag2,
        ['throughput', 'http_put_response_hop_limit']
    )
    return skip, t1, flag1, flag2
```

### 2. Skip Empty Arrays

```python
def aws_vpc_endpoint_service(t1, tt1, tt2, flag1, flag2):
    skip, t1, flag1, flag2 = BaseResourceHandler.skip_if_empty_array(
        t1, tt1, tt2, flag1, flag2,
        ['gateway_load_balancer_arns', 'network_load_balancer_arns']
    )
    return skip, t1, flag1, flag2
```

### 3. Add Resource References

```python
def aws_route_table(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    if tt1 == "nat_gateway_id" and tt2.startswith("nat-"):
        t1 = BaseResourceHandler.add_resource_reference(
            t1, tt1, tt2, "nat_gateway", "id"
        )
    elif tt1 == "gateway_id" and tt2.startswith("igw-"):
        t1 = BaseResourceHandler.add_resource_reference(
            t1, tt1, tt2, "internet_gateway", "id"
        )
    
    return skip, t1, flag1, flag2
```

### 4. Add Lifecycle Blocks

```python
def aws_lambda_function(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    if tt1 == "user_data":
        # Process user data
        t1 = BaseResourceHandler.add_lifecycle_ignore(
            t1, ['user_data', 'user_data_base64', 'source_code_hash']
        )
    
    return skip, t1, flag1, flag2
```

## File Organization

### Service-Specific Files

Each AWS service has its own file:

- `fixtf_ec2.py` - EC2, VPC, networking resources
- `fixtf_s3.py` - S3 bucket and object resources
- `fixtf_lambda.py` - Lambda function resources
- `fixtf_rds.py` - RDS database resources
- `fixtf_iam.py` - IAM roles, policies, users
- ... (201 files total)

### Why Separate Files?

1. **Easier to find**: All EC2 handlers in one place
2. **Easier to maintain**: Changes to EC2 logic don't affect S3
3. **Easier to understand**: Each file focuses on one service
4. **Easier to test**: Can test service handlers independently
5. **Easier to contribute**: Contributors can focus on specific services

## Adding New Resources

### Resource with No Custom Logic

**No code needed!** The default handler automatically handles it.

Just ensure the resource is in `aws_dict.py`:

```python
aws_new_resource = {
    "clfn": "ec2",
    "descfn": "describe_new_resources",
    "topkey": "NewResources",
    "key": "ResourceId",
    "filterid": "ResourceId"
}
```

### Resource with Custom Logic

1. Add to appropriate `fixtf_*.py` file:

```python
def aws_new_resource(t1, tt1, tt2, flag1, flag2):
    skip = 0
    
    # Your custom logic here
    if tt1 == "special_field":
        # Handle special field
        pass
    
    return skip, t1, flag1, flag2

# Register it
registry.register('aws_new_resource', aws_new_resource)
```

2. Add to `aws_dict.py` with boto3 mappings

3. Done!

## Migration Guide

### Before (Old Pattern)

```python
# fixtf_ec2.py - 500+ lines of boilerplate

def aws_ami(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

def aws_ami_copy(t1,tt1,tt2,flag1,flag2):
    skip=0
    return skip,t1,flag1,flag2

# ... 50 more identical functions

def aws_instance(t1,tt1,tt2,flag1,flag2):
    skip=0
    # Actual custom logic
    if tt1 == "user_data":
        # ...
    return skip,t1,flag1,flag2
```

### After (New Pattern)

```python
# fixtf_ec2.py - Only ~50 lines for custom logic

from handler_registry import registry
from base_handler import BaseResourceHandler

# Only define functions with custom logic
def aws_instance(t1, tt1, tt2, flag1, flag2):
    skip = 0
    # Actual custom logic
    if tt1 == "user_data":
        # ...
    return skip, t1, flag1, flag2

def aws_security_group(t1, tt1, tt2, flag1, flag2):
    skip = 0
    # Custom logic for security groups
    return skip, t1, flag1, flag2

# Register only the custom handlers
registry.register('aws_instance', aws_instance)
registry.register('aws_security_group', aws_security_group)

# All other EC2 resources (aws_ami, aws_ami_copy, etc.) 
# automatically use the default handler - no code needed!
```

## Benefits

### Code Reduction
- **Before**: 1,443 function definitions (~40,000 lines)
- **After**: ~200 function definitions (~5,000 lines)
- **Reduction**: 86% less code

### Maintenance
- Only maintain functions with actual logic
- Clear which resources have special handling
- Easy to add new resources (no boilerplate needed)

### Consistency
- All simple resources handled identically
- Common patterns centralized in base_handler
- Reduced chance of copy-paste errors

### Performance
- No performance impact (same function calls)
- Slightly faster for default handlers (no function overhead)

## Statistics

Current state (after optimization):
- **Total resources**: 1,612
- **Resources with custom handlers**: ~200 (14%)
- **Resources using default handler**: ~1,412 (86%)
- **Code reduction**: ~35,000 lines eliminated

## Testing

To verify a handler works correctly:

```python
from handler_registry import registry

# Get handler
handler = registry.get_handler('aws_instance')

# Test it
skip, t1, flag1, flag2 = handler(
    'instance_type = "t2.micro"\n',
    'instance_type',
    't2.micro',
    False,
    'i-12345'
)

assert skip == 0
assert 't2.micro' in t1
```

## Debugging

Enable debug logging to see handler usage:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Shows which handlers are registered and called
```

View registry statistics:

```python
from handler_registry import registry

registry.print_stats()
# Output:
#   Custom handlers registered: 202
#   Custom handler calls: 1250
#   Default handler calls: 8930
#   Total calls: 10180
#   Custom handler usage: 12.3%
```

## Future Enhancements

1. **Auto-registration**: Automatically discover and register handlers
2. **Handler composition**: Combine multiple handlers
3. **Validation**: Validate handler signatures at registration
4. **Caching**: Cache handler lookups for performance
5. **Metrics**: Track which handlers are most frequently called

## Contributing

When adding new resource handlers:

1. Check if resource needs custom logic
2. If yes, add function to appropriate fixtf_*.py file
3. Register with `registry.register('resource_name', function)`
4. If no, do nothing - default handler will work
5. Update `aws_dict.py` with boto3 mappings
6. Test the handler

## Questions?

See `optimization-plan.md` for detailed analysis and implementation strategy.
