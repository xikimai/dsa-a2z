"""
Challenge 2: Count Inversions
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Count the number of inversions in an array. An inversion is a pair of
indices (i, j) where i < j but arr[i] > arr[j].

For example, in [2, 4, 1, 3, 5]:
  - (2,1): index 0 vs index 2, 2 > 1 → inversion
  - (4,1): index 1 vs index 2, 4 > 1 → inversion
  - (4,3): index 1 vs index 3, 4 > 3 → inversion
  Total: 3 inversions

Use a modified merge sort to count inversions in O(n log n) time.
The brute force O(n^2) approach is too slow for large inputs!

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer: the number of inversions.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  2 4 1 3 5
Output: 3

Input:
  1 2 3 4 5
Output: 0

Input:
  5 4 3 2 1
Output: 10

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> int:
    """Count the number of inversions using modified merge sort."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(solve(data))
