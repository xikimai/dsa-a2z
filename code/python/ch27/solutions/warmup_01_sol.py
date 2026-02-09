"""
Solution for Warmup 1: Dijkstra SSSP
======================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Standard Dijkstra with min-heap. Build adjacency list, relax neighbors.

TIME COMPLEXITY:  O((V + E) log V)
SPACE COMPLEXITY: O(V + E)
"""

import heapq


def solve(n: int, edges: list[list[int]], src: int) -> list[int]:
    """Return shortest distances from src to all nodes."""
    INF = 10**9
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        w = int(input_data[idx]); idx += 1
        edges.append([u, v, w])
    src = int(input_data[idx]); idx += 1
    print(solve(n, edges, src))
