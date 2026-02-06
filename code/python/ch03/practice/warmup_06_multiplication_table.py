"""
Warmup 06: Multiplication Table
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given an integer n, return its multiplication table as a list of strings
in the format "i x n = result" for i from 1 to 10.

INPUT FORMAT
------------
A single line containing an integer n.

OUTPUT FORMAT
-------------
Print 10 lines, each showing "i x n = result".

CONSTRAINTS
-----------
1 <= n <= 100

EXAMPLES
--------
Input:  7
Output:
1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
4 x 7 = 28
5 x 7 = 35
6 x 7 = 42
7 x 7 = 49
8 x 7 = 56
9 x 7 = 63
10 x 7 = 70

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[str]:
    """Return n's multiplication table as a list of strings."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    for line in solve(n):
        print(line)
