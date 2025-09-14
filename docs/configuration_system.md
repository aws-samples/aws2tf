# Configuration Management System Documentation

## Overview

The Configuration Management System provides a centralized, thread-safe, and type-safe way to manage application configuration throughout the aws2tf tool. It replaces the previous globals-based approach with a dependency injection pattern that improves testability, maintainability, and thread safety.

## Architecture

### Core Components

#### ConfigurationManager
The main entry point for configuration management. It coordinates all configuration categories and provides high-level operations.

```python
from code.config import ConfigurationManager

# Create a new configuration instance
config = ConfigurationManager()

# Access configuration categories
config.aws.region = 'us-east-1'
config.debug.debug = True
config.runtime.target_type = 'vpc'
```

#### Configuration Categories

The system is organized into logical categories:

- **AWSConfig**: AWS-specific settings (region, profile, credentials)
- **DebugConfig**: Debug flags and logging settings
- **ProcessingConfig**: Processing state and tracking information
- **RuntimeConfig**: Runtime behavior and options
- **ResourceConfig**: Resource lists and caches

### Key Features

1. **Thread Safety**: All configuration access is thread-safe
2. **Type Safety**: Strong typing with dataclasses and validation
3. **Dependency Injection**: Configuration passed as parameters
4. **Validation**: Comprehensive validation of configuration values
5. **Testing Support**: Easy mocking and test configuration creation

## Usage Guide

### Basic Usage

```python
from code.config import ConfigurationManager, parse_and_update_config

# Create configuration from command line arguments
config = ConfigurationManager()
args = parse_and_update_config(config)

# Use configuration in your functions
def process_vpc(config: ConfigurationManager, vpc_id: str):
    if config.debug.debug:
        print(f"Processing VPC {vpc_id} in region {config.aws.region}")
    
    # Mark resource as processed
    config.mark_resource_processed(f'aws_vpc.{vpc_id}')
```

### AWS Configuration

```python
# Set AWS configuration
config.aws.region = 'us-west-2'
config.aws.profile = 'production'
config.aws.account_id = '123456789012'

# Configure AWS credentials
from code.config import configure_aws_credentials
success = configure_aws_credentials(config)

if success:
    print(f"AWS configured for account {config.aws.account_id}")
```

### Debug Configuration

```python
# Enable debug mode
config.debug.debug = True
config.debug.debug5 = True  # Extra verbose

# Check debug state
if config.is_debug_enabled():
    print("Debug mode is active")
```

### Resource Tracking

```python
# Track processed resources
config.mark_resource_processed('aws_vpc.vpc-123456')
config.mark_resource_processed('aws_subnet.subnet-789012')

# Check if resource was processed
if config.is_resource_processed('aws_vpc.vpc-123456'):
    print("VPC already processed")

# Manage resource lists
config.resources.add_vpc_to_list('vpc-123456')
vpc_list = config.resources.get_vpc_list()
```

### Processing State

```python
# Set tracking messages
config.set_tracking_message("Processing VPCs...")

# Track processing time
config.start_processing()
# ... do work ...
elapsed = config.get_processing_elapsed()

# Set processing flags
config.processing.set_processing_flag('vpc_complete', True)
```

## Migration Guide

### From Globals to Dependency Injection

**Before (using globals):**
```python
import globals

def process_resource(resource_type, resource_id):
    if globals.debug:
        print(f"Processing {resource_type}: {resource_id}")
    
    # Use global variables
    region = globals.region
    account_id = globals.account_id
```

**After (using configuration):**
```python
from code.config import ConfigurationManager

def process_resource(config: ConfigurationManager, resource_type: str, resource_id: str):
    if config.debug.debug:
        print(f"Processing {resource_type}: {resource_id}")
    
    # Use configuration
    region = config.aws.region
    account_id = config.aws.account_id
```

### Function Signature Updates

1. Add configuration parameter as first argument
2. Update type hints to include ConfigurationManager
3. Replace globals.* with config.*

```python
# Before
def my_function(param1, param2):
    if globals.debug:
        print("Debug message")

# After  
def my_function(config: ConfigurationManager, param1, param2):
    if config.debug.debug:
        print("Debug message")
```

### Module Migration Checklist

- [ ] Add `config: ConfigurationManager` parameter to all functions
- [ ] Replace `import globals` with `from code.config import ConfigurationManager`
- [ ] Update all `globals.variable` references to `config.category.variable`
- [ ] Update function calls to pass configuration parameter
- [ ] Add type hints for configuration parameter
- [ ] Update unit tests to use test configuration

## Testing

### Creating Test Configurations

```python
from code.config import create_test_config

# Create a test configuration with sensible defaults
config = create_test_config()

# Customize for your test
config.aws.region = 'us-east-1'
config.runtime.target_type = 'vpc'
```

### Mocking Configuration

```python
import unittest
from unittest.mock import MagicMock
from code.config import ConfigurationManager

class TestMyFunction(unittest.TestCase):
    def test_with_mock_config(self):
        # Create mock configuration
        mock_config = MagicMock(spec=ConfigurationManager)
        mock_config.debug.debug = True
        mock_config.aws.region = 'us-east-1'
        
        # Test your function
        result = my_function(mock_config, 'test_param')
        self.assertTrue(result)
```

