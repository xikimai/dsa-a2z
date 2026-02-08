"""
Example 02: Priority Queue Usage Patterns
==========================================
Chapter 17: Heaps & Priority Queues — The VIP Line

This example demonstrates:
  - Part 1: Min-heap vs max-heap in Python (negate trick)
  - Part 2: Heap with tuples for custom priority
  - Part 3: nlargest / nsmallest convenience functions
  - Part 4: Performance comparison — sort vs heap for top-K
"""

import heapq
import time
import random


# ── Part 1: Min-Heap vs Max-Heap ────────────────────────────────────

def part1_min_vs_max():
    """Show how to use heapq for both min-heap and max-heap."""
    print("=" * 60)
    print("PART 1: Min-Heap vs Max-Heap")
    print("=" * 60)

    # Min-heap (default)
    print("\n  Min-heap (default heapq behavior):")
    min_heap = []
    for val in [5, 3, 8, 1, 2, 9, 4]:
        heapq.heappush(min_heap, val)
    print(f"    Heap: {min_heap}")
    print(f"    Peek (minimum): {min_heap[0]}")

    print("\n    Extracting in order:")
    while min_heap:
        print(f"      pop → {heapq.heappop(min_heap)}", end="")
    print()

    # Max-heap (negate trick)
    print("\n  Max-heap (negate trick):")
    max_heap = []
    for val in [5, 3, 8, 1, 2, 9, 4]:
        heapq.heappush(max_heap, -val)  # Push negated
    print(f"    Internal: {max_heap}")
    print(f"    Peek (maximum): {-max_heap[0]}")

    print("\n    Extracting in order:")
    while max_heap:
        print(f"      pop → {-heapq.heappop(max_heap)}", end="")
    print()


# ── Part 2: Heap with Tuples ────────────────────────────────────────

def part2_tuple_priority():
    """Use tuples to add custom priority to heap elements."""
    print("\n" + "=" * 60)
    print("PART 2: Heap with Tuples (Custom Priority)")
    print("=" * 60)

    # ER triage simulation
    patients = [
        (3, "scraped knee"),
        (1, "chest pain"),
        (5, "headache"),
        (2, "broken arm"),
        (1, "allergic reaction"),
    ]
    # Lower number = higher urgency

    print("\n  Patients arriving (priority, condition):")
    heap = []
    for priority, condition in patients:
        heapq.heappush(heap, (priority, condition))
        print(f"    Arrived: priority={priority}, '{condition}'")

    print("\n  Doctor sees patients in priority order:")
    while heap:
        priority, condition = heapq.heappop(heap)
        print(f"    Treating: priority={priority}, '{condition}'")


# ── Part 3: nlargest / nsmallest ────────────────────────────────────

def part3_nlargest_nsmallest():
    """Show the convenience of heapq.nlargest and heapq.nsmallest."""
    print("\n" + "=" * 60)
    print("PART 3: nlargest / nsmallest Convenience Functions")
    print("=" * 60)

    scores = [85, 92, 78, 95, 88, 76, 99, 82, 91, 73]
    print(f"\n  Scores: {scores}")
    print(f"  Top 3:    {heapq.nlargest(3, scores)}")
    print(f"  Bottom 3: {heapq.nsmallest(3, scores)}")

    # With key function
    students = [
        {"name": "Alice", "gpa": 3.9},
        {"name": "Bob", "gpa": 3.5},
        {"name": "Charlie", "gpa": 3.8},
        {"name": "Diana", "gpa": 4.0},
        {"name": "Eve", "gpa": 3.2},
    ]
    print(f"\n  Students by GPA:")
    top2 = heapq.nlargest(2, students, key=lambda s: s["gpa"])
    for s in top2:
        print(f"    {s['name']}: {s['gpa']}")


# ── Part 4: Performance — Sort vs Heap for Top-K ───────────────────

def part4_performance():
    """Compare sort vs heap for finding top-K elements."""
    print("\n" + "=" * 60)
    print("PART 4: Performance — Sort vs Heap for Top-K")
    print("=" * 60)

    print(f"\n  {'N':>10}  {'K':>5}  {'Sort (ms)':>12}  {'Heap (ms)':>12}  {'Winner':>8}")
    print(f"  {'-'*10}  {'-'*5}  {'-'*12}  {'-'*12}  {'-'*8}")

    for n, k in [(10_000, 10), (100_000, 10), (100_000, 100), (1_000_000, 10)]:
        data = [random.randint(0, 10_000_000) for _ in range(n)]

        # Method 1: Sort then slice
        start = time.perf_counter()
        _ = sorted(data, reverse=True)[:k]
        sort_time = (time.perf_counter() - start) * 1000

        # Method 2: heapq.nlargest
        start = time.perf_counter()
        _ = heapq.nlargest(k, data)
        heap_time = (time.perf_counter() - start) * 1000

        winner = "heap" if heap_time < sort_time else "sort"
        print(f"  {n:>10,}  {k:>5}  {sort_time:>12.2f}  {heap_time:>12.2f}  {winner:>8}")

    print("\n  Takeaway: When k << n, heap-based top-K is much faster.")
    print("  When k is close to n, sorting may win due to cache efficiency.")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_min_vs_max()
    part2_tuple_priority()
    part3_nlargest_nsmallest()
    part4_performance()
