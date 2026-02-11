"""
Practice 2: Ship Packages Within D Days
=========================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Packages on a conveyor belt must be shipped in order within d days. Each
day you load packages sequentially until the next package would exceed the
ship capacity. Find the minimum ship capacity to ship all packages in d days.

INPUT FORMAT
------------
First line: space-separated integers (package weights).
Second line: a single integer d (number of days).

OUTPUT FORMAT
-------------
A single integer — the minimum ship capacity.

CONSTRAINTS
-----------
- 1 <= len(weights) <= 5 * 10^4
- 1 <= weights[i] <= 500
- 1 <= d <= len(weights)

EXAMPLES
--------
Input:
  1 2 3 4 5 6 7 8 9 10
  5
Output: 15

Input:
  3 2 2 4 1 4
  3
Output: 6

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(weights: list[int], d: int) -> int:
    """Return minimum ship capacity to deliver all packages in d days."""
    pass  # TODO: Replace this with your solution

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    weights = list(map(int, line.split()))
    d = int(input().strip())
    print(solve(weights, d))
