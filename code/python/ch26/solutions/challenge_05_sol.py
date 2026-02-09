"""
Solution for Challenge 5: Flatten Binary Tree to Linked List
==============================================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Preorder traversal collecting values into a list.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
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
    """Flatten the tree to preorder and return values as a list."""
    if not root:
        return []
    result = []

    def preorder(node):
        if not node:
            return
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return result


if __name__ == "__main__":
    tree = build_tree([1, 2, 5, 3, 4, None, 6])
    print(solve(tree))
