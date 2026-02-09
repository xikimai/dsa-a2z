"""
Solution for Practice 3: Binary Tree Right Side View
======================================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
BFS level-order traversal. The last node of each level is visible
from the right side.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
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
    """Return the right side view of the binary tree as a list."""
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


if __name__ == "__main__":
    tree = build_tree([1, 2, 3, None, 5, None, 4])
    print(solve(tree))
