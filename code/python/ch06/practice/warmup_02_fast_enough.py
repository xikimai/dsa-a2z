"""
Warmup 2: Is It Fast Enough?
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Given an input size n and a complexity string, determine whether an
algorithm with that complexity would finish in time — i.e., whether
the number of operations is strictly less than 10^8 (100 million).

Complexity strings and their operation counts:
  "1"       -> 1
  "log_n"   -> log2(n)
  "n"       -> n
  "n_log_n" -> n * log2(n)
  "n^2"     -> n * n
  "n^3"     -> n * n * n
  "2^n"     -> 2^n  (if n > 30, return False immediately)

INPUT FORMAT
------------
A single line with two values separated by a space: n (integer) and
complexity (string).

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 1 <= n <= 10^9
- complexity is one of the seven valid strings

EXAMPLES
--------
Input:  1000 n^2
Output: True

Input:  100000 n^2
Output: False

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""

import math


def solve(n: int, complexity: str) -> bool:
    """Return True if the algorithm finishes within 10^8 operations."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().split()
    n = int(parts[0])
    complexity = parts[1]
    print(solve(n, complexity))
