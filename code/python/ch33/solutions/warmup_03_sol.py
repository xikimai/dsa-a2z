"""
Solution for Warmup 3: Find Bridges in Graph
==============================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
Tarjan's bridge-finding algorithm: DFS with disc[] and low[] arrays.
Edge (u,v) is a bridge if low[v] > disc[u] (v's subtree has no back edge
to u or above).

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return all bridges in the graph, sorted."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * n
    low = [0] * n
    bridges = []
    timer = [0]

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in adj[u]:
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([min(u, v), max(u, v)])
            elif v != parent:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    bridges.sort()
    return bridges


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    result = solve(n, edges)
    for bridge in result:
        print(bridge[0], bridge[1])
