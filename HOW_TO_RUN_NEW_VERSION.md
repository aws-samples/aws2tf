# How to Run the New AWS2TF Version

The new AWS2TF v2.0 includes a workflow orchestrator and comprehensive CLI interface while maintaining the same directory structure as the original version.

## Quick Start

### Basic Usage

```bash
# Import a VPC and all its dependencies
python aws2tf_new_cli.py vpc vpc-12345

# Import with custom output prefix
python aws2tf_new_cli.py vpc vpc-12345 --output networking

# Dry-run mode (show what would be done)
python aws2tf_new_cli.py subnet subnet-67890 --dry-run

# Discovery-only mode (just discover resources)
python aws2tf_new_cli.py instance i-abcdef --discovery
```

### Output Directory Structure

The new version maintains the **exact same directory structure** as the original aws2tf:

```
generated/
├── tf-{account}-{region}/                    # Default format
├── tf-{prefix}-{account}-{region}/           # With custom prefix
└── tf-{prefix}-{account}-{region}/imported/  # Imported resources subdirectory
```

#### Examples:

| Command | Output Directory |
|---------|------------------|
| `aws2tf vpc vpc-12345` | `generated/tf-123456789012-us-east-1/` |
| `aws2tf subnet subnet-67890 -o network` | `generated/tf-network-123456789012-us-east-1/` |
| `aws2tf instance i-abc123 --region us-west-2` | `generated/tf-123456789012-us-west-2/` |

## Available Commands

### Workflow Modes

```bash
# Complete workflow (default)
python aws2tf_new_cli.py vpc vpc-12345 --full

# Discovery only
python aws2tf_new_cli.py vpc vpc-12345 --discovery

# Validation only  
python aws2tf_new_cli.py vpc vpc-12345 --validate-only

# Dry-run (no changes)
python aws2tf_new_cli.py vpc vpc-12345 --dry-run
```

### Configuration Options

```bash
# Specify AWS region
python aws2tf_new_cli.py vpc vpc-12345 --region us-west-2

# Enable debug mode
python aws2tf_new_cli.py vpc vpc-12345 --debug

# Quiet mode (minimal output)
python aws2tf_new_cli.py vpc vpc-12345 --quiet

# Verbose mode (detailed output)
python aws2tf_new_cli.py vpc vpc-12345 --verbose
```

### Information Commands

```bash
# List supported resource types
python aws2tf_new_cli.py --list-resources

# Validate configuration
python aws2tf_new_cli.py --validate-config

# Show version
python aws2tf_new_cli.py --version

# Show help
python aws2tf_new_cli.py --help
```

## What's New in v2.0

### 🚀 **Workflow Orchestrator**
- **Phases**: Initialization → Discovery → Validation → Import → Generation → Finalization
- **Progress Tracking**: Real-time progress bars and status updates
- **Error Handling**: Comprehensive error handling with rollback capabilities
- **Cancellation**: Graceful workflow cancellation with Ctrl+C

### 🎯 **Enhanced CLI Interface**
- **Rich Output**: Colored output with success (✓), warning (⚠), error (✗) indicators
- **Multiple Modes**: Discovery-only, validation-only, dry-run, and full workflow modes
- **Configuration Management**: No more global variables - proper dependency injection
- **Signal Handling**: Graceful shutdown on interruption

### 🔧 **Configuration System**
- **Centralized Config**: All configuration managed through `ConfigurationManager`
- **Validation**: Comprehensive configuration validation before execution
- **Thread-Safe**: Safe for concurrent operations
- **Testable**: Easy mocking and testing support

### 📁 **Same Directory Structure**
- **Backward Compatible**: Uses the exact same `generated/tf-{account}-{region}/` format
- **Prefix Support**: Optional prefix for organizing multiple projects
- **Imported Subdirectory**: Maintains the `imported/` subdirectory convention
- **Complete Files**: Generates all necessary terraform files (main.tf, variables.tf, etc.)

## Testing the New Version

### 1. Test CLI Interface
```bash
# Test the CLI interface and argument parsing
python cli_standalone_demo.py
```

### 2. Test Workflow Orchestrator
```bash
# Test the workflow orchestrator
python main_workflow_standalone.py
```

### 3. Test Directory Structure
```bash
# Test directory structure creation
python test_output_directory.py
```

### 4. Create Real Directory Structure
```bash
# Create actual directories to see the structure
python demo_real_directory_structure.py
```

## Migration from Original aws2tf

The new version is **100% backward compatible** with the original aws2tf:

### Same Commands Work
```bash
# Original command
aws2tf vpc vpc-12345

# New version (same result)
python aws2tf_new_cli.py vpc vpc-12345
```

### Same Directory Structure
- Output goes to `generated/tf-{account}-{region}/`
- Includes `imported/` subdirectory
- Same terraform file organization

### Same Workflow
1. Discover AWS resources and dependencies
2. Validate resource relationships
3. Generate terraform import commands
4. Create terraform configuration files
5. Provide import script and documentation

## Advanced Usage

### Custom Output Organization
```bash
# Organize by environment
python aws2tf_new_cli.py vpc vpc-12345 --output production
python aws2tf_new_cli.py vpc vpc-67890 --output staging

# Organize by team
python aws2tf_new_cli.py subnet subnet-12345 --output networking-team
python aws2tf_new_cli.py instance i-abcdef --output compute-team
```

### Multi-Region Support
```bash
# Import from different regions
python aws2tf_new_cli.py vpc vpc-12345 --region us-east-1
python aws2tf_new_cli.py vpc vpc-67890 --region us-west-2
python aws2tf_new_cli.py vpc vpc-abcdef --region eu-west-1
```

### Development Workflow
```bash
# 1. Discover what resources exist
python aws2tf_new_cli.py vpc vpc-12345 --discovery

# 2. Validate dependencies
python aws2tf_new_cli.py vpc vpc-12345 --validate-only

# 3. See what would be imported (dry-run)
python aws2tf_new_cli.py vpc vpc-12345 --dry-run

# 4. Actually import the resources
python aws2tf_new_cli.py vpc vpc-12345
```

## Next Steps

1. **Test with Real AWS Resources**: Use your actual AWS credentials and resource IDs
2. **Integrate with Existing Workflow**: Replace calls to original aws2tf with the new version
3. **Customize Configuration**: Adjust settings in the configuration system as needed
4. **Add to CI/CD**: Integrate the new version into your automation pipelines

The new aws2tf v2.0 provides all the functionality of the original version with enhanced reliability, better error handling, and improved user experience while maintaining complete backward compatibility!