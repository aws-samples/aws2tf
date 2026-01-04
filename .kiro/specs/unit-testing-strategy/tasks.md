# Implementation Plan: Unit Testing Strategy for aws2tf

## Overview

This implementation plan breaks down the unit testing strategy into discrete, actionable tasks. The plan follows a phased approach over 5 weeks, starting with foundational infrastructure and progressing to comprehensive coverage of all modules. Each task builds on previous work and includes validation steps.

## Tasks

- [x] 1. Set up testing infrastructure and dependencies
  - Install pytest, pytest-cov, pytest-mock, hypothesis, moto, pytest-xdist
  - Create tests/ directory structure (unit/, integration/, property/, regression/, performance/)
  - Create tests/README.md with documentation on running tests
  - _Requirements: 1.1, 1.2, 18.5, 18.6_

- [x] 2. Create shared test fixtures (conftest.py)
  - [x] 2.1 Create mock_boto3_client fixture
    - Mock boto3.client with configurable responses
    - Support common AWS services (ec2, s3, iam, lambda)
    - _Requirements: 1.3_

  - [x] 2.2 Create mock_context fixture
    - Reset context state before each test
    - Initialize with test defaults (region, account, flags)
    - Clean up after test completion
    - _Requirements: 1.3, 7.6_

  - [x] 2.3 Create temp_workspace fixture
    - Create temporary directory structure
    - Set up generated/ and imported/ subdirectories
    - Clean up after test
    - _Requirements: 1.3_

  - [x] 2.4 Create mock_terraform fixture
    - Mock common.rc() for terraform commands
    - Configure responses for init, validate, plan, apply
    - _Requirements: 1.3_

  - [x] 2.5 Create reset_context autouse fixture
    - Automatically reset context before/after each test
    - Ensure test isolation
    - _Requirements: 7.6_

- [x] 3. Implement input validation tests
  - [x] 3.1 Create tests/unit/test_input_validation.py
    - Test validate_region() with valid AWS regions
    - Test validate_region() rejects invalid formats
    - Test validate_region() rejects path traversal attempts
    - _Requirements: 2.1, 2.2_

  - [x] 3.2 Test resource type validation
    - Test validate_resource_type() with valid terraform types
    - Test validate_resource_type() rejects special characters
    - Test validate_resource_type() handles comma-separated lists
    - _Requirements: 2.3, 2.4_

  - [x] 3.3 Test resource ID validation
    - Test validate_resource_id() accepts valid AWS IDs and ARNs
    - Test validate_resource_id() rejects path traversal (..)
    - Test validate_resource_id() rejects shell metacharacters
    - _Requirements: 2.5, 2.6_

  - [x] 3.4 Test EC2 tag validation
    - Test validate_ec2_tag() with valid key:value pairs
    - Test validate_ec2_tag() rejects invalid formats
    - Test validate_ec2_tag() rejects empty keys/values
    - _Requirements: 2.7_

  - [x] 3.5 Test profile and version validation
    - Test validate_profile() with valid profile names
    - Test validate_terraform_version() with valid versions
    - Test rejection of invalid inputs
    - _Requirements: 2.8_

- [x] 4. Implement file operations tests
  - [x] 4.1 Create tests/unit/test_file_operations.py
    - Test safe_filename() prevents path traversal
    - Test safe_filename() sanitizes dangerous characters
    - Test safe_filename() resolves paths within base directory
    - _Requirements: 2.7, 5.1, 5.2_

  - [x] 4.2 Test safe_write_file()
    - Test file creation with correct permissions (0o644)
    - Test subdirectory handling
    - Test path traversal prevention
    - _Requirements: 5.1, 5.2_

  - [x] 4.3 Test safe_write_sensitive_file()
    - Test sensitive files get 0o600 permissions
    - Test permissions are verified after creation
    - _Requirements: 5.3_

  - [x] 4.4 Test secure_terraform_files()
    - Test terraform.tfstate gets 0o600
    - Test .tfvars files get 0o600
    - Test .terraform.lock.hcl gets 0o644
    - _Requirements: 5.4_

  - [x] 4.5 Test import file generation
    - Test import statements are correctly formatted
    - Test resource blocks have proper syntax
    - _Requirements: 5.5, 5.6_

