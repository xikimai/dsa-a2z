"""
Solution for Warmup 3: Kruskal's MST
======================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Sort edges by weight, greedily add edges that connect different components.

TIME COMPLEXITY:  O(E log E)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the total MST weight using Kruskal's algorithm."""
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

    edges.sort(key=lambda e: e[2])
    total = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
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
