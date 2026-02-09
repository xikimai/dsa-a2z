"""
Solution for Challenge 3: Binary Tree Cameras
===============================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Tree DP with 3 states per node:
- state 0: node is NOT monitored (needs parent to place camera or be covered)
- state 1: node is monitored by a child (no camera here)
- state 2: node has a camera (monitors self, parent, children)

dp[u][0] = min cameras in subtree if u is not covered
dp[u][1] = min cameras in subtree if u is covered but has no camera
dp[u][2] = min cameras in subtree if u has a camera

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(n: int, edges: list[list[int]]) -> int:
    """Return minimum cameras to monitor all nodes."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    INF = float('inf')
    # dp[u] = [not_covered, covered_no_camera, has_camera]
    dp = [[0, 0, 0] for _ in range(n)]

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

    for u in reversed(order):
        children = [v for v in adj[u] if v != parent[u]]

        if not children:
            # Leaf node
            dp[u][0] = 0   # not covered, 0 cameras
            dp[u][1] = INF  # can't be covered without camera or parent
            dp[u][2] = 1   # place camera here
            continue

        # State 2: u has camera -> children can be in any state
        cam = 1
        for v in children:
            cam += min(dp[v][0], dp[v][1], dp[v][2])

        # State 0: u is not covered -> children must be covered (state 1 or 2)
        not_cov = 0
        for v in children:
            not_cov += min(dp[v][1], dp[v][2])

        # State 1: u is covered by a child -> at least one child has camera,
        # all children must be covered
        # All children must be in state 1 or 2 (covered).
        # At least one child must be in state 2 (has camera).
        base = 0
        for v in children:
            base += min(dp[v][1], dp[v][2])

        # Check if at least one child already chose state 2
        # If not, force the cheapest child to upgrade from state 1 to state 2
        cov = INF
        all_use_min = True
        for v in children:
            if dp[v][2] <= dp[v][1]:
                all_use_min = False
                break

        if not all_use_min:
            cov = base
        else:
            # All children prefer state 1. Force one to state 2.
            min_upgrade = INF
            for v in children:
                upgrade_cost = dp[v][2] - dp[v][1]
                min_upgrade = min(min_upgrade, upgrade_cost)
            cov = base + min_upgrade

        dp[u][0] = not_cov
        dp[u][1] = cov
        dp[u][2] = cam

    # Root must be covered: state 1 or state 2
    return min(dp[0][1], dp[0][2])


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