- [x] 5. Implement CLI argument parsing tests
  - [x] 5.1 Create tests/unit/test_cli_parsing.py
    - Test parse_and_validate_arguments() with valid combinations
    - Test rejection of invalid regions
    - Test rejection of invalid resource types
    - Test rejection of dangerous resource IDs
    - _Requirements: 6.1, 6.2, 6.3, 6.4_

  - [x] 5.2 Test argument validation integration
    - Test EC2 tag format validation in CLI
    - Test Terraform version validation in CLI
    - Test exclude list parsing
    - _Requirements: 6.5, 6.6_

  - [x] 5.3 Test error handling for invalid arguments
    - Test appropriate error messages are shown
    - Test tool exits with correct exit codes
    - _Requirements: 6.7_

- [x] 6. Implement context management tests
  - [x] 6.1 Create tests/unit/test_context.py
    - Test context initialization sets all required attributes
    - Test resource tracking dictionaries are initialized
    - Test region and account information storage
    - _Requirements: 7.1, 7.2, 7.3_

  - [x] 6.2 Test context state management
    - Test merge mode state tracking
    - Test exclusion lists maintenance
    - Test context isolation between tests
    - _Requirements: 7.4, 7.5, 7.6_

  - [x] 6.3 Test context thread safety
    - Test concurrent access to context dictionaries
    - Test thread-safe operations
    - _Requirements: 7.7_

- [x] 7. Checkpoint - Ensure all tests pass
  - Run pytest to verify all tests pass
  - Check coverage is at least 40%
  - Ask the user if questions arise

- [x] 8. Implement resource discovery tests
  - [x] 8.1 Create tests/unit/test_resource_discovery.py with moto
    - Set up @mock_aws decorator for tests
    - Create mock VPCs, Lambda functions, S3 buckets
    - _Requirements: 8.1, 8.2, 8.3_

  - [x] 8.2 Test build_lists() VPC discovery
    - Test VPCs are discovered and stored in context.vpclist
    - Test pagination handling
    - _Requirements: 8.1_

  - [x] 8.3 Test build_lists() Lambda discovery
    - Test Lambda functions are discovered
    - Test stored in context.lambdalist
    - _Requirements: 8.2_

  - [x] 8.4 Test build_lists() S3 discovery
    - Test S3 buckets are discovered
    - Test stored in context.s3list
    - _Requirements: 8.3_

  - [x] 8.5 Test build_lists() security group discovery
    - Test security groups are discovered
    - Test stored in context.sglist
    - _Requirements: 8.4_

  - [x] 8.6 Test build_lists() subnet discovery
    - Test subnets are discovered
    - Test JSON file is saved to imported/subnets.json
    - _Requirements: 8.5_

  - [x] 8.7 Test build_lists() IAM role discovery
    - Test IAM roles are discovered
    - Test stored in context.rolelist
    - _Requirements: 8.6_

  - [x] 8.8 Test build_lists() parallel execution
    - Test ThreadPoolExecutor completes successfully
    - Test all resource types are processed
    - _Requirements: 8.7_

  - [x] 8.9 Test build_secondary_lists() IAM policies
    - Test attached policies are fetched
    - Test inline policies are fetched
    - Test stored in context dictionaries
    - _Requirements: 8.8_

- [x] 9. Implement error handling tests
  - [x] 9.1 Create tests/unit/test_error_handling.py
    - Test boto3 ClientError exceptions are caught
    - Test expired credentials are detected
    - Test network errors are handled gracefully
    - _Requirements: 9.1, 9.2, 9.3_

  - [x] 9.2 Test resource not found handling
    - Test missing resources return appropriate messages
    - Test partial failures don't crash the tool
    - _Requirements: 9.4, 9.5_

  - [x] 9.3 Test error logging
    - Test error messages are logged with appropriate severity
    - Test at least 10 common failure scenarios
    - _Requirements: 9.6, 9.7_

- [x] 10. Implement module registry tests
  - [x] 10.1 Create tests/unit/test_module_registry.py
    - Test all services in AWS_RESOURCE_MODULES are valid
    - Test modules can be loaded dynamically
    - Test missing modules are handled gracefully
    - _Requirements: 12.1, 12.2, 12.3_

  - [x] 10.2 Test hyphenated service names
    - Test 'workspaces-web' resolves correctly
    - Test other hyphenated names
    - _Requirements: 12.4_

  - [x] 10.3 Test registry completeness
    - Test registry contains entries for all imported modules
    - Test at least 50 AWS services
    - _Requirements: 12.5, 12.7_

  - [x] 10.4 Test security of module loading
    - Test registry prevents arbitrary code execution
    - Test no eval() is used
    - _Requirements: 12.6_

