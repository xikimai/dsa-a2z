"""
Solution for Warmup 4: Prim's MST
===================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Build adjacency list, use min-heap to greedily pick cheapest edge to unvisited vertex.

TIME COMPLEXITY:  O(E log V)
SPACE COMPLEXITY: O(V + E)
"""

import heapq


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the total MST weight using Prim's algorithm."""
    if n <= 1:
        return 0

    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = [False] * n
    heap = [(0, 0)]
    total = 0
    count = 0

    while heap and count < n:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        count += 1
        for nw, nv in adj[u]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv))

    return total


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        w = int(tokens[idx]); idx += 1
        edges.append([u, v, w])
    print(solve(n, edges))
