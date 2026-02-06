"""
Challenge 03: Collatz Sequence
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given a positive integer n, return the Collatz sequence starting from n.
The rules are:
  - If the current number is even, divide it by 2.
  - If the current number is odd, multiply by 3 and add 1.
  - Continue until you reach 1 (include 1 in the sequence).

Nobody has proven that this always reaches 1, but it has been verified
for all numbers up to about 2^68. It's one of the great unsolved
problems in math!

INPUT FORMAT
------------
A single line containing a positive integer n.

OUTPUT FORMAT
-------------
Print the Collatz sequence as a list.

CONSTRAINTS
-----------
1 <= n <= 10^6

EXAMPLES
--------
Input:  6
Output: [6, 3, 10, 5, 16, 8, 4, 2, 1]

Input:  1
Output: [1]

Input:  2
Output: [2, 1]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[int]:
    """Return the Collatz sequence starting from n until reaching 1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    print(solve(n))
