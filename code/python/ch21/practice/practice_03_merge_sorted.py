"""
Practice 3: Merge Two Sorted Lists
====================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given two sorted arrays of integers, build two sorted linked lists,
merge them into one sorted linked list, and return the result as an array.

INPUT FORMAT
------------
Line 1: space-separated integers (first sorted array, may be empty)
Line 2: space-separated integers (second sorted array, may be empty)

OUTPUT FORMAT
-------------
A sorted list of all integers from both lists.

CONSTRAINTS
-----------
- 0 <= len(arr1), len(arr2) <= 10^4
- -10^9 <= arr1[i], arr2[i] <= 10^9
- Both arrays are sorted in non-decreasing order

EXAMPLES
--------
Input:
  1 2 4
  1 3 4
Output: [1, 1, 2, 3, 4, 4]

Input:
  (empty)
  0
Output: [0]

HINT
----
Use a dummy node to simplify the merge. Compare the heads of both lists,
append the smaller one, and advance that pointer. When one list is done,
append the remaining nodes from the other.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    """Merge two sorted linked lists and return the result as a list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    arr1 = list(map(int, line1.split())) if line1 else []
    line2 = input().strip()
    arr2 = list(map(int, line2.split())) if line2 else []
    print(solve(arr1, arr2))
