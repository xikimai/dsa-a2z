"""
Solution for Practice 4: Tree Diameter via DP
==============================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Tree DP. For each node, compute the longest downward path. The diameter
through a node is the sum of the two longest downward paths from it.
The overall diameter is the max across all nodes.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return the diameter of the tree."""
    if n <= 1:
        return 0

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # depth[u] = longest path going DOWN from u
    depth = [0] * n
    diameter = 0

    visited = [False] * n
    parent = [-1] * n
    order = []
    stack = [0]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                stack.append(v)

    # Process leaves first
    for u in reversed(order):
        top1 = 0  # longest child depth
        top2 = 0  # second longest
        for v in adj[u]:
            if v == parent[u]:
                continue
            d = depth[v] + 1
            if d >= top1:
                top2 = top1
                top1 = d
            elif d > top2:
                top2 = d
        depth[u] = top1
        diameter = max(diameter, top1 + top2)

    return diameter


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
