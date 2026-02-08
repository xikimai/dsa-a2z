"""
Solution for Practice 1: Shortest Path (Unweighted)
=====================================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
BFS from source. Use dist array initialized to -1.
Set dist[source] = 0. When visiting a neighbor with dist == -1,
set dist[neighbor] = dist[node] + 1.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque


def solve(n: int, edges: list[list[int]], source: int) -> list[int]:
    """Return shortest distances from source to all nodes."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * n
    dist[source] = 0
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, m, source = int(parts[0]), int(parts[1]), int(parts[2])
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges, source))
