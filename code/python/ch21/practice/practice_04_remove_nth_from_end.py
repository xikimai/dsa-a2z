"""
Practice 4: Remove Nth Node From End
======================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers and a number n, build a singly linked list,
remove the nth node from the end of the list, and return the result
as an array.

INPUT FORMAT
------------
Line 1: space-separated integers (the array)
Line 2: a single integer n

OUTPUT FORMAT
-------------
A list of integers after removing the nth node from the end.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^4
- 1 <= n <= len(arr)
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 3 4 5
  2
Output: [1, 2, 3, 5]

Input:
  1
  1
Output: []

HINT
----
Use two pointers with a gap of n between them. When the front pointer
reaches the end, the back pointer is right before the node to remove.
Use a dummy node to handle removing the head.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int], n: int) -> list[int]:
    """Remove the nth node from the end and return the result as a list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    n = int(input().strip())
    print(solve(arr, n))
