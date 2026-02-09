"""
Solution for Challenge 3: Largest Color Value in Directed Graph
================================================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
Kahn's BFS + DP. For each node, maintain dp[node][c] = max count
of color c on any path ending at node. Process in topological order,
propagating color counts.

TIME COMPLEXITY:  O((V + E) * 26)
SPACE COMPLEXITY: O(V * 26)
"""

from collections import deque, defaultdict


def solve(colors: str, edges: list[list[int]]) -> int:
    """Return max color frequency on any path, or -1 if cycle."""
    n = len(colors)
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # dp[i][c] = max frequency of color c on any path ending at node i
    dp = [[0] * 26 for _ in range(n)]

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    count = 0
    result = 0
    while queue:
        u = queue.popleft()
        count += 1
        # Include current node's color
        dp[u][ord(colors[u]) - ord('a')] += 1
        result = max(result, max(dp[u]))
        for v in adj[u]:
            # Propagate: for each color, v gets max of its current and u's value
            for c in range(26):
                dp[v][c] = max(dp[v][c], dp[u][c])
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result if count == n else -1


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    colors = tokens[0]
    m = int(tokens[1])
    idx = 2
    edges = []
    for _ in range(m):
        u = int(tokens[idx]); idx += 1
        v = int(tokens[idx]); idx += 1
        edges.append([u, v])
    print(solve(colors, edges))
