"""
Solution for Challenge 1: Construct from Preorder + Inorder
=============================================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Preorder first element is root. Find it in inorder to split into
left/right subtrees. Use a hash map for O(1) inorder lookups.

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


def tree_to_list(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def solve(preorder, inorder):
    """Build tree from preorder+inorder, return as level-order list."""
    if not preorder:
        return []

    in_map = {val: idx for idx, val in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        in_idx = in_map[root_val]
        left_size = in_idx - in_start

        root.left = build(pre_start + 1, pre_start + left_size,
                          in_start, in_idx - 1)
        root.right = build(pre_start + left_size + 1, pre_end,
                           in_idx + 1, in_end)
        return root

    root = build(0, len(preorder) - 1, 0, len(inorder) - 1)
    return tree_to_list(root)


if __name__ == "__main__":
    print(solve([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
