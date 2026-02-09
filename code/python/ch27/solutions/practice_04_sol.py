"""
Solution for Practice 4: Number of Ways to Arrive at Destination
=================================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Dijkstra + counting. Maintain ways[v] alongside dist[v].
When dist improves, reset ways. When dist equals, add ways.

TIME COMPLEXITY:  O((V + E) log V)
SPACE COMPLEXITY: O(V + E)
"""

import heapq


def solve(n: int, roads: list[list[int]]) -> int:
    """Return number of shortest paths from 0 to n-1, mod 10^9+7."""
    MOD = 10**9 + 7
    INF = 10**18
    adj = [[] for _ in range(n)]
    for u, v, t in roads:
        adj[u].append((v, t))
        adj[v].append((u, t))

    dist = [INF] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    heap = [(0, 0)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                ways[v] = ways[u]
                heapq.heappush(heap, (new_dist, v))
            elif new_dist == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD

    return ways[n - 1] % MOD


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    roads = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        roads.append([u, v, w])
    print(solve(n, roads))
