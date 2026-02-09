"""
Solution for Warmup 2: Preorder Traversal
===========================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Recursive DFS: visit node, go left, go right.

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
    """Return the preorder traversal of the binary tree as a list."""
    if not root:
        return []
    return [root.val] + solve(root.left) + solve(root.right)


if __name__ == "__main__":
    tree = build_tree([1, None, 2, 3])
    print(solve(tree))
