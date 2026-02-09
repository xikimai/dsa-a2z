"""
Solution for Challenge 3: Ninja Training
==========================================
Chapter 24: Dynamic Programming II — Grids and Paths

APPROACH
--------
Space-optimized DP. Track prev[0], prev[1], prev[2] = best total points
ending with activity 0, 1, 2 on the previous day. For each new day,
pick the best non-same activity from previous.

TIME COMPLEXITY:  O(n * 3 * 3) = O(n)
SPACE COMPLEXITY: O(1)
"""

from typing import List


def solve(points: List[List[int]]) -> int:
    """Return the maximum total points the ninja can earn."""
    prev = points[0][:]
    for i in range(1, len(points)):
        curr = [0, 0, 0]
        for j in range(3):
            for k in range(3):
                if k != j:
                    curr[j] = max(curr[j], prev[k] + points[i][j])
        prev = curr
    return max(prev)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    import json, sys
    points = json.loads(sys.stdin.readline())
    print(solve(points))
