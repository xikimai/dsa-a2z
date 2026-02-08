"""
Example 01: Prefix Sum Basics — See the Running Total in Action
================================================================
Chapter 14: Prefix Sums — The Running Total Trick

This example demonstrates:
  - Part 1: Building a 1D prefix sum array step by step
  - Part 2: Answering range sum queries in O(1)
  - Part 3: Performance comparison — brute force vs prefix sum queries
  - Part 4: Difference array for range updates
"""

import time


# ── Part 1: Building a Prefix Sum Array ───────────────────────────

def part1_build_prefix():
    """Build a prefix sum array and show each step."""
    print("=" * 60)
    print("PART 1: Building a Prefix Sum Array")
    print("=" * 60)

    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"  Input array: {arr}")
    print(f"  Length n = {len(arr)}")
    print()

    n = len(arr)
    prefix = [0] * (n + 1)
    print(f"  prefix[0] = 0  (sentinel)")

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
        print(f"  prefix[{i}] = prefix[{i-1}] + arr[{i-1}] = {prefix[i-1]} + {arr[i-1]} = {prefix[i]}")

    print(f"\n  Final prefix array: {prefix}")
    print(f"  Length: {len(prefix)} (n + 1 = {n + 1})")


# ── Part 2: Range Sum Queries ─────────────────────────────────────

def part2_range_queries():
    """Answer range sum queries using the prefix array."""
    print("\n" + "=" * 60)
    print("PART 2: Range Sum Queries in O(1)")
    print("=" * 60)

    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]

    print(f"  arr    = {arr}")
    print(f"  prefix = {prefix}")
    print()

    queries = [(0, 7), (2, 5), (0, 0), (4, 7), (3, 3)]
    for l, r in queries:
        result = prefix[r + 1] - prefix[l]
        actual = sum(arr[l:r + 1])
        print(f"  sum({l}, {r}) = prefix[{r+1}] - prefix[{l}] = {prefix[r+1]} - {prefix[l]} = {result}"
              f"  (verify: {' + '.join(str(arr[i]) for i in range(l, r+1))} = {actual})")


# ── Part 3: Performance Comparison ────────────────────────────────

def part3_performance():
    """Compare brute force range sums vs prefix sum queries."""
    print("\n" + "=" * 60)
    print("PART 3: Performance — Brute Force vs Prefix Sum")
    print("=" * 60)

    import random
    random.seed(42)

    for n in [1000, 10000, 100000]:
        arr = [random.randint(1, 100) for _ in range(n)]
        num_queries = 10000
        queries = [(random.randint(0, n // 2), random.randint(n // 2, n - 1))
                   for _ in range(num_queries)]

        # Brute force
        start = time.perf_counter()
        for l, r in queries:
            _ = sum(arr[l:r + 1])
        brute_time = (time.perf_counter() - start) * 1000

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        start = time.perf_counter()
        for l, r in queries:
            _ = prefix[r + 1] - prefix[l]
        prefix_time = (time.perf_counter() - start) * 1000

        speedup = brute_time / prefix_time if prefix_time > 0 else float("inf")
        print(f"  n={n:>7,}, {num_queries} queries:"
              f"  brute={brute_time:>8.2f}ms  prefix={prefix_time:>8.2f}ms"
              f"  speedup={speedup:>.0f}x")


# ── Part 4: Difference Array Demo ─────────────────────────────────

def part4_difference_array():
    """Demonstrate range updates using a difference array."""
    print("\n" + "=" * 60)
    print("PART 4: Difference Array for Range Updates")
    print("=" * 60)

    n = 8
    print(f"  Array size: {n}")
    print(f"  Initial: {[0] * n}")
    print()

    updates = [(1, 4, 5), (2, 6, 3), (0, 2, -1)]
    diff = [0] * (n + 1)

    for l, r, val in updates:
        diff[l] += val
        if r + 1 < n:
            diff[r + 1] -= val
        print(f"  Update: add {val:>2} to range [{l}, {r}]")
        print(f"    diff[{l}] += {val}, diff[{r+1}] -= {val}")
        print(f"    diff = {diff[:n]} (showing first {n} elements)")
        print()

    # Reconstruct
    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running

    print(f"  After prefix sum reconstruction:")
    print(f"  Final array: {result}")

    # Verify manually
    verify = [0] * n
    for l, r, val in updates:
        for i in range(l, r + 1):
            verify[i] += val
    print(f"  Brute force verification: {verify}")
    print(f"  Match: {result == verify}")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_build_prefix()
    part2_range_queries()
    part3_performance()
    part4_difference_array()