- [x] 11. Implement progress tracking tests
  - [x] 11.1 Create tests/unit/test_progress_tracking.py
    - Test progress bars are created correctly
    - Test progress tracking is disabled in debug mode
    - _Requirements: 13.1, 13.7_

  - [x] 11.2 Test adaptive rate learning
    - Test terraform_plan_rate updates correctly
    - Test exponential moving average calculation
    - _Requirements: 13.2_

  - [x] 11.3 Test progress capping
    - Test progress caps at 75% until completion
    - Test progress jumps to 100% on completion
    - _Requirements: 13.3, 13.4_

  - [x] 11.4 Test progress for terraform operations
    - Test progress tracking for terraform plan
    - Test progress tracking for terraform apply
    - _Requirements: 13.5, 13.6_

- [x] 12. Checkpoint - Ensure all tests pass
  - Run pytest to verify all tests pass
  - Check coverage is at least 60%
  - Ask the user if questions arise

- [x] 13. Implement get function tests (10 representative services)
  - [x] 13.1 Create tests/unit/get_functions/test_get_ec2.py
    - Test get_aws_vpc() with mocked EC2 client
    - Test pagination handling
    - Test write_import() is called correctly
    - _Requirements: 3.2, 3.3, 3.4, 3.6_

  - [x] 13.2 Create tests/unit/get_functions/test_get_s3.py
    - Test get_aws_s3_bucket() with mocked S3 client
    - Test error handling for API failures
    - _Requirements: 3.2, 3.5_

  - [x] 13.3 Create tests/unit/get_functions/test_get_iam.py
    - Test get_aws_iam_role() with mocked IAM client
    - Test pagination and error handling
    - _Requirements: 3.2, 3.4, 3.5_

  - [x] 13.4 Create tests/unit/get_functions/test_get_lambda.py
    - Test get_aws_lambda_function() with mocked Lambda client
    - _Requirements: 3.2, 3.4_

  - [x] 13.5 Create tests/unit/get_functions/test_get_dynamodb.py
    - Test get_aws_dynamodb_table() with mocked DynamoDB client
    - _Requirements: 3.2, 3.4_

  - [x] 13.6 Create tests/unit/get_functions/test_get_rds.py
    - Test get_aws_db_instance() with mocked RDS client
    - _Requirements: 3.2, 3.4_

  - [x] 13.7 Create tests/unit/get_functions/test_get_eks.py
    - Test get_aws_eks_cluster() with mocked EKS client
    - _Requirements: 3.2, 3.4_

  - [x] 13.8 Create tests/unit/get_functions/test_get_elbv2.py
    - Test get_aws_lb() with mocked ELBv2 client
    - _Requirements: 3.2, 3.4_

  - [x] 13.9 Create tests/unit/get_functions/test_get_cloudwatch.py
    - Test get_aws_cloudwatch_log_group() with mocked CloudWatch client
    - _Requirements: 3.2, 3.4_

  - [x] 13.10 Create tests/unit/get_functions/test_get_sns.py
    - Test get_aws_sns_topic() with mocked SNS client
    - _Requirements: 3.2, 3.4_

  - [x] 13.11 Verify get function test coverage
    - Ensure at least 20 representative get functions are tested
    - _Requirements: 3.7_

