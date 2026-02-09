"""
Example 01: Tree Basics — Traversals, Height, and More
=======================================================
Chapter 26: Trees — Branches of Logic

This example demonstrates:
  - Building a binary tree from a list (level-order)
  - Inorder, Preorder, Postorder traversals (recursive)
  - Level-order traversal (BFS with queue)
  - Height / max depth of a tree
"""

from collections import deque


# ── TreeNode definition ──────────────────────────────────────────

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Build a binary tree from a level-order list. None means no node."""
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


# ── Traversals (recursive) ──────────────────────────────────────

def inorder(root):
    """Left -> Root -> Right. For BSTs, this gives sorted order."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root):
    """Root -> Left -> Right. Useful for serialization."""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root):
    """Left -> Right -> Root. Useful for deletion and expression trees."""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# ── Level-order (BFS) ───────────────────────────────────────────

def level_order(root):
    """BFS level-by-level. Returns list of lists."""
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result


# ── Height / Max Depth ──────────────────────────────────────────

def max_depth(root):
    """Height of tree = number of nodes on longest root-to-leaf path."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("TREE BASICS: Traversals and Height")
    print("=" * 60)

    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree = build_tree([1, 2, 3, 4, 5])

    print(f"\n  Tree: [1, 2, 3, 4, 5] (level-order input)")
    print(f"  Inorder:     {inorder(tree)}")       # [4, 2, 5, 1, 3]
    print(f"  Preorder:    {preorder(tree)}")       # [1, 2, 4, 5, 3]
    print(f"  Postorder:   {postorder(tree)}")      # [4, 5, 2, 3, 1]
    print(f"  Level-order: {level_order(tree)}")    # [[1], [2, 3], [4, 5]]
    print(f"  Max depth:   {max_depth(tree)}")      # 3

    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    tree2 = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"\n  Tree: [3, 9, 20, None, None, 15, 7]")
    print(f"  Inorder:     {inorder(tree2)}")       # [9, 3, 15, 20, 7]
    print(f"  Level-order: {level_order(tree2)}")    # [[3], [9, 20], [15, 7]]
    print(f"  Max depth:   {max_depth(tree2)}")      # 3

    print("\n  KEY INSIGHT: Inorder on a BST gives sorted order!")
    bst = build_tree([4, 2, 6, 1, 3, 5, 7])
    print(f"  BST [4,2,6,1,3,5,7] inorder: {inorder(bst)}")  # [1,2,3,4,5,6,7]
