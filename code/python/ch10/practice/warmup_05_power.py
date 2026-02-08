"""
Warmup 5: Power
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Compute base^exp (base raised to the power exp) using recursion.
Do not use the ** operator or pow() — build the result through
recursive multiplication.

INPUT FORMAT
------------
Two space-separated integers: base and exp.

OUTPUT FORMAT
-------------
A single integer — the value of base^exp.

CONSTRAINTS
-----------
- 0 <= base <= 100
- 0 <= exp <= 20

EXAMPLES
--------
Input:
  2 10
Output: 1024

Input:
  3 0
Output: 1

Input:
  5 3
Output: 125

HINT
----
Base case: anything^0 = 1. Recursive case: base * solve(base, exp - 1).
This runs in O(exp) time — one multiplication per step.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(base: int, exp: int) -> int:
    """Compute base^exp recursively in O(exp) time."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    b, e = map(int, input().split())
    print(solve(b, e))
