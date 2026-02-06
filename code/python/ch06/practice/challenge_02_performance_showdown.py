"""
Challenge 2: Performance Showdown
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Given two complexity strings and an integer n, compute how many
operations each algorithm would perform and decide which is faster.

Complexity strings and their operation counts:
  "1"       -> 1
  "log_n"   -> log2(n)  (use 0 if n <= 0)
  "n"       -> n
  "n_log_n" -> n * log2(n)  (use 0 if n <= 0)
  "n^2"     -> n * n
  "n^3"     -> n * n * n
  "2^n"     -> 2^n  (cap n at 60 to avoid overflow)

Return "A" if algorithm A is faster (fewer ops), "B" if B is faster,
or "TIE" if they perform the same number of operations.

INPUT FORMAT
------------
A single line with three values: complexity_a complexity_b n

OUTPUT FORMAT
-------------
A, B, or TIE

CONSTRAINTS
-----------
- 1 <= n <= 10^9
- Complexities are valid strings from the list above

EXAMPLES
--------
Input:  n^2 n_log_n 1000
Output: B

Input:  n n 100
Output: TIE

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""

import math


def solve(complexity_a: str, complexity_b: str, n: int) -> str:
    """Return 'A', 'B', or 'TIE' based on which complexity is faster at n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().split()
    complexity_a = parts[0]
    complexity_b = parts[1]
    n = int(parts[2])
    print(solve(complexity_a, complexity_b, n))
