"""
Solution for Warmup 4: Count Inversions (BIT)
=============================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Coordinate compress values, then process array right-to-left.
For each element, count how many already-inserted elements have
smaller rank (using BIT prefix sum). Then insert current element.

TIME COMPLEXITY:  O(n log n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int]) -> int:
    """Return the number of inversions in the array."""
    if not arr:
        return 0

    # Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
    max_rank = len(sorted_unique)

    # BIT
    bit = [0] * (max_rank + 1)

    def update(i, delta):
        while i <= max_rank:
            bit[i] += delta
            i += i & (-i)

    def prefix(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    inversions = 0
    for i in range(len(arr) - 1, -1, -1):
        r = rank[arr[i]]
        # Count elements already inserted with rank < r
        inversions += prefix(r - 1)
        update(r, 1)

    return inversions


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    arr = [int(tokens[i + 1]) for i in range(n)]
    print(solve(arr))
