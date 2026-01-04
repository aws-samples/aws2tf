# Design Document: Unit Testing Strategy for aws2tf

## Overview

This design document outlines a comprehensive unit testing strategy for the aws2tf codebase. The aws2tf tool is a complex Python application that discovers AWS resources via boto3 APIs and generates Terraform configuration files. The testing strategy focuses on improving code resilience, preventing regressions, and providing confidence in correctness across 200+ AWS resource types.

The design emphasizes:
- **Isolation**: Unit tests that don't require AWS credentials or Terraform installation
- **Speed**: Full test suite execution in under 5 minutes
- **Coverage**: Minimum 70% line coverage for core modules
- **Maintainability**: Clear test organization and documentation
- **Security**: Thorough testing of input validation and file operations

## Architecture

### Test Organization Structure

```
tests/
├── unit/
│   ├── test_input_validation.py      # Input validation functions
│   ├── test_file_operations.py       # File I/O and permissions
│   ├── test_cli_parsing.py           # Command-line argument parsing
│   ├── test_context.py                # Context state management
│   ├── test_resource_discovery.py    # build_lists() and related
│   ├── test_error_handling.py        # Exception handling
│   ├── test_module_registry.py       # Dynamic module loading
│   ├── test_progress_tracking.py     # Progress bars and rate learning
│   ├── handlers/
│   │   ├── test_handler_ec2.py       # EC2 resource handlers
│   │   ├── test_handler_s3.py        # S3 resource handlers
│   │   ├── test_handler_iam.py       # IAM resource handlers
│   │   └── ...                        # Other service handlers
│   └── get_functions/
│       ├── test_get_ec2.py           # EC2 get functions
│       ├── test_get_s3.py            # S3 get functions
│       ├── test_get_iam.py           # IAM get functions
│       └── ...                        # Other service get functions
├── integration/
│   ├── test_vpc_workflow.py          # End-to-end VPC import
│   ├── test_lambda_workflow.py       # End-to-end Lambda import
│   ├── test_s3_workflow.py           # End-to-end S3 import
│   └── ...                            # Other workflows
├── property/
│   ├── test_input_properties.py      # Property-based input tests
│   ├── test_handler_properties.py    # Property-based handler tests
│   └── test_file_properties.py       # Property-based file tests
├── regression/
│   ├── test_github_issues.py         # Tests for reported bugs
│   └── test_security_fixes.py        # Tests for security patches
├── performance/
│   ├── test_discovery_performance.py # Resource discovery benchmarks
│   └── test_generation_performance.py # File generation benchmarks
├── conftest.py                        # Shared fixtures and configuration
└── README.md                          # Test documentation
```

### Testing Layers

1. **Unit Tests**: Test individual functions in isolation with mocked dependencies
2. **Integration Tests**: Test multiple components working together (still mocked AWS)
3. **Property Tests**: Test universal properties with generated inputs
4. **Regression Tests**: Prevent previously fixed bugs from reoccurring
5. **Performance Tests**: Ensure the tool remains fast

## Components and Interfaces

### 1. Test Fixtures (conftest.py)

**Purpose**: Provide reusable test setup and teardown

**Key Fixtures**:

```python
@pytest.fixture
def mock_boto3_client():
    """Mock boto3 client with common AWS service responses."""
    with mock.patch('boto3.client') as mock_client:
        # Configure mock responses for common operations
        yield mock_client

@pytest.fixture
def mock_context():
    """Initialize context with test defaults."""
    # Reset context state
    context.reset()
    context.region = 'us-east-1'
    context.acc = '123456789012'
    context.debug = False
    yield context
    # Cleanup after test
    context.reset()

@pytest.fixture
def temp_workspace(tmp_path):
    """Create temporary workspace directory."""
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "generated").mkdir()
    (workspace / "generated" / "tf-123456789012-us-east-1").mkdir()
    return workspace

@pytest.fixture
def mock_terraform():
    """Mock terraform command execution."""
    with mock.patch('common.rc') as mock_rc:
        # Configure mock terraform responses
        yield mock_rc
```

### 2. Input Validation Test Module

**File**: `tests/unit/test_input_validation.py`

**Purpose**: Test all input validation functions for security

**Test Cases**:
- Valid AWS regions pass validation
- Invalid region formats raise ValueError
- Valid resource types pass validation
- Resource types with special characters are rejected
- Path traversal attempts are blocked
- Shell metacharacters are rejected
- EC2 tag format validation
- Terraform version format validation

