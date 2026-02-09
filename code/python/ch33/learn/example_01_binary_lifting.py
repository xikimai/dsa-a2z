"""
Example 01: Binary Lifting — LCA in O(log n)
=============================================
Chapter 33: Advanced Trees & Graph Algorithms

This example demonstrates binary lifting for fast LCA queries:
  - Building the binary lifting table (up[v][k] = 2^k-th ancestor of v)
  - Answering LCA queries in O(log n)
  - Computing distances between tree nodes using LCA
"""

import math
from collections import deque


# ── Binary Lifting ────────────────────────────────────────────

def build(n, edges, root=0):
    """Build adjacency list, depths, and binary lifting table."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    LOG = max(1, math.ceil(math.log2(n)) + 1) if n > 1 else 1
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    # BFS to compute depths and direct parents
    visited = [False] * n
    queue = deque([root])
    visited[root] = True
    while queue:
        node = queue.popleft()
        for nb in adj[node]:
            if not visited[nb]:
                visited[nb] = True
                depth[nb] = depth[node] + 1
                up[nb][0] = node
                queue.append(nb)

    # Fill the rest of the table: up[v][k] = up[up[v][k-1]][k-1]
    for k in range(1, LOG):
        for v in range(n):
            if up[v][k - 1] != -1:
                up[v][k] = up[up[v][k - 1]][k - 1]

    return up, depth, LOG


def lca(u, v, up, depth, LOG):
    """Find the LCA of u and v using binary lifting."""
    if depth[u] < depth[v]:
        u, v = v, u

    # Bring u up to the same depth as v
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if (diff >> k) & 1:
            u = up[u][k]

    if u == v:
        return u

    # Jump both up, stopping just below the LCA
    for k in range(LOG - 1, -1, -1):
        if up[u][k] != up[v][k]:
            u = up[u][k]
            v = up[v][k]

    return up[u][0]


# ── Demo ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("BINARY LIFTING: LCA in O(log n)")
    print("=" * 60)

    #        0
    #       / \
    #      1   2
    #     / \   \
    #    3   4   5
    #             \
    #              6
    n = 7
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6]]

    up, depth, LOG = build(n, edges)

    print(f"\n  Tree: {n} nodes")
    print(f"  LOG = {LOG}")
    print(f"  Depths: {depth}")

    queries = [(3, 4), (3, 6), (4, 5), (6, 0)]
    for u, v in queries:
        result = lca(u, v, up, depth, LOG)
        print(f"  LCA({u}, {v}) = {result}")

    # Expected: LCA(3,4)=1, LCA(3,6)=0, LCA(4,5)=0, LCA(6,0)=0
