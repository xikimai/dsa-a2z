"""
Solution for Challenge 1: Operations to Make Network Connected
===============================================================
Chapter 29: Union-Find & Minimum Spanning Trees

APPROACH
--------
Count connected components and redundant edges (edges within same component).
Need (components - 1) cables to connect all. If redundant >= components - 1,
return components - 1. Otherwise return -1.

Equivalently: need n-1 edges total. If len(connections) < n-1, return -1.
Otherwise count components and return components - 1.

TIME COMPLEXITY:  O(E * alpha(n))
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, connections: list[list[int]]) -> int:
    """Return min cables to move to connect all computers, or -1 if impossible."""
    if len(connections) < n - 1:
        return -1

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
    for u, v in connections:
        if union(u, v):
            components -= 1

    return components - 1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    connections = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        connections.append([u, v])
    print(solve(n, connections))
