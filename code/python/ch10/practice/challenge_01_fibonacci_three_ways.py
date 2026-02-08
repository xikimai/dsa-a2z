"""
Challenge 1: Fibonacci Three Ways
==============================
Chapter 10: The Magic of Recursion — Functions That Call Themselves

PROBLEM
-------
Implement three different approaches to compute the nth Fibonacci number,
showing how solutions evolve from naive to optimal:

1. **solve_naive(n)**: Pure recursion, no memoization. O(2^n) time — very slow!
   Use direct recursion: F(n) = F(n-1) + F(n-2).

2. **solve_memo(n)**: Recursion + dictionary memoization. O(n) time, O(n) space.
   Same recursion, but cache results in a dict to avoid recomputation.

3. **solve_iter(n)**: Iterative with two variables. O(n) time, O(1) space.
   No recursion at all — track the last two values and iterate forward.

Also implement solve(n) which delegates to solve_iter (the best approach).

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
A single integer — the nth Fibonacci number.

CONSTRAINTS
-----------
- 0 <= n <= 50 (for solve_memo and solve_iter)
- 0 <= n <= 30 (for solve_naive — it's too slow for larger inputs!)

EXAMPLES
--------
Input:
  10
Output: 55

Input:
  0
Output: 0

Input:
  1
Output: 1

HINT
----
For solve_naive: base cases are F(0)=0 and F(1)=1, just recurse.
For solve_memo: create a dict inside the function, check before computing.
For solve_iter: start with a=0, b=1 and loop from 2 to n, updating both.

INSTRUCTIONS
------------
Replace the `pass` in each function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_naive(n: int) -> int:
    """Fibonacci using pure recursion (no memo). O(2^n) — very slow!"""
    pass  # TODO: Replace this with your solution


def solve_memo(n: int) -> int:
    """Fibonacci using recursion + memoization. O(n)."""
    pass  # TODO: Replace this with your solution


def solve_iter(n: int) -> int:
    """Fibonacci using iteration. O(n) time, O(1) space."""
    pass  # TODO: Replace this with your solution


def solve(n: int) -> int:
    """Default solver — uses the iterative approach."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
