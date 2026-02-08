"""
Example 01: Graph Representations — Three Ways to Store a Graph
================================================================
Chapter 19: Graphs I — Exploring Networks

This example demonstrates:
  - Part 1: Building an adjacency list from an edge list
  - Part 2: Building an adjacency matrix from an edge list
  - Part 3: Comparing the three representations side by side
  - Part 4: Querying each representation (neighbors, edge existence)
"""


# ── Part 1: Adjacency List ───────────────────────────────────────

def part1_adjacency_list():
    """Build and display an adjacency list."""
    print("=" * 60)
    print("PART 1: Adjacency List")
    print("=" * 60)

    # Graph:
    #   0 --- 1
    #   |     |
    #   2 --- 3
    #         |
    #         4
    n = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

    print(f"  Vertices: {n}")
    print(f"  Edges: {edges}\n")

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        print(f"  Add edge ({u},{v}): adj[{u}].append({v}), adj[{v}].append({u})")

    print(f"\n  Final adjacency list:")
    for i in range(n):
        print(f"    {i}: {adj[i]}")

    print(f"\n  Space used: O(V + 2E) = O({n} + {2 * len(edges)}) = O({n + 2 * len(edges)})")


# ── Part 2: Adjacency Matrix ─────────────────────────────────────

def part2_adjacency_matrix():
    """Build and display an adjacency matrix."""
    print("\n" + "=" * 60)
    print("PART 2: Adjacency Matrix")
    print("=" * 60)

    n = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

    # Build adjacency matrix
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1

    print(f"  Adjacency matrix ({n}x{n}):")
    header = "     " + "  ".join(str(i) for i in range(n))
    print(header)
    for i in range(n):
        row = "  ".join(str(matrix[i][j]) for j in range(n))
        print(f"  {i}: {row}")

    print(f"\n  Space used: O(V^2) = O({n}^2) = O({n * n})")
    print(f"  That's {n * n} entries for just {len(edges)} edges!")


# ── Part 3: Side-by-Side Comparison ──────────────────────────────

def part3_comparison():
    """Compare the three representations."""
    print("\n" + "=" * 60)
    print("PART 3: Side-by-Side Comparison")
    print("=" * 60)

    n = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

    print(f"\n  Graph: {n} vertices, {len(edges)} edges")
    print(f"  Edges: {edges}")

    print(f"\n  {'Representation':<20} {'Space':>15} {'Edge lookup':>15} {'Neighbors':>15}")
    print(f"  {'-'*20} {'-'*15} {'-'*15} {'-'*15}")
    print(f"  {'Adjacency List':<20} {'O(V+E)':>15} {'O(degree)':>15} {'O(degree)':>15}")
    print(f"  {'Adjacency Matrix':<20} {'O(V^2)':>15} {'O(1)':>15} {'O(V)':>15}")
    print(f"  {'Edge List':<20} {'O(E)':>15} {'O(E)':>15} {'O(E)':>15}")

    print(f"\n  For this graph (V={n}, E={len(edges)}):")
    print(f"    Adj List space:   {n + 2 * len(edges)} entries")
    print(f"    Adj Matrix space: {n * n} entries")
    print(f"    Edge List space:  {len(edges)} entries")

    print(f"\n  For a sparse graph (V=10000, E=20000):")
    print(f"    Adj List space:   ~50,000 entries")
    print(f"    Adj Matrix space: 100,000,000 entries  <- way too much!")
    print(f"    Edge List space:  20,000 entries")


# ── Part 4: Queries ──────────────────────────────────────────────

def part4_queries():
    """Show how to query each representation."""
    print("\n" + "=" * 60)
    print("PART 4: Querying the Graph")
    print("=" * 60)

    n = 5
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

    # Build all three
    adj_list = [[] for _ in range(n)]
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        matrix[u][v] = 1
        matrix[v][u] = 1

    # Query 1: Neighbors of node 3
    print(f"\n  Query: 'What are the neighbors of node 3?'")
    print(f"    Adj List:   adj[3] = {adj_list[3]}")
    print(f"    Adj Matrix: [i for i in range(n) if matrix[3][i]] = "
          f"{[i for i in range(n) if matrix[3][i]]}")
    print(f"    Edge List:  scan all edges -> {[v for u, v in edges if u == 3] + [u for u, v in edges if v == 3]}")

    # Query 2: Is there an edge between 0 and 3?
    print(f"\n  Query: 'Is there an edge between 0 and 3?'")
    print(f"    Adj List:   3 in adj[0] = {3 in adj_list[0]}")
    print(f"    Adj Matrix: matrix[0][3] = {matrix[0][3]} ({'Yes' if matrix[0][3] else 'No'})")
    print(f"    Edge List:  (0,3) in edges = {(0, 3) in edges}")

    # Query 3: Degree of each node
    print(f"\n  Query: 'What is the degree of each node?'")
    for i in range(n):
        print(f"    Node {i}: degree = {len(adj_list[i])}")


# ── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_adjacency_list()
    part2_adjacency_matrix()
    part3_comparison()
    part4_queries()
