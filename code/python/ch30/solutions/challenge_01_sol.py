"""
Solution for Challenge 1: Range Update Range Query (Set, Lazy Segment Tree)
===========================================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Lazy segment tree with "set" operation. Lazy value stores the value
to set (use None / sentinel to mean "no pending set"). When pushing
down, replace children's values entirely.

TIME COMPLEXITY:  O(Q * log n)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, queries: list[list[int]]) -> list[int]:
    """Return results of range sum queries with range set updates."""
    tree = [0] * (4 * n)
    lazy = [None] * (4 * n)  # None means no pending set

    def push_down(node, start, end):
        if lazy[node] is not None:
            mid = (start + end) // 2
            val = lazy[node]
            tree[2 * node] = val * (mid - start + 1)
            tree[2 * node + 1] = val * (end - mid)
            lazy[2 * node] = val
            lazy[2 * node + 1] = val
            lazy[node] = None

    def range_set(node, start, end, l, r, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            tree[node] = val * (end - start + 1)
            lazy[node] = val
            return
        push_down(node, start, end)
        mid = (start + end) // 2
        range_set(2 * node, start, mid, l, r, val)
        range_set(2 * node + 1, mid + 1, end, l, r, val)
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
            range_set(1, 0, n - 1, q[1], q[2], q[3])
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
