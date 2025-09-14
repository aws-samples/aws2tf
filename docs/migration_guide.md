# Migration Guide: From Globals to Configuration Management System

## Overview

This guide provides step-by-step instructions for migrating modules from the old globals-based approach to the new Configuration Management System using dependency injection.

## Migration Process

### Step 1: Update Imports

**Before:**
```python
import globals
```

**After:**
```python
from code.config import ConfigurationManager
```

### Step 2: Update Function Signatures

Add `config: ConfigurationManager` as the first parameter to all functions that previously used globals.

**Before:**
```python
def process_vpc(vpc_id: str) -> bool:
    if globals.debug:
        print(f"Processing VPC {vpc_id}")
    return True
```

**After:**
```python
def process_vpc(config: ConfigurationManager, vpc_id: str) -> bool:
    if config.debug.debug:
        print(f"Processing VPC {vpc_id}")
    return True
```

### Step 3: Replace Global Variable Access

Replace all `globals.variable` references with appropriate configuration category access.

#### Common Mappings

| Old Global Variable | New Configuration Access |
|-------------------|-------------------------|
| `globals.region` | `config.aws.region` |
| `globals.profile` | `config.aws.profile` |
| `globals.account_id` | `config.aws.account_id` |
| `globals.debug` | `config.debug.debug` |
| `globals.debug5` | `config.debug.debug5` |
| `globals.target_type` | `config.runtime.target_type` |
| `globals.target_id` | `config.runtime.target_id` |
| `globals.cores` | `config.runtime.cores` |
| `globals.path1` | `config.runtime.path1` |
| `globals.path2` | `config.runtime.path2` |
| `globals.path3` | `config.runtime.path3` |

#### Resource Lists

| Old Global Variable | New Configuration Access |
|-------------------|-------------------------|
| `globals.vpc_list` | `config.resources.get_vpc_list()` |
| `globals.subnet_list` | `config.resources.get_subnet_list()` |
| `globals.processed_resources` | `config.is_resource_processed(resource_id)` |

### Step 4: Update Function Calls

Update all function calls to pass the configuration parameter.

**Before:**
```python
result = process_vpc('vpc-123456')
```

**After:**
```python
result = process_vpc(config, 'vpc-123456')
```

### Step 5: Update Class Constructors

For classes that use configuration, add configuration as a constructor parameter.

**Before:**
```python
class ResourceProcessor:
    def __init__(self):
        self.region = globals.region
    
    def process(self, resource_id):
        if globals.debug:
            print(f"Processing {resource_id}")
```

**After:**
```python
class ResourceProcessor:
    def __init__(self, config: ConfigurationManager):
        self.config = config
    
    def process(self, resource_id):
        if self.config.debug.debug:
            print(f"Processing {resource_id}")
```

## Module-Specific Migration Examples

### Example 1: Simple Function Module

**Before (old_module.py):**
```python
import globals

def get_vpc_info(vpc_id):
    if globals.debug:
        print(f"Getting VPC info for {vpc_id}")
    
    # Use global session
    ec2 = globals.session.client('ec2')
    response = ec2.describe_vpcs(VpcIds=[vpc_id])
    
    return response['Vpcs'][0]

def process_all_vpcs():
    for vpc_id in globals.vpc_list:
        info = get_vpc_info(vpc_id)
        print(f"VPC {vpc_id}: {info['State']}")
```

**After (migrated_module.py):**
```python
from code.config import ConfigurationManager

def get_vpc_info(config: ConfigurationManager, vpc_id: str) -> dict:
    if config.debug.debug:
        print(f"Getting VPC info for {vpc_id}")
    
    # Use configuration session
    session = config.aws.get_session()
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs(VpcIds=[vpc_id])
    
    return response['Vpcs'][0]

def process_all_vpcs(config: ConfigurationManager) -> None:
    vpc_list = config.resources.get_vpc_list()
    for vpc_id in vpc_list:
        info = get_vpc_info(config, vpc_id)
        print(f"VPC {vpc_id}: {info['State']}")
```

