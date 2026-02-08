"""
Solution for Challenge 1: Aggressive Cows
==========================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

APPROACH
--------
Binary search on answer space [1, max-min]. For each candidate minimum
distance, greedily place cows and check if all can be placed.

TIME COMPLEXITY:  O(n * log(max - min))
SPACE COMPLEXITY: O(1) extra (after sorting)
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
