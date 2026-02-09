"""
Example 02: DFS-Based Topological Sort with Cycle Detection
=============================================================
Chapter 28: Topological Sort — Ordering Dependencies

This example demonstrates:
  - DFS topological sort (reverse post-order)
  - Three-color cycle detection (white/gray/black)
  - Why simple visited is insufficient for directed graphs
"""


# ── DFS Topological Sort ─────────────────────────────────────

def dfs_topo_sort(n, edges):
    """DFS-based topological sort with three-color cycle detection.

    Colors: 0=white (unvisited), 1=gray (in progress), 2=black (done).
    A back edge to a gray node means a cycle exists.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    color = [0] * n
    stack = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        if has_cycle:
            return
        color[u] = 1  # gray
        for v in adj[u]:
            if color[v] == 1:
                has_cycle = True
                return
            if color[v] == 0:
                dfs(v)
        color[u] = 2  # black
        stack.append(u)

    for i in range(n):
        if color[i] == 0:
            dfs(i)

    if has_cycle:
        return []
    return stack[::-1]


# ── Verbose version ──────────────────────────────────────────

def dfs_topo_verbose(n, edges):
    """Same algorithm with step-by-step output."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    color_names = {0: "WHITE", 1: "GRAY", 2: "BLACK"}
    color = [0] * n
    stack = []
    has_cycle = False

    def dfs(u, depth=0):
        nonlocal has_cycle
        if has_cycle:
            return
        indent = "    " * depth
        color[u] = 1
        print(f"{indent}Visit {u} (now GRAY)")
        for v in adj[u]:
            if color[v] == 1:
                print(f"{indent}  -> {v} is GRAY = CYCLE DETECTED!")
                has_cycle = True
                return
            if color[v] == 2:
                print(f"{indent}  -> {v} is BLACK (already done, skip)")
            if color[v] == 0:
                dfs(v, depth + 1)
        if not has_cycle:
            color[u] = 2
            stack.append(u)
            print(f"{indent}Finish {u} (now BLACK, push to stack)")

    for i in range(n):
        if color[i] == 0:
            print(f"  Starting DFS from node {i}")
            dfs(i)

    if has_cycle:
        print("  CYCLE exists — no valid topological ordering!")
        return []
    result = stack[::-1]
    print(f"  Stack (finish order): {stack}")
    print(f"  Reversed = topological order: {result}")
    return result


# ── Demo ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("DFS TOPOLOGICAL SORT: Three-Color Cycle Detection")
    print("=" * 60)

    # Example 1: Valid DAG
    print("\nExample 1: DAG")
    print("  Edges: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1")
    edges1 = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    dfs_topo_verbose(6, edges1)
    print()

    # Example 2: Cycle
    print("Example 2: Graph with cycle")
    print("  Edges: 0->1, 1->2, 2->0")
    edges2 = [[0, 1], [1, 2], [2, 0]]
    dfs_topo_verbose(3, edges2)
    print()

    # Why three colors matter
    print("=" * 60)
    print("WHY THREE COLORS? (not just visited/unvisited)")
    print("=" * 60)
    print("  In UNDIRECTED graphs, revisiting any visited node means a cycle.")
    print("  In DIRECTED graphs, that is NOT true!")
    print("  Consider: A->C, B->C. DFS from A visits C (done). DFS from B")
    print("  visits C again — but this is NOT a cycle! C is BLACK (finished).")
    print("  Only visiting a GRAY node (still being processed) means a cycle.")
    print("  That is why we need WHITE/GRAY/BLACK, not just visited/unvisited.")
