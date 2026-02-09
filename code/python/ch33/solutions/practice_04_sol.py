"""
Solution for Practice 4: LCA Queries with Node Values
=======================================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
Binary lifting for LCA, then return values[lca_node] for each query.

TIME COMPLEXITY:  O(n log n + q log n)
SPACE COMPLEXITY: O(n log n)
"""

import math
from collections import deque


def solve(n: int, values: list[int], edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """Return the value at the LCA for each query [u, v]."""
    if n == 1:
        return [values[0]] * len(queries)

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

    return [values[lca(u, v)] for u, v in queries]


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    vals = []
    for _ in range(n):
        vals.append(int(tokens[idx])); idx += 1
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
    result = solve(n, vals, edges, queries)
    print(" ".join(map(str, result)))
