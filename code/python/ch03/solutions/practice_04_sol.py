"""
Solution for Practice 04: Right Triangle
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
For row i (1 to n), print (n - i) spaces followed by i stars. Join all
rows with newlines. The string multiplication operator (*) makes this
clean: " " * spaces + "*" * stars.

TIME COMPLEXITY:  O(n^2) — building n rows each up to n characters
SPACE COMPLEXITY: O(n^2) — the output string
"""


def solve(n: int) -> str:
    """Return a right-aligned triangle of stars with n rows."""
    rows = []
    for i in range(1, n + 1):
        rows.append(" " * (n - i) + "*" * i)
    return "\n".join(rows)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
