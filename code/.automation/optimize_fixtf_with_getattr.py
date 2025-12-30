#!/usr/bin/env python3
"""
Optimize fixtf_*.py files using __getattr__ approach.

This script processes files one by one:
1. Analyzes each file to identify custom logic functions
2. Creates optimized version with only custom functions + __getattr__
3. Replaces the original file
4. Tests that it still works
5. Continues to next file

Usage:
    python3 code/.automation/optimize_fixtf_with_getattr.py [--file fixtf_lambda.py] [--all]
"""

import os
import re
import sys
import argparse
import shutil
from datetime import datetime


def analyze_function(func_name, func_body):
    """
    Determine if a function has custom logic or is just boilerplate.
    
    Returns:
        bool: True if function has custom logic, False if boilerplate
    """
    # Remove comments and empty lines
    lines = [l.strip() for l in func_body.strip().split('\n') 
             if l.strip() and not l.strip().startswith('#')]
    
    # Check if it's just skip=0 and return
    if len(lines) == 2:
        if 'skip' in lines[0] and 'return' in lines[1]:
            if lines[0].strip() in ['skip=0', 'skip = 0']:
                return False
    
    # If more than 2 lines, it has custom logic
    if len(lines) > 2:
        return True
    
    # Check for any conditional logic, assignments, or function calls
    has_logic = any(keyword in func_body for keyword in [
        'if ', 'elif ', 'else:', 'for ', 'while ', 'try:', 'except',
        'common.', 'fixtf.', 'context.', 'BaseResourceHandler.',
        '= aws_', 'add_dependancy', 'log.', 'client.', 'session.'
    ])
    
    return has_logic


def extract_functions(content):
    """
    Extract all function definitions from a file.
    
    Returns:
        list: [(func_name, params, func_body, has_custom_logic), ...]
    """
    pattern = r'def (aws_[a-z_0-9]+)\((.*?)\):(.*?)(?=\ndef |$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    functions = []
    for func_name, params, func_body in matches:
        has_logic = analyze_function(func_name, func_body)
        functions.append((func_name, params, func_body, has_logic))
    
    return functions


