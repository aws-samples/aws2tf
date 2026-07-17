# aws2tf Architecture Overview

**Understanding How aws2tf Works**

## What is aws2tf?

aws2tf is a Python tool that imports existing AWS infrastructure into Terraform, automatically generating the corresponding Terraform HCL configuration files. It discovers AWS resources, imports them into Terraform state, and creates properly formatted `.tf` files with de-referenced values and dependency tracking.

## High-Level Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                     aws2tf Execution Flow                        │
└─────────────────────────────────────────────────────────────────┘

1. Parse Arguments & Setup
   ├─ Validate CLI arguments (region, type, resource ID)
   ├─ Setup logging and context
   └─ Initialize workspace directory

2. Build Resource Lists (Parallel Discovery)
   ├─ Discover VPCs, Subnets, Security Groups
   ├─ Discover Lambda functions, S3 buckets
   ├─ Discover IAM roles, policies, instance profiles
   └─ Store in context for later reference

3. Process Requested Resources
   ├─ Call AWS APIs to list/describe resources
   ├─ Generate import statements
   └─ Track dependencies

4. Process Known Dependencies
   ├─ Import parent resources (VPCs for subnets, etc.)
   └─ Follow predefined dependency chains

5. Process Detected Dependencies (Iterative)
   ├─ Parse generated .tf files
   ├─ Find resource references
   ├─ Import missing dependencies
   └─ Repeat until no new dependencies found

6. Validate & Import
   ├─ Run terraform init
   ├─ Run terraform import for all resources
   ├─ Run terraform plan to verify
   └─ Check for drift

7. Finalize & Cleanup
   ├─ Run security checks (trivy)
   ├─ Merge files if requested (-s flag)
   ├─ Generate summary report
   └─ Exit
```

## Major Components

### 1. Main Entry Point (`aws2tf.py`)

**Purpose:** Orchestrates the entire workflow

**Key Functions:**
- `main_new()` - Main entry point with 10 phases
- `parse_and_validate_arguments()` - CLI argument parsing
- `setup_environment_and_context()` - Initialize global state
- `build_resource_lists_phase()` - Parallel resource discovery
- `process_resource_types()` - Handle requested resource types
- `process_known_dependencies()` - Import parent resources
- `process_detected_dependencies()` - Iterative dependency resolution
- `validate_and_import()` - Terraform import and validation
- `finalize_and_cleanup()` - Security checks and cleanup

**10 Execution Phases:**
1. Parse and validate arguments
2. Setup environment and context
3. Setup workspace and initialize terraform
4. Handle merge mode (if enabled)
5. Build core resource lists
6. Process requested resource types
7. Process known dependencies
8. Process detected dependencies (iterative)
9. Validate and import
10. Finalize and cleanup

### 2. Resource Discovery (`code/build_lists.py`)

**Purpose:** Parallel discovery of AWS resources across the account

**Key Functions:**
- `build_lists()` - Main function that discovers 10 core resource types in parallel
- `build_secondary_lists()` - Discovers IAM policy attachments

**Optimizations (2024):**
- ThreadPoolExecutor with configurable worker count
- S3 bucket validation parallelized
- Dispatch table for result processing
- File I/O batching
- 73% reduction in nesting depth
- 52% reduction in local variables

**Resources Discovered:**
- VPCs, Subnets, Security Groups
- Lambda functions
- S3 buckets (with validation)
- Transit Gateways
- IAM roles, policies, instance profiles
- Launch templates

**Performance:**
- Parallel execution using ThreadPoolExecutor
- Progress bars with tqdm
- Estimated 25-50% faster than previous version

### 3. Resource Type Handlers (`code/resources.py`)

**Purpose:** Maps resource type codes to Terraform resource types

**Key Functions:**
- `resources()` - Main dispatcher that routes resource types to appropriate handlers
- Type code mapping (e.g., `vpc` → `aws_vpc`, `efs` → `aws_efs_file_system`)

**Supported Types:**
- Short codes: `vpc`, `efs`, `ecs`, `lambda`, `s3`, etc.
- Direct Terraform types: `aws_vpc`, `aws_lambda_function`, etc.
- Stack imports: `stack` for CloudFormation stacks

### 4. Get Functions (`code/get_aws_resources/`)

**Purpose:** AWS API calls to discover and list specific resource types

**Structure:**
- One file per AWS service (e.g., `aws_ec2.py`, `aws_lambda.py`, `aws_s3.py`)
- Each file contains get functions for that service's resources

**Key Pattern:**
```python
def get_aws_<resource>(type, id, clfn, descfn, topkey, key, filterid):
    """
    Discover resources and write import statements.
    
    Args:
        type: Terraform resource type (e.g., 'aws_vpc')
        id: Specific resource ID (None for all resources)
        clfn: Boto3 client name (e.g., 'ec2')
        descfn: Boto3 API method (e.g., 'describe_vpcs')
        topkey: Response key containing resources
        key: Field name for resource ID
        filterid: Field name for filtering
    """
    # List all resources or get specific resource
    # Write import statements via common.write_import()
