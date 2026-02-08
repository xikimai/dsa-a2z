"""
Solution for Practice 4: Range Update with Difference Array
=============================================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Use a difference array. For each update [l, r, val]:
  diff[l] += val, diff[r+1] -= val.
Then compute prefix sum of diff to reconstruct.

TIME COMPLEXITY:  O(n + q)
SPACE COMPLEXITY: O(n) — difference array
"""


def solve(n: int, updates: list[list[int]]) -> list[int]:
    """Return the final array after all range updates."""
    diff = [0] * (n + 1)
    for l, r, val in updates:
        diff[l] += val
        if r + 1 <= n:
            diff[r + 1] -= val

    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    q = int(input())
    updates = []
    for _ in range(q):
        parts = list(map(int, input().split()))
        updates.append(parts)
    print(solve(n, updates))
