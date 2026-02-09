"""
Practice 2: Balanced Binary Tree
================================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Return True if the binary tree is height-balanced.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Bottom-up: compute height, return -1 if unbalanced. If left or right is -1, or heights differ by > 1, the subtree is unbalanced.

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
    """Return True if the binary tree is height-balanced."""
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([3, 9, 20, None, None, 15, 7])
    print(solve(tree))
