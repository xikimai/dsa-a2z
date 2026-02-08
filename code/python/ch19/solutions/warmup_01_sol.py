"""
Solution for Warmup 1: Build Adjacency List
=============================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Create a list of n empty lists. For each edge (u, v), add v to adj[u]
and u to adj[v]. Sort each neighbor list at the end.

TIME COMPLEXITY:  O(V + E log E) — building + sorting neighbors
SPACE COMPLEXITY: O(V + E)
"""


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return adjacency list as list of lists (sorted neighbors)."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for i in range(n):
        adj[i].sort()
    return adj


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    adj = solve(n, edges)
    for i in range(n):
        print(f"{i}: {adj[i]}")
