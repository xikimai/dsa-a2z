"""
Challenge 2: Serialize and Deserialize Binary Tree
====================================================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Implement two functions: serialize() encodes a tree to a single string,
and deserialize() decodes a string back to a tree. The round-trip must
reproduce the original tree structure.

EXAMPLES
--------
  tree = build_tree([1, 2, 3, None, None, 4, 5])
  tree_to_list(deserialize(serialize(tree))) -> [1, 2, 3, None, None, 4, 5]
  deserialize(serialize(None)) -> None

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
BFS serialization: level-order with "N" for null nodes. Deserialization: reverse BFS to rebuild the tree.

INSTRUCTIONS
------------
Replace the `pass` in the serialize() and deserialize() functions with your solution.
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


def serialize(root):
    """Encode a tree to a single string."""
    pass  # TODO: Replace this with your solution


def deserialize(data):
    """Decode a string back to a tree."""
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([1, 2, 3, None, None, 4, 5])
    s = serialize(tree)
    print(f"Serialized: {s}")
    restored = deserialize(s)
    print(f"Restored: {tree_to_list(restored)}")
