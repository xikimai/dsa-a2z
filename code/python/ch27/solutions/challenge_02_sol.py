"""
Solution for Challenge 2: Shortest Path with Alternating Colors
================================================================
Chapter 27: Shortest Paths — Finding the Best Route

APPROACH
--------
BFS with state = (node, last_color). 0 = red, 1 = blue.
Start BFS from (0, -1) to allow first edge to be either color.
Track dist for each (node, color) state.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V)
"""

from collections import deque


def solve(n: int, red_edges: list[list[int]], blue_edges: list[list[int]]) -> list[int]:
    """Return shortest alternating-color path distances from node 0."""
    # Build adjacency list: adj[node][color] = [neighbors]
    # color 0 = red, color 1 = blue
    adj = [[[] for _ in range(2)] for _ in range(n)]
    for u, v in red_edges:
        adj[u][0].append(v)
    for u, v in blue_edges:
        adj[u][1].append(v)

    INF = 10**9
    # dist[node][color] = shortest distance to node ending with color
    dist = [[INF, INF] for _ in range(n)]
    dist[0][0] = 0
    dist[0][1] = 0

    # BFS: (node, last_color_used)
    q = deque([(0, 0), (0, 1)])  # start with both colors

    while q:
        u, color = q.popleft()
        next_color = 1 - color  # alternate
        for v in adj[u][next_color]:
            if dist[u][color] + 1 < dist[v][next_color]:
                dist[v][next_color] = dist[u][color] + 1
                q.append((v, next_color))

    result = []
    for i in range(n):
        best = min(dist[i][0], dist[i][1])
        result.append(best if best < INF else -1)
    return result


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys, json
    data = sys.stdin.read().strip().split('\n')
    n = int(data[0])
    red_edges = json.loads(data[1])
    blue_edges = json.loads(data[2])
    print(solve(n, red_edges, blue_edges))
