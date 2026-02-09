"""
Solution for Practice 6: LCA of Binary Tree
=============================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Recursive single-pass: if current node is p or q, return it.
Recurse left and right. If both return non-null, current is LCA.
Otherwise, return the non-null one.

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


def solve(root, p, q):
    """Return the value of the LCA of nodes with values p and q."""
    def lca(node):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        left = lca(node.left)
        right = lca(node.right)
        if left and right:
            return node
        return left if left else right

    result = lca(root)
    return result.val if result else -1


if __name__ == "__main__":
    tree = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(solve(tree, 5, 1))
