"""
Example 01: Bitmask DP Basics — Subset Encoding & TSP
=====================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

This example demonstrates:
  - How to encode subsets as integers (bitmasks)
  - Common bitmask operations
  - The Traveling Salesman Problem (TSP) using bitmask DP
"""


# ── Bitmask Basics ───────────────────────────────────────────

def show_subset(mask, n):
    """Show which items are in the subset represented by mask."""
    items = []
    for i in range(n):
        if mask & (1 << i):
            items.append(i)
    return items


def enumerate_subsets(n):
    """Enumerate all 2^n subsets of {0, 1, ..., n-1}."""
    for mask in range(1 << n):
        print(f"  mask={mask:0{n}b} (decimal {mask}) -> subset {show_subset(mask, n)}")


# ── TSP with Bitmask DP ─────────────────────────────────────

def tsp(n, dist):
    """
    Traveling Salesman Problem using bitmask DP.
    Returns the minimum cost to visit all cities and return to start (city 0).
    Time: O(2^n * n^2), Space: O(2^n * n)
    """
    INF = float('inf')
    full = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at city 0, only city 0 visited

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue  # already visited
                new_mask = mask | (1 << v)
                cost = dp[mask][u] + dist[u][v]
                if cost < dp[new_mask][v]:
                    dp[new_mask][v] = cost

    # Return to start city
    ans = INF
    for u in range(n):
        ans = min(ans, dp[full][u] + dist[u][0])
    return ans


# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("BITMASK BASICS: Subset Encoding")
    print("=" * 60)

    n = 4
    print(f"\nAll subsets of {{0, 1, 2, 3}} (n={n}):")
    enumerate_subsets(n)

    print(f"\n  Total subsets: {1 << n}")
    print(f"  Full set mask: {(1 << n) - 1} = {(1 << n) - 1:0{n}b}")

    print("\n" + "=" * 60)
    print("TRAVELING SALESMAN PROBLEM (TSP)")
    print("=" * 60)

    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print(f"\n  Distance matrix (4 cities):")
    for row in dist:
        print(f"    {row}")
    print(f"\n  Minimum TSP tour cost: {tsp(4, dist)}")  # 80

    dist2 = [
        [0, 1, 15],
        [1, 0, 7],
        [15, 7, 0]
    ]
    print(f"\n  Distance matrix (3 cities):")
    for row in dist2:
        print(f"    {row}")
    print(f"  Minimum TSP tour cost: {tsp(3, dist2)}")  # 23
