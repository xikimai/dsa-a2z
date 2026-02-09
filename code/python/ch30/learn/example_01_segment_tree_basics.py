"""
Example 01: Segment Tree Basics — Build, Query, Update
=======================================================
Chapter 30: Segment Trees & Range Queries

This example demonstrates the core segment tree operations:
  - Build a segment tree from an array
  - Range sum query in O(log n)
  - Point update in O(log n)

We also show how the tree structure maps to the array.
"""


# ── Segment Tree: Sum ────────────────────────────────────────

class SegmentTree:
    """Segment tree for range sum queries with point updates."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node, start, mid)
            self._build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l, r):
        """Return sum of arr[l..r] (inclusive)."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return (self._query(2 * node, start, mid, l, r) +
                self._query(2 * node + 1, mid + 1, end, l, r))

    def update(self, idx, val):
        """Set arr[idx] = val."""
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node, start, mid, idx, val)
            else:
                self._update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


# ── Segment Tree: Min ────────────────────────────────────────

class MinSegmentTree:
    """Segment tree for range minimum queries with point updates."""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node, start, mid)
            self._build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r):
        """Return min of arr[l..r]."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self._query(2 * node, start, mid, l, r),
                   self._query(2 * node + 1, mid + 1, end, l, r))

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node, start, mid, idx, val)
            else:
                self._update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])


# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("SEGMENT TREE BASICS")
    print("=" * 60)

    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)
    print(f"\n  Array: {arr}")
    print(f"  Sum(1, 3) = {st.query(1, 3)}")  # 3+5+7 = 15
    print(f"  Sum(0, 5) = {st.query(0, 5)}")  # 1+3+5+7+9+11 = 36

    st.update(1, 10)
    print(f"\n  After setting arr[1] = 10:")
    print(f"  Sum(1, 3) = {st.query(1, 3)}")  # 10+5+7 = 22
    print(f"  Sum(0, 5) = {st.query(0, 5)}")  # 1+10+5+7+9+11 = 43

    print("\n" + "=" * 60)
    print("MIN SEGMENT TREE")
    print("=" * 60)

    arr2 = [2, 5, 1, 4, 9, 3]
    mst = MinSegmentTree(arr2)
    print(f"\n  Array: {arr2}")
    print(f"  Min(0, 5) = {mst.query(0, 5)}")  # 1
    print(f"  Min(3, 5) = {mst.query(3, 5)}")  # 3

    mst.update(2, 8)
    print(f"\n  After setting arr[2] = 8:")
    print(f"  Min(0, 5) = {mst.query(0, 5)}")  # 2
    print(f"  Min(0, 2) = {mst.query(0, 2)}")  # 2

    print("\n" + "=" * 60)
    print("TREE STRUCTURE VISUALIZATION")
    print("=" * 60)

    arr3 = [1, 3, 5, 7]
    st3 = SegmentTree(arr3)
    print(f"\n  Array: {arr3}")
    print(f"  Tree array (nodes 1..7): {st3.tree[1:8]}")
    print(f"  Node 1 (root, [0..3]): {st3.tree[1]}")
    print(f"  Node 2 ([0..1]):       {st3.tree[2]}")
    print(f"  Node 3 ([2..3]):       {st3.tree[3]}")
    print(f"  Node 4 ([0]):          {st3.tree[4]}")
    print(f"  Node 5 ([1]):          {st3.tree[5]}")
    print(f"  Node 6 ([2]):          {st3.tree[6]}")
    print(f"  Node 7 ([3]):          {st3.tree[7]}")