```

**Responsibilities:**
- Call AWS APIs using boto3
- Handle pagination
- Extract resource IDs
- Write import statements
- Handle errors gracefully

### 5. Resource Handlers (`code/fixtf_aws_resources/`)

**Purpose:** Transform Terraform-generated HCL into clean, de-referenced configuration

**Structure:**
- One file per AWS service (e.g., `fixtf_ec2.py`, `fixtf_lambda.py`)
- Each file contains handler functions for that service's resources

**Handler System (2024 Optimization):**
- **Base handler** (`base_handler.py`) with common utilities
- **`__getattr__` pattern** for automatic default handling
- **86.5% code reduction** (1,265 boilerplate functions eliminated)
- **100% coverage** of 1,612 Terraform AWS resources

**Key Pattern:**
```python
def aws_<resource>(t1, tt1, tt2, flag1, flag2):
    """
    Transform a single line of Terraform HCL.
    
    Args:
        t1: Current line content
        tt1: Field name
        tt2: Field value
        flag1: Processing flags
        flag2: Processing flags
    
    Returns:
        (skip, t1, flag1, flag2)
        skip: 1 to skip line, 0 to keep
        t1: Modified line content
    """
    skip = 0
    
    # Skip computed fields
    if tt1 in ["arn", "id", "tags_all"]:
        skip = 1
    
    # De-reference parent resources
    if tt1 == "vpc_id" and tt2 != "null":
        t1 = tt1 + " = aws_vpc.r-" + vpc_id + ".id\n"
        common.add_dependancy("aws_vpc", vpc_id)
    
    # Add lifecycle blocks
    if tt1 == "name":
        t1 = t1 + "\n lifecycle {\n   ignore_changes = [tags]\n}\n"
    
    return skip, t1, flag1, flag2
```

**Responsibilities:**
- Skip computed/read-only fields
- De-reference hardcoded IDs to Terraform resource references
- Add lifecycle blocks to prevent drift
- Track dependencies via `common.add_dependancy()`
- Handle special cases per resource type

### 6. Resource Dictionary (`code/fixtf_aws_resources/aws_dict.py`)

**Purpose:** Central registry mapping Terraform resource types to AWS API details

**Structure:**
```python
aws_<resource> = {
    "clfn": "ec2",                    # Boto3 client name
    "descfn": "describe_vpcs",        # Boto3 API method
    "topkey": "Vpcs",                 # Response key
    "key": "VpcId",                   # Resource ID field
    "filterid": "VpcId"               # Filter field
}
```

**Coverage:**
- **1,612 Terraform AWS resources** mapped
- **177 new resources** added in 2024
- Proper boto3 API mappings for all resources

**Usage:**
- Looked up by `common.py` to route resource processing
- Provides all information needed to discover and import resources

### 7. Common Utilities (`code/common.py`)

**Purpose:** Shared utilities used throughout the codebase

**Key Functions:**
- `write_import()` - Write Terraform import statements
- `add_dependancy()` - Track resource dependencies
- `rc()` - Execute shell commands
- `wrapup()` - Final terraform plan and validation
- `secure_terraform_files()` - Set secure file permissions
- `trivy_check()` - Run security scanning

**Module Registry:**
- Maps service names to get function modules
- Maps service names to handler modules
- Enables dynamic loading of handlers

### 8. Context Management (`code/context.py`)

**Purpose:** Global state management across the application

**Key Attributes:**
- `region` - AWS region
- `cores` - CPU cores for parallel execution
- `vpclist`, `subnetlist`, `sglist` - Discovered resources
- `lambdalist`, `s3list`, `rolelist` - More discovered resources
- `rproc` - Processed resources (avoid duplicates)
- `tracking_message` - Current operation status
- `esttime` - Estimated time remaining

**Thread Safety:**
- Dictionary updates are GIL-protected
- Each fetch function writes to different attributes
- No locks needed for current usage pattern

### 9. Stack Processing (`code/stacks.py`)

**Purpose:** Import CloudFormation stacks and their resources

**Key Functions:**
- `get_stacks()` - Discover CloudFormation stacks
- `process_stack()` - Import stack and all its resources

**Workflow:**
1. List CloudFormation stacks
2. Get stack resources
3. Import each resource in the stack
4. Track dependencies between stack resources

### 10. File Operations (`code/fixtf.py`)

**Purpose:** Process and transform Terraform files

**Key Functions:**
- `fixtf()` - Main function to process a Terraform file
- Reads generated `.tf` files line by line
- Calls appropriate handler for each resource type
- Writes cleaned/transformed output

**Processing Flow:**
```
Generated .tf file
    ↓
