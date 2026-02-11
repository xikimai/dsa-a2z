"""
Warmup 4: Peak Element in Array
==================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given an array of integers, find any peak element and return its index.
A peak element is strictly greater than its neighbors. For boundary
elements, only the one existing neighbor matters.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
A single integer — the index of any peak element.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- arr[i] != arr[i+1] for all valid i (no adjacent duplicates)

EXAMPLES
--------
Input:
  1 2 3 1
Output: 2

Input:
  1 2 1 3 5 6 4
Output: 1 (or 5, any valid peak index)

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Return index of any peak element (greater than its neighbors)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
