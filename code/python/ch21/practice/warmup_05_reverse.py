"""
Warmup 5: Reverse a Linked List
=================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers, build a singly linked list from the array,
reverse the linked list, and return the values as an array.

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
A list of integers in reversed order.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 3 4 5
Output: [5, 4, 3, 2, 1]

Input:
  (empty)
Output: []

HINT
----
Use the 3-pointer approach: prev, current, next_node. At each step,
save current.next, point current.next to prev, advance prev and current.
When current is None, prev is the new head.

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
    """Reverse the linked list built from arr, return as list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
