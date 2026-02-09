"""
Warmup 4: Count Inversions (BIT)
================================
Chapter 30: Segment Trees & Range Queries

PROBLEM
-------
Return the number of inversions in the array.

EXAMPLES
--------
  solve([2, 3, 8, 6, 1]) -> 5
  solve([5, 4, 3, 2, 1]) -> 10
  solve([1, 2, 3, 4, 5]) -> 0

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
Coordinate compress values, then process array right-to-left. For each element, count how many already-inserted elements have

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int]) -> int:
    """Return the number of inversions in the array."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    arr = [int(tokens[i + 1]) for i in range(n)]
    print(solve(arr))