**Example Test**:
```python
def test_validate_region_valid():
    """Test that valid AWS regions pass validation."""
    valid_regions = ['us-east-1', 'eu-west-2', 'ap-southeast-1']
    for region in valid_regions:
        assert validate_region(region) == region

def test_validate_region_invalid():
    """Test that invalid regions raise ValueError."""
    invalid_regions = ['invalid', 'us_east_1', '../etc/passwd']
    for region in invalid_regions:
        with pytest.raises(ValueError):
            validate_region(region)
```

### 3. File Operations Test Module

**File**: `tests/unit/test_file_operations.py`

**Purpose**: Test file I/O, permissions, and security

**Test Cases**:
- `safe_filename()` prevents path traversal
- `safe_write_file()` creates files with correct permissions
- `safe_write_sensitive_file()` sets 0o600 permissions
- `secure_terraform_files()` secures state files
- Subdirectory handling works correctly
- File permissions are verified after creation

**Example Test**:
```python
def test_safe_filename_prevents_traversal(tmp_path):
    """Test that path traversal is prevented."""
    with pytest.raises(ValueError, match="Path traversal"):
        safe_filename("../../../etc/passwd", base_dir=str(tmp_path))

def test_safe_write_sensitive_file_permissions(tmp_path):
    """Test that sensitive files get 0o600 permissions."""
    filepath = tmp_path / "test.tfstate"
    safe_write_sensitive_file(str(filepath), "content")
    
    stat_info = os.stat(filepath)
    permissions = stat_info.st_mode & 0o777
    assert permissions == 0o600
```

### 4. AWS API Mocking Strategy

**Library**: `moto` for AWS service mocking

**Approach**:
- Use `@mock_aws` decorator for test functions
- Create realistic AWS resource responses
- Test pagination handling
- Test error conditions (ClientError, ExpiredToken, etc.)

**Example Mock Setup**:
```python
from moto import mock_aws
import boto3

@mock_aws
def test_get_aws_vpc(mock_context):
    """Test VPC discovery with mocked AWS."""
    # Create mock VPC
    ec2 = boto3.client('ec2', region_name='us-east-1')
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']
    
    # Test get function
    from get_aws_resources.aws_ec2 import get_aws_vpc
    result = get_aws_vpc('aws_vpc', None, 'ec2', 'describe_vpcs', 
                         'Vpcs', 'VpcId', 'VpcId')
    
    # Verify write_import was called
    assert result == True
    # Verify VPC was discovered
    # (would need to mock write_import to verify parameters)
```

### 5. Resource Handler Test Strategy

**Approach**: Test handler functions with sample Terraform output

**Test Pattern**:
```python
def test_handler_skips_computed_field():
    """Test that computed fields are skipped."""
    handler = fixtf_ec2.aws_vpc
    
    # Test with computed field
    result_skip, result_t1, result_flag1, result_flag2 = handler(
        "arn = \"arn:aws:ec2:us-east-1:123:vpc/vpc-123\"\n",
        "arn",
        "\"arn:aws:ec2:us-east-1:123:vpc/vpc-123\"",
        0,
        0
    )
    
    assert result_skip == 1  # Field should be skipped

def test_handler_adds_lifecycle_block():
    """Test that lifecycle blocks are added correctly."""
    handler = fixtf_s3.aws_s3_bucket
    
    # Test with field that needs lifecycle
    result_skip, result_t1, result_flag1, result_flag2 = handler(
        "bucket = \"my-bucket\"\n",
        "bucket",
        "\"my-bucket\"",
        0,
        0
    )
    
    assert "lifecycle" in result_t1
    assert "ignore_changes" in result_t1
```

### 6. Module Registry Test Module

**File**: `tests/unit/test_module_registry.py`

**Purpose**: Test dynamic module loading without eval()

**Test Cases**:
- All services in AWS_RESOURCE_MODULES are valid
- Modules can be loaded dynamically
- Missing modules are handled gracefully
- Hyphenated service names resolve correctly
- Registry prevents arbitrary code execution

