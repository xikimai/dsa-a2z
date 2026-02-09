"""
Solution for Warmup 3: House Robber on Tree
=============================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Tree DP. For each node: dp[u][0] = max if u NOT robbed,
dp[u][1] = max if u IS robbed. Process leaves to root.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, values: list[int], edges: list[list[int]]) -> int:
    """Return max sum of non-adjacent nodes in the tree."""
    if n == 0:
        return 0
    if n == 1:
        return values[0]

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0, 0] for _ in range(n)]

    # Iterative BFS to get processing order
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

    # Process in reverse order (leaves first)
    for u in reversed(order):
        dp[u][1] = values[u]
        for v in adj[u]:
            if v == parent[u]:
                continue
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

    return max(dp[0][0], dp[0][1])


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    values = []
    for _ in range(n):
        values.append(int(tokens[idx])); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    print(solve(n, values, edges))
