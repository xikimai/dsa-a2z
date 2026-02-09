"""
Solution for Warmup 3: Prefix Sum with BIT (Fenwick Tree)
=========================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Fenwick tree (BIT) with 1-indexed internal storage.
  - type 1: prefix sum query (0..l)
  - type 2: point add (arr[l] += val)

TIME COMPLEXITY:  O(n * log n + Q * log n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of prefix sum queries with point add updates."""
    n = len(arr)
    bit = [0] * (n + 1)

    def update(i, delta):
        i += 1  # convert to 1-indexed
        while i <= n:
            bit[i] += delta
            i += i & (-i)

    def prefix(i):
        i += 1  # convert to 1-indexed
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    # Build BIT from array
    for i, v in enumerate(arr):
        update(i, v)

    results = []
    for q in queries:
        if q[0] == 1:
            results.append(prefix(q[1]))
        else:
            # type 2: add val to index l
            update(q[1], q[2])
    return results


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    arr = [int(tokens[idx + i]) for i in range(n)]; idx += n
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        t = int(tokens[idx]); idx += 1
        a = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1
        queries.append([t, a, b])
    for r in solve(arr, queries):
        print(r)