**Example Test**:
```python
def test_module_registry_contains_all_services():
    """Test that registry has entries for all imported modules."""
    from common import AWS_RESOURCE_MODULES
    
    # Verify key services are present
    assert 'ec2' in AWS_RESOURCE_MODULES
    assert 's3' in AWS_RESOURCE_MODULES
    assert 'iam' in AWS_RESOURCE_MODULES
    assert 'lambda' in AWS_RESOURCE_MODULES
    
    # Verify hyphenated names work
    assert 'workspaces-web' in AWS_RESOURCE_MODULES

def test_module_registry_loads_module():
    """Test that modules can be loaded from registry."""
    from common import AWS_RESOURCE_MODULES
    
    ec2_module = AWS_RESOURCE_MODULES['ec2']
    assert hasattr(ec2_module, 'get_aws_vpc')
```

### 7. Progress Tracking Test Module

**File**: `tests/unit/test_progress_tracking.py`

**Purpose**: Test progress bar and adaptive rate learning

**Test Cases**:
- Progress bars are created correctly
- Adaptive rate learning updates
- Progress caps at 75% until completion
- Progress jumps to 100% on completion
- Progress tracking disabled in debug mode

**Example Test**:
```python
def test_adaptive_rate_learning():
    """Test that terraform plan rate adapts to actual performance."""
    context.terraform_plan_rate = 25.0  # Initial estimate
    context.terraform_plan_samples = 0
    
    # Simulate a plan that took 10 seconds for 200 resources
    # Actual rate: 20 resources/second
    # Expected: rate should move toward 20
    
    # (Would need to refactor code to make rate calculation testable)
    # This test would verify the exponential moving average logic
```

### 8. Context Management Test Module

**File**: `tests/unit/test_context.py`

**Purpose**: Test global state management

**Test Cases**:
- Context initialization sets all required attributes
- Resource tracking dictionaries are initialized
- Region and account information is stored
- Merge mode state is tracked
- Exclusion lists are maintained
- Context is isolated between tests
- Context is thread-safe

**Example Test**:
```python
def test_context_initialization():
    """Test that context initializes with correct defaults."""
    context.reset()
    
    assert hasattr(context, 'region')
    assert hasattr(context, 'acc')
    assert hasattr(context, 'vpclist')
    assert hasattr(context, 'lambdalist')
    assert hasattr(context, 's3list')
    assert isinstance(context.vpclist, dict)
    assert isinstance(context.rproc, dict)
```

## Data Models

### Test Data Structures

**Mock AWS Responses**:
```python
MOCK_VPC_RESPONSE = {
    'Vpcs': [
        {
            'VpcId': 'vpc-12345678',
            'CidrBlock': '10.0.0.0/16',
            'State': 'available',
            'Tags': [{'Key': 'Name', 'Value': 'test-vpc'}]
        }
    ]
}

MOCK_LAMBDA_RESPONSE = {
    'Functions': [
        {
            'FunctionName': 'test-function',
            'FunctionArn': 'arn:aws:lambda:us-east-1:123:function:test',
            'Runtime': 'python3.12',
            'Handler': 'index.handler'
        }
    ]
}
```

