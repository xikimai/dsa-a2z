"""
Practice 4: Find Median from Data Stream
============================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Design a data structure that supports:
  - add_num(num): adds an integer from the stream
  - find_median(): returns the median of all added numbers

The function `solve` receives a list of numbers and returns a list of medians
after adding each number. For even counts, the median is the average of
the two middle values.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A list of floats — the median after each insertion.

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^5
- -10^5 <= nums[i] <= 10^5

EXAMPLES
--------
Input:
  5 15 1 3
Output: [5.0, 10.0, 5.0, 4.0]

Input:
  2 3 4
Output: [2.0, 2.5, 3.0]

HINT
----
Use two heaps: a max-heap for the lower half and a min-heap for the
upper half. Balance them so they differ in size by at most 1.
The median is at the top of one or both heaps.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> list[float]:
    """Return a list of medians after adding each number."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
