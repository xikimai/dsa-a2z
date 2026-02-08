"""
Solution for Challenge 3: N-Queens All Solutions
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Extend N-Queens count: when a complete placement is found, build
the board string representation and store it.

TIME COMPLEXITY:  O(n!)
SPACE COMPLEXITY: O(n^2) — storing solutions
"""


def solve(n: int) -> list[list[str]]:
    """Return all N-Queens solutions as lists of strings."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    result = solve(n)
    for solution in result:
        for row in solution:
            print(row)
        print()

