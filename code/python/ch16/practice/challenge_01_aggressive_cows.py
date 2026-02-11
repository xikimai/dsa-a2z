"""
Challenge 1: Aggressive Cows
===============================
Chapter 16: Binary Search Beyond — When the Answer Is the Question

PROBLEM
-------
Given n stall positions and c cows, place all cows into stalls such that
the minimum distance between any two cows is maximized. The stalls may
not be sorted initially. Return the largest possible minimum distance.

INPUT FORMAT
------------
First line: space-separated integers (stall positions).
Second line: a single integer (number of cows).

OUTPUT FORMAT
-------------
A single integer — the maximum possible minimum distance.

CONSTRAINTS
-----------
- 2 <= len(stalls) <= 10^5
- 0 <= stalls[i] <= 10^9
- 2 <= cows <= len(stalls)

EXAMPLES
--------
Input:
  1 2 8 4 9
  3
Output: 3

Input:
  1 2 4 8 9
  2
Output: 8

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(stalls: list[int], cows: int) -> int:
    """Return maximum possible minimum distance between any two cows."""
    pass  # TODO: Replace this with your solution

    def feasible(min_dist):
        count, last = 1, stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last >= min_dist:
                count += 1
                last = stalls[i]
                if count >= cows:
                    return True
        return False

    lo, hi = 1, stalls[-1] - stalls[0]
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2  # round UP for "find maximum"
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    stalls = list(map(int, line.split()))
    cows = int(input().strip())
    print(solve(stalls, cows))
