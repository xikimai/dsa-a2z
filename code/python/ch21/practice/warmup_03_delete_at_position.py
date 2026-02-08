"""
Warmup 3: Delete Node at Position
===================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers and a position, build a singly linked list
from the array, delete the node at the given position, and return the
resulting list as an array.

INPUT FORMAT
------------
Line 1: space-separated integers (the array, may be empty)
Line 2: a single integer (the position to delete)

OUTPUT FORMAT
-------------
A list of integers after deletion.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- 0 <= pos < len(arr)
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 3 4
  2
Output: [1, 2, 4]

Input:
  1 2 3
  0
Output: [2, 3]

HINT
----
Walk to position pos-1, then skip: current.next = current.next.next.
Handle pos=0 by returning head.next.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], pos: int) -> list[int]:
    """Delete the node at pos in the linked list built from arr, return as list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    pos = int(input().strip())
    print(solve(arr, pos))
