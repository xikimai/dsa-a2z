"""
Solution for Challenge 1: Minimum Height Trees
================================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Iterative leaf removal (like Kahn's on undirected tree).
Remove all leaves (degree 1) simultaneously. Repeat until
1 or 2 nodes remain — those are the MHT roots.

TIME COMPLEXITY:  O(V)
SPACE COMPLEXITY: O(V)
"""

from collections import deque


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """Return list of root nodes that minimize tree height."""
    if n == 1:
        return [0]

    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # Start with all leaves
    leaves = deque()
    for i in range(n):
        if len(adj[i]) == 1:
            leaves.append(i)

    remaining = n
    while remaining > 2:
        new_leaves = deque()
        remaining -= len(leaves)
        while leaves:
            leaf = leaves.popleft()
            for neighbor in adj[leaf]:
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
        leaves = new_leaves

    return list(leaves)


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
