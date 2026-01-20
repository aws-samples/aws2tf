# Requirements Document: Flexible ID Handling in get_aws_* Functions

## Introduction

This feature adds flexibility to the `get_aws_*` functions in the `get_aws_resources` module to accept both resource names/IDs and ARNs as input parameters. When an ARN is provided, the system will automatically extract the appropriate resource identifier and use it for API calls, while maintaining the original behavior for `common.write_import()` calls.

## Glossary

- **ARN**: Amazon Resource Name - A unique identifier for AWS resources in the format `arn:partition:service:region:account-id:resource-type/resource-id`
- **Resource ID**: The specific identifier for a resource (e.g., bucket name, function name, VPC ID)
- **get_aws_* function**: Functions in `get_aws_resources` module that retrieve AWS resources
- **common.write_import()**: Function that writes Terraform import statements

## Requirements

### Requirement 1: ARN Parsing Utility

**User Story:** As a developer, I want a utility function to extract resource identifiers from ARNs, so that I can handle both ARNs and resource IDs uniformly.

#### Acceptance Criteria

1. WHEN a valid ARN is provided, THE System SHALL extract the resource identifier from the ARN
2. WHEN a non-ARN string is provided, THE System SHALL return the string unchanged
3. WHEN an ARN with resource-type/resource-id format is provided, THE System SHALL extract only the resource-id portion
4. WHEN an ARN with resource-type:resource-id format is provided, THE System SHALL extract only the resource-id portion
5. WHEN an ARN with just resource-id is provided, THE System SHALL extract the resource-id

### Requirement 2: S3 Bucket ID Extraction

**User Story:** As a user, I want to pass either a bucket name or bucket ARN to S3 functions, so that I can use whichever identifier I have available.

#### Acceptance Criteria

1. WHEN an S3 bucket ARN is provided to `get_aws_s3_bucket`, THE System SHALL extract the bucket name
2. WHEN a bucket name is provided to `get_aws_s3_bucket`, THE System SHALL use it directly
3. WHEN `common.write_import()` is called, THE System SHALL use the extracted bucket name (not the original ARN)
4. WHEN the extracted bucket name is used in API calls, THE System SHALL function correctly

### Requirement 3: Generic Resource ID Extraction

**User Story:** As a developer, I want all `get_aws_*` functions to support ARN inputs, so that the system is consistent across all resource types.

#### Acceptance Criteria

1. WHEN any `get_aws_*` function receives an ARN in the `id` parameter, THE System SHALL extract the resource identifier
2. WHEN the extracted identifier is used in boto3 API calls, THE System SHALL function correctly
3. WHEN `common.write_import()` is called, THE System SHALL use the extracted identifier (not the original ARN)
4. WHEN a non-ARN identifier is provided, THE System SHALL maintain backward compatibility

### Requirement 4: Preserve Import Behavior

**User Story:** As a system maintainer, I want `common.write_import()` calls to remain unchanged, so that Terraform import statements use the correct identifier format.

#### Acceptance Criteria

1. WHEN `common.write_import()` is called, THE System SHALL pass the extracted resource identifier (not the ARN)
2. WHEN the resource identifier is extracted from an ARN, THE System SHALL use only the identifier portion
3. WHEN a non-ARN is provided, THE System SHALL pass it unchanged to `common.write_import()`

### Requirement 5: Error Handling

**User Story:** As a user, I want clear error messages when invalid ARNs are provided, so that I can correct my input.

#### Acceptance Criteria

1. WHEN an invalid ARN format is provided, THE System SHALL log a warning and attempt to use the value as-is
2. WHEN ARN parsing fails, THE System SHALL not crash but continue with the original value
3. WHEN debugging is enabled, THE System SHALL log the ARN extraction process
