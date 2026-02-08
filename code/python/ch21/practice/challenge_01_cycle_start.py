"""
Challenge 1: Find Cycle Start
===============================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers and a cycle position, build a singly linked
list where the last node's next pointer points to the node at cycle_pos
(0-indexed). If cycle_pos is -1, no cycle is created.
Return the index of the node where the cycle begins, or -1 if no cycle.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: a single integer (the cycle position, -1 for no cycle)

OUTPUT FORMAT
-------------
A single integer — the index where the cycle starts, or -1.

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
Output: 1

Input:
  1 2
  -1
Output: -1

HINT
----
Phase 1: Use Floyd's algorithm to detect the cycle (slow/fast meet).
Phase 2: Move one pointer to head, then advance both one step at a time.
They meet at the cycle start. Then count steps from head to that node.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], cycle_pos: int) -> int:
    """Return the index where the cycle starts, or -1 if no cycle."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    cycle_pos = int(input().strip())
    print(solve(arr, cycle_pos))
