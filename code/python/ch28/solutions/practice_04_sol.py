"""
Solution for Practice 4: All Ancestors of a Node
==================================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
For each node, run DFS/BFS in the original graph and mark all
reachable nodes as descendants. Equivalently, iterate over each
node u and DFS forward, adding u to each reachable node's ancestor set.

TIME COMPLEXITY:  O(n * (V + E))
SPACE COMPLEXITY: O(n^2) for the ancestor lists
"""


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return sorted ancestors for each node."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    ancestors = [set() for _ in range(n)]

    # For each node u, DFS forward and add u as ancestor of every reachable node
    for u in range(n):
        stack = [u]
        visited = set()
        while stack:
            node = stack.pop()
            for v in adj[node]:
                if v not in visited:
                    visited.add(v)
                    ancestors[v].add(u)
                    stack.append(v)

    return [sorted(anc) for anc in ancestors]


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
    result = solve(n, edges)
    for row in result:
        print(row)
