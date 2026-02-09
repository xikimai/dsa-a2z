"""
Solution for Practice 3: Find City with Smallest Neighbors at Threshold
========================================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Floyd-Warshall for all-pairs shortest paths (bidirectional edges).
Then for each city, count how many other cities are within threshold.
Return city with smallest count (largest index if tie).

TIME COMPLEXITY:  O(V^3)
SPACE COMPLEXITY: O(V^2)
"""


def solve(n: int, edges: list[list[int]], threshold: int) -> int:
    """Return the city with smallest neighbors at threshold distance."""
    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    best_city = -1
    best_count = n + 1
    for i in range(n):
        count = sum(1 for j in range(n) if j != i and dist[i][j] <= threshold)
        if count <= best_count:
            best_count = count
            best_city = i

    return best_city


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
    threshold = int(data[idx]); idx += 1
    print(solve(n, edges, threshold))
