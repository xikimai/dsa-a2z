"""
Solution for Challenge 2: Distinct Values in Range (Offline + BIT)
==================================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Process queries offline sorted by right endpoint.
Maintain a BIT where bit[i] = 1 if arr[i] is the latest occurrence
of its value up to the current position.
For each value, track its last seen index. When we see a value again,
remove its previous occurrence from the BIT and add the new one.
Answer for query [l, r] is prefix_sum(r) - prefix_sum(l-1).

TIME COMPLEXITY:  O((n + Q) * log n)
SPACE COMPLEXITY: O(n + Q)
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return count of distinct values in arr[l..r] for each query."""
    n = len(arr)
    bit = [0] * (n + 2)  # 1-indexed

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

    # Sort queries by right endpoint
    indexed_queries = sorted(enumerate(queries), key=lambda x: x[1][1])

    results = [0] * len(queries)
    last_seen = {}  # value -> last index where it appeared
    qi = 0  # pointer into sorted queries
    j = 0   # current position in arr

    for qi_idx in range(len(indexed_queries)):
        orig_idx, (l, r) = indexed_queries[qi_idx]
        # Process array elements up to r
        while j <= r:
            val = arr[j]
            if val in last_seen:
                update(last_seen[val], -1)  # remove old occurrence
            last_seen[val] = j
            update(j, 1)
            j += 1
        # Answer query
        left_sum = prefix(l - 1) if l > 0 else 0
        results[orig_idx] = prefix(r) - left_sum

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
        l = int(tokens[idx]); idx += 1
        r = int(tokens[idx]); idx += 1
        queries.append([l, r])
    for r in solve(arr, queries):
        print(r)
