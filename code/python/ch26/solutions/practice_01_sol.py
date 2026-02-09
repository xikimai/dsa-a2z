"""
Solution for Practice 1: Diameter of Binary Tree
==================================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
For each node, the longest path through it = left_height + right_height.
Track the global maximum while computing heights.

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
    """Return the diameter (longest path in edges) of the binary tree."""
    diameter = [0]

    def height(node):
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        diameter[0] = max(diameter[0], lh + rh)
        return 1 + max(lh, rh)

    height(root)
    return diameter[0]


if __name__ == "__main__":
    tree = build_tree([1, 2, 3, 4, 5])
    print(solve(tree))
