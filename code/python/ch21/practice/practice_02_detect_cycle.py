"""
Practice 2: Detect Cycle
=========================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers and a cycle position, build a singly linked
list where the last node's next pointer points to the node at cycle_pos
(0-indexed). If cycle_pos is -1, no cycle is created.
Return True if the list has a cycle, False otherwise.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: a single integer (the cycle position, -1 for no cycle)

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- -1 <= cycle_pos < len(arr)
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  3 2 0 -4
  1
Output: True

Input:
  1 2
  -1
Output: False

HINT
----
Use Floyd's cycle detection: slow moves one step, fast moves two.
If they ever meet, there's a cycle. If fast reaches null, there's no cycle.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], cycle_pos: int) -> bool:
    """Return True if the linked list (with cycle at cycle_pos) has a cycle."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    cycle_pos = int(input().strip())
    print(solve(arr, cycle_pos))
