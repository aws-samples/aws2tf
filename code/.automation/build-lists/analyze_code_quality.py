#!/usr/bin/env python3
"""
Code quality analyzer for build_lists.py
Checks nesting depth and local variable count
"""

import ast
import sys

class CodeQualityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.max_nesting = 0
        self.current_nesting = 0
        self.function_vars = {}
        self.current_function = None
        
    def visit_FunctionDef(self, node):
        # Track function name
        old_function = self.current_function
        self.current_function = node.name
        self.function_vars[node.name] = set()
        
        # Count parameters as local variables
        for arg in node.args.args:
            self.function_vars[node.name].add(arg.arg)
        
        # Visit function body
        self.generic_visit(node)
        
        # Restore previous function context
        self.current_function = old_function
    
    def visit_Name(self, node):
        # Track variable assignments in current function
        if self.current_function and isinstance(node.ctx, ast.Store):
            self.function_vars[self.current_function].add(node.id)
        self.generic_visit(node)
    
    def visit_For(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        self.generic_visit(node)
        self.current_nesting -= 1
    
    def visit_While(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        self.generic_visit(node)
        self.current_nesting -= 1
    
    def visit_If(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        self.generic_visit(node)
        self.current_nesting -= 1
    
    def visit_With(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        self.generic_visit(node)
        self.current_nesting -= 1
    
    def visit_Try(self, node):
        self.current_nesting += 1
        self.max_nesting = max(self.max_nesting, self.current_nesting)
        self.generic_visit(node)
        self.current_nesting -= 1

def analyze_file(filepath):
    with open(filepath, 'r') as f:
        source = f.read()
    
    tree = ast.parse(source)
    analyzer = CodeQualityAnalyzer()
    analyzer.visit(tree)
    
    print(f"Code Quality Analysis for {filepath}")
    print("=" * 60)
    print(f"\nMaximum Nesting Depth: {analyzer.max_nesting}")
    print(f"Target: ≤ 5 levels")
    print(f"Status: {'✓ PASS' if analyzer.max_nesting <= 5 else '✗ FAIL'}")
    
    print(f"\nLocal Variables per Function:")
    print("-" * 60)
    
    max_vars = 0
    max_vars_func = None
    
    for func_name, vars_set in sorted(analyzer.function_vars.items()):
        var_count = len(vars_set)
        status = "✓" if var_count < 20 else "✗"
        print(f"{status} {func_name}: {var_count} variables")
        
        if var_count > max_vars:
            max_vars = var_count
            max_vars_func = func_name
    
    print(f"\nMaximum Local Variables: {max_vars} (in {max_vars_func})")
    print(f"Target: < 20 variables")
    print(f"Status: {'✓ PASS' if max_vars < 20 else '✗ FAIL'}")
    
    print("\n" + "=" * 60)
    
    # Overall status
    nesting_pass = analyzer.max_nesting <= 5
    vars_pass = max_vars < 20
    
    if nesting_pass and vars_pass:
        print("Overall: ✓ ALL CHECKS PASSED")
        return 0
    else:
        print("Overall: ✗ SOME CHECKS FAILED")
        return 1

if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "code/build_lists.py"
    sys.exit(analyze_file(filepath))
