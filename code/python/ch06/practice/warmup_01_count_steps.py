"""
Warmup 1: Count the Steps
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Given a code_id string and an integer n, return the exact number of
operations that the corresponding code pattern would perform.

The code patterns are:
  "single_loop"    -> n              (one loop from 1 to n)
  "double_loop"    -> n * n          (two nested loops, each 1 to n)
  "half_loop"      -> n // 2         (loop that skips every other)
  "dependent_loop" -> n*(n+1) // 2   (inner loop depends on outer)
  "log_loop"       -> floor(log2(n)) (halving loop), 0 if n < 1

INPUT FORMAT
------------
Two lines:
  Line 1: a code_id string (one of the five above)
  Line 2: an integer n

OUTPUT FORMAT
-------------
A single integer: the operation count.

CONSTRAINTS
-----------
- 0 <= n <= 10^9
- code_id is always one of the five valid strings

EXAMPLES
--------
Input:
  single_loop
  100
Output: 100

Input:
  log_loop
  16
Output: 4

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""

import math


def solve(code_id: str, n: int) -> int:
    """Return the exact operation count for the given code pattern and n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    code_id = input().strip()
    n = int(input().strip())
    print(solve(code_id, n))
