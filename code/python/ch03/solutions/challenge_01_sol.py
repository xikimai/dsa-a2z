"""
Solution for Challenge 01: Diamond Pattern
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
The diamond has 2n-1 rows. The top half (rows 1 to n) has increasing
stars (1, 3, 5, ..., 2n-1) and decreasing leading spaces (n-1, n-2,
..., 0). The bottom half mirrors the top half (excluding the middle).

For row i (1-indexed from the middle = row n):
  - Stars in row i of top half: 2*i - 1
  - Spaces: n - i

TIME COMPLEXITY:  O(n^2) — building 2n-1 rows each up to 2n-1 characters
SPACE COMPLEXITY: O(n^2) — the output string
"""


def solve(n: int) -> str:
    """Return a diamond pattern of stars with n rows in the top half."""
    rows = []
    # Top half (including middle)
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        rows.append(spaces + stars)
    # Bottom half (mirror of top, excluding middle)
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        rows.append(spaces + stars)
    return "\n".join(rows)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