- [x] 14. Implement resource handler tests (10 representative services)
  - [x] 14.1 Create tests/unit/handlers/test_handler_ec2.py
    - Test aws_vpc() skips computed fields (arn, id)
    - Test aws_subnet() adds lifecycle blocks
    - Test aws_security_group() handles dependencies
    - _Requirements: 4.1, 4.2, 4.3_

  - [x] 14.2 Create tests/unit/handlers/test_handler_s3.py
    - Test aws_s3_bucket() skips computed fields
    - Test aws_s3_bucket_policy() adds lifecycle for JSON normalization
    - _Requirements: 4.1, 4.6_

  - [x] 14.3 Create tests/unit/handlers/test_handler_iam.py
    - Test aws_iam_role() transforms assume_role_policy
    - Test aws_iam_policy() handles JSON normalization
    - _Requirements: 4.4, 4.6_

  - [x] 14.4 Create tests/unit/handlers/test_handler_lambda.py
    - Test aws_lambda_function() skips computed fields
    - Test field transformations for IAM role references
    - _Requirements: 4.1, 4.4_

  - [x] 14.5 Create tests/unit/handlers/test_handler_dynamodb.py
    - Test aws_dynamodb_table() handles lifecycle blocks
    - _Requirements: 4.2_

  - [x] 14.6 Create tests/unit/handlers/test_handler_rds.py
    - Test aws_db_instance() skips computed fields
    - Test dependency handling for VPC/subnet references
    - _Requirements: 4.1, 4.3_

  - [x] 14.7 Create tests/unit/handlers/test_handler_eks.py
    - Test aws_eks_cluster() handles dependencies
    - _Requirements: 4.3_

  - [x] 14.8 Create tests/unit/handlers/test_handler_apigateway.py
    - Test aws_api_gateway_rest_api() transformations
    - Test parent resource dependency handling
    - _Requirements: 4.3, 4.4_

  - [x] 14.9 Create tests/unit/handlers/test_handler_cloudwatch.py
    - Test aws_cloudwatch_log_group() handler
    - _Requirements: 4.1_

  - [x] 14.10 Create tests/unit/handlers/test_handler_sns.py
    - Test aws_sns_topic() handler
    - _Requirements: 4.1_

  - [x] 14.11 Verify handler test coverage
    - Ensure at least 30 representative handlers are tested
    - _Requirements: 4.5_

- [x] 15. Checkpoint - Ensure all tests pass
  - Run pytest to verify all tests pass
  - Check coverage is at least 65%
  - Ask the user if questions arise

- [x] 16. Implement property-based tests
  - [x] 16.1 Create tests/property/test_input_properties.py
    - Use hypothesis to generate random region strings
    - Test validate_region() with generated inputs
    - Use hypothesis to generate random resource types
    - Test validate_resource_type() with generated inputs
    - _Requirements: 14.2_

  - [x] 16.2 Create tests/property/test_handler_properties.py
    - Generate random Terraform blocks
    - Test handlers don't crash on any input
    - Test handlers preserve valid Terraform syntax
    - _Requirements: 14.3, 4.7_

  - [x] 16.3 Create tests/property/test_file_properties.py
    - Generate random filenames and paths
    - Test safe_filename() always prevents traversal
    - Test file operations maintain security
    - _Requirements: 14.4_

  - [x] 16.4 Configure property test settings
    - Set max_examples=100 for all property tests
    - Configure deadline=None for slow properties
    - _Requirements: 14.5_

  - [x] 16.5 Implement property test failure persistence
    - Configure hypothesis to save failing examples
    - Create regression tests from failures
    - _Requirements: 14.6_

  - [x] 16.6 Verify property test coverage
    - Ensure at least 10 properties are tested
    - _Requirements: 14.7_

- [x] 17. Implement integration tests
  - [x] 17.1 Create tests/integration/test_vpc_workflow.py
    - Test complete VPC discovery → import → file generation
    - Use mocked AWS APIs
    - Verify generated Terraform files are syntactically valid
    - _Requirements: 15.2, 15.6, 15.7_

  - [x] 17.2 Create tests/integration/test_lambda_workflow.py
    - Test complete Lambda discovery → import → file generation
    - _Requirements: 15.3_

  - [x] 17.3 Create tests/integration/test_s3_workflow.py
    - Test complete S3 discovery → import → file generation
    - _Requirements: 15.4_

  - [x] 17.4 Create tests/integration/test_iam_workflow.py
    - Test IAM role discovery → import → file generation
    - _Requirements: 15.1_

  - [x] 17.5 Create tests/integration/test_dependency_workflow.py
    - Test parent-child resource dependency resolution
    - Test multi-level dependency chains
    - _Requirements: 15.1_

  - [x] 17.6 Verify integration test coverage
    - Ensure at least 5 complete end-to-end workflows
    - _Requirements: 15.5_

- [ ] 18. Implement regression tests
  - [ ] 18.1 Create tests/regression/test_github_issues.py
    - Add test for each previously reported GitHub issue
    - Document which test covers which issue
    - _Requirements: 16.1, 16.4_

  - [ ] 18.2 Create tests/regression/test_security_fixes.py
    - Test all security fixes remain effective
    - Test path traversal prevention
    - Test input validation security
    - _Requirements: 16.6_

  - [ ] 18.3 Add regression tests for edge cases
    - Test edge cases discovered during manual testing
    - _Requirements: 16.7_

  - [ ] 18.4 Verify regression test coverage
    - Ensure at least 20 historical bug fixes are tested
    - _Requirements: 16.5_

  - [ ] 18.5 Set up regression test suite
    - Configure to run on every commit
    - Add to CI/CD pipeline
    - _Requirements: 16.3_

