"""
Example 02: MST Demo — Kruskal's and Prim's Side by Side
=========================================================
Chapter 29: Union-Find & Minimum Spanning Trees

This example demonstrates both MST algorithms on the same graph
and shows they produce the same total weight.
"""

import heapq


# ── Union-Find for Kruskal's ──────────────────────────────────

class UnionFind:
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


# ── Kruskal's Algorithm ───────────────────────────────────────

def kruskal(n, edges):
    """Return (total_weight, mst_edges) using Kruskal's algorithm."""
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(n)
    total = 0
    mst_edges = []
    for u, v, w in sorted_edges:
        if uf.union(u, v):
            total += w
            mst_edges.append((u, v, w))
    return total, mst_edges


# ── Prim's Algorithm ──────────────────────────────────────────

def prim(n, edges):
    """Return (total_weight, mst_edges) using Prim's algorithm."""
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v, u))
        adj[v].append((w, u, v))

    visited = [False] * n
    heap = [(0, 0, -1)]  # (weight, vertex, from_vertex)
    total = 0
    mst_edges = []

    while heap:
        w, u, frm = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        if frm >= 0:
            mst_edges.append((frm, u, w))
        for nw, nv, nu in adj[u]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv, u))

    return total, mst_edges


# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("MST: Kruskal's vs. Prim's")
    print("=" * 60)

    # Graph from the Discovery puzzle
    # Cities: 0=A, 1=B, 2=C, 3=D, 4=E
    n = 5
    edges = [
        [0, 1, 4],   # A-B
        [0, 2, 8],   # A-C
        [1, 2, 2],   # B-C
        [1, 3, 6],   # B-D
        [2, 3, 3],   # C-D
        [2, 4, 9],   # C-E
        [3, 4, 5],   # D-E
    ]

    kw, ke = kruskal(n, edges)
    pw, pe = prim(n, edges)

    print(f"\n  Graph: {n} vertices, {len(edges)} edges")
    print(f"\n  Kruskal's MST: total weight = {kw}")
    for u, v, w in ke:
        print(f"    Edge ({u}, {v}) weight {w}")

    print(f"\n  Prim's MST:    total weight = {pw}")
    for u, v, w in pe:
        print(f"    Edge ({u}, {v}) weight {w}")

    assert kw == pw == 14, f"MST weights should match! Got {kw} and {pw}"
    print(f"\n  Both algorithms give the same total weight: {kw}")
