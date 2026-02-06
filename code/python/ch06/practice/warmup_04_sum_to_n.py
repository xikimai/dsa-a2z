"""
Warmup 4: Sum of 1 to N
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Compute the sum 1 + 2 + ... + n using three different methods and
return all three results in a list.

Method 1 — O(n) loop:
  Add numbers one at a time from 1 to n.

Method 2 — O(1) formula:
  Use the formula n * (n + 1) // 2.

Method 3 — O(n^2) nested loop:
  For each i from 1 to n, add 1 exactly i times using an inner loop.

All three methods should give the same answer!

INPUT FORMAT
------------
A single integer n.

OUTPUT FORMAT
-------------
Three space-separated integers: loop_result formula_result nested_result

CONSTRAINTS
-----------
- 0 <= n <= 1000

EXAMPLES
--------
Input:  10
Output: 55 55 55

Input:  0
Output: 0 0 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(n: int) -> list[int]:
    """Return [loop_result, formula_result, nested_result]."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    result = solve(n)
    print(" ".join(map(str, result)))
