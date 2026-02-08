"""
Warmup 1: Traverse Linked List
================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers, build a singly linked list from the array,
then traverse the list and return the values as an array.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
A list of the same integers in the same order.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 3
Output: [1, 2, 3]

Input:
  (empty)
Output: []

HINT
----
Create a ListNode class with val and next fields. Use a dummy head
node to simplify building the list, then walk from head collecting values.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> list[int]:
    """Build a linked list from arr, traverse and return values as list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
