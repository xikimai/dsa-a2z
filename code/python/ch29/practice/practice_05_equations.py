"""
Practice 5: Satisfiability of Equality Equations
================================================
Chapter 29: Union-Find & Minimum Spanning Trees

PROBLEM
-------
Return True if all equations can be satisfied simultaneously.

CONSTRAINTS
-----------
- See test cases for input constraints

HINT
----
First pass: process all "==" equations and union the variables. Second pass: process all "!=" equations and check if they conflict.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(equations: list[str]) -> bool:
    """Return True if all equations can be satisfied simultaneously."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    print(solve(data))
