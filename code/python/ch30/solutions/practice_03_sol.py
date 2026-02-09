"""
Solution for Practice 3: Count of Elements in Range
====================================================
Chapter 30: Segment Trees & Range Queries

APPROACH
--------
Merge sort tree: build a segment tree where each node stores a sorted
list of elements in its range. To count elements in [lo, hi] within
arr[l..r], query the tree and use bisect on each relevant node's list.

TIME COMPLEXITY:  O(n log n + Q * log^2 n)
SPACE COMPLEXITY: O(n log n)
"""
from bisect import bisect_left, bisect_right


def solve(arr: list[int], queries: list[list[int]]) -> list[int]:
    """Return count of elements in arr[l..r] within [lo, hi] for each query."""
    n = len(arr)
    # Build merge sort tree
    tree = [[] for _ in range(4 * n)]

    def build(node, start, end):
        if start == end:
            tree[node] = [arr[start]]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            # Merge two sorted lists
            left, right = tree[2 * node], tree[2 * node + 1]
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i]); i += 1
                else:
                    merged.append(right[j]); j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            tree[node] = merged

    def query(node, start, end, l, r, lo, hi):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            # Count elements in [lo, hi] using binary search
            return bisect_right(tree[node], hi) - bisect_left(tree[node], lo)
        mid = (start + end) // 2
        return (query(2 * node, start, mid, l, r, lo, hi) +
                query(2 * node + 1, mid + 1, end, l, r, lo, hi))

    build(1, 0, n - 1)
    results = []
    for q in queries:
        l, r, lo, hi = q
        results.append(query(1, 0, n - 1, l, r, lo, hi))
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
        lo = int(tokens[idx]); idx += 1
        hi = int(tokens[idx]); idx += 1
        queries.append([l, r, lo, hi])
    for r in solve(arr, queries):
        print(r)
