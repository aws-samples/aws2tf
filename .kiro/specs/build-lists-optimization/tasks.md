# Implementation Plan: build_lists.py Multi-Threading Optimization

## Overview

This plan optimizes build_lists.py by simplifying result processing, parallelizing S3 validation, improving error handling, and reducing code complexity. All changes remain within the single file. Each task includes validation checkpoints using `./aws2tf.py -t vpc` and existing test suite.

## Tasks

- [x] 1. Create backup and add module-level constants
  - Create build_lists.py.backup if it doesn't exist
  - Add BOTO3_RETRY_CONFIG constant at module level
  - Add module docstring explaining thread safety
  - _Requirements: 11.1, 11.2, 11.3, 10.3, 4.1, 4.2, 4.3_
  - **Validation**: Run `./aws2tf.py -t vpc` and `pytest tests/unit/test_resource_discovery.py -v`

- [x] 2. Update fetch function return formats
  - [x] 2.1 Update fetch_vpc_data to return dict format
    - Return `{'resource_type': 'vpc', 'items': [...], 'metadata': {'full_data': response}}`
    - Store full VPC data in metadata for context.vpcs assignment
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.2 Update fetch_lambda_data to return dict format
    - Return `{'resource_type': 'lambda', 'items': [...], 'metadata': {}}`
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.3 Update fetch_s3_data to return dict format with validation
    - Move list_objects_v2 validation into this function
    - Return only validated buckets in items list
    - _Requirements: 9.1, 2.1, 7.1, 7.2, 2.3, 2.4_
  
  - [x] 2.4 Update fetch_sg_data to return dict format
    - Return `{'resource_type': 'sg', 'items': [...], 'metadata': {}}`
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.5 Update fetch_subnet_data to return dict format
    - Return `{'resource_type': 'subnet', 'items': [...], 'metadata': {'full_data': response}}`
    - Store full subnet data in metadata for file writing
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.6 Update fetch_tgw_data to return dict format
    - Return `{'resource_type': 'tgw', 'items': [...], 'metadata': {}}`
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.7 Update fetch_roles_data to return dict format
    - Return `{'resource_type': 'iam', 'items': [...], 'metadata': {'full_data': response}}`
    - Store full roles data in metadata for file writing
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.8 Update fetch_policies_data to return dict format
    - Return `{'resource_type': 'pol', 'items': [...], 'metadata': {}}`
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.9 Update fetch_instprof_data to return dict format
    - Return `{'resource_type': 'inp', 'items': [...], 'metadata': {}}`
    - _Requirements: 9.1, 2.1_
  
  - [x] 2.10 Update fetch_launch_templates to return dict format
    - Return `{'resource_type': 'lt', 'items': [...], 'metadata': {}}`
    - _Requirements: 9.1, 2.1_
  
  - **Validation**: Run `./aws2tf.py -t vpc` and `pytest tests/unit/test_resource_discovery.py tests/unit/test_error_handling.py -v`

- [x] 3. Checkpoint - Ensure all tests pass
  - Run full test suite: `pytest tests/unit/test_resource_discovery.py tests/unit/test_error_handling.py tests/integration/ -v`
  - Run VPC import: `./aws2tf.py -t vpc`
  - Verify no regressions before proceeding

- [x] 4. Implement result processing dispatch table
  - [x] 4.1 Create _process_vpc_result handler function
    - Update context.vpcs from metadata
    - Update context.vpclist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.2 Create _process_lambda_result handler function
    - Update context.lambdalist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.3 Create _process_s3_result handler function
    - Update context.s3list from items (already validated)
    - _Requirements: 6.2, 2.2, 7.3_
  
  - [x] 4.4 Create _process_sg_result handler function
    - Update context.sglist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.5 Create _process_subnet_result handler function
    - Update context.subnets from metadata
    - Update context.subnetlist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.6 Create _process_tgw_result handler function
    - Update context.tgwlist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.7 Create _process_iam_result handler function
    - Update context.rolelist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.8 Create _process_pol_result handler function
    - Update context.policylist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.9 Create _process_inp_result handler function
    - Update context.inplist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.10 Create _process_lt_result handler function
    - Update context.ltlist from items
    - _Requirements: 6.2, 2.2_
  
  - [x] 4.11 Create RESULT_HANDLERS dispatch dictionary
    - Map resource types to handler functions
    - _Requirements: 6.2_
  
  - [x] 4.12 Replace result processing if-elif chain with dispatch
    - Use `RESULT_HANDLERS.get(resource_type)` pattern
    - Reduce nesting from 6 to 2 levels
    - _Requirements: 6.1, 6.2, 9.3_
  
  - **Validation**: Run `./aws2tf.py -t vpc` and `pytest tests/unit/test_resource_discovery.py tests/integration/test_vpc_workflow.py -v`

