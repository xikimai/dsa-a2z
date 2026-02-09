"""
Example 02: Bellman-Ford Algorithm — Handling Negative Weights
==============================================================
Chapter 27: Shortest Paths — Finding the Best Route

This example demonstrates:
  - Bellman-Ford step-by-step with negative edges
  - Negative cycle detection
  - Comparison with Dijkstra on negative-weight graphs
"""


# ── Bellman-Ford: Step-by-Step ───────────────────────────────────

def bellman_ford_verbose(n, edges, src):
    """Bellman-Ford with step-by-step prints."""
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0

    print(f"  Initial: dist = {dist}")

    for round_num in range(1, n):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                old = dist[v]
                dist[v] = dist[u] + w
                updated = True
                print(f"  Round {round_num}: Relax {u}→{v} (w={w}): "
                      f"dist[{v}] = {old} → {dist[v]}")
        if not updated:
            print(f"  Round {round_num}: No updates — early stop!")
            break

    # Negative cycle check
    print("\n  Negative cycle check (round V):")
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            print(f"    NEGATIVE CYCLE DETECTED via edge {u}→{v}")
            return None
    print("    No negative cycle found.")

    return dist


# ── Bellman-Ford: Clean Implementation ───────────────────────────

def bellman_ford(n, edges, src):
    """Standard Bellman-Ford. O(V * E)."""
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative cycle detection
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None  # negative cycle

    return dist


# ── Demo ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Example with negative weights (no negative cycle)
    edges = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2],
             [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]]

    print("=" * 60)
    print("BELLMAN-FORD: Negative Weights (No Cycle)")
    print("=" * 60)
    print(f"  Graph: 5 nodes, edges = {edges}")
    print(f"  Source: 0\n")

    dist = bellman_ford_verbose(5, edges, 0)
    print(f"\n  Final distances: {dist}")
    assert dist == [0, -1, 2, -2, 1]

    # Example WITH a negative cycle
    print("\n" + "=" * 60)
    print("BELLMAN-FORD: Negative Cycle Detection")
    print("=" * 60)
    cycle_edges = [[0, 1, 1], [1, 2, -1], [2, 0, -1]]
    print(f"  Graph: 3 nodes, edges = {cycle_edges}")
    print(f"  Cycle: 0→1→2→0 has total weight 1+(-1)+(-1) = -1")
    print(f"  Source: 0\n")

    result = bellman_ford_verbose(3, cycle_edges, 0)
    if result is None:
        print("\n  Result: Negative cycle detected! No shortest paths exist.")
    else:
        print(f"\n  Result: {result}")

    # Comparison: Dijkstra vs Bellman-Ford on negative weights
    print("\n" + "=" * 60)
    print("DIJKSTRA vs BELLMAN-FORD")
    print("=" * 60)
    print("  Dijkstra:     O((V+E) log V) — FAST but NO negative weights")
    print("  Bellman-Ford: O(V * E)       — SLOWER but handles negatives")
    print("  Rule: If all weights >= 0, use Dijkstra. Otherwise, Bellman-Ford.")
