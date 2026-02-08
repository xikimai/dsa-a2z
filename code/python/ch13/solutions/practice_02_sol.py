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
    count = 0
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
