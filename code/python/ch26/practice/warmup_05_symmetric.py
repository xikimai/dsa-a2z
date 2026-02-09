"""
Warmup 5: Symmetric Tree
========================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Return True if the binary tree is symmetric, False otherwise.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Mirror check: compare left subtree with right subtree. Two trees are mirrors if roots match and left.left mirrors right.right

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
    """Return True if the binary tree is symmetric, False otherwise."""
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(solve(tree))
