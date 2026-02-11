"""
Warmup 2: First and Last Position
====================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given a sorted array of integers and a target value, find the first and
last position (0-indexed) of the target. Return [-1, -1] if not found.

INPUT FORMAT
------------
First line: space-separated integers (sorted array, may be empty).
Second line: a single integer (the target).

OUTPUT FORMAT
-------------
A list of two integers [first, last].

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6
- Array is sorted in non-decreasing order

EXAMPLES
--------
Input:
  5 7 7 8 8 10
  8
Output: [3, 4]

Input:
  5 7 7 8 8 10
  6
Output: [-1, -1]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], target: int) -> list[int]:
    """Return [first, last] indices of target in sorted array, or [-1, -1]."""
    pass  # TODO: Replace this with your solution

    # Find first occurrence
    lo, hi = 0, len(arr) - 1
    first = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            first = mid
            hi = mid - 1  # keep searching left
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    if first == -1:
        return [-1, -1]

    # Find last occurrence
    lo, hi = first, len(arr) - 1
    last = first
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == target:
            last = mid
            lo = mid + 1  # keep searching right
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return [first, last]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))