Read line by line
    ↓
Identify resource type
    ↓
Call handler function
    ↓
Transform line (skip, modify, add lifecycle)
    ↓
Write to output file
```

## Data Flow

### Discovery Phase
```
AWS Account
    ↓
boto3 API calls (parallel)
    ↓
build_lists.py
    ↓
Context dictionaries (vpclist, lambdalist, etc.)
```

### Import Phase
```
User request (-t vpc -i vpc-123)
    ↓
resources.py (type mapping)
    ↓
aws_dict.py (lookup API details)
    ↓
get_aws_resources/aws_ec2.py (API call)
    ↓
common.write_import() (write import statement)
    ↓
terraform import (execute)
    ↓
terraform show (generate .tf file)
    ↓
fixtf.py (transform)
    ↓
fixtf_aws_resources/fixtf_ec2.py (handler)
    ↓
Clean .tf file
```

### Dependency Resolution
```
Generated .tf files
    ↓
Parse for resource references
    ↓
Extract referenced resource types/IDs
    ↓
Check if already imported
    ↓
If not imported:
    ├─ Add to dependency queue
    └─ Import resource
    ↓
Repeat until no new dependencies
```

## Key Design Patterns

### 1. Parallel Execution
- ThreadPoolExecutor for resource discovery
- Configurable worker count (context.cores)
- Progress bars for user feedback

### 2. Dispatch Tables
- Resource type → handler function mapping
- Service name → module mapping
- Eliminates long if-elif chains

### 3. Handler Pattern
- Base handler with common utilities
- `__getattr__` for automatic default handling
- Service-specific overrides only when needed

### 4. Dependency Tracking
- `common.add_dependancy()` called by handlers
- Iterative resolution until no new dependencies
- Prevents circular dependencies

### 5. Idempotency
- Track processed resources in `context.rproc`
- Skip already-imported resources
- Safe to run multiple times

## File Organization

```
aws2tf/
├── aws2tf.py                    # Main entry point
├── code/
│   ├── build_lists.py          # Parallel resource discovery
│   ├── resources.py            # Type code mapping
│   ├── common.py               # Shared utilities
│   ├── context.py              # Global state
│   ├── stacks.py               # CloudFormation stack handling
│   ├── fixtf.py                # File transformation
│   ├── get_aws_resources/      # AWS API calls (discovery)
│   │   ├── aws_ec2.py
│   │   ├── aws_lambda.py
│   │   └── ... (one per service)
│   └── fixtf_aws_resources/    # Terraform transformations
│       ├── base_handler.py     # Common utilities
│       ├── aws_dict.py         # Resource registry
│       ├── fixtf_ec2.py
│       ├── fixtf_lambda.py
│       └── ... (one per service)
├── tests/                       # Comprehensive test suite
├── documentation/               # Project documentation
└── generated/                   # Output directory (created at runtime)
    └── tf-<account>-<region>/  # Terraform files
