"""
Warmup 4: Check if i-th Bit Is Set
====================================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given an integer n and a bit position i (0-indexed from the right),
determine whether the i-th bit of n is set (1) or not (0).

INPUT FORMAT
------------
Two space-separated integers: n and i.

OUTPUT FORMAT
-------------
True if the i-th bit is set, False otherwise.

CONSTRAINTS
-----------
- 0 <= n <= 10^9
- 0 <= i <= 30

EXAMPLES
--------
Input:
  42 1
Output: True

Input:
  42 2
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int, i: int) -> bool:
    """Return True if the i-th bit of n is set."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, i = int(parts[0]), int(parts[1])
    print(solve(n, i))

