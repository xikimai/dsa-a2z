"""
Solution for Warmup 1: Connected Components (Union-Find)
=========================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Union-Find: start with n components, merge for each edge, count remaining.

TIME COMPLEXITY:  O(n + E * alpha(n))
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the number of connected components in an undirected graph."""
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

    components = n
    for u, v in edges:
        if union(u, v):
            components -= 1
    return components


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
        edges.append([u, v])
    print(solve(n, edges))
