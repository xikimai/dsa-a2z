"""
Example 02: Tarjan's Bridges & Kosaraju's SCC
==============================================
Chapter 33: Advanced Trees & Graph Algorithms

This example demonstrates:
  - Finding bridges (critical edges) with Tarjan's algorithm
  - Finding articulation points
  - Finding SCCs with Kosaraju's two-pass algorithm
"""

import sys
sys.setrecursionlimit(10000)


# ── Tarjan's Bridges ─────────────────────────────────────────

def find_bridges(n, edges):
    """Find all bridges in an undirected graph."""
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


# ── Kosaraju's SCC ───────────────────────────────────────────

def kosaraju(n, edges):
    """Find number of SCCs in a directed graph using Kosaraju's."""
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

    return count, comp


# ── Demo ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("TARJAN'S BRIDGES")
    print("=" * 60)

    # Graph: 0-1-2-0 (cycle), 1-3, 3-4
    n = 5
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    bridges = find_bridges(n, edges)
    print(f"\n  Graph: {n} nodes, edges = {edges}")
    print(f"  Bridges: {bridges}")  # [[1,3], [3,4]]

    print("\n" + "=" * 60)
    print("KOSARAJU'S SCC")
    print("=" * 60)

    # Directed: 0->1->2->0 (SCC), 1->3, 3->4
    n = 5
    directed_edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    num_scc, comp = kosaraju(n, directed_edges)
    print(f"\n  Directed graph: {n} nodes, edges = {directed_edges}")
    print(f"  Number of SCCs: {num_scc}")  # 3
    print(f"  Component labels: {comp}")

    # Group by SCC
    from collections import defaultdict
    groups = defaultdict(list)
    for node, label in enumerate(comp):
        groups[label].append(node)
    for label, nodes in sorted(groups.items()):
        print(f"    SCC {label}: {nodes}")