- [x] 5. Checkpoint - Ensure all tests pass
  - Run full test suite
  - Run VPC import
  - Verify dispatch table works correctly

- [x] 6. Implement file I/O batching
  - [x] 6.1 Create _write_resource_files helper function
    - Accept results list as parameter
    - Extract metadata from subnet and IAM results
    - Write subnets.json with UTF-8 encoding
    - Write roles.json with UTF-8 encoding
    - Handle file write errors gracefully
    - _Requirements: 3.1, 3.2, 3.3_
  
  - [x] 6.2 Remove file writes from fetch functions
    - Remove file write from fetch_subnet_data
    - Remove file write from fetch_roles_data
    - _Requirements: 3.1_
  
  - [x] 6.3 Call _write_resource_files after thread pool
    - Collect all results from thread pool
    - Call _write_resource_files with results list
    - _Requirements: 3.1_
  
  - **Validation**: Run `./aws2tf.py -t vpc` and `pytest tests/unit/test_resource_discovery.py -v` (check JSON files created)

- [x] 7. Improve error handling and logging
  - [x] 7.1 Update all fetch functions to use lazy logging
    - Replace f-strings with % formatting in log statements
    - Pattern: `log.error("Message: %s", var)` instead of `log.error(f"Message: {var}")`
    - _Requirements: 5.4_
  
  - [x] 7.2 Ensure all fetch functions return empty dict on error
    - Verify all try-except blocks return `{'resource_type': 'xxx', 'items': [], 'metadata': {}}`
    - _Requirements: 5.2, 9.2_
  
  - [x] 7.3 Add error handling to result processing loop
    - Wrap handler calls in try-except
    - Log errors and continue processing other results
    - _Requirements: 5.3_
  
  - **Validation**: Run `./aws2tf.py -t vpc` and `pytest tests/unit/test_error_handling.py -v`

- [x] 8. Checkpoint - Ensure all tests pass
  - Run full test suite
  - Run VPC import
  - Verify error handling works correctly

- [x] 9. Add retry configuration to all boto3 clients
  - [x] 9.1 Update all fetch functions to use BOTO3_RETRY_CONFIG
    - Pattern: `boto3.client('service', config=BOTO3_RETRY_CONFIG)`
    - Apply to all 10 fetch functions
    - _Requirements: 1.3, 10.2_
  
  - **Validation**: Run `./aws2tf.py -t vpc` and `pytest tests/unit/test_resource_discovery.py -v`

- [-] 10. Final validation and cleanup
  - [x] 10.1 Run complete test suite
    - `pytest tests/unit/test_resource_discovery.py -v`
    - `pytest tests/unit/test_error_handling.py -v`
    - `pytest tests/integration/test_vpc_workflow.py -v`
    - `pytest tests/integration/test_lambda_workflow.py -v`
    - `pytest tests/integration/test_s3_workflow.py -v`
    - `pytest tests/integration/test_iam_workflow.py -v`
    - All tests should pass
  
  - [x] 10.2 Run real-world validation
    - `./aws2tf.py -t vpc` - should complete successfully
    - `./aws2tf.py -t lambda` - should complete successfully
    - `./aws2tf.py -t aws_s3_bucket` - should complete successfully
    - Verify generated files exist and are valid
  
  - [x] 10.3 Verify backup file exists
    - Check `code/build_lists.py.backup` exists
    - Verify it contains original content
  
  - [x] 10.4 Verify code quality improvements
    - Check nesting depth ≤ 5 levels
    - Check local variables < 20
    - Check no unused variables
    - Run linter to verify improvements
  
  - [x] 10.5 Document performance improvements
    - Run timing comparison (before/after)
    - Document actual performance gains
    - Update analysis.md with results

## Notes

- All changes remain within `code/build_lists.py`
- Backup file created automatically on first run
- Context attribute assignments not modified (documented only)
- Each checkpoint includes both `./aws2tf.py -t vpc` and relevant test suite
- If any validation fails, revert last change and debug before proceeding
- Estimated total improvement: 25-50% faster execution
