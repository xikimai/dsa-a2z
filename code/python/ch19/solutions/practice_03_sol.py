"""
Solution for Practice 3: Bipartite Check
==========================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
BFS 2-coloring. Use a color array initialized to -1.
For each unvisited node, assign color 0 and BFS. For each neighbor,
if uncolored, assign the opposite color. If already colored the
SAME color as current node, return False.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""

from collections import deque


def solve(n: int, edges: list[list[int]]) -> bool:
    """Return True if the graph is bipartite."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    print(solve(n, edges))