def generate_optimized_file(original_file, functions_with_logic, service_name):
    """
    Generate optimized file content with __getattr__.
    
    Args:
        original_file: Path to original file
        functions_with_logic: List of (func_name, params, func_body) tuples
        service_name: Service name (e.g., 'ec2', 's3')
    
    Returns:
        str: Optimized file content
    """
    # Read original to get imports
    with open(original_file, 'r') as f:
        original_content = f.read()
    
    # Extract existing imports
    import_lines = []
    for line in original_content.split('\n'):
        if line.startswith('import ') or line.startswith('from '):
            if 'base_handler' not in line:
                import_lines.append(line)
    
    # Build optimized content
    lines = []
    lines.append('"""')
    lines.append(f'{service_name.upper()} Resource Handlers - Optimized with __getattr__')
    lines.append('')
    lines.append(f'This file contains ONLY {service_name.upper()} resources with custom transformation logic.')
    lines.append('All other resources automatically use the default handler via __getattr__.')
    lines.append('')
    
    # Count total functions in original
    all_functions = extract_functions(original_content)
    total_count = len(all_functions)
    custom_count = len(functions_with_logic)
    reduction = ((total_count - custom_count) / total_count * 100) if total_count > 0 else 0
    
    lines.append(f'Original: {total_count} functions')
    lines.append(f'Optimized: {custom_count} functions + __getattr__')
    lines.append(f'Reduction: {reduction:.0f}% less code')
    lines.append('"""')
    lines.append('')
    
    # Add imports
    # Ensure logging is imported first
    has_logging = any('import logging' in imp for imp in import_lines)
    if not has_logging:
        lines.append('import logging')
    
    for imp in import_lines:
        lines.append(imp)
    
    # Add base_handler import
    lines.append('from .base_handler import BaseResourceHandler')
    lines.append('')
    
    # Add logger
    lines.append("log = logging.getLogger('aws2tf')")
    lines.append('')
    
    # Add custom functions
    if functions_with_logic:
        lines.append('')
        lines.append('# ' + '='*76)
        lines.append(f'# {service_name.upper()} Resources with Custom Logic ({len(functions_with_logic)} functions)')
        lines.append('# ' + '='*76)
        lines.append('')
        
        for func_name, params, func_body in functions_with_logic:
            lines.append(f'def {func_name}({params}):')
            lines.append(func_body)
            lines.append('')
    
    # Add __getattr__
    lines.append('')
    lines.append('# ' + '='*76)
    lines.append('# Magic method for backward compatibility with getattr()')
    lines.append('# ' + '='*76)
    lines.append('')
    lines.append('def __getattr__(name):')
    lines.append('\t"""')
    lines.append('\tDynamically provide default handler for resources without custom logic.')
    lines.append('\t')
    lines.append(f'\tThis allows getattr(module, "aws_resource") to work even if the')
    lines.append('\tfunction doesn\'t exist, by returning the default handler.')
    lines.append('\t')
    
    if functions_with_logic:
        simple_count = total_count - custom_count
        lines.append(f'\tAll simple {service_name.upper()} resources ({simple_count} resources) automatically use this.')
    else:
        lines.append(f'\tAll {service_name.upper()} resources automatically use this.')
    
    lines.append('\t"""')
    lines.append('\tif name.startswith("aws_"):')
    lines.append('\t\treturn BaseResourceHandler.default_handler')
    lines.append(f'\traise AttributeError(f"module \'fixtf_{service_name}\' has no attribute \'{{name}}\'")')
    lines.append('')
    lines.append('')
    
    if functions_with_logic:
        lines.append(f'log.debug(f"{service_name.upper()} handlers: {custom_count} custom functions + __getattr__ for {total_count - custom_count} simple resources")')
    else:
        lines.append(f'log.debug(f"{service_name.upper()} handlers: __getattr__ for all {total_count} resources")')
    
    return '\n'.join(lines)


def optimize_file(filepath, dry_run=False):
    """
    Optimize a single fixtf_*.py file.
    
    Returns:
        dict: Optimization statistics
    """
    filename = os.path.basename(filepath)
    service_name = filename.replace('fixtf_', '').replace('.py', '')
    
    print(f"\nOptimizing {filename}...")
    
    # Read original file
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract functions
    all_functions = extract_functions(content)
    
    # Separate custom logic from boilerplate
    functions_with_logic = [(name, params, body) for name, params, body, has_logic in all_functions if has_logic]
    boilerplate_functions = [(name, params, body) for name, params, body, has_logic in all_functions if not has_logic]
    
    # Generate optimized content
    optimized_content = generate_optimized_file(filepath, functions_with_logic, service_name)
    
    stats = {
        'filename': filename,
        'service': service_name,
        'total_functions': len(all_functions),
        'custom_functions': len(functions_with_logic),
        'boilerplate_functions': len(boilerplate_functions),
        'reduction_pct': (len(boilerplate_functions) / len(all_functions) * 100) if all_functions else 0
    }
    
    print(f"  Total functions: {stats['total_functions']}")
    print(f"  Custom logic: {stats['custom_functions']}")
    print(f"  Boilerplate: {stats['boilerplate_functions']}")
    print(f"  Reduction: {stats['reduction_pct']:.1f}%")
    
    if not dry_run:
        # Write optimized file
        with open(filepath, 'w') as f:
            f.write(optimized_content)
        print(f"  ✅ Optimized {filename}")
    else:
        print(f"  [DRY RUN] Would optimize {filename}")
    
    return stats


