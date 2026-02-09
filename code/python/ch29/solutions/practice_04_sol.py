"""
Solution for Practice 4: Min Cost to Connect All Points
========================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Generate all pairwise edges with Manhattan distance, then run Kruskal's MST.

TIME COMPLEXITY:  O(n^2 log n)
SPACE COMPLEXITY: O(n^2) for edges
"""


def solve(points: list[list[int]]) -> int:
    """Return the minimum cost to connect all points (MST of Manhattan distances)."""
    n = len(points)
    if n <= 1:
        return 0

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    # Generate all edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))

    edges.sort()
    total = 0
    count = 0
    for w, u, v in edges:
        if union(u, v):
            total += w
            count += 1
            if count == n - 1:
                break
    return total


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    points = []
    for _ in range(n):
        x = int(tokens[idx]); idx += 1
        y = int(tokens[idx]); idx += 1
        points.append([x, y])
    print(solve(points))
