"""
Solution for Warmup 5: Is Path Exists
=======================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Build adjacency list, then BFS from source. If we visit dest during
the BFS, return True. If BFS completes without visiting dest, return False.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque


def solve(n: int, edges: list[list[int]], source: int, dest: int) -> bool:
    """Return True if a path exists from source to dest."""
    if source == dest:
        return True

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    visited[source] = True
    queue = deque([source])

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor == dest:
                return True
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return False


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    n, m, source, dest = int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges, source, dest))