### Example 2: Class-Based Module

**Before:**
```python
import globals

class VPCProcessor:
    def __init__(self):
        self.processed_count = 0
    
    def process_vpc(self, vpc_id):
        if globals.debug:
            print(f"Processing VPC {vpc_id}")
        
        # Mark as processed
        globals.processed_resources.add(f'aws_vpc.{vpc_id}')
        self.processed_count += 1
        
        return True
    
    def get_stats(self):
        return {
            'processed': self.processed_count,
            'region': globals.region
        }
```

**After:**
```python
from code.config import ConfigurationManager

class VPCProcessor:
    def __init__(self, config: ConfigurationManager):
        self.config = config
        self.processed_count = 0
    
    def process_vpc(self, vpc_id: str) -> bool:
        if self.config.debug.debug:
            print(f"Processing VPC {vpc_id}")
        
        # Mark as processed
        self.config.mark_resource_processed(f'aws_vpc.{vpc_id}')
        self.processed_count += 1
        
        return True
    
    def get_stats(self) -> dict:
        return {
            'processed': self.processed_count,
            'region': self.config.aws.region
        }
```

### Example 3: Module with Complex State

**Before:**
```python
import globals
import threading

# Module-level state
_processing_lock = threading.Lock()
_current_operation = None

def start_operation(operation_name):
    global _current_operation
    with _processing_lock:
        _current_operation = operation_name
        if globals.debug:
            print(f"Started operation: {operation_name}")

def get_current_operation():
    with _processing_lock:
        return _current_operation

def process_with_tracking(resource_id):
    start_operation(f"Processing {resource_id}")
    
    # Do processing
    if globals.debug5:
        print(f"Detailed processing of {resource_id}")
    
    # Update tracking
    globals.tracking_message = f"Processed {resource_id}"
    
    return True
```

**After:**
```python
from code.config import ConfigurationManager

def start_operation(config: ConfigurationManager, operation_name: str) -> None:
    config.set_tracking_message(f"Started operation: {operation_name}")
    if config.debug.debug:
        print(f"Started operation: {operation_name}")

def get_current_operation(config: ConfigurationManager) -> str:
    return config.get_tracking_message()

def process_with_tracking(config: ConfigurationManager, resource_id: str) -> bool:
    start_operation(config, f"Processing {resource_id}")
    
    # Do processing
    if config.debug.debug5:
        print(f"Detailed processing of {resource_id}")
    
    # Update tracking
    config.set_tracking_message(f"Processed {resource_id}")
    
    return True
```

## Testing Migration

### Update Unit Tests

**Before:**
```python
import unittest
from unittest.mock import patch
import globals
from my_module import process_vpc

class TestVPCProcessing(unittest.TestCase):
    def setUp(self):
        globals.debug = True
        globals.region = 'us-east-1'
    
    def test_process_vpc(self):
        result = process_vpc('vpc-123456')
        self.assertTrue(result)
```

**After:**
```python
import unittest
from unittest.mock import MagicMock
from code.config import ConfigurationManager, create_test_config
from my_module import process_vpc

class TestVPCProcessing(unittest.TestCase):
    def setUp(self):
        self.config = create_test_config()
        self.config.debug.debug = True
        self.config.aws.region = 'us-east-1'
    
    def test_process_vpc(self):
        result = process_vpc(self.config, 'vpc-123456')
        self.assertTrue(result)
    
    def test_with_mock_config(self):
        mock_config = MagicMock(spec=ConfigurationManager)
        mock_config.debug.debug = True
        
        result = process_vpc(mock_config, 'vpc-123456')
        self.assertTrue(result)
```

## Migration Checklist

Use this checklist for each module you migrate:

### Code Changes
- [ ] Remove `import globals` statements
- [ ] Add `from code.config import ConfigurationManager` import
- [ ] Add `config: ConfigurationManager` parameter to all functions
- [ ] Replace all `globals.variable` with `config.category.variable`
- [ ] Update all function calls to pass configuration parameter
- [ ] Update class constructors to accept configuration
- [ ] Add type hints for configuration parameters

