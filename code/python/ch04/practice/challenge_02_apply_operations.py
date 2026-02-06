"""
Challenge 2: Apply Operations
==============================
Chapter 4: Functions

PROBLEM
-------
Given a list of integers and a list of operations, apply each operation
in order to the list and return the final result.

Supported operations:
  - "double"  : multiply every element by 2
  - "negate"  : flip the sign of every element
  - "sort"    : sort the list in ascending order
  - "reverse" : reverse the list

Define a separate helper function for each operation.

INPUT FORMAT
------------
First line: space-separated integers (the list)
Second line: space-separated operation names

OUTPUT FORMAT
-------------
The final list, space-separated.

CONSTRAINTS
-----------
- List can be empty
- Operations list can be empty (return original list)
- Unknown operations are silently ignored

EXAMPLES
--------
Input:  3 1 2
        double sort
Output: 2 4 6

Input:  1 -2 3
        negate reverse
Output: -3 2 -1

Input:  5 3 1
        sort reverse double
Output: 10 6 2

INSTRUCTIONS
------------
Replace the `pass` in each helper function and solve() with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def op_double(nums: list[int]) -> list[int]:
    """Multiply every element by 2 (in place) and return the list."""
    pass  # TODO: Replace this with your solution


def op_negate(nums: list[int]) -> list[int]:
    """Flip the sign of every element (in place) and return the list."""
    pass  # TODO: Replace this with your solution


def op_sort(nums: list[int]) -> list[int]:
    """Sort the list in ascending order (in place) and return it."""
    pass  # TODO: Replace this with your solution


def op_reverse(nums: list[int]) -> list[int]:
    """Reverse the list (in place) and return it."""
    pass  # TODO: Replace this with your solution


def solve(nums: list[int], operations: list[str]) -> list[int]:
    """Apply each operation in order and return the final list."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line1 = input().strip()
    if line1:
        nums = list(map(int, line1.split()))
    else:
        nums = []
    line2 = input().strip()
    if line2:
        operations = line2.split()
    else:
        operations = []
    result = solve(nums, operations)
    print(" ".join(map(str, result)))
