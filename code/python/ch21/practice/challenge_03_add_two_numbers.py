"""
Challenge 3: Add Two Numbers
==============================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given two arrays representing non-negative integers in reverse-digit
order (ones place first), build two linked lists, add the two numbers,
and return the sum as an array in the same reverse-digit format.

INPUT FORMAT
------------
Line 1: space-separated digits (first number, reverse order)
Line 2: space-separated digits (second number, reverse order)

OUTPUT FORMAT
-------------
A list of digits representing the sum (reverse order).

CONSTRAINTS
-----------
- 1 <= len(arr1), len(arr2) <= 100
- 0 <= arr1[i], arr2[i] <= 9

EXAMPLES
--------
Input:
  2 4 3
  5 6 4
Output: [7, 0, 8]
(Explanation: 342 + 465 = 807)

Input:
  9 9 9
  1
Output: [0, 0, 0, 1]
(Explanation: 999 + 1 = 1000)

HINT
----
Walk both lists simultaneously. At each step, add the two digits plus
any carry from the previous step. Create a new node with digit = total % 10
and carry = total // 10. Don't forget the final carry!

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr1: list[int], arr2: list[int]) -> list[int]:
    """Add two numbers (in reverse-digit linked list form) and return result."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))
    print(solve(arr1, arr2))