### Variable Mapping
- [ ] Map AWS variables (`region`, `profile`, `account_id`) to `config.aws.*`
- [ ] Map debug variables (`debug`, `debug5`) to `config.debug.*`
- [ ] Map runtime variables (`target_type`, `cores`, `paths`) to `config.runtime.*`
- [ ] Map resource lists to `config.resources.*` methods
- [ ] Map processing state to `config.processing.*` or helper methods

### Testing
- [ ] Update unit tests to use `create_test_config()`
- [ ] Replace globals setup in tests with configuration setup
- [ ] Update test function calls to pass configuration
- [ ] Add tests for configuration validation
- [ ] Verify all existing functionality still works

### Integration
- [ ] Update all callers of migrated functions
- [ ] Ensure configuration is passed through call chains
- [ ] Test integration with other migrated modules
- [ ] Verify no remaining globals usage

## Common Pitfalls and Solutions

### Pitfall 1: Forgetting to Pass Configuration

**Problem:**
```python
def function_a(config: ConfigurationManager):
    return function_b()  # Missing config parameter!

def function_b(config: ConfigurationManager):
    return config.aws.region
```

**Solution:**
```python
def function_a(config: ConfigurationManager):
    return function_b(config)  # Pass configuration

def function_b(config: ConfigurationManager):
    return config.aws.region
```

### Pitfall 2: Mixing Old and New Patterns

**Problem:**
```python
def mixed_function(config: ConfigurationManager):
    region = config.aws.region  # New pattern
    debug = globals.debug       # Old pattern - Don't do this!
```

**Solution:**
```python
def consistent_function(config: ConfigurationManager):
    region = config.aws.region  # New pattern
    debug = config.debug.debug  # New pattern
```

### Pitfall 3: Not Updating All Call Sites

**Problem:**
```python
# Function updated but caller not updated
def process_vpc(config: ConfigurationManager, vpc_id: str):
    pass

# Somewhere else in code
process_vpc('vpc-123456')  # Missing config parameter!
```

**Solution:**
Use IDE search/replace to find all call sites and update them systematically.

### Pitfall 4: Incorrect Resource List Access

**Problem:**
```python
# Trying to access resource list directly
vpc_list = config.resources.vpc_list  # This might not work as expected
```

**Solution:**
```python
# Use the proper method
vpc_list = config.resources.get_vpc_list()
```

## Validation After Migration

### 1. Run All Tests
```bash
python -m pytest tests/ -v
```

### 2. Check for Remaining Globals Usage
```bash
grep -r "import globals" . --exclude-dir=.git
grep -r "globals\." . --exclude-dir=.git
```

### 3. Verify Configuration Usage
```bash
grep -r "ConfigurationManager" . --include="*.py"
```

### 4. Test Integration
Run the full application with various configurations to ensure everything works.

## Performance Considerations

The migration should not significantly impact performance:

- Configuration access is fast (simple attribute access)
- Resource tracking uses efficient data structures
- Thread safety is built-in without performance penalties
- Memory usage is comparable to the old globals approach

## Getting Help

If you encounter issues during migration:

1. Check the examples in `examples/` directory
2. Review the API documentation in `docs/configuration_system.md`
3. Look at existing migrated modules for patterns
4. Run the validation tests to check your migration

## Migration Timeline

For large codebases, consider this phased approach:

### Phase 1: Core Infrastructure
- Migrate main entry points
- Migrate configuration and argument parsing
- Migrate AWS credential handling

### Phase 2: Core Modules
- Migrate frequently used utility modules
- Migrate resource processing modules
- Update main processing loops

### Phase 3: Specialized Modules
- Migrate remaining specialized modules
- Update error handling and logging
- Migrate testing utilities

### Phase 4: Cleanup
- Remove globals.py
- Clean up unused imports
- Update documentation
- Run comprehensive tests