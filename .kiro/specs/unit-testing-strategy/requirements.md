# Requirements Document: Unit Testing Strategy for aws2tf

## Introduction

This document defines the requirements for implementing a comprehensive unit testing strategy for the aws2tf codebase. The aws2tf tool converts AWS infrastructure to Terraform configuration files by discovering AWS resources via boto3 APIs and generating corresponding Terraform code. The testing strategy aims to improve code resilience, catch regressions early, and provide confidence in the tool's correctness across the 200+ AWS resource types it supports.

## Glossary

- **aws2tf**: The AWS-to-Terraform conversion tool being tested
- **Resource_Handler**: Python modules in `code/fixtf_aws_resources/` that transform Terraform output for specific AWS resource types
- **Get_Function**: Python functions in `code/get_aws_resources/` that discover and list AWS resources via boto3
- **Test_Suite**: Collection of automated tests that validate system behavior
- **Coverage_Metric**: Percentage of code lines/branches executed by tests
- **Mock_Object**: Test double that simulates AWS API responses without making real API calls
- **Integration_Test**: Test that validates multiple components working together
- **Unit_Test**: Test that validates a single function or class in isolation
- **Property_Test**: Test that validates universal properties across many generated inputs
- **Regression_Test**: Test that prevents previously fixed bugs from reoccurring

## Requirements

### Requirement 1: Core Testing Infrastructure

**User Story:** As a developer, I want a standardized testing framework, so that I can write and run tests consistently across the codebase.

#### Acceptance Criteria

1. THE Test_Suite SHALL use pytest as the testing framework
2. THE Test_Suite SHALL organize tests in a `tests/` directory mirroring the `code/` structure
3. THE Test_Suite SHALL provide test fixtures for common setup (boto3 mocks, context initialization)
4. THE Test_Suite SHALL support running tests with `pytest` command from the workspace root
5. THE Test_Suite SHALL generate coverage reports showing line and branch coverage
6. THE Test_Suite SHALL integrate with CI/CD pipelines for automated execution
7. THE Test_Suite SHALL complete execution in under 5 minutes for the full suite

### Requirement 2: Input Validation Testing

**User Story:** As a security-conscious developer, I want comprehensive tests for input validation, so that path traversal and injection attacks are prevented.

#### Acceptance Criteria

