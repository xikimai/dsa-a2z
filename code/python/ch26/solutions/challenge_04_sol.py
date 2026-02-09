"""
Solution for Challenge 4: Binary Tree Cameras
===============================================
Chapter 26: Trees — Branches of Logic

APPROACH
--------
Greedy DFS from leaves up. Three states per node:
  0 = NOT covered (needs camera from parent)
  1 = HAS camera
  2 = covered (by child's camera)

If a child is NOT covered, parent MUST have a camera.
If a child HAS camera, parent is covered.
After DFS, if root is NOT covered, add one more camera.

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


def solve(root):
    """Return the minimum number of cameras to monitor all nodes."""
    if not root:
        return 0

    cameras = [0]
    NOT_COVERED = 0
    HAS_CAMERA = 1
    COVERED = 2

    def dfs(node):
        if not node:
            return COVERED  # null nodes are considered covered
        left = dfs(node.left)
        right = dfs(node.right)
        if left == NOT_COVERED or right == NOT_COVERED:
            cameras[0] += 1
            return HAS_CAMERA
        if left == HAS_CAMERA or right == HAS_CAMERA:
            return COVERED
        return NOT_COVERED

    if dfs(root) == NOT_COVERED:
        cameras[0] += 1
    return cameras[0]


if __name__ == "__main__":
    tree = build_tree([0, 0, None, 0, 0])
    print(solve(tree))
