# Design Document

## Overview

This design replaces the global variables pattern in aws2tf with a modern configuration management system using dependency injection and proper encapsulation. The solution provides a `ConfigurationManager` class that centralizes all application state, organized into logical categories, with thread-safe access and comprehensive testing support.

## Architecture

### Core Components

```
ConfigurationManager
├── AWSConfig (AWS-related settings)
├── DebugConfig (Debug and logging settings)  
├── ProcessingConfig (Processing state and tracking)
├── RuntimeConfig (Runtime flags and options)
└── ResourceConfig (Resource lists and caches)
```

### Configuration Categories

**AWSConfig**: Manages AWS-specific configuration
- Account ID, region, profile
- Credential type and SSO status
- Terraform provider version

**DebugConfig**: Handles debugging and logging
- Debug flags (debug, debug5)
- Validation settings
- Fast mode flag

**ProcessingConfig**: Tracks processing state
- Tracking messages and progress
- Estimated time and cores
- Processing flags and counters

**RuntimeConfig**: Runtime behavior settings
- Merge, serverless, expected flags
- EC2 tag filtering
- Data source flags (dnet, dsgs, dkms, dkey)

**ResourceConfig**: Resource lists and caches
- VPC, subnet, security group lists
- Lambda, S3, IAM resource lists
- Processing and dependency tracking dictionaries

## Components and Interfaces

### ConfigurationManager Class

```python
class ConfigurationManager:
    def __init__(self):
        self.aws = AWSConfig()
        self.debug = DebugConfig()
        self.processing = ProcessingConfig()
        self.runtime = RuntimeConfig()
        self.resources = ResourceConfig()
        self._lock = threading.RLock()
    
    def update_from_args(self, args: argparse.Namespace) -> None
    def get_aws_session(self) -> boto3.Session
    def is_debug_enabled(self) -> bool
    def get_tracking_message(self) -> str
    def set_tracking_message(self, message: str) -> None
```

### Configuration Category Classes

Each configuration category implements a base interface:

```python
class ConfigCategory:
    def validate(self) -> List[str]
    def to_dict(self) -> Dict[str, Any]
    def from_dict(self, data: Dict[str, Any]) -> None
```

### Dependency Injection Pattern

Functions that need configuration receive it as a parameter:

```python
# Before (global access)
def some_function():
    if globals.debug:
        print("Debug message")

# After (dependency injection)
def some_function(config: ConfigurationManager):
    if config.debug.enabled:
        print("Debug message")
```

## Data Models

### AWSConfig

```python
@dataclass
class AWSConfig(ConfigCategory):
    version: str = "v1010"
    tf_version: str = "5.100.0"
    profile: str = "default"
    region: str = "xx-xxxx-x"
    account_id: str = "xxxxxxxxxxxx"
    credential_type: str = "invalid"
    is_sso: bool = False
    sso_instance: Optional[str] = None
```

### DebugConfig

```python
@dataclass
class DebugConfig(ConfigCategory):
    enabled: bool = False
    debug5: bool = False
    validate: bool = False
    fast: bool = False
```

### ProcessingConfig

```python
@dataclass
class ProcessingConfig(ConfigCategory):
    tracking_message: str = "aws2tf: Starting, update messages every 20 seconds"
    estimated_time: float = 120.0
    cores: int = 2
    processed: List[str] = field(default_factory=list)
    dependencies: List[str] = field(default_factory=list)
    types: List[str] = field(default_factory=list)
```

### Thread Safety

The ConfigurationManager uses `threading.RLock()` for thread-safe access to mutable state, particularly for:
- Tracking message updates
- Resource list modifications
- Processing state changes

## Error Handling

### Configuration Validation

Each configuration category implements validation:

```python
def validate(self) -> List[str]:
    errors = []
    if not self.region or self.region == "xx-xxxx-x":
        errors.append("Invalid AWS region specified")
    if not self.account_id or self.account_id == "xxxxxxxxxxxx":
        errors.append("AWS account ID not set")
    return errors
```

### Error Recovery

- Invalid configuration values trigger validation errors with clear messages
- Missing required configuration causes graceful failure with helpful error messages
- AWS credential errors are handled with specific guidance for resolution

## Testing Strategy

### Unit Testing

```python
class TestConfigurationManager(unittest.TestCase):
    def setUp(self):
        self.config = ConfigurationManager()
    
    def test_aws_config_validation(self):
        self.config.aws.region = "us-east-1"
        self.config.aws.account_id = "123456789012"
        errors = self.config.aws.validate()
        self.assertEqual(len(errors), 0)
```

### Integration Testing

- Test configuration loading from command-line arguments
- Test AWS credential detection and configuration
- Test thread-safe access under concurrent load
- Test backward compatibility with existing functionality

### Mock Support

```python
def create_test_config(**overrides) -> ConfigurationManager:
    config = ConfigurationManager()
    config.aws.region = overrides.get('region', 'us-east-1')
    config.aws.account_id = overrides.get('account_id', '123456789012')
    config.debug.enabled = overrides.get('debug', False)
    return config
```

## Migration Strategy

### Phase 1: Create Configuration System
- Implement ConfigurationManager and category classes
- Add comprehensive unit tests
- Create factory functions for easy instantiation

### Phase 2: Gradual Migration
- Update main entry point (aws2tf.py) to use ConfigurationManager
- Migrate core modules (common.py, resources.py) with dependency injection
- Maintain backward compatibility through adapter pattern if needed

### Phase 3: Complete Migration
- Update all remaining modules to use dependency injection
- Remove globals.py entirely
- Update all function signatures to accept configuration parameters

### Phase 4: Optimization
- Add configuration caching where appropriate
- Optimize thread-safe access patterns
- Add configuration serialization for debugging

## Performance Considerations

- Configuration access is optimized for read-heavy workloads
- Thread-safe operations use RLock for minimal overhead
- Resource lists use efficient data structures (dictionaries for O(1) lookup)
- Configuration validation is performed once at startup, not on every access