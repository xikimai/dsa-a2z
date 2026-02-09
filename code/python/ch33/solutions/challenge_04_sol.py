"""
Solution for Challenge 4: SCC Condensation (DAG of SCCs)
=========================================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
1. Kosaraju's to find SCC labels for each node.
2. For each original edge (u,v), if comp[u] != comp[v], add edge to condensed DAG.
3. Use a set to avoid duplicate edges. Return the count.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of edges in the condensed DAG of SCCs."""
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

    # Count edges in condensed DAG
    dag_edges = set()
    for u, v in edges:
        if comp[u] != comp[v]:
            dag_edges.add((comp[u], comp[v]))

    return len(dag_edges)


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
