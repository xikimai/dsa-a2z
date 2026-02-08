"""
Example 02: BFS vs DFS — Two Ways to Explore a Graph
=====================================================
Chapter 19: Graphs I — Exploring Networks

This example demonstrates:
  - Part 1: BFS traversal with step-by-step visualization
  - Part 2: DFS traversal with step-by-step visualization
  - Part 3: BFS finds shortest paths; DFS does NOT
  - Part 4: Connected components using BFS/DFS
"""

from collections import deque


# ── Part 1: BFS Step-by-Step ─────────────────────────────────────

def part1_bfs_demo():
    """BFS with detailed step-by-step output."""
    print("=" * 60)
    print("PART 1: BFS Traversal (Level by Level)")
    print("=" * 60)

    # Graph:
    #   0 --- 1
    #   |     |
    #   2 --- 3
    #         |
    #         4
    adj = [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3]]
    source = 0

    print(f"  Graph adjacency list:")
    for i, neighbors in enumerate(adj):
        print(f"    {i}: {neighbors}")
    print(f"  Starting BFS from node {source}\n")

    visited = [False] * len(adj)
    visited[source] = True
    queue = deque([source])
    order = []
    step = 0

    while queue:
        step += 1
        node = queue.popleft()
        order.append(node)
        new_neighbors = []
        for neighbor in sorted(adj[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                new_neighbors.append(neighbor)

        print(f"  Step {step}: Dequeue {node}, "
              f"enqueue {new_neighbors if new_neighbors else '(none)'}, "
              f"queue = {list(queue)}")

    print(f"\n  BFS order: {order}")
    print(f"  Notice: visits level-by-level (0 -> 1,2 -> 3 -> 4)")


# ── Part 2: DFS Step-by-Step ─────────────────────────────────────

def part2_dfs_demo():
    """DFS with detailed step-by-step output."""
    print("\n" + "=" * 60)
    print("PART 2: DFS Traversal (Go Deep First)")
    print("=" * 60)

    adj = [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3]]
    source = 0

    print(f"  Graph adjacency list:")
    for i, neighbors in enumerate(adj):
        print(f"    {i}: {neighbors}")
    print(f"  Starting DFS from node {source}\n")

    visited = [False] * len(adj)
    order = []
    call_depth = [0]  # track recursion depth for visualization

    def _dfs(node):
        visited[node] = True
        order.append(node)
        indent = "    " * call_depth[0]
        print(f"  {indent}Visit {node} (depth {call_depth[0]})")

        for neighbor in sorted(adj[node]):
            if not visited[neighbor]:
                call_depth[0] += 1
                _dfs(neighbor)
                call_depth[0] -= 1

        if all(visited[nb] for nb in adj[node]):
            indent = "    " * call_depth[0]
            print(f"  {indent}  -> Backtrack from {node}")

    _dfs(source)
    print(f"\n  DFS order: {order}")
    print(f"  Notice: dives deep (0 -> 1 -> 3 -> 2 -> backtrack -> 4)")


# ── Part 3: Shortest Paths ──────────────────────────────────────

def part3_shortest_paths():
    """Show that BFS finds shortest paths but DFS does not."""
    print("\n" + "=" * 60)
    print("PART 3: BFS Finds Shortest Paths, DFS Does NOT")
    print("=" * 60)

    # Graph:
    #   0 --- 1
    #   |     |
    #   2 --- 3
    adj = [[1, 2], [0, 3], [0, 3], [1, 2]]
    source = 0

    print(f"  Graph:")
    print(f"    0 --- 1")
    print(f"    |     |")
    print(f"    2 --- 3")
    print(f"  Source: {source}\n")

    # BFS distances
    dist_bfs = [-1] * len(adj)
    dist_bfs[source] = 0
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist_bfs[neighbor] == -1:
                dist_bfs[neighbor] = dist_bfs[node] + 1
                queue.append(neighbor)

    print(f"  BFS distances from {source}: {dist_bfs}")
    print(f"    Node 0: distance {dist_bfs[0]}")
    print(f"    Node 1: distance {dist_bfs[1]}")
    print(f"    Node 2: distance {dist_bfs[2]}")
    print(f"    Node 3: distance {dist_bfs[3]}")

    # DFS "distances" (NOT shortest!)
    dist_dfs = [-1] * len(adj)
    dist_dfs[source] = 0
    visited = [False] * len(adj)

    def _dfs(node, depth):
        visited[node] = True
        dist_dfs[node] = depth
        for neighbor in sorted(adj[node]):
            if not visited[neighbor]:
                _dfs(neighbor, depth + 1)

    _dfs(source, 0)

    print(f"\n  DFS 'distances' from {source}: {dist_dfs}")
    print(f"    Node 0: distance {dist_dfs[0]}")
    print(f"    Node 1: distance {dist_dfs[1]}")
    print(f"    Node 2: distance {dist_dfs[2]}  <- WRONG! Should be 1, got {dist_dfs[2]}")
    print(f"    Node 3: distance {dist_dfs[3]}")

    print(f"\n  DFS went 0->1->3->2 (distance 3 to node 2)")
    print(f"  But the shortest path 0->2 is just 1 step!")
    print(f"  LESSON: NEVER use DFS for shortest paths!")


# ── Part 4: Connected Components ─────────────────────────────────

def part4_components():
    """Find connected components."""
    print("\n" + "=" * 60)
    print("PART 4: Connected Components")
    print("=" * 60)

    # Graph with 3 components:
    #   0 --- 1     3 --- 4
    #   |           |
    #   2           5     6
    n = 7
    adj = [
        [1, 2],  # 0
        [0],     # 1
        [0],     # 2
        [4, 5],  # 3
        [3],     # 4
        [3],     # 5
        [],      # 6
    ]

    print(f"  Graph with {n} nodes:")
    print(f"    0 --- 1     3 --- 4")
    print(f"    |           |")
    print(f"    2           5     6\n")

    visited = [False] * n
    components = []

    for v in range(n):
        if not visited[v]:
            # BFS to find all nodes in this component
            component = []
            queue = deque([v])
            visited[v] = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            components.append(component)

    print(f"  Found {len(components)} connected components:")
    for i, comp in enumerate(components):
        print(f"    Component {i + 1}: {comp}")

    print(f"\n  Algorithm: loop through all nodes, BFS from each unvisited node.")
    print(f"  Each BFS discovers one full component.")


# ── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_bfs_demo()
    part2_dfs_demo()
    part3_shortest_paths()
    part4_components()
