"""
Warmup 5: Count Occurrences
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
Given a sorted array of integers and a target value, count how many
times the target appears in the array. Your solution should run in
O(log n) time, not O(n).

INPUT FORMAT
------------
First line: space-separated integers (a sorted array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A single integer: the number of times the target appears.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 2 2 2 3 4
  2
Output: 3

Input:
  1 3 5 7
  4
Output: 0

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> int:
    """Count occurrences of target in sorted array in O(log n)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    print(solve(data, target))
