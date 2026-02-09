"""
Solution for Practice 2: Strongly Connected Components (Kosaraju's)
====================================================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
Kosaraju's two-pass algorithm:
1. DFS on original graph to get finish order
2. DFS on transposed graph in reverse finish order

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of SCCs in the directed graph."""
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * n
    count = 0

    def dfs2(u, label):
        comp[u] = label
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v, label)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, count)
            count += 1

    return count


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
    print(solve(n, edges))
