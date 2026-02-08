"""
Challenge 2: Trapping Rain Water
====================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.

CONSTRAINTS
-----------
- 0 <= len(height) <= 2 * 10^4
- 0 <= height[i] <= 10^5

EXAMPLES
--------
Input: 0 1 0 2 1 0 1 3 2 1 2 1
Output: 6

Input: 4 2 0 3 2 5
Output: 9

HINT
----
Two-pointer approach: maintain left_max and right_max, process from
the side with the smaller max.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(height: list[int]) -> int:
    """Return total trapped water."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        height = list(map(int, line.split()))
    else:
        height = []
    print(solve(height))
