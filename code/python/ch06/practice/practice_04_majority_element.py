"""
Practice 4: Majority Element
==============================
Chapter 6: How Fast Is Your Code?

PROBLEM
-------
Find the element that appears more than n/2 times in the list.
The majority element is guaranteed to exist.

Use the Boyer-Moore Voting Algorithm for O(n) time and O(1) space.

The idea: maintain a candidate and a count.  Walk through the array:
  - If count is 0, pick the current element as the new candidate.
  - If current element equals candidate, increment count.
  - Otherwise, decrement count.
The surviving candidate is the majority element.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer: the majority element.

CONSTRAINTS
-----------
- 1 <= len(nums) <= 10^5
- The majority element always exists

EXAMPLES
--------
Input:  3 2 3
Output: 3

Input:  2 2 1 1 1 2 2
Output: 2

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nums: list[int]) -> int:
    """Return the majority element using Boyer-Moore Voting."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(solve(nums))