### Integration Testing

```python
def test_full_workflow(self):
    config = create_test_config()
    config.aws.region = 'us-east-1'
    config.runtime.target_type = 'vpc'
    
    # Test complete workflow
    result = process_resources(config)
    self.assertTrue(result)
    
    # Verify state changes
    self.assertTrue(config.is_resource_processed('aws_vpc.vpc-123456'))
```

## Configuration Categories Reference

### AWSConfig

Manages AWS-specific configuration settings.

**Fields:**
- `region: str` - AWS region (e.g., 'us-east-1')
- `profile: str` - AWS profile name
- `account_id: str` - AWS account ID
- `session: boto3.Session` - Boto3 session instance

**Methods:**
- `validate() -> List[str]` - Validate AWS configuration
- `get_session() -> boto3.Session` - Get or create boto3 session

### DebugConfig

Manages debug and logging settings.

**Fields:**
- `debug: bool` - Enable debug mode
- `debug5: bool` - Enable extra verbose debug mode

**Methods:**
- `validate() -> List[str]` - Validate debug configuration

### ProcessingConfig

Manages processing state and tracking.

**Fields:**
- `start_time: float` - Processing start timestamp
- `tracking_message: str` - Current tracking message
- `processing_flags: Dict[str, bool]` - Processing state flags

**Methods:**
- `set_processing_flag(name: str, value: bool)` - Set processing flag
- `get_processing_flag(name: str) -> bool` - Get processing flag value

### RuntimeConfig

Manages runtime behavior and options.

**Fields:**
- `target_type: str` - Target resource type
- `target_id: str` - Target resource ID
- `path1: str` - Primary output path
- `path2: str` - Secondary output path
- `path3: str` - Tertiary output path
- `cores: int` - Number of processing cores

**Methods:**
- `validate() -> List[str]` - Validate runtime configuration

### ResourceConfig

Manages resource lists and caches.

**Fields:**
- `processed_resources: Set[str]` - Set of processed resource IDs
- `vpc_list: List[str]` - List of VPC IDs
- `subnet_list: List[str]` - List of subnet IDs
- (Additional resource lists...)

**Methods:**
- `add_vpc_to_list(vpc_id: str)` - Add VPC to list
- `get_vpc_list() -> List[str]` - Get VPC list
- (Additional resource list methods...)

## Best Practices

### 1. Always Pass Configuration

```python
# Good: Pass configuration explicitly
def process_vpc(config: ConfigurationManager, vpc_id: str):
    pass

# Bad: Access global state
def process_vpc(vpc_id: str):
    import globals  # Don't do this
```

### 2. Use Type Hints

```python
from code.config import ConfigurationManager

def my_function(config: ConfigurationManager, param: str) -> bool:
    """Function with proper type hints."""
    return True
```

### 3. Validate Configuration Early

```python
config = ConfigurationManager()
# ... populate configuration ...

# Validate before use
errors = config.validate_all()
if errors:
    print(f"Configuration errors: {errors}")
    sys.exit(1)
```

### 4. Use Factory Functions for Tests

```python
from code.config import create_test_config

def test_my_function():
    config = create_test_config()
    # Test configuration is ready to use
    result = my_function(config)
```

### 5. Handle Thread Safety

```python
# Configuration is thread-safe, but be mindful of state changes
def worker_thread(config: ConfigurationManager, resource_id: str):
    # Safe to access configuration from multiple threads
    if config.debug.debug:
        print(f"Processing {resource_id}")
    
    # Safe to update resource tracking
    config.mark_resource_processed(resource_id)
```

## Performance Considerations

### Memory Usage
- Configuration objects are lightweight
- Resource tracking uses efficient data structures
- Memory usage scales linearly with tracked resources

### Thread Safety
- All configuration access is thread-safe
- No performance penalty for concurrent access
- Lock-free operations where possible

### Validation
- Validation is fast and cached where appropriate
- Only validate when necessary (e.g., at startup)
- Incremental validation for configuration changes

## Troubleshooting

### Common Issues

**ImportError: No module named 'code.config'**
```bash
# Ensure you're in the correct directory and Python path is set
export PYTHONPATH="${PYTHONPATH}:."
```

**Configuration validation errors**
```python
# Check validation errors
errors = config.validate_all()
for error in errors:
    print(f"Validation error: {error}")
```

**AWS credential issues**
```python
from code.config import validate_aws_credentials

validation = validate_aws_credentials(config)
if not validation['valid']:
    print(f"AWS credential error: {validation['error']}")
```

### Debug Mode

Enable debug mode to see detailed configuration information:

```python
config.debug.debug = True
config.debug.debug5 = True  # Extra verbose

# Configuration will now log detailed information
```

## Examples

See the `examples/` directory for complete working examples:

- `examples/basic_usage.py` - Basic configuration usage
- `examples/aws_integration.py` - AWS credential setup
- `examples/resource_processing.py` - Resource tracking patterns
- `examples/testing_patterns.py` - Testing with configuration

## API Reference

For complete API documentation, see the docstrings in the source code:

- `code/config/__init__.py` - Main configuration classes
- `code/config/argument_parser.py` - Argument parsing utilities
- `code/config/aws_credentials.py` - AWS credential management
- `code/config/validation.py` - Configuration validation