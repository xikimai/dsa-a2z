"""
Challenge 3: Minimum Bit Flips
================================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Given two non-negative integers start and goal, return the minimum number
of bit flips needed to convert start to goal.

INPUT FORMAT
------------
Two space-separated non-negative integers: start and goal.

OUTPUT FORMAT
-------------
A single integer — the number of bits that differ.

CONSTRAINTS
-----------
- 0 <= start, goal <= 10^9

EXAMPLES
--------
Input:
  10 7
Output: 3

Input:
  3 4
Output: 3

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(start: int, goal: int) -> int:
    """Return minimum bit flips to convert start to goal."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    start, goal = int(parts[0]), int(parts[1])
    print(solve(start, goal))

