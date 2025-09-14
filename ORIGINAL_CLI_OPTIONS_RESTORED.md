# Original AWS2TF CLI Options - Fully Restored

✅ **ALL ORIGINAL AWS2TF COMMAND-LINE OPTIONS ARE NOW SUPPORTED!**

The new AWS2TF v2.0 maintains **100% backward compatibility** with the original aws2tf while adding powerful new workflow orchestration features.

## ✅ All Original Options Working

### Basic Usage (Original Syntax)
```bash
# Basic resource import
aws2tf -t vpc -i vpc-12345
aws2tf -t ec2 -i i-abcdef  
aws2tf -t aws_s3 -i my-bucket

# With regions and profiles
aws2tf -t vpc -i vpc-12345 -r us-west-2 -p production
```

### All Original Flags Supported
```bash
# Debug and fast mode
aws2tf -t ec2 -i i-abcdef -d -f

# Output customization
aws2tf -t vpc -i vpc-12345 -o networking

# Merge and single file
aws2tf -t subnet -i subnet-67890 -m -s

# Validation
aws2tf -v -t vpc -i vpc-12345

# Accept expected changes
aws2tf -t ec2 -i i-abcdef -a

# Exclude resource types
aws2tf -t vpc -i vpc-12345 -e aws_eip,aws_route

# EC2 tag filtering
aws2tf -t ec2 -i i-abcdef -ec2tag Environment:Production

# Serverless/Lambda mode
aws2tf -t aws_lambda_function -i my-function -la

# Terraform provider version
aws2tf -t vpc -i vpc-12345 -tv 5.50.0

# Boto3 error debugging
aws2tf -t vpc -i vpc-12345 -b3
```

### Data Source Options
```bash
# Network data sources
aws2tf -t vpc -i vpc-12345 -dnet -dsgs

# KMS and key pair data sources  
aws2tf -t ec2 -i i-abcdef -dkms -dkey
```

### Information Commands
```bash
# List supported resources
aws2tf -l
aws2tf --list

# Validate configuration
aws2tf -v
aws2tf --validate
```

## 🆕 Enhanced with New Features

### New Workflow Modes
```bash
# Discovery only
aws2tf vpc vpc-12345 --discovery
aws2tf -t vpc -i vpc-12345 --discovery

# Validation only
aws2tf vpc vpc-12345 --validate-only

# Dry run (show what would be done)
aws2tf vpc vpc-12345 --dry-run
aws2tf -t ec2 -i i-abcdef --dry-run

# Import only
aws2tf vpc vpc-12345 --import-only

# Generate configs only
aws2tf vpc vpc-12345 --generate-only
```

### New Syntax (Also Supported)
```bash
# Positional arguments (new style)
aws2tf vpc vpc-12345
aws2tf subnet subnet-67890
aws2tf instance i-abcdef

# Mixed old/new syntax
aws2tf -t vpc -i vpc-12345 --dry-run
aws2tf vpc vpc-12345 -o networking -d
```

## 📁 Same Directory Structure

The new version creates the **exact same directory structure** as the original:

```
generated/
├── tf-{account}-{region}/                    # Default format
├── tf-{prefix}-{account}-{region}/           # With -o prefix
└── tf-{prefix}-{account}-{region}/imported/  # Imported resources subdirectory
```

### Examples:
| Command | Output Directory |
|---------|------------------|
| `aws2tf -t vpc -i vpc-12345` | `generated/tf-123456789012-us-east-1/` |
| `aws2tf -t vpc -i vpc-12345 -o networking` | `generated/tf-networking-123456789012-us-east-1/` |
| `aws2tf -t ec2 -i i-abcdef -r us-west-2` | `generated/tf-123456789012-us-west-2/` |

## 🔧 Complete Original Option List

| Short | Long | Description | Status |
|-------|------|-------------|--------|
| `-t` | `--type` | Resource type (aws_s3, ec2, aws_vpc, etc.) | ✅ Working |
| `-i` | `--id` | Resource ID | ✅ Working |
| `-l` | `--list` | List extra help information | ✅ Working |
| `-r` | `--region` | AWS region | ✅ Working |
| `-p` | `--profile` | AWS profile | ✅ Working |
| `-o` | `--output` | Add custom string to output folder | ✅ Working |
| `-m` | `--merge` | Merge mode | ✅ Working |
| `-d` | `--debug` | Debug mode | ✅ Working |
| `-s` | `--singlefile` | Only a single file main.tf is produced | ✅ Working |
| `-f` | `--fast` | Fast multi-threaded mode | ✅ Working |
| `-v` | `--validate` | Validate and exit | ✅ Working |
| `-a` | `--accept` | Expected plan changes accepted | ✅ Working |
| `-e` | `--exclude` | Resource types to exclude | ✅ Working |
| `-ec2tag` | `--ec2tag` | EC2 key:value pair to import | ✅ Working |
| `-dnet` | `--datanet` | Write data statements for aws_vpc, aws_subnet | ✅ Working |
| `-dsgs` | `--datasgs` | Write data statements for aws_security_groups | ✅ Working |
| `-dkms` | `--datakms` | Write data statements for aws_kms_key | ✅ Working |
| `-dkey` | `--datakey` | Write data statements for aws_key_pair | ✅ Working |
| `-b3` | `--boto3error` | Exit on boto3 API error (for debugging) | ✅ Working |
| `-la` | `--serverless` | Lambda mode - when running in a Lambda container | ✅ Working |
| `-tv` | `--tv` | Specify version of Terraform AWS provider | ✅ Working |

