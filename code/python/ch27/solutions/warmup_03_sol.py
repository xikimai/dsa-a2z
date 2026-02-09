"""
Solution for Warmup 3: Bellman-Ford SSSP
=========================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Standard Bellman-Ford: relax all edges n-1 times.

TIME COMPLEXITY:  O(V * E)
SPACE COMPLEXITY: O(V)
"""


def solve(n: int, edges: list[list[int]], src: int) -> list[int]:
    """Return shortest distances from src to all nodes (Bellman-Ford)."""
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        edges.append([u, v, w])
    src = int(data[idx]); idx += 1
    print(solve(n, edges, src))