1. WHEN testing `validate_region()`, THE Test_Suite SHALL verify valid AWS regions pass validation
2. WHEN testing `validate_region()`, THE Test_Suite SHALL verify invalid formats raise ValueError
3. WHEN testing `validate_resource_type()`, THE Test_Suite SHALL verify valid terraform types pass
4. WHEN testing `validate_resource_type()`, THE Test_Suite SHALL reject types with special characters
5. WHEN testing `validate_resource_id()`, THE Test_Suite SHALL reject path traversal attempts (`../`)
6. WHEN testing `validate_resource_id()`, THE Test_Suite SHALL reject shell metacharacters (`;`, `|`, `` ` ``)
7. WHEN testing `safe_filename()`, THE Test_Suite SHALL prevent directory traversal attacks
8. WHEN testing `safe_filename()`, THE Test_Suite SHALL verify resolved paths stay within base directory

### Requirement 3: AWS API Interaction Testing

**User Story:** As a developer, I want tests that validate AWS API interactions without making real API calls, so that tests run quickly and don't require AWS credentials.

#### Acceptance Criteria

1. THE Test_Suite SHALL use `moto` library for mocking AWS services
2. WHEN testing Get_Functions, THE Test_Suite SHALL mock boto3 client responses
3. WHEN testing Get_Functions, THE Test_Suite SHALL verify correct API methods are called
4. WHEN testing Get_Functions, THE Test_Suite SHALL verify pagination is handled correctly
5. WHEN testing Get_Functions, THE Test_Suite SHALL verify error handling for API failures
6. WHEN testing Get_Functions, THE Test_Suite SHALL verify `write_import()` is called with correct parameters
7. THE Test_Suite SHALL test at least 20 representative Get_Functions across different AWS services

### Requirement 4: Resource Handler Testing

**User Story:** As a developer, I want tests for resource handlers, so that Terraform output transformations are correct and don't cause drift.

#### Acceptance Criteria

1. WHEN testing Resource_Handlers, THE Test_Suite SHALL verify computed fields are skipped correctly
2. WHEN testing Resource_Handlers, THE Test_Suite SHALL verify lifecycle blocks are added appropriately
3. WHEN testing Resource_Handlers, THE Test_Suite SHALL verify parent resource dependencies are added
4. WHEN testing Resource_Handlers, THE Test_Suite SHALL verify field transformations (ID to resource reference)
5. WHEN testing Resource_Handlers, THE Test_Suite SHALL test at least 30 representative handlers
6. WHEN testing Resource_Handlers, THE Test_Suite SHALL verify JSON policy normalization handling
7. THE Test_Suite SHALL use property-based testing for handler field transformations

### Requirement 5: File Operations Testing

**User Story:** As a developer, I want tests for file operations, so that generated Terraform files are correct and secure.

#### Acceptance Criteria

1. WHEN testing `safe_write_file()`, THE Test_Suite SHALL verify files are created with correct permissions
2. WHEN testing `safe_write_file()`, THE Test_Suite SHALL verify path traversal is prevented
3. WHEN testing `safe_write_sensitive_file()`, THE Test_Suite SHALL verify 0o600 permissions are set
4. WHEN testing `secure_terraform_files()`, THE Test_Suite SHALL verify state files get 0o600 permissions
5. WHEN testing file generation, THE Test_Suite SHALL verify import statements are correctly formatted
6. WHEN testing file generation, THE Test_Suite SHALL verify resource blocks have proper syntax
7. THE Test_Suite SHALL test file operations on both Unix and Windows paths

### Requirement 6: Command-Line Argument Parsing Testing

**User Story:** As a developer, I want tests for CLI argument parsing, so that invalid inputs are rejected before processing begins.

#### Acceptance Criteria

1. WHEN testing `parse_and_validate_arguments()`, THE Test_Suite SHALL verify valid argument combinations pass
2. WHEN testing `parse_and_validate_arguments()`, THE Test_Suite SHALL verify invalid regions are rejected
3. WHEN testing `parse_and_validate_arguments()`, THE Test_Suite SHALL verify invalid resource types are rejected
4. WHEN testing `parse_and_validate_arguments()`, THE Test_Suite SHALL verify dangerous resource IDs are rejected
5. WHEN testing `parse_and_validate_arguments()`, THE Test_Suite SHALL verify EC2 tag format validation
6. WHEN testing `parse_and_validate_arguments()`, THE Test_Suite SHALL verify Terraform version format validation
7. THE Test_Suite SHALL test all argument validation functions independently

### Requirement 7: Context Management Testing

**User Story:** As a developer, I want tests for context state management, so that global state is correctly initialized and maintained.

#### Acceptance Criteria

1. WHEN testing context initialization, THE Test_Suite SHALL verify all required attributes are set
2. WHEN testing context, THE Test_Suite SHALL verify resource tracking dictionaries are initialized
3. WHEN testing context, THE Test_Suite SHALL verify region and account information is stored correctly
4. WHEN testing context, THE Test_Suite SHALL verify merge mode state is tracked correctly
5. WHEN testing context, THE Test_Suite SHALL verify exclusion lists are maintained correctly
6. THE Test_Suite SHALL test context isolation between test runs
7. THE Test_Suite SHALL verify context is thread-safe for multi-threaded operations

### Requirement 8: Resource Discovery Testing

**User Story:** As a developer, I want tests for resource discovery logic, so that all AWS resources in an account are correctly identified.

#### Acceptance Criteria

1. WHEN testing `build_lists()`, THE Test_Suite SHALL verify VPCs are discovered and stored
2. WHEN testing `build_lists()`, THE Test_Suite SHALL verify Lambda functions are discovered
3. WHEN testing `build_lists()`, THE Test_Suite SHALL verify S3 buckets are discovered
4. WHEN testing `build_lists()`, THE Test_Suite SHALL verify security groups are discovered
5. WHEN testing `build_lists()`, THE Test_Suite SHALL verify subnets are discovered and JSON is saved
6. WHEN testing `build_lists()`, THE Test_Suite SHALL verify IAM roles are discovered
7. WHEN testing `build_lists()`, THE Test_Suite SHALL verify parallel execution completes successfully
8. WHEN testing `build_secondary_lists()`, THE Test_Suite SHALL verify IAM policy attachments are fetched

### Requirement 9: Error Handling Testing

**User Story:** As a developer, I want tests for error handling, so that failures are gracefully handled and reported.

#### Acceptance Criteria

1. WHEN testing error handling, THE Test_Suite SHALL verify boto3 ClientError exceptions are caught
2. WHEN testing error handling, THE Test_Suite SHALL verify expired credentials are detected
3. WHEN testing error handling, THE Test_Suite SHALL verify network errors are handled gracefully
4. WHEN testing error handling, THE Test_Suite SHALL verify missing resources return appropriate messages
5. WHEN testing error handling, THE Test_Suite SHALL verify partial failures don't crash the tool
6. THE Test_Suite SHALL test error handling for at least 10 common failure scenarios
7. THE Test_Suite SHALL verify error messages are logged with appropriate severity

### Requirement 10: Terraform Integration Testing

**User Story:** As a developer, I want tests for Terraform command execution, so that generated files can be validated and applied.

#### Acceptance Criteria

1. WHEN testing Terraform integration, THE Test_Suite SHALL verify `terraform init` is called correctly
2. WHEN testing Terraform integration, THE Test_Suite SHALL verify `terraform validate` detects syntax errors
3. WHEN testing Terraform integration, THE Test_Suite SHALL verify `terraform plan` output is parsed correctly
4. WHEN testing Terraform integration, THE Test_Suite SHALL verify import counts are extracted from plan JSON
5. WHEN testing Terraform integration, THE Test_Suite SHALL verify progress tracking works for plan/apply
6. THE Test_Suite SHALL mock Terraform command execution to avoid requiring Terraform installation
7. THE Test_Suite SHALL test Terraform version checking logic

### Requirement 11: Dependency Resolution Testing

**User Story:** As a developer, I want tests for dependency resolution, so that parent resources are imported before child resources.

#### Acceptance Criteria

1. WHEN testing `add_dependancy()`, THE Test_Suite SHALL verify dependencies are tracked correctly
2. WHEN testing dependency resolution, THE Test_Suite SHALL verify parent resources are queued for import
3. WHEN testing dependency resolution, THE Test_Suite SHALL verify circular dependencies are detected
4. WHEN testing dependency resolution, THE Test_Suite SHALL verify dependency order is correct
5. THE Test_Suite SHALL test dependency resolution for at least 10 resource type pairs
6. THE Test_Suite SHALL verify resources in `needid_dict` require parent IDs
7. THE Test_Suite SHALL test multi-level dependency chains (grandparent → parent → child)

### Requirement 12: Module Registry Testing

**User Story:** As a developer, I want tests for the module registry, so that resource handlers are correctly loaded without using eval().

#### Acceptance Criteria

1. WHEN testing module registry, THE Test_Suite SHALL verify all services in `AWS_RESOURCE_MODULES` are valid
2. WHEN testing module registry, THE Test_Suite SHALL verify handler modules can be loaded dynamically
3. WHEN testing module registry, THE Test_Suite SHALL verify missing modules are handled gracefully
4. WHEN testing module registry, THE Test_Suite SHALL verify hyphenated service names are resolved correctly
5. THE Test_Suite SHALL verify the registry contains entries for all imported get_aws_resources modules
6. THE Test_Suite SHALL verify the registry prevents arbitrary code execution
7. THE Test_Suite SHALL test module loading for at least 50 AWS services

### Requirement 13: Progress Tracking Testing

**User Story:** As a developer, I want tests for progress tracking, so that users see accurate progress during long operations.

#### Acceptance Criteria

1. WHEN testing progress tracking, THE Test_Suite SHALL verify progress bars are created correctly
2. WHEN testing progress tracking, THE Test_Suite SHALL verify adaptive rate learning updates correctly
3. WHEN testing progress tracking, THE Test_Suite SHALL verify progress caps at 75% until completion
4. WHEN testing progress tracking, THE Test_Suite SHALL verify progress jumps to 100% on completion
5. THE Test_Suite SHALL test progress tracking for terraform plan operations
6. THE Test_Suite SHALL test progress tracking for terraform apply operations
7. THE Test_Suite SHALL verify progress tracking is disabled in debug mode

### Requirement 14: Property-Based Testing

**User Story:** As a developer, I want property-based tests, so that edge cases and unexpected inputs are automatically discovered.

#### Acceptance Criteria

1. THE Test_Suite SHALL use `hypothesis` library for property-based testing
2. WHEN testing input validation, THE Test_Suite SHALL generate random strings and verify validation
3. WHEN testing resource handlers, THE Test_Suite SHALL generate random Terraform blocks
4. WHEN testing file operations, THE Test_Suite SHALL generate random filenames and paths
5. THE Test_Suite SHALL run at least 100 iterations per property test
6. THE Test_Suite SHALL save failing examples for regression testing
7. THE Test_Suite SHALL test at least 10 properties across the codebase

### Requirement 15: Integration Testing

**User Story:** As a developer, I want integration tests, so that end-to-end workflows are validated.

#### Acceptance Criteria

1. THE Test_Suite SHALL include integration tests for complete resource import workflows
2. WHEN testing integration, THE Test_Suite SHALL verify VPC discovery → import → file generation
3. WHEN testing integration, THE Test_Suite SHALL verify Lambda discovery → import → file generation
4. WHEN testing integration, THE Test_Suite SHALL verify S3 discovery → import → file generation
5. THE Test_Suite SHALL test at least 5 complete end-to-end workflows
6. THE Test_Suite SHALL use mocked AWS APIs for integration tests
7. THE Test_Suite SHALL verify generated Terraform files are syntactically valid

### Requirement 16: Regression Testing

**User Story:** As a developer, I want regression tests, so that previously fixed bugs don't reoccur.

#### Acceptance Criteria

1. THE Test_Suite SHALL include tests for all previously reported GitHub issues
2. WHEN a bug is fixed, THE Test_Suite SHALL add a regression test before closing the issue
3. THE Test_Suite SHALL maintain a regression test suite that runs on every commit
4. THE Test_Suite SHALL document which test covers which bug/issue
5. THE Test_Suite SHALL test at least 20 historical bug fixes
6. THE Test_Suite SHALL verify security fixes remain effective
7. THE Test_Suite SHALL test edge cases discovered during manual testing

### Requirement 17: Coverage Requirements

**User Story:** As a project maintainer, I want high test coverage, so that I can be confident in code quality.

#### Acceptance Criteria

1. THE Test_Suite SHALL achieve at least 70% line coverage for core modules
2. THE Test_Suite SHALL achieve at least 60% branch coverage for core modules
3. THE Test_Suite SHALL achieve at least 80% coverage for input validation functions
4. THE Test_Suite SHALL achieve at least 60% coverage for resource handlers
5. THE Test_Suite SHALL achieve at least 70% coverage for Get_Functions
6. THE Test_Suite SHALL generate HTML coverage reports
7. THE Test_Suite SHALL fail CI builds if coverage drops below thresholds

### Requirement 18: Test Documentation

**User Story:** As a developer, I want well-documented tests, so that I understand what each test validates.

#### Acceptance Criteria

1. WHEN writing tests, THE Test_Suite SHALL include docstrings explaining test purpose
2. WHEN writing tests, THE Test_Suite SHALL use descriptive test function names
3. WHEN writing tests, THE Test_Suite SHALL document expected behavior and edge cases
4. THE Test_Suite SHALL include a README.md in the tests/ directory
5. THE Test_Suite SHALL document how to run tests locally
6. THE Test_Suite SHALL document how to run specific test subsets
7. THE Test_Suite SHALL document how to interpret coverage reports

### Requirement 19: Performance Testing

**User Story:** As a developer, I want performance tests, so that the tool remains fast as features are added.

#### Acceptance Criteria

1. THE Test_Suite SHALL include performance benchmarks for resource discovery
2. THE Test_Suite SHALL include performance benchmarks for file generation
3. WHEN testing performance, THE Test_Suite SHALL verify build_lists() completes in under 30 seconds
4. WHEN testing performance, THE Test_Suite SHALL verify single resource import completes in under 5 seconds
5. THE Test_Suite SHALL track performance metrics over time
6. THE Test_Suite SHALL fail if performance regresses by more than 20%
7. THE Test_Suite SHALL test multi-threaded performance vs single-threaded

### Requirement 20: Test Maintenance

**User Story:** As a developer, I want maintainable tests, so that tests don't become a burden.

#### Acceptance Criteria

1. THE Test_Suite SHALL use shared fixtures to reduce code duplication
2. THE Test_Suite SHALL use helper functions for common test patterns
3. THE Test_Suite SHALL avoid brittle tests that break with minor code changes
4. THE Test_Suite SHALL use parameterized tests for testing multiple similar cases
5. THE Test_Suite SHALL keep individual test functions under 50 lines
6. THE Test_Suite SHALL organize tests into logical modules
7. THE Test_Suite SHALL provide clear failure messages when tests fail
