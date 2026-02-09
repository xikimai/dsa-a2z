"""
Challenge 4: Binary Tree Cameras
================================
Chapter 26: Trees — Branches of Logic

PROBLEM
-------
Return the minimum number of cameras to monitor all nodes.

EXAMPLES
--------
  solve(build_tree([0, 0, None, 0, 0])) -> 1
  solve(build_tree([0, 0, None, 0, None, 0, None, None, 0])) -> 2

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Greedy DFS from leaves up. Three states per node: 0 = NOT covered (needs camera from parent)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
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
    pass  # TODO: Replace this with your solution


if __name__ == "__main__":
    tree = build_tree([0, 0, None, 0, 0])
    print(solve(tree))
