"""
Challenge 2: Intersection of Two Lists
========================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given two arrays and skip values, build two singly linked lists that
share a common suffix (intersection). The first skip_a elements of arr_a
form list A's prefix, and the first skip_b elements of arr_b form list B's
prefix. The remaining elements (which must match) form the shared tail.
Return the value at the intersection point, or -1 if no intersection.

INPUT FORMAT
------------
Line 1: space-separated integers (arr_a)
Line 2: space-separated integers (arr_b)
Line 3: two space-separated integers: skip_a skip_b

OUTPUT FORMAT
-------------
A single integer — the value at the intersection, or -1.

CONSTRAINTS
-----------
- 0 <= len(arr_a), len(arr_b) <= 10^4
- 0 <= skip_a <= len(arr_a)
- 0 <= skip_b <= len(arr_b)
- arr_a[skip_a:] == arr_b[skip_b:]

EXAMPLES
--------
Input:
  4 1 8 4 5
  5 6 1 8 4 5
  2 3
Output: 8

Input:
  2 6 4
  1 5
  3 2
Output: -1

HINT
----
Use two pointers, one starting at each head. When a pointer reaches null,
redirect it to the other list's head. They will meet at the intersection
(or both reach null if no intersection) after at most n+m steps.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(arr_a: list[int], arr_b: list[int], skip_a: int, skip_b: int) -> int:
    """Return the value at the intersection point, or -1."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr_a = list(map(int, input().strip().split()))
    arr_b = list(map(int, input().strip().split()))
    parts = input().strip().split()
    skip_a, skip_b = int(parts[0]), int(parts[1])
    print(solve(arr_a, arr_b, skip_a, skip_b))
