"""
Solution for Challenge 2: Reorder Routes to City Zero
=======================================================
Chapter 33: Advanced Trees & Graph Algorithms

APPROACH
--------
Build undirected adjacency list but track which edges are original (away from 0)
vs reversed (toward 0). BFS/DFS from node 0. For each edge traversed from 0
outward, if it was an original directed edge (pointing away from 0), it needs
to be reversed.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""

from collections import deque


def solve(n: int, connections: list[list[int]]) -> int:
    """Return the number of roads to reverse so all cities can reach city 0."""
    # Build adjacency list: (neighbor, cost)
    # cost=1 if edge goes away from 0 (needs reversal), 0 if toward 0
    adj = [[] for _ in range(n)]
    for u, v in connections:
        adj[u].append((v, 1))  # original direction u->v
        adj[v].append((u, 0))  # reverse direction (already toward v)

    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    count = 0

    while queue:
        node = queue.popleft()
        for nb, cost in adj[node]:
            if not visited[nb]:
                visited[nb] = True
                count += cost
                queue.append(nb)

    return count


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
