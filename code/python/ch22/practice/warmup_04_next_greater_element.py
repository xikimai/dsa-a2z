"""
Warmup 4: Next Greater Element
==================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given an array of integers, for each element find the next greater element
to its right. If no greater element exists, use -1.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input: 4 5 2 10 8
Output: [5, 10, 10, -1, -1]

HINT
----
Use a monotonic stack: process from right to left, maintaining a decreasing stack.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(arr: list[int]) -> list[int]:
    """Return list of next greater elements for each position."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