```

## Performance Characteristics

### Resource Discovery (build_lists.py)
- **Parallel execution:** 10 resource types discovered simultaneously
- **Estimated improvement:** 25-50% faster than sequential
- **Bottlenecks:** AWS API rate limits, S3 bucket validation

### Import Phase
- **Sequential:** Resources imported one at a time
- **Bottleneck:** Terraform import command execution
- **Optimization:** Batch imports where possible

### Dependency Resolution
- **Iterative:** Multiple passes until no new dependencies
- **Typical passes:** 2-4 for most infrastructures
- **Worst case:** Deep dependency chains (10+ passes)

## Error Handling

### Graceful Degradation
- Failed resource discovery doesn't stop other resources
- Failed imports logged to `.err` files
- Continue processing remaining resources

### Logging
- Console output for user feedback
- File logging (`aws2tf.log`) for debugging
- Secure file permissions (0o600) for sensitive data

### Validation
- Input validation for CLI arguments
- AWS credential validation
- Terraform version validation
- Region validation

## Security Features

### File Permissions
- Terraform state files: 0o600 (rw-------)
- Log files: 0o600 (rw-------)
- Prevents unauthorized access to sensitive data

### Security Scanning
- Optional trivy integration
- Scans generated Terraform files
- Reports security issues

### Credential Handling
- Uses AWS CLI credentials
- No credential storage in code
- Respects AWS credential chain

## Extension Points

### Adding New Resource Types

1. **Add to aws_dict.py:**
```python
aws_new_resource = {
    "clfn": "service_name",
    "descfn": "describe_resources",
    "topkey": "Resources",
    "key": "ResourceId",
    "filterid": "ResourceId"
}
```

2. **Create get function** in `get_aws_resources/aws_service.py`:
```python
def get_aws_new_resource(type, id, clfn, descfn, topkey, key, filterid):
    # Implement discovery logic
    pass
```

3. **Create handler** in `fixtf_aws_resources/fixtf_service.py`:
```python
def aws_new_resource(t1, tt1, tt2, flag1, flag2):
    # Implement transformation logic
    return skip, t1, flag1, flag2
```

4. **Register modules** in `common.py` if new service

### Testing New Resources
See `code/.automation/new-resource-testing.md` for comprehensive testing procedure.

## Related Documentation

- **[testing-guide.md](testing-guide.md)** - How to run and write tests
- **[build-lists-optimization-summary.md](build-lists-optimization-summary.md)** - Recent optimization work
- **[code/fixtf_aws_resources/README.md](../code/fixtf_aws_resources/README.md)** - Handler system details
- **[code/.automation/new-resource-testing.md](../code/.automation/new-resource-testing.md)** - Testing procedure
- **[tests/README.md](../tests/README.md)** - Test suite documentation

## Troubleshooting

### Common Issues

**"No module named 'code'"**
- Run from workspace root: `cd /path/to/aws2tf && ./aws2tf.py`

**AWS credential errors**
- Verify: `aws sts get-caller-identity`
- Configure: `aws configure`

**Terraform version errors**
- Requires Terraform v1.12.0+
- Use tfenv to manage versions

**Import failures**
- Check `.err` files for details
- Verify resource exists in AWS
- Check IAM permissions

### Debug Mode

```bash
# Enable debug logging
./aws2tf.py -t vpc --debug

# Check log file
cat aws2tf.log
```

## Performance Tuning

### Adjust Worker Count
```python
# In context.py
cores = 8  # Increase for faster discovery
```

### Skip Security Checks
```bash
# Faster execution, skip trivy
# (trivy runs automatically if installed)
```

### Single File Mode
```bash
# Merge all resources into main.tf
./aws2tf.py -t vpc -s
```

## Future Enhancements

Potential areas for improvement:
- Parallel terraform imports
- Caching of discovered resources
- Incremental updates (only import changes)
- Support for additional cloud providers
- Web UI for resource selection

---

**Questions?** Check the [README.md](../README.md) or open a GitHub issue!
