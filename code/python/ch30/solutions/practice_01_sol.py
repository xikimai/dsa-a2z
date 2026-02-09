"""
Solution for Practice 1: Range Sum with Range Update (Lazy Propagation)
=======================================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Lazy segment tree: each node stores the sum for its range.
Lazy value stores the pending add value.
Push down before accessing children.

TIME COMPLEXITY:  O(Q * log n)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, queries: list[list[int]]) -> list[int]:
    """Return results of range sum queries with range add updates."""
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def push_down(node, start, end):
        if lazy[node] != 0:
            mid = (start + end) // 2
            tree[2 * node] += lazy[node] * (mid - start + 1)
            tree[2 * node + 1] += lazy[node] * (end - mid)
            lazy[2 * node] += lazy[node]
            lazy[2 * node + 1] += lazy[node]
            lazy[node] = 0

    def range_update(node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            tree[node] += val * (end - start + 1)
            lazy[node] += val
            return
        push_down(node, start, end)
        mid = (start + end) // 2
        range_update(2 * node, start, mid, l, r, val)
        range_update(2 * node + 1, mid + 1, end, l, r, val)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def range_query(node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        push_down(node, start, end)
        mid = (start + end) // 2
        return (range_query(2 * node, start, mid, l, r) +
                range_query(2 * node + 1, mid + 1, end, l, r))

    results = []
    for q in queries:
        if q[0] == 1:
            range_update(1, 0, n - 1, q[1], q[2], q[3])
        else:
            results.append(range_query(1, 0, n - 1, q[1], q[2]))
    return results


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        t = int(tokens[idx]); idx += 1
        if t == 1:
            l = int(tokens[idx]); idx += 1
            r = int(tokens[idx]); idx += 1
            v = int(tokens[idx]); idx += 1
            queries.append([t, l, r, v])
        else:
            l = int(tokens[idx]); idx += 1
            r = int(tokens[idx]); idx += 1
            queries.append([t, l, r])
    for r in solve(n, queries):
        print(r)
