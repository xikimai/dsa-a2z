"""
Warmup 3: Running Sum of Array
================================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array of integers, return a new array where each element is
the running sum (cumulative sum) up to that index. The output has the
same length as the input.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
The running sum array as a list.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  1 2 3 4
Output: [1, 3, 6, 10]

Input:
  3 -1 2 -4 5
Output: [3, 2, 4, 0, 5]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[int]:
    """Return the running sum array (same length as input)."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))

