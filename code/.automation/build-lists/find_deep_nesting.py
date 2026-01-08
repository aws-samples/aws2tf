#!/usr/bin/env python3
"""
Find locations with deep nesting in build_lists.py
"""

import ast

class NestingFinder(ast.NodeVisitor):
    def __init__(self):
        self.nesting_stack = []
        self.deep_locations = []
        
    def _enter_block(self, node, block_type):
        self.nesting_stack.append((block_type, node.lineno))
        depth = len(self.nesting_stack)
        
        if depth > 5:
            self.deep_locations.append({
                'line': node.lineno,
                'depth': depth,
                'stack': list(self.nesting_stack)
            })
        
        self.generic_visit(node)
        self.nesting_stack.pop()
    
    def visit_For(self, node):
        self._enter_block(node, 'for')
    
    def visit_While(self, node):
        self._enter_block(node, 'while')
    
    def visit_If(self, node):
        self._enter_block(node, 'if')
    
    def visit_With(self, node):
        self._enter_block(node, 'with')
    
    def visit_Try(self, node):
        self._enter_block(node, 'try')

def find_deep_nesting(filepath):
    with open(filepath, 'r') as f:
        source = f.read()
        lines = source.split('\n')
    
    tree = ast.parse(source)
    finder = NestingFinder()
    finder.visit(tree)
    
    print(f"Deep Nesting Locations (> 5 levels) in {filepath}")
    print("=" * 70)
    
    for loc in finder.deep_locations:
        print(f"\nLine {loc['line']}: Depth {loc['depth']}")
        print(f"Code: {lines[loc['line']-1].strip()}")
        print("Nesting stack:")
        for i, (block_type, line) in enumerate(loc['stack'], 1):
            print(f"  {i}. {block_type} (line {line})")

if __name__ == "__main__":
    find_deep_nesting("code/build_lists.py")
