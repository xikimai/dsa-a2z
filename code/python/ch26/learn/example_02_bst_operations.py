"""
Example 02: BST Operations — Search, Insert, Delete, Validate
=============================================================
Chapter 26: Trees — Branches of Logic

This example demonstrates:
  - Searching in a BST
  - Inserting into a BST
  - Deleting from a BST
  - Validating whether a tree is a BST
"""


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


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# ── BST Search ──────────────────────────────────────────────────

def bst_search(root, target):
    """O(h) — follow left/right based on comparison."""
    if not root:
        return None
    if target == root.val:
        return root
    elif target < root.val:
        return bst_search(root.left, target)
    else:
        return bst_search(root.right, target)


# ── BST Insert ──────────────────────────────────────────────────

def bst_insert(root, val):
    """O(h) — find the right spot and add a new leaf."""
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = bst_insert(root.left, val)
    elif val > root.val:
        root.right = bst_insert(root.right, val)
    # If val == root.val, we skip (no duplicates)
    return root


# ── BST Delete ──────────────────────────────────────────────────

def bst_delete(root, val):
    """O(h) — three cases: leaf, one child, two children."""
    if not root:
        return None
    if val < root.val:
        root.left = bst_delete(root.left, val)
    elif val > root.val:
        root.right = bst_delete(root.right, val)
    else:
        # Found the node to delete
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Two children: replace with inorder successor (smallest in right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = bst_delete(root.right, successor.val)
    return root


# ── BST Validation ──────────────────────────────────────────────

def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    """O(n) — every node must be within (lo, hi) range."""
    if not root:
        return True
    if root.val <= lo or root.val >= hi:
        return False
    return (is_valid_bst(root.left, lo, root.val) and
            is_valid_bst(root.right, root.val, hi))


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("BST OPERATIONS: Search, Insert, Delete, Validate")
    print("=" * 60)

    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    bst = build_tree([4, 2, 6, 1, 3, 5, 7])
    print(f"\n  BST inorder: {inorder(bst)}")  # [1,2,3,4,5,6,7]

    # Search
    found = bst_search(bst, 5)
    print(f"  Search 5: {'Found' if found else 'Not found'}")  # Found
    found = bst_search(bst, 8)
    print(f"  Search 8: {'Found' if found else 'Not found'}")  # Not found

    # Insert
    bst = bst_insert(bst, 8)
    print(f"  After inserting 8: {inorder(bst)}")  # [1,2,3,4,5,6,7,8]

    # Delete
    bst = bst_delete(bst, 4)
    print(f"  After deleting 4: {inorder(bst)}")   # [1,2,3,5,6,7,8]

    # Validate
    print(f"\n  Is valid BST: {is_valid_bst(bst)}")  # True

    # A non-BST example:
    #       5
    #      / \
    #     1   4    <-- 4 is less than 5 but in right subtree
    #        / \       AND 3 < 5 and 6 > 5, but 3 < 4 violates BST
    #       3   6
    bad = build_tree([5, 1, 4, None, None, 3, 6])
    print(f"  Non-BST [5,1,4,None,None,3,6] valid? {is_valid_bst(bad)}")  # False

    print("\n  COMMON GOTCHA: Checking only parent-child is NOT enough!")
    print("  You must check the ENTIRE valid range (lo, hi) for each node.")
