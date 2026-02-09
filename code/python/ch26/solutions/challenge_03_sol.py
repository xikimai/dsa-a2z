"""
Solution for Challenge 3: Boundary Traversal
==============================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Three parts: left boundary (top-down), leaves (left-to-right),
right boundary (bottom-up). Each excludes the root (added once).

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
    """Return the boundary traversal of the binary tree."""
    if not root:
        return []

    def is_leaf(node):
        return node and not node.left and not node.right

    if is_leaf(root):
        return [root.val]

    result = [root.val]

    # Left boundary (exclude root and leaves)
    node = root.left
    while node:
        if not is_leaf(node):
            result.append(node.val)
        node = node.left if node.left else node.right

    # All leaves left to right
    def add_leaves(node):
        if not node:
            return
        if is_leaf(node):
            result.append(node.val)
            return
        add_leaves(node.left)
        add_leaves(node.right)

    add_leaves(root)

    # Right boundary (exclude root and leaves, bottom-up)
    right_boundary = []
    node = root.right
    while node:
        if not is_leaf(node):
            right_boundary.append(node.val)
        node = node.right if node.right else node.left
    result.extend(reversed(right_boundary))

    return result


if __name__ == "__main__":
    tree = build_tree([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10])
    print(solve(tree))
