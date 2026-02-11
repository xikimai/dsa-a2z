"""
Warmup 2: Range Sum Query
============================
Chapter 14: Prefix Sums — The Power of Pre-computation

PROBLEM
-------
Given an array and multiple queries, each specifying a range [l, r]
(0-indexed, inclusive), return the sum of elements from index l to r
for each query.

INPUT FORMAT
------------
First line: space-separated integers (the array).
Second line: integer q (number of queries).
Next q lines: two integers l and r per line.

OUTPUT FORMAT
-------------
A list of range sums.

CONSTRAINTS
-----------
- 1 <= len(arr) <= 10^5
- 0 <= l <= r < len(arr)
- 1 <= q <= 10^5

EXAMPLES
--------
Input:
  3 1 4 1 5 9
  2
  0 5
  2 4
Output: [23, 10]

Input:
  10 20 30
  3
  0 0
  1 1
  2 2
Output: [10, 20, 30]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return list of range sums for each [l, r] query."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append([l, r])
    print(solve(arr, queries))

