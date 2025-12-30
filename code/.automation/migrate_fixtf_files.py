#!/usr/bin/env python3
"""
Automated migration script to refactor all fixtf_*.py files.

This script:
1. Analyzes each fixtf_*.py file
2. Identifies functions with custom logic vs boilerplate
3. Creates refactored version with only custom handlers
4. Adds registry imports and registrations
5. Backs up original files
6. Generates migration report
"""

import os
import re
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
            # Check if skip is just set to 0 with no other logic
            if lines[0].strip() in ['skip=0', 'skip = 0']:
                return False
    
    # If more than 2 lines, it has custom logic
    if len(lines) > 2:
        return True
    
    # Check for any conditional logic, assignments, or function calls
    has_logic = any(keyword in func_body for keyword in [
        'if ', 'elif ', 'else:', 'for ', 'while ', 'try:', 'except',
        'common.', 'fixtf.', 'context.', 'BaseResourceHandler.',
        '= aws_', 'add_dependancy', 'log.', 'client.'
    ])
    
    return has_logic


def extract_functions(content):
    """
    Extract all function definitions from a file.
    
    Returns:
        list: [(func_name, func_body, has_custom_logic), ...]
    """
    # Find all function definitions
    pattern = r'def (aws_[a-z_0-9]+)\((.*?)\):(.*?)(?=\ndef |$)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    functions = []
    for func_name, params, func_body in matches:
        has_logic = analyze_function(func_name, func_body)
        functions.append((func_name, params, func_body, has_logic))
    
    return functions


def generate_refactored_file(original_file, functions_with_logic, service_name):
    """
    Generate refactored file content.
    
    Args:
        original_file: Path to original file
        functions_with_logic: List of (func_name, params, func_body) tuples
        service_name: Service name (e.g., 'ec2', 's3')
    
    Returns:
        str: Refactored file content
    """
    # Read original to get imports
    with open(original_file, 'r') as f:
        original_content = f.read()
    
    # Extract existing imports (keep them)
    import_lines = []
    for line in original_content.split('\n'):
        if line.startswith('import ') or line.startswith('from '):
            if 'handler_registry' not in line and 'base_handler' not in line:
                import_lines.append(line)
    
    # Build refactored content
    lines = []
    lines.append('"""')
    lines.append(f'{service_name.upper()} Resource Handlers - Refactored Version')
    lines.append('')
    lines.append(f'This file contains ONLY the {service_name.upper()} resources with custom transformation logic.')
    lines.append('All other resources automatically use the default handler from base_handler.py.')
    lines.append('')
    lines.append(f'Refactored: {len(functions_with_logic)} functions with custom logic')
    lines.append('"""')
    lines.append('')
    
    # Add imports
    # Ensure logging is imported
    has_logging_import = any('import logging' in imp for imp in import_lines)
    if not has_logging_import:
        lines.append('import logging')
    
    for imp in import_lines:
        lines.append(imp)
    
    # Add new imports
    lines.append('from .handler_registry import registry')
    lines.append('from .base_handler import BaseResourceHandler')
    lines.append('')
    
    # Add logger initialization
    lines.append("log = logging.getLogger('aws2tf')")
    lines.append('')
    
    # Add custom functions
    if functions_with_logic:
        lines.append('# ' + '='*76)
        lines.append(f'# {service_name.upper()} Resources with Custom Logic')
        lines.append('# ' + '='*76)
        lines.append('')
        
        for func_name, params, func_body in functions_with_logic:
            lines.append(f'def {func_name}({params}):')
            lines.append(func_body)
            lines.append('')
        
        # Add registrations
        lines.append('')
        lines.append('# ' + '='*76)
        lines.append('# Magic method for backward compatibility')
        lines.append('# ' + '='*76)
        lines.append('')
        lines.append('def __getattr__(name):')
        lines.append('    """')
        lines.append('    Dynamically provide default handler for resources without custom logic.')
        lines.append('    ')
        lines.append('    This allows getattr(module, "aws_resource") to work even if the')
        lines.append('    function does not exist, by returning the default handler.')
        lines.append('    """')
        lines.append('    if name.startswith("aws_"):')
        lines.append('        return BaseResourceHandler.default_handler')
        lines.append(f'    raise AttributeError(f"module fixtf_{service_name} has no attribute {{name}}")')
        lines.append('')
        lines.append(f'log.debug(f"Registered {{len(registry.list_custom_handlers())}} custom {service_name.upper()} handlers")')
    else:
        lines.append(f'# No custom handlers needed for {service_name.upper()} resources')
        lines.append('# All resources use the default handler via __getattr__')
        lines.append('')
        lines.append('def __getattr__(name):')
        lines.append('    """Provide default handler for all resources."""')
        lines.append('    if name.startswith("aws_"):')
        lines.append('        return BaseResourceHandler.default_handler')
        lines.append(f'    raise AttributeError(f"module fixtf_{service_name} has no attribute {{name}}")')
    
    return '\n'.join(lines)


