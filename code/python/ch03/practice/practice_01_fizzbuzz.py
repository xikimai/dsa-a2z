"""
Practice 01: FizzBuzz
==============================
Chapter 3: Decisions and Loops

PROBLEM
-------
Given a positive integer n, return the FizzBuzz sequence from 1 to n.
For each number:
  - If divisible by both 3 and 5, use "FizzBuzz"
  - If divisible by 3 only, use "Fizz"
  - If divisible by 5 only, use "Buzz"
  - Otherwise, use the number as a string

INPUT FORMAT
------------
A single line containing a positive integer n.

OUTPUT FORMAT
-------------
Print each element of the FizzBuzz sequence on its own line.

CONSTRAINTS
-----------
1 <= n <= 1000

EXAMPLES
--------
Input:  5
Output:
1
2
Fizz
4
Buzz

Input:  15
Output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[str]:
    """Return the FizzBuzz sequence from 1 to n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    for item in solve(n):
        print(item)
