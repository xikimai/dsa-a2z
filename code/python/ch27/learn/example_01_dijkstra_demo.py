"""
Example 01: Dijkstra's Algorithm — Step-by-Step Demo
=====================================================
Chapter 27: Shortest Paths — Finding the Best Route

This example demonstrates Dijkstra's SSSP algorithm through
three levels of detail:
  - Step-by-step with print statements
  - Clean implementation with a min-heap
  - Path reconstruction (not just distances)
"""

import heapq


# ── Dijkstra: Step-by-Step (verbose) ─────────────────────────────

def dijkstra_verbose(n, edges, src):
    """Dijkstra with print statements showing each step."""
    INF = 10**9
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]
    processed = set()

    print(f"  Initial: dist = {dist}")
    step = 0

    while heap:
        d, u = heapq.heappop(heap)
        if u in processed:
            print(f"  Skip stale entry for node {u} (d={d}, actual={dist[u]})")
            continue
        processed.add(u)
        step += 1
        print(f"\n  Step {step}: Process node {u} (distance = {d})")

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                old = dist[v]
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
                print(f"    Relax edge {u}→{v} (weight {w}): "
                      f"dist[{v}] = {old} → {dist[v]}")

    return dist


# ── Dijkstra: Clean Implementation ──────────────────────────────

def dijkstra(n, edges, src):
    """Standard Dijkstra. O((V+E) log V)."""
    INF = 10**9
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


# ── Dijkstra with Path Reconstruction ───────────────────────────

def dijkstra_with_path(n, edges, src, dst):
    """Returns (distance, path) from src to dst."""
    INF = 10**9
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [INF] * n
    dist[src] = 0
    parent = [-1] * n
    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[dst] == INF:
        return INF, []

    # Reconstruct path
    path = []
    node = dst
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    return dist[dst], path


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 5],
             [2, 3, 8], [3, 4, 1]]

    print("=" * 60)
    print("DIJKSTRA'S ALGORITHM: Step-by-Step")
    print("=" * 60)
    print(f"  Graph: 5 nodes, edges = {edges}")
    print(f"  Source: 0\n")

    dist = dijkstra_verbose(5, edges, 0)
    print(f"\n  Final distances: {dist}")
    assert dist == [0, 3, 1, 8, 9]

    print("\n" + "=" * 60)
    print("DIJKSTRA WITH PATH RECONSTRUCTION")
    print("=" * 60)
    for dst in range(5):
        d, path = dijkstra_with_path(5, edges, 0, dst)
        print(f"  0 → {dst}: distance = {d}, path = {' → '.join(map(str, path))}")

    # Why Dijkstra fails on negative weights
    print("\n" + "=" * 60)
    print("WHY DIJKSTRA FAILS ON NEGATIVE WEIGHTS")
    print("=" * 60)
    print("  Consider: A→B cost 4, B→C cost -2, A→C cost 3")
    print("  Dijkstra pops A (d=0), relaxes B to 4 and C to 3.")
    print("  Dijkstra pops C (d=3) — FINALIZED as shortest.")
    print("  But A→B→C = 4 + (-2) = 2 < 3! Dijkstra missed it.")
    print("  Lesson: Use Bellman-Ford when negative weights exist.")
