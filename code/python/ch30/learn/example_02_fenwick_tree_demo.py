"""
Example 02: Fenwick Tree (Binary Indexed Tree) Demo
====================================================
Chapter 30: Segment Trees & Range Queries

This example demonstrates the Fenwick tree (BIT):
  - Point update (add delta to an index)
  - Prefix sum query
  - Range sum query
  - Using BIT for counting inversions
"""


# ── Fenwick Tree ──────────────────────────────────────────────

class FenwickTree:
    """Binary Indexed Tree for prefix sum queries with point updates.
    Uses 1-based indexing internally."""

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        """Add delta to index i (1-indexed)."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def prefix_sum(self, i):
        """Sum of elements from index 1 to i (1-indexed)."""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

    def range_sum(self, l, r):
        """Sum of elements from index l to r (1-indexed, inclusive)."""
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

    @classmethod
    def from_array(cls, arr):
        """Build a BIT from a 0-indexed array."""
        bit = cls(len(arr))
        for i, v in enumerate(arr):
            bit.update(i + 1, v)  # convert to 1-indexed
        return bit


# ── Count Inversions using BIT ────────────────────────────────

def count_inversions(arr):
    """Count the number of inversions in arr using a BIT.

    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    Strategy: process from right to left, for each element count how many
    smaller elements are already in the BIT (to its right in original array).
    """
    if not arr:
        return 0

    # Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {v: i + 1 for i, v in enumerate(sorted_unique)}

    bit = FenwickTree(len(sorted_unique))
    inversions = 0

    for i in range(len(arr) - 1, -1, -1):
        r = rank[arr[i]]
        # Count elements already inserted that are smaller (rank 1 to r-1)
        inversions += bit.prefix_sum(r - 1)
        bit.update(r, 1)

    return inversions


# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("FENWICK TREE (BIT) DEMO")
    print("=" * 60)

    arr = [1, 2, 3, 4, 5]
    bit = FenwickTree.from_array(arr)

    print(f"\n  Array: {arr} (0-indexed)")
    print(f"  Prefix sum to index 3 (1-indexed): {bit.prefix_sum(3)}")  # 1+2+3=6
    print(f"  Prefix sum to index 5 (1-indexed): {bit.prefix_sum(5)}")  # 15
    print(f"  Range sum [2, 4] (1-indexed):      {bit.range_sum(2, 4)}")  # 2+3+4=9

    # Point update: add 5 to index 3 (1-indexed)
    bit.update(3, 5)
    print(f"\n  After adding 5 to index 3:")
    print(f"  Prefix sum to index 3: {bit.prefix_sum(3)}")  # 1+2+8=11
    print(f"  Range sum [2, 4]:      {bit.range_sum(2, 4)}")  # 2+8+4=14

    print("\n" + "=" * 60)
    print("THE i & (-i) TRICK")
    print("=" * 60)

    for i in range(1, 9):
        lsb = i & (-i)
        print(f"  i={i} (binary {i:04b}): i&(-i) = {lsb} -> "
              f"responsible for {lsb} element(s)")

    print("\n" + "=" * 60)
    print("COUNTING INVERSIONS")
    print("=" * 60)

    test_cases = [
        ([2, 3, 8, 6, 1], 5),
        ([5, 4, 3, 2, 1], 10),
        ([1, 2, 3, 4, 5], 0),
        ([1, 1, 1], 0),
    ]

    for arr, expected in test_cases:
        result = count_inversions(arr)
        status = "OK" if result == expected else "FAIL"
        print(f"  {arr} -> {result} inversions ({status})")
