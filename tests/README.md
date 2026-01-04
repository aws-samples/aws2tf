# aws2tf Test Suite

This directory contains the comprehensive test suite for the aws2tf tool. The tests ensure code quality, prevent regressions, and validate that AWS-to-Terraform conversion works correctly across 200+ AWS resource types.

## Test Organization

```
tests/
├── unit/                    # Unit tests for individual functions/modules
│   ├── handlers/           # Tests for resource handler functions
│   ├── get_functions/      # Tests for AWS resource discovery functions
│   └── *.py                # Core functionality tests
├── integration/            # End-to-end workflow tests
├── property/               # Property-based tests using hypothesis
├── regression/             # Tests for previously fixed bugs
├── performance/            # Performance benchmarks
├── conftest.py            # Shared fixtures and configuration
└── README.md              # This file
```

## Running Tests

### Prerequisites

Install test dependencies:
```bash
pip install pytest pytest-cov pytest-mock hypothesis moto pytest-xdist
```

### Run All Tests

```bash
# From workspace root
pytest

# With verbose output
pytest -v

# With coverage report
pytest --cov=code --cov-report=html
```

### Run Specific Test Subsets

```bash
# Run only unit tests
pytest tests/unit/

# Run only integration tests
pytest tests/integration/

# Run only property tests
pytest tests/property/

# Run specific test file
pytest tests/unit/test_input_validation.py

# Run specific test function
pytest tests/unit/test_input_validation.py::test_validate_region_valid
```

### Run Tests by Marker

```bash
# Run only fast tests (skip integration)
pytest -m "not integration"

# Run only slow tests
pytest -m slow

# Run only property tests
pytest -m property

# Run only performance tests
pytest -m performance
```

### Run Tests in Parallel

```bash
# Use all available CPU cores
pytest -n auto

# Use specific number of workers
pytest -n 4
```

## Coverage Reports

### Generate HTML Coverage Report

```bash
pytest --cov=code --cov-report=html
# Open htmlcov/index.html in browser
```

### Generate Terminal Coverage Report

```bash
pytest --cov=code --cov-report=term-missing
```

### Coverage Thresholds

The test suite enforces minimum coverage thresholds:
- **Core modules** (aws2tf.py, common.py, build_lists.py): 70% line coverage
- **Input validation functions**: 80% line coverage
- **Resource handlers**: 60% line coverage
- **Get functions**: 70% line coverage

### Fail Build on Low Coverage

```bash
pytest --cov=code --cov-fail-under=70
```

## Test Markers

Tests are marked with pytest markers for selective execution:

- `@pytest.mark.slow` - Tests that take more than 1 second
- `@pytest.mark.integration` - Integration tests (multiple components)
- `@pytest.mark.property` - Property-based tests using hypothesis
- `@pytest.mark.performance` - Performance benchmarks
- `@pytest.mark.regression` - Tests for previously fixed bugs

## Writing Tests

### Test File Naming

- Test files must start with `test_`
- Test functions must start with `test_`
- Example: `test_input_validation.py` with `test_validate_region_valid()`

### Test Function Structure

```python
def test_function_name():
    """
    Brief description of what is being tested.
    
    Explains why this test matters and what behavior it validates.
    
    Validates: Requirement X.Y
    """
    # Arrange - Set up test data
    input_data = "test-value"
    
    # Act - Execute the function being tested
    result = function_under_test(input_data)
    
    # Assert - Verify expected behavior
    assert result == expected_value
```

### Using Fixtures

```python
def test_with_mock_context(mock_context):
    """Test that uses the mock_context fixture."""
    # mock_context is automatically initialized
    assert mock_context.region == 'us-east-1'
    
    # Test your code
    result = some_function()
    
    # Fixture automatically cleans up after test
```

### Property-Based Tests

```python
from hypothesis import given, strategies as st

@given(region=st.from_regex(r'^[a-z]{2}-[a-z]+-\d{1,2}$'))
def test_validate_region_property(region):
    """Property: All strings matching AWS region format should validate."""
    result = validate_region(region)
    assert result == region
```

## Debugging Failing Tests

### Run with Verbose Output

```bash
pytest -v tests/unit/test_input_validation.py
```

### Run with Print Statements

```bash
pytest -s tests/unit/test_input_validation.py
```

### Run with Debugger

```bash
pytest --pdb tests/unit/test_input_validation.py
```

### Show Local Variables on Failure

```bash
pytest -l tests/unit/test_input_validation.py
```

### Run Only Failed Tests

```bash
# Run tests, then re-run only failures
pytest --lf
```

## Continuous Integration

Tests run automatically on every push and pull request via GitHub Actions.

### CI Workflow

1. Install dependencies
2. Run full test suite with coverage
3. Fail if coverage drops below 70%
4. Upload coverage reports to codecov

### Local CI Simulation

```bash
# Run the same checks as CI
pytest --cov=code --cov-fail-under=70 --cov-report=xml
```

## Test Performance

### Target Execution Times

- **Unit tests**: < 100ms each
- **Integration tests**: < 1s each
- **Property tests**: < 5s each
- **Full suite**: < 5 minutes

### Measuring Test Performance

```bash
# Show slowest 10 tests
pytest --durations=10

# Show all test durations
pytest --durations=0
```

## Common Issues

### Tests Fail with "No module named 'code'"

Make sure you're running pytest from the workspace root:
```bash
cd /path/to/aws2tf
pytest
```

### Tests Fail with AWS Credential Errors

Tests should NOT require AWS credentials. If you see credential errors:
1. Check that tests use `@mock_aws` decorator
2. Verify boto3 clients are mocked
3. Ensure no real AWS API calls are made

### Coverage Report Shows Wrong Files

Make sure you're using the correct coverage source:
```bash
pytest --cov=code --cov-report=html
```

### Tests Are Too Slow

1. Run tests in parallel: `pytest -n auto`
2. Skip slow tests: `pytest -m "not slow"`
3. Run only changed tests: `pytest --lf`

## Contributing

When adding new code:
1. Write tests for new functionality
2. Ensure tests pass: `pytest`
3. Check coverage: `pytest --cov=code`
4. Update this README if adding new test categories

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
- [hypothesis documentation](https://hypothesis.readthedocs.io/)
- [moto documentation](https://docs.getmoto.org/)
