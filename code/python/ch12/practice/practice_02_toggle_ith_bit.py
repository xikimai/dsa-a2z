"""
Practice 2: Toggle i-th Bit
=============================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given an integer n and a bit position i (0-indexed from the right),
toggle the i-th bit of n (flip it from 0 to 1 or from 1 to 0) and
return the result.

INPUT FORMAT
------------
Two space-separated integers: n and i.

OUTPUT FORMAT
-------------
A single integer — the result after toggling the i-th bit.

CONSTRAINTS
-----------
- 0 <= n <= 10^9
- 0 <= i <= 30

EXAMPLES
--------
Input:
  42 0
Output: 43

Input:
  42 1
Output: 40

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, i: int) -> int:
    """Return n with the i-th bit toggled."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, i = int(parts[0]), int(parts[1])
    print(solve(n, i))