**Test Context State**:
```python
TEST_CONTEXT = {
    'region': 'us-east-1',
    'acc': '123456789012',
    'debug': False,
    'fast': False,
    'merge': False,
    'vpclist': {},
    'lambdalist': {},
    's3list': {},
    'rproc': {}
}
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

Based on the prework analysis, most of the acceptance criteria are meta-requirements (requirements about what tests should exist, not about system behavior). However, we can define a few testable properties for the test infrastructure itself:

### Property 1: Test Discovery Completeness
*For any* test file in the tests/ directory that follows the naming convention `test_*.py`, pytest SHALL discover and execute all test functions within it.
**Validates: Requirements 1.4**

### Property 2: Coverage Threshold Enforcement
*For any* test run, if line coverage for core modules falls below 70%, the coverage report SHALL indicate failure status.
**Validates: Requirements 17.1**

### Property 3: Test Execution Time Bound
*For any* full test suite execution, the total runtime SHALL complete in under 5 minutes (300 seconds).
**Validates: Requirements 1.7**

### Property 4: Performance Regression Detection
*For any* performance test, if execution time exceeds the baseline by more than 20%, the test SHALL fail and report the regression.
**Validates: Requirements 19.6**

### Property 5: Test Function Size Limit
*For any* test function in the test suite, the function SHALL contain fewer than 50 lines of code.
**Validates: Requirements 20.5**

**Note on Correctness Properties**: This specification is unique in that it defines a testing infrastructure rather than application behavior. Most acceptance criteria describe what tests should exist (meta-requirements) rather than testable properties of the system. The properties above focus on the few measurable characteristics of the test infrastructure itself (discovery, coverage, performance, maintainability).

The actual correctness properties for the aws2tf application (input validation, resource discovery, file generation, etc.) will be tested by the unit tests defined in this specification, but those properties belong to the application design, not the test infrastructure design.

## Error Handling

### Test Error Handling Strategy

**Principle**: Tests should fail fast with clear error messages

**Error Categories**:

1. **Setup Errors**: Missing fixtures, invalid test data
   - Action: Fail immediately with descriptive message
   - Example: "Mock boto3 client not configured"

2. **Assertion Errors**: Test expectations not met
   - Action: Show expected vs actual values
   - Example: "Expected coverage 70%, got 65%"

3. **Timeout Errors**: Tests taking too long
   - Action: Fail after 30 seconds per test
   - Example: "Test exceeded 30 second timeout"

4. **Mock Configuration Errors**: Mocks not set up correctly
   - Action: Fail with mock configuration details
   - Example: "Mock AWS service 'ec2' not configured"

### Test Isolation

**Strategy**: Each test should be independent

**Implementation**:
- Use fixtures to reset context between tests
- Clean up temporary files after each test
- Reset mock state between tests
- Use `tmp_path` fixture for file operations

**Example**:
```python
@pytest.fixture(autouse=True)
def reset_context():
    """Automatically reset context before each test."""
    context.reset()
    yield
    context.reset()
```

## Testing Strategy

### Dual Testing Approach

The test suite uses both unit tests and property-based tests:

**Unit Tests**:
- Verify specific examples and edge cases
- Test error conditions
- Test integration points between components
- Fast execution (milliseconds per test)

**Property-Based Tests**:
- Verify universal properties across all inputs
- Discover edge cases automatically
- Run 100+ iterations per property
- Use `hypothesis` library

**Together**: Comprehensive coverage (unit tests catch concrete bugs, property tests verify general correctness)

### Property-Based Testing Configuration

**Library**: `hypothesis` (https://hypothesis.readthedocs.io/)

**Configuration**:
```python
from hypothesis import given, settings, strategies as st

@settings(max_examples=100, deadline=None)
@given(region=st.from_regex(r'^[a-z]{2}-[a-z]+-\d{1,2}$'))
def test_validate_region_property(region):
    """Property: All strings matching AWS region format should validate."""
    result = validate_region(region)
    assert result == region
```

**Minimum 100 iterations per property test**

**Tag format**: Tests reference design properties in docstrings
- Example: `"""Property 1: Test Discovery Completeness - validates Requirements 1.4"""`

### Test Execution Strategy

**Local Development**:
```bash
# Run all tests
pytest

# Run specific module
pytest tests/unit/test_input_validation.py

# Run with coverage
pytest --cov=code --cov-report=html

# Run only fast tests (skip integration)
pytest -m "not integration"

# Run with verbose output
pytest -v
```

**CI/CD Pipeline**:
```bash
# Run with coverage and fail on threshold
pytest --cov=code --cov-fail-under=70

# Generate XML coverage for CI tools
pytest --cov=code --cov-report=xml

# Run with parallel execution
pytest -n auto
```

### Test Markers

```python
# Mark slow tests
@pytest.mark.slow
def test_full_integration():
    pass

# Mark integration tests
@pytest.mark.integration
def test_vpc_workflow():
    pass

# Mark property tests
@pytest.mark.property
def test_input_property():
    pass

# Mark performance tests
@pytest.mark.performance
def test_discovery_speed():
    pass
```

### Coverage Strategy

**Target Coverage**:
- Core modules (aws2tf.py, common.py, build_lists.py): 70% line coverage
- Input validation functions: 80% line coverage
- Resource handlers: 60% line coverage
- Get functions: 70% line coverage

**Coverage Exclusions**:
- Debug-only code paths
- Error handling for impossible conditions
- Deprecated code marked for removal

**Coverage Reporting**:
```bash
# Generate HTML report
pytest --cov=code --cov-report=html
# Open htmlcov/index.html in browser

# Generate terminal report
pytest --cov=code --cov-report=term-missing

