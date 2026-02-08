"""
Challenge 4: House Robber III (Binary Tree)
============================================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
Houses are arranged in a binary tree. You cannot rob two directly-linked houses.
Given the tree as a level-order array (-1 means null node), return the
maximum amount of money you can rob.

EXAMPLES
--------
  tree=[3,2,3,-1,3,-1,1] -> 7  (rob 3+3+1)
  tree=[3,4,5,1,3,-1,1] -> 9  (rob 4+5)
  tree=[1] -> 1

CONSTRAINTS
-----------
- 0 <= len(tree) <= 10^4
- -1 represents a null node
- 0 <= tree[i] <= 10^4 (for non-null nodes)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(tree: list[int]) -> int:
    """Return maximum money from tree-shaped houses without robbing adjacent."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tree = list(map(int, input().split()))
    print(solve(tree))
