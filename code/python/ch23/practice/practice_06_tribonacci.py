"""
Practice 6: Tribonacci Number
==============================
Chapter 23: Dynamic Programming I — The Foundation

PROBLEM
-------
The Tribonacci sequence: T(0)=0, T(1)=1, T(2)=1,
and T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3.
Given n, return T(n).

EXAMPLES
--------
  n=0 -> 0
  n=1 -> 1
  n=2 -> 1
  n=4 -> 4
  n=25 -> 1389537

CONSTRAINTS
-----------
- 0 <= n <= 37

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(n: int) -> int:
    """Return the nth Tribonacci number."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
