"""
Solution for Challenge 3: Maximum Subarray Sum in Range (Segment Tree)
======================================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Each segment tree node stores 4 values:
  - total: sum of all elements in the range
  - prefix: maximum prefix sum
  - suffix: maximum suffix sum
  - best: maximum subarray sum

Merge(left, right):
  total = left.total + right.total
  prefix = max(left.prefix, left.total + right.prefix)
  suffix = max(right.suffix, right.total + left.suffix)
  best = max(left.best, right.best, left.suffix + right.prefix)

TIME COMPLEXITY:  O(n + Q * log n)
SPACE COMPLEXITY: O(n)
"""


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return max subarray sum in arr[l..r] for each query."""
    n = len(arr)
    # Each node: (total, prefix_max, suffix_max, best)
    tree = [(0, 0, 0, 0)] * (4 * n)

    def make_leaf(val):
        return (val, val, val, val)

    def merge(left, right):
        total = left[0] + right[0]
        prefix = max(left[1], left[0] + right[1])
        suffix = max(right[2], right[0] + left[2])
        best = max(left[3], right[3], left[2] + right[1])
        return (total, prefix, suffix, best)

    def build(node, start, end):
        if start == end:
            tree[node] = make_leaf(arr[start])
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

    NEG_INF = float('-inf')
    IDENTITY = (0, NEG_INF, NEG_INF, NEG_INF)

    def query(node, start, end, l, r):
        if r < start or end < l:
            return IDENTITY
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        left_res = query(2 * node, start, mid, l, r)
        right_res = query(2 * node + 1, mid + 1, end, l, r)
        if left_res[3] == NEG_INF:
            return right_res
        if right_res[3] == NEG_INF:
            return left_res
        return merge(left_res, right_res)

    build(1, 0, n - 1)
    results = []
    for q in queries:
        l, r = q[0], q[1]
        res = query(1, 0, n - 1, l, r)
        results.append(res[3])
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