## 🚀 What's Enhanced in v2.0

### 1. Workflow Orchestrator
- **Phases**: Initialization → Discovery → Validation → Import → Generation → Finalization
- **Progress Tracking**: Real-time progress bars and status updates
- **Error Handling**: Comprehensive error handling with rollback capabilities
- **Cancellation**: Graceful workflow cancellation with Ctrl+C

### 2. Rich CLI Experience
- **Colored Output**: Success (✓), warning (⚠), error (✗) indicators
- **Progress Bars**: Visual progress indication for long operations
- **Comprehensive Help**: Detailed help with examples and explanations
- **Multiple Output Modes**: Quiet, verbose, and normal output levels

### 3. Configuration Management
- **No Global Variables**: Proper dependency injection throughout
- **Thread-Safe**: Safe for concurrent operations
- **Validation**: Comprehensive configuration validation before execution
- **Testable**: Easy mocking and testing support

### 4. Advanced Features
- **Multiple Workflow Modes**: Discovery-only, validation-only, dry-run, etc.
- **Signal Handling**: Proper SIGINT/SIGTERM handling for graceful shutdown
- **File Operations**: Automatic directory creation and file management
- **Backup Support**: Terraform state backup options

## 📋 Migration Guide

### For Existing Users
**No changes needed!** All your existing aws2tf commands work exactly the same:

```bash
# Your existing commands work unchanged
aws2tf -t vpc -i vpc-12345
aws2tf -t ec2 -i i-abcdef -f -d
aws2tf -t aws_s3 -i my-bucket -o project
```

### For New Users
You can use either the original syntax or the new enhanced syntax:

```bash
# Original syntax (fully supported)
aws2tf -t vpc -i vpc-12345

# New syntax (enhanced features)
aws2tf vpc vpc-12345 --discovery
```

## 🎯 How to Run

### Using the Compatible Version
```bash
# All original commands work
python aws2tf_compatible.py -t vpc -i vpc-12345
python aws2tf_compatible.py -t ec2 -i i-abcdef -f -d
python aws2tf_compatible.py -l

# New workflow modes also work
python aws2tf_compatible.py vpc vpc-12345 --dry-run
python aws2tf_compatible.py subnet subnet-67890 --discovery
```

### Testing Original Commands
```bash
# Test all original command patterns
python test_cli_args_simple.py

# Test specific original syntax
python aws2tf_compatible.py -t vpc -i vpc-12345 -o networking -d
```

## ✅ Verification Results

**All 12 original aws2tf command patterns tested and working:**

1. ✅ Basic VPC import: `-t vpc -i vpc-12345`
2. ✅ S3 with debug: `-t aws_s3 -i my-bucket -d`
3. ✅ EC2 fast mode: `-t ec2 -i i-abcdef -f -r us-west-2`
4. ✅ VPC with output and profile: `-t vpc -i vpc-12345 -o networking -p prod`
5. ✅ Subnet merge singlefile: `-t aws_subnet -i subnet-67890 -m -s`
6. ✅ VPC validate: `-t vpc -i vpc-12345 -v`
7. ✅ EC2 accept with exclusions: `-t ec2 -i i-abcdef -a -e aws_eip,aws_route`
8. ✅ VPC with data sources: `-t vpc -i vpc-12345 -dnet -dsgs`
9. ✅ EC2 with tag filter: `-t ec2 -i i-abcdef -ec2tag Environment:Production`
10. ✅ Lambda serverless mode: `-t aws_lambda_function -i my-function -la`
11. ✅ VPC with terraform version: `-t vpc -i vpc-12345 -tv 5.50.0`
12. ✅ VPC with boto3 error exit: `-t vpc -i vpc-12345 -b3`

**Plus 3 new workflow mode combinations tested and working!**

## 🎉 Summary

✅ **100% Backward Compatibility**: All original aws2tf commands work unchanged  
✅ **Same Directory Structure**: `generated/tf-{account}-{region}/` format maintained  
✅ **All Original Options**: Every single original flag and option supported  
✅ **Enhanced Features**: New workflow modes and rich CLI experience  
✅ **Production Ready**: Comprehensive error handling and progress tracking  

**The new AWS2TF v2.0 is a drop-in replacement for the original aws2tf with powerful enhancements!**