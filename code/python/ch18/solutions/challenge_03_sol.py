"""
Solution for Challenge 3: Minimum Platforms
=============================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort arrivals and departures separately. Use two pointers to count
max simultaneous trains.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(1) extra
"""


def solve(arrivals: list[int], departures: list[int]) -> int:
    """Return minimum platforms needed."""
    if not arrivals:
        return 0
    arrivals.sort()
    departures.sort()
    platforms = 0
    max_platforms = 0
    i, j = 0, 0
    n = len(arrivals)
    while i < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    return max_platforms


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arrivals = list(map(int, input().strip().split()))
    departures = list(map(int, input().strip().split()))
    print(solve(arrivals, departures))
