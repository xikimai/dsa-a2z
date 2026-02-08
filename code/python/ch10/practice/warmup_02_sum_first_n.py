"""
Warmup 2: Sum of First N
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Compute the sum 1 + 2 + ... + n using recursion.

If n is 0, the sum is 0.

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer — the sum 1 + 2 + ... + n.

CONSTRAINTS
-----------
- 0 <= n <= 10000

EXAMPLES
--------
Input:
  5
Output: 15

Input:
  0
Output: 0

Input:
  1
Output: 1

HINT
----
Base case: when n == 0, return 0. Otherwise, return n + solve(n - 1).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Compute 1 + 2 + ... + n recursively."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
