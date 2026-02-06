"""
Challenge 3: Rotate Array
==============================
Chapter 5: Collections

PROBLEM
-------
Given a list of integers and a non-negative integer k, rotate the list
to the right by k steps.

For example, [1,2,3,4,5,6,7] rotated by k=3 becomes [5,6,7,1,2,3,4].

Handle cases where k is larger than the length of the list.

INPUT FORMAT
------------
First line: space-separated integers (the list).
Second line: a single integer k.

OUTPUT FORMAT
-------------
The rotated list as space-separated integers.

CONSTRAINTS
-----------
- The list can be empty or have one element
- 0 <= k <= 10^5
- k can be larger than len(nums)

EXAMPLES
--------
Input:
1 2 3 4 5 6 7
3
Output: 5 6 7 1 2 3 4

Input:
1 2
3
Output: 2 1

Input:
-1 -100 3 99
2
Output: 3 99 -1 -100

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int], k: int) -> list[int]:
    """Rotate the list to the right by k steps and return it."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    result = solve(nums, k)
    print(" ".join(map(str, result)))
