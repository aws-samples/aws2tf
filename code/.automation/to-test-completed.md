# Completed Resource Tests

This file tracks all resources that have been successfully tested following the new resource testing procedure.

**Total Completed:** 7
**Last Updated:** 2026-01-01

---

## Successfully Tested Resources

Resources are listed by service group in the order they were completed.

### aws_api_gateway

- [x] `aws_api_gateway_api_key` - ✓ PASSED (2026-01-01) - [test results](test_aws_api_gateway_api_key/test-results.md)
- [x] `aws_api_gateway_client_certificate` - ✓ PASSED (2026-01-01) - [test results](test_aws_api_gateway_client_certificate/test-results.md)
- [x] `aws_api_gateway_documentation_part` - ✓ PASSED (2026-01-01) - [test results](test_aws_api_gateway_documentation_part/test-results.md)
- [x] `aws_api_gateway_model` - ✓ PASSED (2026-01-01) - [test results](test_aws_api_gateway_model/test-results.md)
- [x] `aws_api_gateway_request_validator` - ✓ PASSED (2026-01-01) - [test results](test_aws_api_gateway_request_validator/test-results.md)

### aws_lambda

- [x] `aws_lambda_function_recursion_config` - ✓ PASSED (2026-01-01) - [test results](test_aws_lambda_function_recursion_config/test-results.md)
- [x] `aws_lambda_capacity_provider` - ✓ PASSED (2026-01-01) - [test results](test_aws_lambda_capacity_provider/test-results.md)

<!-- Add completed resources below in this format:

### aws_service_name

- [x] `aws_service_resource` - ✓ PASSED (YYYY-MM-DD) - [test results](test_aws_service_resource/test-results.md)

-->

---

## Testing Notes

- All resources listed here have passed both basic and comprehensive configuration tests
- Each resource has a test directory with full documentation
- Test results include deployment, import, and cleanup verification
- Resources with composite IDs are excluded (see to-test-composite.md)
- Deprecated resources are excluded (see to-test-deprecated.md)
