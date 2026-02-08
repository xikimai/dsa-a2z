"""
Practice 5: Palindrome Linked List
====================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given an array of integers, build a singly linked list, and determine
whether the list is a palindrome (reads the same forwards and backwards).

INPUT FORMAT
------------
A single line of space-separated integers (may be empty).

OUTPUT FORMAT
-------------
True or False

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^4
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 2 1
Output: True

Input:
  1 2
Output: False

Input:
  1
Output: True

HINT
----
1. Find the middle using slow/fast pointers
2. Reverse the second half of the list
3. Compare the first half with the reversed second half

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr: list[int]) -> bool:
    """Return True if the linked list built from arr is a palindrome."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
