"""
Solution for Practice 5: XOR on Range (Segment Tree)
=====================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Segment tree with XOR operation. Identity element is 0.

TIME COMPLEXITY:  O(n + Q * log n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return results of range XOR queries with point updates."""
    n = len(arr)
    tree = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] ^ tree[2 * node + 1]

    def query(node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return (query(2 * node, start, mid, l, r) ^
                query(2 * node + 1, mid + 1, end, l, r))

    build(1, 0, n - 1)
    results = []
    for q in queries:
        if q[0] == 1:
            results.append(query(1, 0, n - 1, q[1], q[2]))
        else:
            update(1, 0, n - 1, q[1], q[2])
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
