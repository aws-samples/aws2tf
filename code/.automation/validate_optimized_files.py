#!/usr/bin/env python3
"""
Validate optimized fixtf_*.py files against backup copies.

This script systematically checks every optimized file to ensure no custom
logic functions were accidentally removed during optimization.

For each file:
1. Compare functions in backup vs current
2. Identify missing functions
3. Check if missing functions have custom logic
4. Report any functions with custom logic that are missing
"""

import os
import re


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
    if len(lines) <= 2:
        if all('skip' in l or 'return' in l for l in lines):
            # Check if skip is just set to 0 with no other logic
            skip_line = [l for l in lines if 'skip' in l]
            if skip_line and skip_line[0].strip() in ['skip=0', 'skip = 0']:
                return False
    
    # If more than 2 lines, likely has custom logic
    if len(lines) > 2:
        return True
    
    # Check for any conditional logic, assignments, or function calls
    has_logic = any(keyword in func_body for keyword in [
        'if ', 'elif ', 'else:', 'for ', 'while ', 'try:', 'except',
        'common.', 'fixtf.', 'context.', 'BaseResourceHandler.',
        '= aws_', 'add_dependancy', 'log.', 'client.', 'session.',
        'flag1=', 'flag2=', 't1='
    ])
    
    return has_logic


def validate_file(current_file, backup_file):
    """
    Validate a single file against its backup.
    
    Returns:
        dict: Validation results
    """
    filename = os.path.basename(current_file)
    service = filename.replace('fixtf_', '').replace('.py', '')
    
    # Read backup
    if not os.path.exists(backup_file):
        return {
            'filename': filename,
            'service': service,
            'status': 'no_backup',
            'missing_custom': []
        }
    
    with open(backup_file, 'r') as f:
        backup_content = f.read()
    
    # Read current
    with open(current_file, 'r') as f:
        current_content = f.read()
    
    # Extract functions from backup
    backup_pattern = r'def (aws_[a-z_0-9]+)\((.*?)\):(.*?)(?=\ndef |$)'
    backup_functions = re.findall(backup_pattern, backup_content, re.DOTALL)
    
    # Extract functions from current
    current_function_names = set(re.findall(r'def (aws_[a-z_0-9]+)\(', current_content))
    
    # Check for missing functions with custom logic
    missing_custom = []
    for func_name, params, func_body in backup_functions:
        if func_name not in current_function_names:
            if analyze_function(func_name, func_body):
                missing_custom.append({
                    'name': func_name,
                    'body_preview': func_body.strip()[:150]
                })
    
    return {
        'filename': filename,
        'service': service,
        'backup_total': len(backup_functions),
        'current_total': len(current_function_names),
        'missing_custom': missing_custom,
        'status': 'error' if missing_custom else 'ok'
    }


def main():
    """Main validation function."""
    print("="*70)
    print("VALIDATE OPTIMIZED FILES AGAINST BACKUPS")
    print("="*70)
    print()
    print("Checking each file systematically...")
    print()
    
    backup_dir = 'code/fixtf_aws_resources/backup_before_getattr_20251230_180054'
    current_dir = 'code/fixtf_aws_resources'
    
    # Get all current fixtf files
    current_files = [
        f for f in os.listdir(current_dir)
        if f.startswith('fixtf_') and f.endswith('.py')
    ]
    
    print(f"Validating {len(current_files)} files...")
    print()
    
    # Validate each file
    results = []
    files_with_issues = []
    
    for filename in sorted(current_files):
        current_path = os.path.join(current_dir, filename)
        backup_path = os.path.join(backup_dir, filename)
        
        result = validate_file(current_path, backup_path)
        results.append(result)
        
        if result['status'] == 'error':
            files_with_issues.append(result)
            print(f"❌ {result['service']}: {len(result['missing_custom'])} custom functions missing")
            for func in result['missing_custom']:
                print(f"     - {func['name']}")
        elif result['status'] == 'no_backup':
            print(f"⚠️  {result['service']}: No backup found (new file)")
        else:
            print(f"✅ {result['service']}: All custom functions present")
    
    # Summary
    print()
    print("="*70)
    print("VALIDATION SUMMARY")
    print("="*70)
    
    ok_count = len([r for r in results if r['status'] == 'ok'])
    error_count = len([r for r in results if r['status'] == 'error'])
    no_backup_count = len([r for r in results if r['status'] == 'no_backup'])
    
    print(f"\n✅ Valid: {ok_count}")
    print(f"❌ Missing custom functions: {error_count}")
    print(f"⚠️  No backup: {no_backup_count}")
    
    if files_with_issues:
        print(f"\n⚠️  {len(files_with_issues)} files have missing custom functions:")
        for result in files_with_issues:
            print(f"\n  {result['service']}:")
            for func in result['missing_custom']:
                print(f"    - {func['name']}")
                print(f"      Preview: {func['body_preview'][:100]}...")
        
        # Save detailed report
        report_path = 'code/.automation/validation_issues.md'
        with open(report_path, 'w') as f:
            f.write('# Validation Issues - Missing Custom Functions\n\n')
            for result in files_with_issues:
                f.write(f'## {result["service"]}\n\n')
                f.write(f'Missing {len(result["missing_custom"])} custom functions:\n\n')
                for func in result['missing_custom']:
                    f.write(f'### {func["name"]}\n\n')
                    f.write('```python\n')
                    f.write(func['body_preview'])
                    f.write('\n...\n```\n\n')
        
        print(f"\n✅ Detailed report saved to {report_path}")
        print("\nAction required: Add missing custom functions to the affected files")
    else:
        print("\n🎉 ALL FILES VALIDATED SUCCESSFULLY!")
        print("No custom logic functions are missing.")
    
    print()


if __name__ == '__main__':
    main()
