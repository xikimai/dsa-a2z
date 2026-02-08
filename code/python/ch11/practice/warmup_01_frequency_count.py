"""
Warmup 1: Frequency Count
==============================
Chapter 11: Hashing — The Secret Decoder Ring

PROBLEM
-------
Given an array of integers, count the frequency of each element.
Return a list of [value, count] pairs sorted by value in ascending order.

INPUT FORMAT
------------
A single line of space-separated integers.

OUTPUT FORMAT
-------------
A list of [value, count] pairs sorted by value.

CONSTRAINTS
-----------
- 0 <= len(arr) <= 10^5
- -10^9 <= arr[i] <= 10^9

EXAMPLES
--------
Input:
  1 2 2 3 3 3
Output: [[1, 1], [2, 2], [3, 3]]

Input:
  3 1 2 1
Output: [[1, 2], [2, 1], [3, 1]]

HINT
----
Use a dictionary to count occurrences. Then convert to a list
of pairs and sort by the value (first element).

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int]) -> list[list[int]]:
    """Return sorted list of [value, count] pairs."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        arr = list(map(int, line.split()))
    else:
        arr = []
    print(solve(arr))
