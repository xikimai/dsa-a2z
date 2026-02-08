"""
Practice 1: Fibonacci
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Return the nth Fibonacci number using recursion.
The Fibonacci sequence is defined as:
  F(0) = 0
  F(1) = 1
  F(n) = F(n-1) + F(n-2) for n >= 2

Plain recursion is O(2^n) which is very slow for large n.
Use memoization (a dictionary to cache results) to bring it down to O(n).

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer — the nth Fibonacci number.

CONSTRAINTS
-----------
- 0 <= n <= 50

EXAMPLES
--------
Input:
  0
Output: 0

Input:
  1
Output: 1

Input:
  10
Output: 55

HINT
----
Create a memo dictionary inside solve(). Write a helper function
fib(k) that checks the memo before computing, stores results in
the memo after computing, and uses F(0)=0, F(1)=1 as base cases.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> int:
    """Return the nth Fibonacci number using memoized recursion."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
