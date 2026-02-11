"""
Practice 1: Koko Eating Bananas
=================================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Koko loves bananas. There are n piles of bananas. She can eat at most k
bananas per hour from one pile. If a pile has fewer than k bananas, she
eats all of them and waits for the next hour. Find the minimum integer k
such that she can eat all bananas within h hours.

INPUT FORMAT
------------
First line: space-separated integers (pile sizes).
Second line: a single integer h (hours available).

OUTPUT FORMAT
-------------
A single integer — the minimum eating speed k.

CONSTRAINTS
-----------
- 1 <= len(piles) <= 10^4
- 1 <= piles[i] <= 10^9
- len(piles) <= h <= 10^9

EXAMPLES
--------
Input:
  3 6 7 11
  8
Output: 4

Input:
  30 11 23 4 20
  5
Output: 30

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""

import math


def solve(piles: list[int], h: int) -> int:
    """Return minimum eating speed to finish all piles in h hours."""
    pass  # TODO: Replace this with your solution

    lo, hi = 1, max(piles)
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
    piles = list(map(int, line.split()))
    h = int(input().strip())
    print(solve(piles, h))
