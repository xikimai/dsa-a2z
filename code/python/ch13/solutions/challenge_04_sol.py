"""
Solution for Challenge 4: Fence Painting (USACO Bronze Style)
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Sort intervals by start. Merge overlapping intervals.
Sum the lengths of merged intervals.

TIME COMPLEXITY:  O(N log N) — sorting
SPACE COMPLEXITY: O(1) — in-place
"""


def solve(fences: list[list[int]]) -> int:
    """Return total painted length (no double counting)."""
    if not fences:
        return 0
    fences.sort()
    total = 0
    cur_start, cur_end = fences[0]
    for start, end in fences[1:]:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            total += cur_end - cur_start
            cur_start, cur_end = start, end
    total += cur_end - cur_start
    return total


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    fences = []
    for _ in range(n):
        s, e = map(int, input().split())
        fences.append([s, e])
    print(solve(fences))