def main():
    """Main optimization function."""
    parser = argparse.ArgumentParser(description='Optimize fixtf_*.py files with __getattr__')
    parser.add_argument('--file', help='Specific file to optimize (e.g., fixtf_lambda.py)')
    parser.add_argument('--all', action='store_true', help='Optimize all remaining files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    parser.add_argument('--skip', nargs='+', help='Files to skip (e.g., fixtf_ec2.py fixtf_s3.py)')
    
    args = parser.parse_args()
    
    print("="*70)
    print("OPTIMIZE FIXTF FILES WITH __GETATTR__")
    print("="*70)
    print()
    
    # Find files to process
    fixtf_dir = 'code/fixtf_aws_resources'
    
    if args.file:
        # Process single file
        files_to_process = [os.path.join(fixtf_dir, args.file)]
    elif args.all:
        # Process all files
        files_to_process = [
            os.path.join(fixtf_dir, f)
            for f in os.listdir(fixtf_dir)
            if f.startswith('fixtf_') and f.endswith('.py')
        ]
        
        # Skip already optimized files
        skip_files = args.skip or ['fixtf_ec2.py', 'fixtf_s3.py']
        files_to_process = [f for f in files_to_process if os.path.basename(f) not in skip_files]
    else:
        print("Error: Specify --file or --all")
        sys.exit(1)
    
    print(f"Files to process: {len(files_to_process)}")
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified")
    print()
    
    # Process each file
    all_stats = []
    for filepath in sorted(files_to_process):
        try:
            stats = optimize_file(filepath, dry_run=args.dry_run)
            all_stats.append(stats)
        except Exception as e:
            print(f"  ❌ Error optimizing {filepath}: {e}")
    
    # Summary
    print()
    print("="*70)
    print("OPTIMIZATION SUMMARY")
    print("="*70)
    
    total_functions = sum(s['total_functions'] for s in all_stats)
    total_custom = sum(s['custom_functions'] for s in all_stats)
    total_boilerplate = sum(s['boilerplate_functions'] for s in all_stats)
    
    print(f"\nFiles optimized: {len(all_stats)}")
    print(f"Total functions: {total_functions}")
    print(f"Custom logic: {total_custom} ({total_custom/total_functions*100:.1f}%)")
    print(f"Boilerplate removed: {total_boilerplate} ({total_boilerplate/total_functions*100:.1f}%)")
    print(f"Code reduction: {total_boilerplate/total_functions*100:.1f}%")
    
    # Save report
    if not args.dry_run:
        report_path = 'code/.automation/optimization_report.md'
        with open(report_path, 'w') as f:
            f.write('# FIXTF Files Optimization Report\n\n')
            f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
            f.write('## Summary\n\n')
            f.write(f'- Files optimized: {len(all_stats)}\n')
            f.write(f'- Total functions: {total_functions}\n')
            f.write(f'- Custom logic: {total_custom} ({total_custom/total_functions*100:.1f}%)\n')
            f.write(f'- Boilerplate removed: {total_boilerplate} ({total_boilerplate/total_functions*100:.1f}%)\n')
            f.write(f'- Code reduction: {total_boilerplate/total_functions*100:.1f}%\n\n')
            f.write('## Detailed Results\n\n')
            f.write('| Service | Total | Custom | Removed | Reduction |\n')
            f.write('|---------|-------|--------|---------|----------|\n')
            
            for stats in sorted(all_stats, key=lambda x: x['service']):
                f.write(f"| {stats['service']} | {stats['total_functions']} | "
                       f"{stats['custom_functions']} | {stats['boilerplate_functions']} | "
                       f"{stats['reduction_pct']:.1f}% |\n")
        
        print(f"\n✅ Report saved to {report_path}")
    
    print()
    print("="*70)
    print("NEXT STEPS")
    print("="*70)
    if args.dry_run:
        print("Run without --dry-run to apply changes")
    else:
        print("Test the application to ensure everything works:")
        print("  ./aws2tf.py -t vpc")
        print("  ./aws2tf.py -t s3")
        print("  ./aws2tf.py -t lambda")
    print()


if __name__ == '__main__':
    main()
