"""
Solution for Practice 5: Kth Smallest in BST
==============================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Inorder traversal of a BST visits nodes in ascending order.
Do inorder, count, and return when count == k.

TIME COMPLEXITY:  O(h + k)
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


def solve(root, k):
    """Return the kth smallest element in the BST (1-indexed)."""
    count = [0]
    result = [0]

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        inorder(node.right)

    inorder(root)
    return result[0]


if __name__ == "__main__":
    tree = build_tree([3, 1, 4, None, 2])
    print(solve(tree, 1))
