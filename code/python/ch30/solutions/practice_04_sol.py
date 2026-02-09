"""
Solution for Practice 4: Kth Order Statistics (Segment Tree on Values)
======================================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Build a segment tree over the value range [1, MAX_VAL]. Each node stores
the count of elements in that value range. To find kth smallest, walk
the tree: if left child count >= k, go left; otherwise go right with
k -= left_count.

TIME COMPLEXITY:  O(Q * log(MAX_VAL))
SPACE COMPLEXITY: O(MAX_VAL)
"""


def solve(queries: list[list[int]]) -> list[int]:
    """Return results of kth-smallest queries on a dynamic multiset."""
    MAX_VAL = 100001
    tree = [0] * (4 * MAX_VAL)

    def update(node, start, end, idx, delta):
        if start == end:
            tree[node] += delta
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, delta)
            else:
                update(2 * node + 1, mid + 1, end, idx, delta)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def kth(node, start, end, k):
        if start == end:
            return start
        mid = (start + end) // 2
        left_count = tree[2 * node]
        if k <= left_count:
            return kth(2 * node, start, mid, k)
        else:
            return kth(2 * node + 1, mid + 1, end, k - left_count)

    results = []
    for q in queries:
        if q[0] == 1:
            update(1, 1, MAX_VAL - 1, q[1], 1)
        elif q[0] == 2:
            update(1, 1, MAX_VAL - 1, q[1], -1)
        else:
            results.append(kth(1, 1, MAX_VAL - 1, q[1]))
    return results


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        t = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        queries.append([t, v])
    for r in solve(queries):
        print(r)
