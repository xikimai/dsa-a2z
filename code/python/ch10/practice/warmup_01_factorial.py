"""
Warmup 1: Factorial
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Compute n! (n factorial) using recursion.

n! is defined as:
  0! = 1
  n! = n * (n-1)! for n > 0

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer — the value of n!.

CONSTRAINTS
-----------
- 0 <= n <= 20

EXAMPLES
--------
Input:
  5
Output: 120

Input:
  0
Output: 1

Input:
  1
Output: 1

HINT
----
The base case is n == 0 (returns 1). For the recursive case,
multiply n by the factorial of n - 1.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Compute n! recursively."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