- [x] 19. Implement performance tests
  - [x] 19.1 Create tests/performance/test_discovery_performance.py
    - Benchmark build_lists() execution time
    - Test completes in under 30 seconds
    - _Requirements: 19.1, 19.3_

  - [x] 19.2 Create tests/performance/test_generation_performance.py
    - Benchmark file generation for single resource
    - Test completes in under 5 seconds
    - _Requirements: 19.2, 19.4_

  - [x] 19.3 Implement performance tracking
    - Track performance metrics over time
    - Store baseline performance data
    - _Requirements: 19.5_

  - [x] 19.4 Implement performance regression detection
    - Fail if performance regresses by more than 20%
    - _Requirements: 19.6_

  - [x] 19.5 Test multi-threaded vs single-threaded performance
    - Compare execution times
    - Verify multi-threading provides speedup
    - _Requirements: 19.7_

- [x] 20. Checkpoint - Ensure all tests pass
  - Run pytest to verify all tests pass
  - Check coverage is at least 70%
  - Ask the user if questions arise

- [ ] 21. Implement CI/CD integration
  - [ ] 21.1 Create .github/workflows/tests.yml
    - Configure GitHub Actions workflow
    - Run tests on push and pull_request
    - _Requirements: 1.6_

  - [ ] 21.2 Configure coverage reporting
    - Generate coverage reports in CI
    - Upload to codecov or similar service
    - _Requirements: 1.5, 17.6_

  - [ ] 21.3 Configure coverage thresholds
    - Fail build if coverage drops below 70%
    - _Requirements: 17.7_

  - [ ] 21.4 Configure test execution timeout
    - Set 5 minute timeout for full suite
    - _Requirements: 1.7_

- [-] 22. Complete test documentation
  - [ ] 22.1 Update tests/README.md
    - Document how to run tests locally
    - Document how to run specific test subsets
    - Document how to interpret coverage reports
    - _Requirements: 18.5, 18.6, 18.7_

  - [ ] 22.2 Add docstrings to all test functions
    - Explain test purpose
    - Document expected behavior
    - Reference requirements
    - _Requirements: 18.1, 18.2, 18.3_

  - [ ] 22.3 Create test documentation in main README
    - Add testing section to project README
    - Link to tests/README.md
    - _Requirements: 18.4_

- [ ] 23. Implement test maintenance improvements
  - [ ] 23.1 Create shared test helpers
    - Extract common test patterns into helper functions
    - Reduce code duplication
    - _Requirements: 20.2_

  - [ ] 23.2 Refactor tests to use parameterization
    - Use pytest.mark.parametrize for similar test cases
    - _Requirements: 20.4_

  - [ ] 23.3 Verify test function size limits
    - Ensure all test functions are under 50 lines
    - Refactor long tests
    - _Requirements: 20.5_

  - [ ] 23.4 Organize tests into logical modules
    - Ensure clear module organization
    - _Requirements: 20.6_

  - [ ] 23.5 Improve test failure messages
    - Add clear failure messages to assertions
    - _Requirements: 20.7_

  - [ ] 23.6 Reduce test brittleness
    - Avoid tests that break with minor code changes
    - Use flexible assertions where appropriate
    - _Requirements: 20.3_

- [ ] 24. Final checkpoint - Verify all requirements met
  - Run full test suite and verify all tests pass
  - Verify coverage meets all thresholds (70% core, 80% validation, 60% handlers)
  - Verify test execution completes in under 5 minutes
  - Verify CI/CD integration works correctly
  - Verify all documentation is complete
  - Ask the user if questions arise

## Notes

- Tasks marked with sub-tasks should complete all sub-tasks before marking the parent complete
- Each checkpoint task should verify tests pass before proceeding
- Coverage targets: 70% for core modules, 80% for input validation, 60% for handlers
- Test execution should complete in under 5 minutes for the full suite
- All tests should use mocked AWS APIs (no real AWS calls)
- Property tests should run at least 100 iterations each
