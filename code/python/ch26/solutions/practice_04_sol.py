"""
Solution for Practice 4: Validate BST
=======================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Pass valid range (lo, hi) down the tree. Each node must be within range.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(h)
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
    """Return True if the binary tree is a valid BST."""
    def validate(node, lo, hi):
        if not node:
            return True
        if node.val <= lo or node.val >= hi:
            return False
        return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)

    return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    tree = build_tree([2, 1, 3])
    print(solve(tree))
