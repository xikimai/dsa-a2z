"""
Solution for Practice 7: Maximum Path Sum
===========================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
For each node, compute the max path sum that can be extended upward
(single branch). Update global max with left + right + node.val.

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
    """Return the maximum path sum in the binary tree."""
    max_sum = [float('-inf')]

    def max_gain(node):
        if not node:
            return 0
        left = max(max_gain(node.left), 0)
        right = max(max_gain(node.right), 0)
        # Path through this node
        max_sum[0] = max(max_sum[0], left + right + node.val)
        # Return max single branch to parent
        return node.val + max(left, right)

    max_gain(root)
    return max_sum[0]


if __name__ == "__main__":
    tree = build_tree([1, 2, 3])
    print(solve(tree))
