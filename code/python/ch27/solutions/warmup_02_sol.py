"""
Solution for Warmup 2: Network Delay Time
==========================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Dijkstra from node k (1-indexed). Answer is max of all distances.
If any node is unreachable (dist == INF), return -1.

TIME COMPLEXITY:  O((V + E) log V)
SPACE COMPLEXITY: O(V + E)
"""

import heapq


def solve(times: list[list[int]], n: int, k: int) -> int:
    """Return the minimum time for all nodes to receive the signal."""
    INF = 10**9
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append((v, w))

    dist = [INF] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    ans = max(dist[1:])
    return ans if ans < INF else -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    m = int(data[idx]); idx += 1
    times = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        times.append([u, v, w])
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    print(solve(times, n, k))
