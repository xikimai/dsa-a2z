"""
Solution for Practice 2: Detect Cycle in Undirected Graph
==========================================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
DFS with parent tracking. For each unvisited node, run DFS. If we
encounter a visited neighbor that is NOT the parent, there's a cycle.
Handle disconnected components by checking all nodes.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""


def solve(n: int, edges: list[list[int]]) -> bool:
    """Return True if the undirected graph contains a cycle."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    def _dfs(node, parent):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if _dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for v in range(n):
        if not visited[v]:
            if _dfs(v, -1):
                return True

    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges))
