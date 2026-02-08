"""
Challenge 4: Flatten a Multilevel Doubly Linked List
=====================================================
Chapter 21: Linked Lists — Pointers and Connections

PROBLEM
-------
Given a nested list of integers (which may contain sublists at any depth),
flatten it into a single-level list using depth-first order.

INPUT FORMAT
------------
A single line of JSON representing a nested list, e.g. [1,[2,3],[4,[5]]]

OUTPUT FORMAT
-------------
A flat list of all integers in depth-first order.

CONSTRAINTS
-----------
- 0 <= total integers <= 10^4
- Nesting depth <= 100
- -10^9 <= each integer <= 10^9

EXAMPLES
--------
Input:
  [1, [2, 3], [4, [5, 6]], 7]
Output: [1, 2, 3, 4, 5, 6, 7]

Input:
  [[1, 2], [3, [4, [5]]]]
Output: [1, 2, 3, 4, 5]

HINT
----
Use recursion: for each element, if it's a list, recursively flatten it;
if it's an integer, add it to the result.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(nested: list) -> list[int]:
    """Flatten the nested list into a single-level list (depth-first)."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json
    nested = json.loads(input().strip())
    print(solve(nested))
