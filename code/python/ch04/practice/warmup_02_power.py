"""
Warmup 2: Power
==============================
Chapter 4: Functions

PROBLEM
-------
Compute base raised to the power of exponent using a loop.
Do NOT use the built-in pow() or the ** operator.

INPUT FORMAT
------------
Two integers on separate lines: base, then exponent.

OUTPUT FORMAT
-------------
A single integer: the result of base^exponent.

CONSTRAINTS
-----------
- exponent >= 0
- base can be any integer (including 0 and negatives)

EXAMPLES
--------
Input:  2, 10
Output: 1024

Input:  5, 0
Output: 1

Input:  0, 5
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(base: int, exponent: int) -> int:
    """Compute base^exponent using a loop (no built-in pow or **)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    base = int(input())
    exponent = int(input())
    print(solve(base, exponent))
