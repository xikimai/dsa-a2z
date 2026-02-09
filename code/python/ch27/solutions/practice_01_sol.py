"""
Solution for Practice 1: Cheapest Flights Within K Stops
=========================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
Modified Bellman-Ford with at most k+1 relaxation rounds.
Use a copy of dist each round to prevent cascading updates within the same round.

TIME COMPLEXITY:  O(k * E)
SPACE COMPLEXITY: O(V)
"""


def solve(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    """Return cheapest price from src to dst with at most k stops."""
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0

    for _ in range(k + 1):
        prev = dist[:]
        for u, v, w in flights:
            if prev[u] != INF and prev[u] + w < dist[v]:
                dist[v] = prev[u] + w

    return dist[dst] if dist[dst] < INF else -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    flights = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        flights.append([u, v, w])
    src = int(data[idx]); idx += 1
    dst = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    print(solve(n, flights, src, dst, k))
