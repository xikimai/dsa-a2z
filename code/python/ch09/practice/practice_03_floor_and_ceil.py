"""
Practice 3: Floor and Ceil
==============================
Chapter 9: Finding Needles — The Power of Searching

PROBLEM
-------
Given a sorted array of integers and a target value, find:
- Floor: the largest element in the array that is <= target.
- Ceil: the smallest element in the array that is >= target.
Return [floor, ceil]. If the floor does not exist, use -1.
If the ceil does not exist, use -1.

INPUT FORMAT
------------
First line: space-separated integers (a sorted array).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
Two space-separated integers: floor and ceil.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9
- The array is sorted in non-decreasing order.

EXAMPLES
--------
Input:
  1 3 5 7 9
  4
Output: 3 5

Input:
  1 3 5 7 9
  5
Output: 5 5

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> list[int]:
    """Return [floor, ceil] for target in sorted array."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    target = int(input())
    result = solve(data, target)
    print(result[0], result[1])
