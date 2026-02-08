"""
Example 01: Hash Fundamentals — See O(1) in Action
===================================================
Chapter 11: Hashing — The Secret Decoder Ring

This example demonstrates:
  - Part 1: Hash set — add elements, check membership, timing vs list search
  - Part 2: Hash map — build a frequency map step by step
  - Part 3: Collision visualization — conceptual tiny hash table (size 5)
  - Part 4: Performance comparison — linear search vs set lookup vs binary search
"""

import time


# ── Part 1: Hash Set Demo ──────────────────────────────────────────

def part1_hash_set_demo():
    """Show O(1) membership testing with a hash set."""
    print("=" * 60)
    print("PART 1: Hash Set — O(1) Membership Testing")
    print("=" * 60)

    # Basic set operations
    fruits = set()
    for fruit in ["apple", "banana", "cherry", "apple", "date"]:
        before = len(fruits)
        fruits.add(fruit)
        after = len(fruits)
        if after > before:
            print(f"  Added '{fruit}'  -> set = {fruits}")
        else:
            print(f"  '{fruit}' already in set, skipped  -> set = {fruits}")

    print(f"\n  'banana' in set? {('banana' in fruits)}")
    print(f"  'grape' in set?  {('grape' in fruits)}")

    # Timing comparison: list vs set for membership testing
    print("\n  Timing: list search vs set lookup")
    print(f"  {'Size':>10}  {'List (ms)':>12}  {'Set (ms)':>12}  {'Speedup':>10}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*10}")

    for size in [10, 1_000, 100_000]:
        data_list = list(range(size))
        data_set = set(data_list)
        target = size - 1  # worst case for list

        # Time list search
        start = time.perf_counter()
        for _ in range(1000):
            _ = target in data_list
        list_time = (time.perf_counter() - start) * 1000

        # Time set lookup
        start = time.perf_counter()
        for _ in range(1000):
            _ = target in data_set
        set_time = (time.perf_counter() - start) * 1000

        speedup = list_time / set_time if set_time > 0 else float("inf")
        print(f"  {size:>10,}  {list_time:>12.4f}  {set_time:>12.4f}  {speedup:>9.1f}x")


# ── Part 2: Hash Map Demo ──────────────────────────────────────────

def part2_hash_map_demo():
    """Build a frequency map step by step."""
    print("\n" + "=" * 60)
    print("PART 2: Hash Map — Building a Frequency Map")
    print("=" * 60)

    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"  Input array: {arr}\n")

    freq = {}
    for num in arr:
        old_count = freq.get(num, 0)
        freq[num] = old_count + 1
        print(f"  Process {num}: freq[{num}] = {old_count} -> {freq[num]}  |  map = {freq}")

    print(f"\n  Final frequency map: {freq}")
    print(f"  Most frequent: {max(freq, key=lambda k: freq[k])} "
          f"(appears {max(freq.values())} times)")


# ── Part 3: Collision Visualization ────────────────────────────────

def part3_collision_demo():
    """Show what happens when multiple keys hash to the same bucket."""
    print("\n" + "=" * 60)
    print("PART 3: Collision Visualization (Tiny Hash Table, size 5)")
    print("=" * 60)

    table_size = 5
    # Simulate a hash table with chaining (each bucket is a list)
    buckets = [[] for _ in range(table_size)]

    keys = [10, 22, 31, 4, 15, 28, 17, 88, 59, 25]
    print(f"  Table size: {table_size}")
    print(f"  Keys to insert: {keys}\n")

    for key in keys:
        bucket_idx = key % table_size
        buckets[bucket_idx].append(key)
        print(f"  Insert {key:>3}:  hash = {key} % {table_size} = {bucket_idx}  "
              f"-> bucket[{bucket_idx}] = {buckets[bucket_idx]}")

    print(f"\n  Final hash table (chaining):")
    for i, bucket in enumerate(buckets):
        chain = " -> ".join(str(k) for k in bucket) if bucket else "(empty)"
        collision_tag = " ** collision!" if len(bucket) > 1 else ""
        print(f"    bucket[{i}]: {chain}{collision_tag}")


# ── Part 4: Performance Comparison ─────────────────────────────────

def part4_performance_comparison():
    """Compare linear search vs set lookup vs binary search."""
    print("\n" + "=" * 60)
    print("PART 4: Performance Comparison")
    print("=" * 60)

    import bisect

    print(f"\n  {'Size':>10}  {'Linear (ms)':>12}  {'BinSearch (ms)':>15}  {'Set (ms)':>12}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*15}  {'-'*12}")

    for size in [100, 10_000, 1_000_000]:
        sorted_list = list(range(size))
        data_set = set(sorted_list)
        target = size - 1
        iterations = 1000

        # Linear search
        start = time.perf_counter()
        for _ in range(iterations):
            _ = target in sorted_list
        linear_time = (time.perf_counter() - start) * 1000

        # Binary search
        start = time.perf_counter()
        for _ in range(iterations):
            idx = bisect.bisect_left(sorted_list, target)
            _ = idx < len(sorted_list) and sorted_list[idx] == target
        bin_time = (time.perf_counter() - start) * 1000

        # Set lookup
        start = time.perf_counter()
        for _ in range(iterations):
            _ = target in data_set
        set_time = (time.perf_counter() - start) * 1000

        print(f"  {size:>10,}  {linear_time:>12.4f}  {bin_time:>15.4f}  {set_time:>12.4f}")

    print("\n  Takeaway: Set lookup is O(1) — nearly constant regardless of size!")
    print("  Binary search is O(log n) — fast but grows slowly.")
    print("  Linear search is O(n) — grows proportionally with size.")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_hash_set_demo()
    part2_hash_map_demo()
    part3_collision_demo()
    part4_performance_comparison()
