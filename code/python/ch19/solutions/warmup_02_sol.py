"""
Solution for Warmup 2: BFS Traversal
======================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Build adjacency list, then BFS from source using a queue.
Sort neighbors for deterministic order (visit smallest first).

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V)
"""

from collections import deque


def solve(n: int, edges: list[list[int]], source: int) -> list[int]:
    """Return BFS traversal order from source."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    visited[source] = True
    queue = deque([source])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in sorted(adj[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return order


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, m, source = int(parts[0]), int(parts[1]), int(parts[2])
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges, source))
