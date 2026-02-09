"""
Challenge 4: Smallest String With Swaps
=======================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the lexicographically smallest string achievable by swapping.

EXAMPLES
--------
  solve("dcab", [[0, 3], [1, 2]]) -> "bacd"
  solve("dcab", [[0, 3], [1, 2], [0, 2]]) -> "abcd"
  solve("cba", [[0, 1], [1, 2]]) -> "abc"

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Use Union-Find to group indices that are connected via swap pairs. Within each group, sort the characters and place them back in sorted index order.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""

from collections import defaultdict


def solve(s: str, pairs: list[list[int]]) -> str:
    """Return the lexicographically smallest string achievable by swapping."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split("\n")
    s = data[0]
    pairs = []
    for line in data[1:]:
        a, b = map(int, line.split())
        pairs.append([a, b])
    print(solve(s, pairs))
