"""
Solution for Warmup 2: Euler Tour of Tree
==========================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
DFS from root (node 0). Record each node when first entered.
Use iterative DFS to avoid recursion limit issues.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return the Euler tour order (DFS entry order) of the tree."""
    if n == 1:
        return [0]

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Sort adjacency lists so DFS visits smaller-numbered children first
    for i in range(n):
        adj[i].sort()

    order = []
    visited = [False] * n

    # Iterative DFS
    stack = [0]
    visited[0] = True
    while stack:
        node = stack.pop()
        order.append(node)
        # Push children in reverse sorted order so smallest is processed first
        for nb in reversed(adj[node]):
            if not visited[nb]:
                visited[nb] = True
                stack.append(nb)

    return order


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    result = solve(n, edges)
    print(" ".join(map(str, result)))
