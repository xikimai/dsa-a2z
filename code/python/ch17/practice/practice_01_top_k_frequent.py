"""
Practice 1: Top K Frequent Elements
=======================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an integer array and an integer k, return the k most frequent elements.
Return them sorted in ascending order.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: integer k

OUTPUT FORMAT
-------------
A sorted list of the k most frequent elements.

CONSTRAINTS
-----------
- 1 <= k <= number of unique elements <= 10^5
- 1 <= len(nums) <= 10^5

EXAMPLES
--------
Input:
  1 1 1 2 2 3
  2
Output: [1, 2]

Input:
  1
  1
Output: [1]

HINT
----
Build a frequency map, then use a min-heap of size k to track
the k elements with highest frequency.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent elements, sorted ascending."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
