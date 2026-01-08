# aws2tf Testing Guide

**Quick Start Guide for Running and Understanding Tests**

## Overview

The aws2tf project has a comprehensive test suite with 200+ tests covering unit tests, integration tests, property-based tests, and performance benchmarks. This guide helps you quickly navigate the test documentation and run the tests you need.

## 📚 Essential Documentation

### Start Here

1. **[tests/README.md](../tests/README.md)** - **READ THIS FIRST**
   - Complete test suite documentation
   - How to run tests (all tests, specific subsets, with coverage)
   - Test organization and structure
   - Writing new tests
   - Debugging failing tests
   - CI/CD integration

### Test Categories

The test suite is organized into these directories:

- **`tests/unit/`** - Unit tests for individual functions and modules
  - Fast tests (< 100ms each)
  - Test individual functions in isolation
  - Mock external dependencies (AWS APIs, file I/O)
  
- **`tests/integration/`** - End-to-end workflow tests
  - Test complete workflows (discovery → import → generation)
  - Verify multiple components work together
  - Slower tests (< 1s each)

- **`tests/property/`** - Property-based tests using Hypothesis
  - Test universal properties across many generated inputs
  - Catch edge cases that example-based tests miss
  - Validate correctness properties

- **`tests/regression/`** - Tests for previously fixed bugs
  - Prevent bugs from reappearing
  - Document historical issues

- **`tests/performance/`** - Performance benchmarks
  - Track execution time improvements
  - Identify performance regressions

## 🚀 Quick Start Commands

### Run All Tests
```bash
pytest
```

### Run Unit Tests Only (Fast)
```bash
pytest tests/unit/
```

### Run with Coverage Report
```bash
pytest --cov=code --cov-report=html
# Open htmlcov/index.html in browser
```

### Run Specific Test File
```bash
# Test resource discovery (build_lists.py)
pytest tests/unit/test_resource_discovery.py -v

# Test error handling
pytest tests/unit/test_error_handling.py -v

# Test input validation
pytest tests/unit/test_input_validation.py -v
```

### Run Tests in Parallel (Faster)
```bash
pytest -n auto
```

## 📋 Key Unit Test Files

### Core Functionality Tests

| Test File | What It Tests | Key Functions |
|-----------|---------------|---------------|
| **test_resource_discovery.py** | AWS resource discovery and listing | `build_lists()`, `build_secondary_lists()` |
| **test_error_handling.py** | Error handling and resilience | Exception handling, logging |
| **test_input_validation.py** | CLI argument validation | Region validation, resource type validation |
| **test_cli_parsing.py** | Command-line argument parsing | Argument parsing, flag handling |
| **test_context.py** | Global context management | Context initialization, state management |
| **test_file_operations.py** | File I/O operations | JSON writing, file creation |
| **test_module_registry.py** | Handler module registration | Module loading, registry lookup |
| **test_progress_tracking.py** | Progress bar and status updates | Progress reporting, time estimation |

### Handler Tests

Located in `tests/unit/handlers/`:
- Test resource-specific handler functions
- Verify Terraform generation for each AWS resource type
- Example: `test_handler_vpc.py`, `test_handler_lambda.py`

### Get Function Tests

Located in `tests/unit/get_functions/`:
- Test AWS resource discovery functions
- Verify API calls and response parsing
- Example: `test_get_vpc.py`, `test_get_lambda.py`

## 🎯 Testing the build_lists.py Optimization

The recent optimization of `build_lists.py` is thoroughly tested:

### Run build_lists Tests
```bash
# All resource discovery tests
pytest tests/unit/test_resource_discovery.py -v

# Specific test classes
pytest tests/unit/test_resource_discovery.py::TestBuildListsVPC -v
pytest tests/unit/test_resource_discovery.py::TestBuildListsLambda -v
pytest tests/unit/test_resource_discovery.py::TestBuildListsS3 -v
```

### Test Coverage
```bash
# Check coverage for build_lists.py specifically
pytest tests/unit/test_resource_discovery.py --cov=code.build_lists --cov-report=term-missing
```

### Related Documentation
- [build-lists-optimization-summary.md](build-lists-optimization-summary.md) - Optimization overview
- [build-lists-optimization-code-quality-report.md](build-lists-optimization-code-quality-report.md) - Code quality metrics

## 🔍 Understanding Test Results

### Successful Test Run
```
============================= test session starts ==============================
tests/unit/test_resource_discovery.py::TestBuildListsVPC::test_discovers_vpcs PASSED
tests/unit/test_resource_discovery.py::TestBuildListsVPC::test_handles_no_vpcs PASSED
...
============================== 11 passed in 7.98s ==============================
```

### Failed Test
```
FAILED tests/unit/test_resource_discovery.py::test_discovers_vpcs - AssertionError
```

To debug:
```bash
# Run with verbose output and show local variables
pytest tests/unit/test_resource_discovery.py::test_discovers_vpcs -vl

# Run with debugger
pytest tests/unit/test_resource_discovery.py::test_discovers_vpcs --pdb
```

## 📊 Coverage Reports

### Generate HTML Coverage Report
```bash
pytest --cov=code --cov-report=html
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

### Coverage Thresholds
- **Core modules**: 70% minimum
- **Input validation**: 80% minimum
- **Resource handlers**: 60% minimum

### Check Coverage for Specific Module
```bash
pytest --cov=code.build_lists --cov-report=term-missing
```

## 🐛 Debugging Tests

### Show Print Statements
```bash
pytest -s tests/unit/test_resource_discovery.py
```

### Show Detailed Failure Info
```bash
pytest -vl tests/unit/test_resource_discovery.py
```

### Run Only Failed Tests
```bash
# First run
pytest

# Re-run only failures
pytest --lf
```

### Show Slowest Tests
```bash
pytest --durations=10
```

## 🔧 Common Issues

### "No module named 'code'"
**Solution:** Run pytest from workspace root:
```bash
cd /path/to/aws2tf
pytest
```

### AWS Credential Errors
**Solution:** Tests should NOT require AWS credentials. They use mocked AWS APIs.
- Check tests use `@mock_aws` decorator
- Verify boto3 clients are mocked

### Tests Are Slow
**Solutions:**
```bash
# Run in parallel
pytest -n auto

# Skip slow tests
pytest -m "not slow"

# Run only unit tests
pytest tests/unit/
```

## 📖 Additional Resources

### Test Documentation
- **[tests/README.md](../tests/README.md)** - Complete test suite guide
- **[tests/conftest.py](../tests/conftest.py)** - Shared fixtures and configuration

### Optimization Documentation
- **[build-lists-optimization-summary.md](build-lists-optimization-summary.md)** - Optimization overview
- **[build-lists-optimization-code-quality-report.md](build-lists-optimization-code-quality-report.md)** - Detailed metrics

### External Resources
- [pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
- [hypothesis documentation](https://hypothesis.readthedocs.io/)
- [moto documentation](https://docs.getmoto.org/) (AWS mocking)

## 🎓 Next Steps

1. **Read** [tests/README.md](../tests/README.md) for comprehensive documentation
2. **Run** `pytest tests/unit/` to verify your environment
3. **Explore** specific test files relevant to your work
4. **Write** new tests when adding features
5. **Check** coverage with `pytest --cov=code`

## 💡 Pro Tips

- **Run tests frequently** during development
- **Use `-n auto`** for faster test runs
- **Check coverage** before committing
- **Write tests first** (TDD) when fixing bugs
- **Use property tests** for complex logic
- **Mock AWS APIs** - never make real API calls in tests

---

**Questions?** Check [tests/README.md](../tests/README.md) or ask the team!
