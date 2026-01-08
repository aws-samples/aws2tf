#!/usr/bin/env python3
"""
Check for unused variables in build_lists.py
"""

import ast
import sys

class UnusedVariableChecker(ast.NodeVisitor):
    def __init__(self):
        self.scopes = [{}]  # Stack of scopes
        self.unused_vars = []
        
    def _current_scope(self):
        return self.scopes[-1]
    
    def visit_FunctionDef(self, node):
        # Enter new scope
        self.scopes.append({})
        
        # Add parameters to scope
        for arg in node.args.args:
            self._current_scope()[arg.arg] = {
                'defined': node.lineno,
                'used': False,
                'name': arg.arg
            }
        
        # Visit function body
        self.generic_visit(node)
        
        # Check for unused variables in this scope
        for var_name, var_info in self._current_scope().items():
            if not var_info['used'] and not var_name.startswith('_'):
                self.unused_vars.append({
                    'name': var_name,
                    'line': var_info['defined'],
                    'function': node.name
                })
        
        # Exit scope
        self.scopes.pop()
    
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            # Variable assignment
            self._current_scope()[node.id] = {
                'defined': node.lineno,
                'used': False,
                'name': node.id
            }
        elif isinstance(node.ctx, ast.Load):
            # Variable usage
            if node.id in self._current_scope():
                self._current_scope()[node.id]['used'] = True
        
        self.generic_visit(node)

def check_unused_variables(filepath):
    with open(filepath, 'r') as f:
        source = f.read()
    
    tree = ast.parse(source)
    checker = UnusedVariableChecker()
    checker.visit(tree)
    
    print(f"Unused Variable Check for {filepath}")
    print("=" * 60)
    
    if not checker.unused_vars:
        print("\n✓ No unused variables found!")
        return 0
    else:
        print(f"\n✗ Found {len(checker.unused_vars)} unused variables:")
        print("-" * 60)
        for var in checker.unused_vars:
            print(f"Line {var['line']}: '{var['name']}' in function '{var['function']}'")
        return 1

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "code/build_lists.py"
    sys.exit(check_unused_variables(filepath))
