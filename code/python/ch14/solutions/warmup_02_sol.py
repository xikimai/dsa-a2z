"""
Solution for Warmup 2: Range Sum Query
========================================
Chapter 14: Prefix Sums — The Running Total Trick

APPROACH
--------
Build prefix sum once, answer each query with prefix[r+1] - prefix[l].

TIME COMPLEXITY:  O(n + q) — n to build prefix, O(1) per query
SPACE COMPLEXITY: O(n) — prefix array
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return list of range sums for each [l, r] query."""
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    result = []
    for l, r in queries:
        result.append(prefix[r + 1] - prefix[l])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        l, r = map(int, input().split())
        queries.append([l, r])
    print(solve(arr, queries))
