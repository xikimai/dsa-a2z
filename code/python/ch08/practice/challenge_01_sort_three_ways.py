"""
Challenge 1: Sort Three Ways
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

PROBLEM
-------
Implement sorting using three different algorithms:

1. **Bubble Sort** (solve_bubble): Compare adjacent elements and swap.
   Use early termination if no swaps happen in a pass.

2. **Merge Sort** (solve_merge): Divide-and-conquer. Split, sort halves,
   merge. Always O(n log n).

3. **Built-in Sort** (solve_builtin): Use Python's sorted() function.

Also implement solve(arr) which calls solve_merge(arr) as the default.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single line of space-separated integers in non-decreasing order.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^6 <= arr[i] <= 10^6

EXAMPLES
--------
Input:
  5 3 8 1 2
Output: 1 2 3 5 8

Input:
  10 9 8 7 6 5 4 3 2 1
Output: 1 2 3 4 5 6 7 8 9 10

INSTRUCTIONS
------------
Replace the `pass` in each function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve_bubble(arr: list[int]) -> list[int]:
    """Sort using bubble sort with early termination."""
    pass  # TODO: Replace this with your solution


def solve_merge(arr: list[int]) -> list[int]:
    """Sort using merge sort."""
    pass  # TODO: Replace this with your solution


def solve_builtin(arr: list[int]) -> list[int]:
    """Sort using Python's built-in sorted()."""
    pass  # TODO: Replace this with your solution


def solve(arr: list[int]) -> list[int]:
    """Default sort — uses merge sort."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    data = list(map(int, input().split()))
    print(*solve(data))
