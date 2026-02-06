"""
Warmup 05: Sum 1 to N
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given a non-negative integer n, return the sum 1 + 2 + ... + n using a
loop. Do NOT use the formula n*(n+1)/2 — the point is to practice loops!

INPUT FORMAT
------------
A single line containing a non-negative integer n.

OUTPUT FORMAT
-------------
Print the sum of all integers from 1 to n.

CONSTRAINTS
-----------
0 <= n <= 10^6

EXAMPLES
--------
Input:  5
Output: 15

Input:  1
Output: 1

Input:  10
Output: 55

Input:  0
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the sum 1 + 2 + ... + n using a loop."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
