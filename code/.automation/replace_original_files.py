#!/usr/bin/env python3
"""
Replace original fixtf_*.py files with refactored versions.

This script:
1. Verifies all refactored files exist and are valid Python
2. Creates a final backup of all original files
3. Replaces original files with refactored versions
4. Cleans up temporary refactored files
5. Generates completion report

IMPORTANT: Run this only after reviewing and testing refactored files!
"""

import os
import shutil
import sys
from datetime import datetime


def verify_refactored_file(filepath):
    """
    Verify a refactored file is valid Python.
    
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        with open(filepath, 'r') as f:
            compile(f.read(), filepath, 'exec')
        return True
    except SyntaxError as e:
        print(f"  ❌ Syntax error in {filepath}: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error validating {filepath}: {e}")
        return False


def main():
    """Main replacement function."""
    print("="*70)
    print("REPLACE ORIGINAL FILES WITH REFACTORED VERSIONS")
    print("="*70)
    print()
    print("⚠️  WARNING: This will replace all original fixtf_*.py files!")
    print()
    
    # Find all refactored files
    fixtf_dir = 'code/fixtf_aws_resources'
    refactored_files = [
        f for f in os.listdir(fixtf_dir)
        if f.startswith('fixtf_') and f.endswith('_refactored.py')
    ]
    
    if not refactored_files:
        print("❌ No refactored files found!")
        print("   Run migrate_fixtf_files.py first.")
        sys.exit(1)
    
    print(f"Found {len(refactored_files)} refactored files")
    print()
    
    # Verify all refactored files
    print("Verifying refactored files...")
    invalid_files = []
    for filename in refactored_files:
        filepath = os.path.join(fixtf_dir, filename)
        if verify_refactored_file(filepath):
            print(f"  ✅ {filename}")
        else:
            invalid_files.append(filename)
    
    if invalid_files:
        print()
        print(f"❌ {len(invalid_files)} files have errors!")
        print("   Fix these files before proceeding:")
        for f in invalid_files:
            print(f"     - {f}")
        sys.exit(1)
    
    print()
    print("✅ All refactored files are valid Python")
    print()
    
    # Confirm with user
    response = input("Proceed with replacement? (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted.")
        sys.exit(0)
    
    # Create final backup
    backup_dir = os.path.join(fixtf_dir, 'backup_final_' + datetime.now().strftime('%Y%m%d_%H%M%S'))
    os.makedirs(backup_dir, exist_ok=True)
    print(f"\nCreating final backup in {backup_dir}...")
    
    replaced_count = 0
    for refactored_filename in refactored_files:
        # Get original filename
        original_filename = refactored_filename.replace('_refactored', '')
        original_path = os.path.join(fixtf_dir, original_filename)
        refactored_path = os.path.join(fixtf_dir, refactored_filename)
        backup_path = os.path.join(backup_dir, original_filename)
        
        # Backup original
        if os.path.exists(original_path):
            shutil.copy2(original_path, backup_path)
        
        # Replace with refactored
        shutil.copy2(refactored_path, original_path)
        
        # Remove refactored file
        os.remove(refactored_path)
        
        replaced_count += 1
        print(f"  ✅ Replaced {original_filename}")
    
    print()
    print("="*70)
    print("REPLACEMENT COMPLETE")
    print("="*70)
    print(f"\n✅ Replaced {replaced_count} files")
    print(f"✅ Backup saved to {backup_dir}")
    print()
    print("Next steps:")
    print("1. Test the application with refactored code")
    print("2. If issues occur, restore from backup:")
    print(f"   cp {backup_dir}/*.py {fixtf_dir}/")
    print()


if __name__ == '__main__':
    main()
