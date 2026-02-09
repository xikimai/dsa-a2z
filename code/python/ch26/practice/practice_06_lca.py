"""
Practice 6: LCA of Binary Tree
==============================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Return the value of the LCA of nodes with values p and q.

EXAMPLES
--------
  solve(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 1) -> 3
  solve(build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), 5, 4) -> 5
  solve(build_tree([1, 2]), 1, 2) -> 1

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Recursive single-pass: if current node is p or q, return it. Recurse left and right. If both return non-null, current is LCA.

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


def solve(root, p, q):
    """Return the value of the LCA of nodes with values p and q."""
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(solve(tree, 5, 1))
