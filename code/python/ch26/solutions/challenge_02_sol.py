"""
Solution for Challenge 2: Serialize and Deserialize Binary Tree
================================================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
BFS serialization: level-order with "N" for null nodes.
Deserialization: reverse BFS to rebuild the tree.

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


def serialize(root):
    """Encode a tree to a single string."""
    if not root:
        return ""
    tokens = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            tokens.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            tokens.append("N")
    return ",".join(tokens)


def deserialize(data):
    """Decode a string back to a tree."""
    if not data:
        return None
    tokens = data.split(",")
    root = TreeNode(int(tokens[0]))
    q = deque([root])
    i = 1
    while q and i < len(tokens):
        node = q.popleft()
        if tokens[i] != "N":
            node.left = TreeNode(int(tokens[i]))
            q.append(node.left)
        i += 1
        if i < len(tokens) and tokens[i] != "N":
            node.right = TreeNode(int(tokens[i]))
            q.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    tree = build_tree([1, 2, 3, None, None, 4, 5])
    s = serialize(tree)
    print(f"Serialized: {s}")
    restored = deserialize(s)
    print(f"Restored: {tree_to_list(restored)}")
