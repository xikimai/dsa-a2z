"""
Warmup 1: Kth Largest Element
================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given an unsorted array of integers and an integer k, return the kth largest
element in the array.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: integer k

OUTPUT FORMAT
-------------
A single integer — the kth largest element.

CONSTRAINTS
-----------
- 1 <= k <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

EXAMPLES
--------
Input:
  3 2 1 5 6 4
  2
Output: 5

Input:
  3 2 3 1 2 4 5 5 6
  4
Output: 4

HINT
----
Use a min-heap of size k. For each element, push it onto the heap.
If the heap size exceeds k, pop the smallest. The top of the heap
is the kth largest.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int], k: int) -> int:
    """Return the kth largest element in nums."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    k = int(input().strip())
    print(solve(nums, k))
