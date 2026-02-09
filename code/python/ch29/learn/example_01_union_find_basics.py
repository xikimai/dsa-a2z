"""
Example 01: Union-Find Basics — Step-by-Step DSU
=================================================
Chapter 29: Union-Find & Minimum Spanning Trees

This example demonstrates the Union-Find (Disjoint Set Union) data
structure through three stages:
  - Naive (no optimizations)
  - Path compression only
  - Path compression + union by rank (optimal)

We also show how to use Union-Find for connected component counting
and cycle detection.
"""


# ── Union-Find: Naive ─────────────────────────────────────────

class UnionFindNaive:
    """O(n) per find in worst case — tree can become a chain."""

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            return True
        return False


# ── Union-Find: Path Compression ──────────────────────────────

class UnionFindPC:
    """Path compression makes find nearly O(1) amortized."""

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            return True
        return False


# ── Union-Find: Full (Path Compression + Union by Rank) ──────

class UnionFind:
    """O(alpha(n)) amortized per operation — effectively O(1)."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


# ── Demo: Connected Components ────────────────────────────────

def count_components(n, edges):
    """Count connected components using Union-Find."""
    uf = UnionFind(n)
    components = n
    for u, v in edges:
        if uf.union(u, v):
            components -= 1
    return components


# ── Demo: Cycle Detection ─────────────────────────────────────

def has_cycle(n, edges):
    """Detect if an undirected graph has a cycle."""
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True  # u and v were already connected
    return False


# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("UNION-FIND: Three Implementations")
    print("=" * 60)

    # Demo graph: 5 nodes, edges connect them into 2 components
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(f"\n  Graph: {n} nodes, edges = {edges}")
    print(f"  Connected components: {count_components(n, edges)}")  # 2

    # Cycle detection
    edges_cycle = [[0, 1], [1, 2], [0, 2]]
    edges_no_cycle = [[0, 1], [1, 2], [3, 4]]
    print(f"\n  Edges {edges_cycle} -> has cycle? {has_cycle(3, edges_cycle)}")  # True
    print(f"  Edges {edges_no_cycle} -> has cycle? {has_cycle(5, edges_no_cycle)}")  # False

    # Show path compression effect
    print("\n" + "=" * 60)
    print("PATH COMPRESSION VISUALIZATION")
    print("=" * 60)
    uf = UnionFind(6)
    # Build a chain: 0->1->2->3->4->5
    for i in range(5):
        uf.parent[i] = i + 1
    print(f"  Before find(0): parent = {uf.parent}")
    uf.find(0)  # triggers path compression
    print(f"  After  find(0): parent = {uf.parent}")
    print("  Notice: all nodes now point directly to root (5)!")
