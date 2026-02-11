"""
Practice 3: Set and Clear Bits
================================
Chapter 12: Bit Manipulation — The Language of Computers

PROBLEM
-------
Implement two operations on an integer n at bit position i (0-indexed):
  - SET: Force the i-th bit to 1 and return the result.
  - CLEAR: Force the i-th bit to 0 and return the result.

INPUT FORMAT
------------
A line with an operation ("set" or "clear"), followed by two integers n and i.

OUTPUT FORMAT
-------------
A single integer — the result after the operation.

CONSTRAINTS
-----------
- 0 <= n <= 10^9
- 0 <= i <= 30

EXAMPLES
--------
Input:
  set 42 0
Output: 43

Input:
  clear 42 1
Output: 40

INSTRUCTIONS
------------
Replace the `pass` in solve_set() and solve_clear() with your solutions.
The main block at the bottom handles input/output — don't change it.
"""


def solve_set(n: int, i: int) -> int:
    """Return n with the i-th bit set to 1."""
    pass  # TODO: Replace this with your solution


def solve_clear(n: int, i: int) -> int:
    """Return n with the i-th bit cleared to 0."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    op = parts[0]
    n, i = int(parts[1]), int(parts[2])
    if op == "set":
        print(solve_set(n, i))
    else:
        print(solve_clear(n, i))

