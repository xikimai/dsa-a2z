"""
Solution for Warmup 4: Count Connected Components
===================================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Build adjacency list. Loop through all nodes; for each unvisited node,
run BFS to mark all reachable nodes as visited. Count the number of
BFS launches.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of connected components."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    count = 0

    for v in range(n):
        if not visited[v]:
            queue = deque([v])
            visited[v] = True
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            count += 1

    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges))
