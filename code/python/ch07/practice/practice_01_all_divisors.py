"""
Practice 1: All Divisors (Sorted)
==============================
Chapter 7: Number Wizardry — Math for Programmers

PROBLEM
-------
Given a positive integer n, return a sorted list of ALL divisors of n.
Your solution should run in O(sqrt(n)) time, not O(n).

Hint: If i divides n, then both i and n//i are divisors. Be careful
not to add the same divisor twice when n is a perfect square.

INPUT FORMAT
------------
A single positive integer n.

OUTPUT FORMAT
-------------
A single line of space-separated integers: all divisors of n in
ascending order.

CONSTRAINTS
-----------
- 1 <= n <= 10^9

EXAMPLES
--------
Input:
  36
Output: 1 2 3 4 6 9 12 18 36

Input:
  7
Output: 1 7

Input:
  12
Output: 1 2 3 4 6 12

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[int]:
    """Return a sorted list of all divisors of n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    print(" ".join(map(str, result)))
