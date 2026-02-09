"""
Challenge 1: Construct from Preorder + Inorder
==============================================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Build tree from preorder+inorder, return as level-order list.

EXAMPLES
--------
  solve([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) -> [3, 9, 20, None, None, 15, 7]
  solve([-1], [-1]) -> [-1]

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Preorder first element is root. Find it in inorder to split into left/right subtrees. Use a hash map for O(1) inorder lookups.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
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
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    print(solve([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
