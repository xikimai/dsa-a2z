"""
Solution for Practice 5: All Paths from Source to Target
=========================================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Build directed adjacency list. DFS backtracking from node 0.
Maintain a current path. When we reach node n-1, save a copy.
Sort the result lexicographically.

TIME COMPLEXITY:  O(2^n * n) — up to 2^n paths, each of length up to n
SPACE COMPLEXITY: O(2^n * n) — storing all paths
"""


def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """Return all paths from node 0 to node n-1, sorted."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)  # directed!

    result = []
    path = [0]

    def _dfs(node):
        if node == n - 1:
            result.append(list(path))
            return
        for neighbor in sorted(adj[node]):
            path.append(neighbor)
            _dfs(neighbor)
            path.pop()

    _dfs(0)
    result.sort()
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().strip().split())
        edges.append([u, v])
    paths = solve(n, edges)
    for path in paths:
        print(" -> ".join(map(str, path)))
