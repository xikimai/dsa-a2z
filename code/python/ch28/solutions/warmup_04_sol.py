"""
Solution for Warmup 4: Detect Cycle in Directed Graph
=======================================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Three-color DFS. WHITE=0, GRAY=1, BLACK=2.
If we visit a GRAY node, cycle exists. Return False.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""


def solve(n: int, edges: list[list[int]]) -> bool:
    """Return True if graph is a DAG (no cycle), False if cycle exists."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    color = [0] * n  # 0=white, 1=gray, 2=black

    def has_cycle(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and has_cycle(v):
                return True
        color[u] = 2
        return False

    for i in range(n):
        if color[i] == 0 and has_cycle(i):
            return False

    return True


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
