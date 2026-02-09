"""
Solution for Warmup 2: Redundant Connection
=============================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Process edges in order. The first edge where both endpoints are already
connected (find(u) == find(v)) is the redundant edge.
NOTE: Nodes are 1-indexed, so Union-Find uses size n+1.

TIME COMPLEXITY:  O(n * alpha(n))
SPACE COMPLEXITY: O(n)
"""


def solve(edges: list[list[int]]) -> list[int]:
    """Return the redundant edge [u, v] that creates a cycle."""
    n = len(edges)
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

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

    for u, v in edges:
        if not union(u, v):
            return [u, v]
    return []


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    result = solve(edges)
    print(result[0], result[1])
