"""
Warmup 3: Level Order Traversal
===============================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Return the level-order traversal as a list of lists.

EXAMPLES
--------
  solve(build_tree([3, 9, 20, None, None, 15, 7])) -> [[3], [9, 20], [15, 7]]
  solve(build_tree([1])) -> [[1]]
  solve(None) -> []

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
BFS with a queue. Process one level at a time.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import deque


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
    """Return the level-order traversal as a list of lists."""
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, None, None, 15, 7])
    print(solve(tree))