# Generate XML for CI
pytest --cov=code --cov-report=xml
```

### Test Prioritization

**Priority 1 (Critical)**: Security and input validation
- Input validation functions
- File operations and permissions
- Path traversal prevention

**Priority 2 (High)**: Core functionality
- Resource discovery (build_lists)
- Resource handlers
- Get functions
- Module registry

**Priority 3 (Medium)**: User experience
- Progress tracking
- Error handling
- CLI parsing

**Priority 4 (Low)**: Nice-to-have
- Performance optimizations
- Debug features
- Logging

### Continuous Integration

**GitHub Actions Workflow**:
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov hypothesis moto
      - name: Run tests
        run: pytest --cov=code --cov-fail-under=70
      - name: Upload coverage
        uses: codecov/codecov-action@v2
```

## Implementation Phases

### Phase 1: Foundation (Week 1)
- Set up test directory structure
- Create conftest.py with basic fixtures
- Implement input validation tests
- Implement file operations tests
- Target: 20 tests, basic CI integration

### Phase 2: Core Functionality (Week 2)
- Implement resource discovery tests
- Implement context management tests
- Implement CLI parsing tests
- Implement error handling tests
- Target: 50 tests, 40% coverage

### Phase 3: AWS Integration (Week 3)
- Set up moto for AWS mocking
- Implement get function tests (10 services)
- Implement resource handler tests (10 services)
- Target: 100 tests, 60% coverage

### Phase 4: Advanced Testing (Week 4)
- Implement property-based tests
- Implement integration tests
- Implement performance tests
- Target: 150 tests, 70% coverage

### Phase 5: Completion (Week 5)
- Implement remaining handler tests
- Implement remaining get function tests
- Implement regression tests
- Documentation and cleanup
- Target: 200+ tests, 70%+ coverage

## Dependencies

**Testing Libraries**:
- `pytest`: Test framework
- `pytest-cov`: Coverage reporting
- `pytest-mock`: Mocking utilities
- `hypothesis`: Property-based testing
- `moto`: AWS service mocking
- `pytest-xdist`: Parallel test execution

**Installation**:
```bash
pip install pytest pytest-cov pytest-mock hypothesis moto pytest-xdist
```

## Performance Considerations

**Test Execution Speed**:
- Unit tests: < 100ms each
- Integration tests: < 1s each
- Property tests: < 5s each
- Full suite: < 5 minutes

**Optimization Strategies**:
- Use mocks instead of real AWS calls
- Use tmp_path for file operations (in-memory when possible)
- Run tests in parallel with pytest-xdist
- Cache expensive setup operations
- Skip slow tests in development (use markers)

**Monitoring**:
- Track test execution time in CI
- Alert on tests that exceed time budgets
- Profile slow tests and optimize

## Security Considerations

**Test Data Security**:
- Never use real AWS credentials in tests
- Never commit sensitive data to test files
- Use fake/mock data for all tests
- Sanitize any logged output

**Test Isolation**:
- Tests should not affect each other
- Tests should not affect the host system
- Use temporary directories for file operations
- Clean up all resources after tests

**Permission Testing**:
- Verify file permissions are set correctly
- Test that sensitive files get 0o600
- Test that path traversal is prevented
- Test that shell injection is prevented

## Maintenance and Evolution

**Adding New Tests**:
1. Identify the module/function to test
2. Create test file in appropriate directory
3. Write test cases covering happy path and edge cases
4. Add property tests if applicable
5. Update coverage targets if needed
6. Document test purpose in docstring

**Updating Tests**:
- Update tests when requirements change
- Keep tests in sync with code changes
- Refactor tests to reduce duplication
- Remove obsolete tests

**Test Review Process**:
- All new code requires tests
- PRs must maintain or improve coverage
- Tests must pass before merging
- Review test quality, not just coverage numbers

## Documentation

**Test README** (`tests/README.md`):
- How to run tests locally
- How to run specific test subsets
- How to interpret coverage reports
- How to add new tests
- How to debug failing tests

**Test Docstrings**:
- Every test function has a docstring
- Docstring explains what is being tested
- Docstring explains why it matters
- Docstring references requirements if applicable

**Example**:
```python
def test_validate_region_prevents_path_traversal():
    """
    Test that validate_region rejects path traversal attempts.
    
    This is critical for security - prevents attackers from using
    region parameter to access arbitrary files on the system.
    
    Validates: Requirement 2.2 - Input validation security
    """
    with pytest.raises(ValueError, match="Invalid AWS region"):
        validate_region("../../../etc/passwd")
```
