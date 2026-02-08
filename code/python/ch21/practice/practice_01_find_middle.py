"""
Practice 1: Find Middle Node
==============================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers, build a singly linked list from the array,
find the middle node, and return its value. For even-length lists,
return the second middle node's value.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A single integer — the value of the middle node.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^4
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 3 4 5
Output: 3

Input:
  1 2 3 4 5 6
Output: 4

HINT
----
Use the slow/fast pointer technique. Move slow one step and fast two
steps. When fast reaches the end, slow is at the middle.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> int:
    """Return the value of the middle node."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(solve(arr))
