# Requirements Document: build_lists.py Multi-Threading Optimization

## Introduction

This document outlines requirements for optimizing the multi-threaded execution in `code/build_lists.py`. The current implementation uses `ThreadPoolExecutor` but has several inefficiencies that impact performance and maintainability.

## Glossary

- **ThreadPoolExecutor**: Python's concurrent.futures executor for managing thread pools
- **Boto3_Client**: AWS SDK client for making API calls
- **Paginator**: Boto3 mechanism for handling paginated API responses
- **Context_Module**: Global state management module storing resource lists
- **Resource_Fetch_Function**: Individual function that fetches a specific AWS resource type

## Project Constraints

1. **All code must remain within build_lists.py** - No extraction to separate modules or files
2. **Create backup before modifications** - Save build_lists.py.backup before any changes
3. **Context attribute assignments are out of scope** - Document the thread safety assumption but do not modify

## Requirements

### Requirement 1: Thread-Safe Boto3 Client Management

**User Story:** As a developer, I want boto3 clients to be created within worker threads, so that thread safety is guaranteed and connection pooling works correctly.

#### Acceptance Criteria

1. WHEN a fetch function executes, THE System SHALL create the boto3 client within the function scope
2. WHEN multiple threads execute simultaneously, THE System SHALL ensure each thread has its own boto3 client instance
3. WHEN boto3 clients are created, THE System SHALL use proper retry configuration for resilience

### Requirement 2: Eliminate Redundant Result Processing

**User Story:** As a developer, I want to eliminate the complex nested result processing logic, so that the code is more maintainable and performs better.

#### Acceptance Criteria

1. WHEN fetch functions return results, THE System SHALL return data in a consistent format
2. WHEN processing results, THE System SHALL directly update context dictionaries without intermediate tuple conversions
3. WHEN handling S3 buckets, THE System SHALL avoid unnecessary list_objects_v2 calls in the main thread
4. THE System SHALL eliminate the unused 'objs' variable assignment

### Requirement 3: Separate I/O Operations from Thread Pool

**User Story:** As a developer, I want file I/O operations moved outside the thread pool, so that threads focus on API calls and don't block on disk operations.

#### Acceptance Criteria

1. WHEN saving JSON files, THE System SHALL perform file writes after thread pool completion
2. WHEN writing files, THE System SHALL explicitly specify UTF-8 encoding
3. WHEN multiple resources need file persistence, THE System SHALL batch file operations

### Requirement 4: Document Context Update Thread Safety

**User Story:** As a developer, I want the thread safety assumptions for context updates documented, so that future maintainers understand the design.

#### Acceptance Criteria

1. WHEN reviewing the code, THE Documentation SHALL explain that context dictionary updates are GIL-protected
2. WHEN reviewing the code, THE Documentation SHALL note that context attribute assignments (context.vpcs, context.subnets) happen in separate threads
3. WHEN reviewing the code, THE Documentation SHALL document the assumption that each fetch function writes to different context attributes
4. THE System SHALL NOT modify the context attribute assignment pattern (out of scope)

### Requirement 5: Improve Error Handling

**User Story:** As a developer, I want consistent error handling across all fetch functions, so that failures are properly logged and don't crash the application.

#### Acceptance Criteria

1. WHEN a fetch function encounters an error, THE System SHALL log the error with proper context
2. WHEN an API call fails, THE System SHALL return an empty result rather than raising an exception
3. WHEN processing results, THE System SHALL handle exceptions without stopping other threads
4. THE System SHALL use lazy logging formatting for performance

### Requirement 6: Reduce Code Complexity

**User Story:** As a developer, I want the main processing loop simplified, so that the code is easier to understand and maintain.

#### Acceptance Criteria

1. WHEN processing results, THE System SHALL have no more than 5 nested blocks
2. WHEN handling different resource types, THE System SHALL use a dispatch pattern instead of if-elif chains
3. WHEN organizing code, THE System SHALL keep all functions within build_lists.py (no extraction to separate files)
4. THE System SHALL reduce the number of local variables in build_lists() from 33 to under 20

### Requirement 7: Optimize S3 Bucket Validation

**User Story:** As a developer, I want S3 bucket validation to be parallelized, so that it doesn't become a bottleneck.

#### Acceptance Criteria

1. WHEN validating S3 buckets, THE System SHALL perform list_objects_v2 calls in parallel
2. WHEN S3 validation fails, THE System SHALL handle exceptions gracefully
3. WHEN processing S3 results, THE System SHALL avoid blocking the main result processing loop

### Requirement 8: Improve Progress Reporting

**User Story:** As a user, I want accurate progress reporting, so that I can monitor the operation's status.

#### Acceptance Criteria

1. WHEN fetching resources, THE System SHALL display resource counts as they complete
2. WHEN all fetches complete, THE System SHALL show total resources discovered
3. WHEN errors occur, THE System SHALL update progress bar with error status

### Requirement 9: Consistent Return Types

**User Story:** As a developer, I want all fetch functions to return consistent data structures, so that result processing is simplified.

#### Acceptance Criteria

1. WHEN fetch functions complete, THE System SHALL return a dictionary with resource_type and items keys
2. WHEN fetch functions fail, THE System SHALL return a dictionary with empty items list
3. WHEN processing results, THE System SHALL not need to check tuple vs list types

### Requirement 10: Configuration Management

**User Story:** As a developer, I want thread pool size and retry configuration to be easily adjustable, so that performance can be tuned for different environments.

#### Acceptance Criteria

1. WHEN creating thread pools, THE System SHALL use context.cores for max_workers
2. WHEN creating boto3 clients, THE System SHALL use consistent retry configuration
3. WHEN retry configuration is needed, THE System SHALL define it once and reuse it

### Requirement 11: Create Backup Before Modifications

**User Story:** As a developer, I want a backup of the original file created before any changes, so that I can revert if needed.

#### Acceptance Criteria

1. WHEN starting implementation, THE System SHALL create a backup file named build_lists.py.backup
2. WHEN the backup is created, THE System SHALL preserve the exact original content
3. WHEN the backup exists, THE System SHALL not overwrite it with subsequent backups
4. THE Backup SHALL be created in the same directory as the original file (code/build_lists.py.backup)
