"""
Warmup 4: Search in Linked List
=================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers and a target value, build a singly linked
list from the array, then search for the target value. Return True if
found, False otherwise.

INPUT FORMAT
------------
Line 1: space-separated integers (the array, may be empty)
Line 2: a single integer (the target)

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- -10^9 <= arr[i], target <= 10^9

EXAMPLES
--------
Input:
  1 2 3 4 5
  3
Output: True

Input:
  1 2 3
  7
Output: False

HINT
----
Traverse the linked list. At each node, compare its value to the target.
If found, return True immediately. If you reach the end, return False.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], target: int) -> bool:
    """Return True if target exists in the linked list built from arr."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    target = int(input().strip())
    print(solve(arr, target))
