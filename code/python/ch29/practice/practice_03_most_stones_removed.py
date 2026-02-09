"""
Practice 3: Most Stones Removed
===============================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return the maximum number of stones that can be removed.

EXAMPLES
--------
  solve([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) -> 5
  solve([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) -> 3
  solve([[0, 0]]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Two stones are connected if they share a row or column. Use Union-Find to group stones by connectivity. The answer is total_stones - number_of_components

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(stones: list[list[int]]) -> int:
    """Return the maximum number of stones that can be removed."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    stones = []
    for _ in range(n):
        r = int(tokens[idx]); idx += 1
        c = int(tokens[idx]); idx += 1
        stones.append([r, c])
    print(solve(stones))
