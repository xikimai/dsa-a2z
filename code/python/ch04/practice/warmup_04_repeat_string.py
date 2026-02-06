"""
Warmup 4: Repeat String
==============================
Chapter 4: Functions

PROBLEM
-------
Return a string repeated n times, separated by spaces.
If n is 0, return an empty string.

INPUT FORMAT
------------
A string on the first line, then an integer n on the second line.

OUTPUT FORMAT
-------------
The string repeated n times with spaces between them.

CONSTRAINTS
-----------
- n >= 0
- s can be any string

EXAMPLES
--------
Input:  ha, 3
Output: ha ha ha

Input:  yo, 5
Output: yo yo yo yo yo

Input:  x, 0
Output: (empty string)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str, n: int = 3) -> str:
    """Return s repeated n times separated by spaces."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    n = int(input())
    print(solve(s, n))
