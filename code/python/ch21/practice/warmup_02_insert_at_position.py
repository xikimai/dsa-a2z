"""
Warmup 2: Insert at Position
==============================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers, a value, and a position, build a singly
linked list from the array, insert the value at the given position,
and return the resulting list as an array.

INPUT FORMAT
------------
Line 1: space-separated integers (the array, may be empty)
Line 2: two space-separated integers: val pos

OUTPUT FORMAT
-------------
A list of integers after insertion.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- 0 <= pos <= len(arr)
- -10^9 <= val, arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 3 4
  99 2
Output: [1, 2, 99, 3, 4]

Input:
  1 2 3
  99 0
Output: [99, 1, 2, 3]

HINT
----
Walk to position pos-1, then rewire: new_node.next = current.next,
current.next = new_node. Handle pos=0 as inserting a new head.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], val: int, pos: int) -> list[int]:
    """Insert val at pos in the linked list built from arr, return as list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    parts = input().strip().split()
    val, pos = int(parts[0]), int(parts[1])
    print(solve(arr, val, pos))
