"""
Solution for Practice 2: N-Queens Count
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Place queens row by row. Track used columns and diagonals with sets.
row-col identifies one diagonal direction, row+col the other.

TIME COMPLEXITY:  O(n!) — bounded by permutation-like branching
SPACE COMPLEXITY: O(n) — sets + recursion depth
"""


def solve(n: int) -> int:
    """Return the number of valid N-Queens placements."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))

