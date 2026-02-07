"""
Practice 3: Modular Exponentiation
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given three integers base, exp, and mod, compute (base^exp) % mod
using binary exponentiation (also known as fast exponentiation).

Do NOT use Python's built-in pow(base, exp, mod) — implement the
algorithm yourself to learn it!

Binary exponentiation works by squaring the base and halving the
exponent at each step. If the exponent is odd, multiply the result
by the current base.

INPUT FORMAT
------------
Three space-separated integers: base, exp, mod.

OUTPUT FORMAT
-------------
A single integer: (base^exp) % mod.

CONSTRAINTS
-----------
- 1 <= base <= 10^9
- 0 <= exp <= 10^18
- 2 <= mod <= 10^9

EXAMPLES
--------
Input:
  2 10 1000000007
Output: 1024

Input:
  2 20 1000000007
Output: 1048576

Input:
  123456789 0 1000000007
Output: 1

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(base: int, exp: int, mod: int) -> int:
    """Return base^exp mod m using binary exponentiation."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    base, exp, mod = map(int, input().split())
    print(solve(base, exp, mod))