def migrate_file(filepath):
    """
    Migrate a single fixtf_*.py file.
    
    Returns:
        dict: Migration statistics
    """
    filename = os.path.basename(filepath)
    service_name = filename.replace('fixtf_', '').replace('.py', '')
    
    print(f"\nMigrating {filename}...")
    
    # Read original file
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract functions
    all_functions = extract_functions(content)
    
    # Separate custom logic from boilerplate
    functions_with_logic = [(name, params, body) for name, params, body, has_logic in all_functions if has_logic]
    boilerplate_functions = [(name, params, body) for name, params, body, has_logic in all_functions if not has_logic]
    
    # Generate refactored content
    refactored_content = generate_refactored_file(filepath, functions_with_logic, service_name)
    
    # Create backup
    backup_dir = 'code/fixtf_aws_resources/backup_' + datetime.now().strftime('%Y%m%d_%H%M%S')
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, filename)
    shutil.copy2(filepath, backup_path)
    
    # Write refactored file
    refactored_path = filepath.replace('.py', '_refactored.py')
    with open(refactored_path, 'w') as f:
        f.write(refactored_content)
    
    stats = {
        'filename': filename,
        'service': service_name,
        'total_functions': len(all_functions),
        'custom_functions': len(functions_with_logic),
        'boilerplate_functions': len(boilerplate_functions),
        'reduction_pct': (len(boilerplate_functions) / len(all_functions) * 100) if all_functions else 0,
        'backup_path': backup_path,
        'refactored_path': refactored_path
    }
    
    print(f"  Total functions: {stats['total_functions']}")
    print(f"  Custom logic: {stats['custom_functions']}")
    print(f"  Boilerplate: {stats['boilerplate_functions']}")
    print(f"  Reduction: {stats['reduction_pct']:.1f}%")
    print(f"  ✅ Created {refactored_path}")
    
    return stats


def main():
    """Main migration function."""
    print("="*70)
    print("FIXTF FILES MIGRATION SCRIPT")
    print("="*70)
    print()
    print("This script will refactor all fixtf_*.py files to use the handler system.")
    print()
    
    # Find all fixtf_*.py files
    fixtf_dir = 'code/fixtf_aws_resources'
    fixtf_files = [
        os.path.join(fixtf_dir, f) 
        for f in os.listdir(fixtf_dir) 
        if f.startswith('fixtf_') and f.endswith('.py') and '_refactored' not in f
    ]
    
    print(f"Found {len(fixtf_files)} fixtf_*.py files to migrate")
    print()
    
    # Migrate each file
    all_stats = []
    for filepath in sorted(fixtf_files):
        try:
            stats = migrate_file(filepath)
            all_stats.append(stats)
        except Exception as e:
            print(f"  ❌ Error migrating {filepath}: {e}")
    
    # Generate summary report
    print()
    print("="*70)
    print("MIGRATION SUMMARY")
    print("="*70)
    
    total_functions = sum(s['total_functions'] for s in all_stats)
    total_custom = sum(s['custom_functions'] for s in all_stats)
    total_boilerplate = sum(s['boilerplate_functions'] for s in all_stats)
    
    print(f"\nFiles migrated: {len(all_stats)}")
    print(f"Total functions: {total_functions}")
    print(f"Custom logic functions: {total_custom} ({total_custom/total_functions*100:.1f}%)")
    print(f"Boilerplate functions: {total_boilerplate} ({total_boilerplate/total_functions*100:.1f}%)")
    print(f"Code reduction: {total_boilerplate/total_functions*100:.1f}%")
    
    # Top services by custom logic
    print("\nTop 10 services by custom logic:")
    sorted_stats = sorted(all_stats, key=lambda x: x['custom_functions'], reverse=True)
    for i, stats in enumerate(sorted_stats[:10], 1):
        print(f"  {i}. {stats['service']}: {stats['custom_functions']} custom handlers")
    
    # Services with no custom logic
    no_logic = [s for s in all_stats if s['custom_functions'] == 0]
    if no_logic:
        print(f"\nServices with no custom logic ({len(no_logic)}):")
        for stats in no_logic[:10]:
            print(f"  - {stats['service']}")
        if len(no_logic) > 10:
            print(f"  ... and {len(no_logic) - 10} more")
    
    # Save detailed report
    report_path = 'code/.automation/migration_report.md'
    with open(report_path, 'w') as f:
        f.write('# FIXTF Files Migration Report\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('## Summary\n\n')
        f.write(f'- Files migrated: {len(all_stats)}\n')
        f.write(f'- Total functions: {total_functions}\n')
        f.write(f'- Custom logic: {total_custom} ({total_custom/total_functions*100:.1f}%)\n')
        f.write(f'- Boilerplate: {total_boilerplate} ({total_boilerplate/total_functions*100:.1f}%)\n')
        f.write(f'- Code reduction: {total_boilerplate/total_functions*100:.1f}%\n\n')
        f.write('## Detailed Results\n\n')
        f.write('| Service | Total | Custom | Boilerplate | Reduction |\n')
        f.write('|---------|-------|--------|-------------|----------|\n')
        
        for stats in sorted(all_stats, key=lambda x: x['service']):
            f.write(f"| {stats['service']} | {stats['total_functions']} | "
                   f"{stats['custom_functions']} | {stats['boilerplate_functions']} | "
                   f"{stats['reduction_pct']:.1f}% |\n")
    
    print(f"\n✅ Detailed report saved to {report_path}")
    print()
    print("="*70)
    print("NEXT STEPS")
    print("="*70)
    print("1. Review the refactored files (*_refactored.py)")
    print("2. Test a few refactored files")
    print("3. Run: python3 code/.automation/replace_original_files.py")
    print("   (This will replace original files with refactored versions)")
    print()


if __name__ == '__main__':
    main()
