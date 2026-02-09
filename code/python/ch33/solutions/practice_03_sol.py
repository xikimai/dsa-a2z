"""
Solution for Practice 3: Subtree Sum (Euler Tour + Array)
==========================================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
1. Euler Tour to get tin/tout for each node.
2. Build flat array in Euler tour order with node values.
3. Build prefix sums on this array.
4. Subtree sum of v = prefix[tout[v]+1] - prefix[tin[v]].

TIME COMPLEXITY:  O(n + q)
SPACE COMPLEXITY: O(n)
"""

import sys
sys.setrecursionlimit(200000)


def solve(n: int, values: list[int], edges: list[list[int]], queries: list[int]) -> list[int]:
    """Return the subtree sum for each query node."""
    if n == 1:
        return [values[0]] * len(queries)

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    tin = [0] * n
    tout = [0] * n
    order = []
    timer = [0]

    def dfs(node, parent):
        tin[node] = timer[0]
        order.append(node)
        timer[0] += 1
        for nb in adj[node]:
            if nb != parent:
                dfs(nb, node)
        tout[node] = timer[0] - 1

    dfs(0, -1)

    # Build prefix sums in Euler tour order
    flat = [values[order[i]] for i in range(n)]
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + flat[i]

    result = []
    for q in queries:
        subtree_sum = prefix[tout[q] + 1] - prefix[tin[q]]
        result.append(subtree_sum)

    return result


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    vals = []
    for _ in range(n):
        vals.append(int(tokens[idx])); idx += 1
    m = int(tokens[idx]); idx += 1
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    q = int(tokens[idx]); idx += 1
    queries = []
    for _ in range(q):
        queries.append(int(tokens[idx])); idx += 1
    result = solve(n, vals, edges, queries)
    print(" ".join(map(str, result)))
