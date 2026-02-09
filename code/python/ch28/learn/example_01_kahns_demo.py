"""
Example 01: Kahn's Algorithm Demo — BFS Topological Sort
=========================================================
Chapter 28: Topological Sort — Ordering Dependencies

This example demonstrates Kahn's Algorithm step-by-step:
  - Build adjacency list and in-degree array
  - Process zero-indegree nodes via BFS
  - Detect cycles (unprocessed nodes)
"""

from collections import deque, defaultdict


# ── Kahn's Algorithm ─────────────────────────────────────────

def kahns_topo_sort(n, edges):
    """BFS-based topological sort using in-degree tracking.

    Args:
        n: number of nodes (0 to n-1)
        edges: list of [u, v] meaning u must come before v

    Returns:
        list of nodes in topological order, or [] if cycle exists
    """
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result if len(result) == n else []


# ── Step-by-step visualization ────────────────────────────────

def kahns_verbose(n, edges):
    """Same algorithm but prints each step for learning."""
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    print(f"  Initial in-degrees: {in_degree}")

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    print(f"  Zero-indegree nodes (starting queue): {list(queue)}")

    result = []
    step = 1
    while queue:
        u = queue.popleft()
        result.append(u)
        print(f"  Step {step}: Process node {u}")
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                print(f"    Node {v} now has in-degree 0 — added to queue")
        step += 1

    if len(result) == n:
        print(f"  Result: {result} (all {n} nodes processed — valid DAG!)")
    else:
        print(f"  Only {len(result)} of {n} nodes processed — CYCLE detected!")
    return result if len(result) == n else []


# ── Demo ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("KAHN'S ALGORITHM: BFS Topological Sort")
    print("=" * 60)

    # Example 1: DAG with valid ordering
    print("\nExample 1: Course prerequisites (DAG)")
    print("  Edges: 5->2, 5->0, 4->0, 4->1, 2->3, 3->1")
    edges1 = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    result1 = kahns_verbose(6, edges1)
    print()

    # Example 2: Graph with a cycle
    print("Example 2: Circular dependency (CYCLE)")
    print("  Edges: 0->1, 1->2, 2->0")
    edges2 = [[0, 1], [1, 2], [2, 0]]
    result2 = kahns_verbose(3, edges2)
    print()

    # Example 3: Linear chain
    print("Example 3: Linear chain (unique ordering)")
    print("  Edges: 0->1, 1->2, 2->3")
    edges3 = [[0, 1], [1, 2], [2, 3]]
    result3 = kahns_verbose(4, edges3)
    assert result3 == [0, 1, 2, 3], "Linear chain must give unique order"
    print()

    print("Key insight: Kahn's removes nodes with no remaining dependencies.")
    print("If some nodes can never reach in-degree 0, they are in a cycle.")
