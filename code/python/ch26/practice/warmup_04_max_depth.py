"""
Warmup 4: Maximum Depth of Binary Tree
======================================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Return the maximum depth of the binary tree.

EXAMPLES
--------
  solve(build_tree([3, 9, 20, None, None, 15, 7])) -> 3
  solve(build_tree([1, None, 2])) -> 2
  solve(None) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Recursive: depth = 1 + max(left depth, right depth). Base: null -> 0.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def solve(root):
    """Return the maximum depth of the binary tree."""
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, None, None, 15, 7])
    print(solve(tree))
