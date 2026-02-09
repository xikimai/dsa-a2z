"""
Solution for Warmup 1: LCA with Binary Lifting
=================================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
Binary lifting: BFS to compute depths and parents, then fill up[v][k] table.
LCA query: equalize depths, then jump both up until they meet.

TIME COMPLEXITY:  O(n log n) preprocessing, O(log n) per query
SPACE COMPLEXITY: O(n log n)
"""

import math
from collections import deque


def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return the LCA for each query [u, v] using binary lifting."""
    if n == 1:
        return [0] * len(queries)

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    LOG = max(1, math.ceil(math.log2(n)) + 1)
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    visited = [False] * n
    queue = deque([0])
    visited[0] = True
    while queue:
        node = queue.popleft()
        for nb in adj[node]:
            if not visited[nb]:
                visited[nb] = True
                depth[nb] = depth[node] + 1
                up[nb][0] = node
                queue.append(nb)

    for k in range(1, LOG):
        for v in range(n):
            if up[v][k - 1] != -1:
                up[v][k] = up[up[v][k - 1]][k - 1]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG):
            if (diff >> k) & 1:
                u = up[u][k]
        if u == v:
            return u
        for k in range(LOG - 1, -1, -1):
            if up[u][k] != up[v][k]:
                u = up[u][k]
                v = up[v][k]
        return up[u][0]

    return [lca(u, v) for u, v in queries]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        queries.append([u, v])
    result = solve(n, edges, queries)
    print(" ".join(map(str, result)))
