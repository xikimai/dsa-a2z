"""
Example 02: Space vs. Time
==============================
Chapter 6: How Fast Is Your Code?

Run with:
    python code/python/ch06/learn/example_02_space_vs_time.py

This demo solves "Contains Duplicate" three different ways and times
each approach to show the space-time tradeoff in action.
"""

import time
import random

# ============================================================
# PART 1: O(n^2) brute force, O(1) extra space
# ============================================================
# Check every pair.  Simple, but slow for large arrays.


def contains_duplicate_brute(nums: list[int]) -> bool:
    """O(n^2) time, O(1) space — check all pairs."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ============================================================
# PART 2: O(n log n) sort-first, O(1) extra space
# ============================================================
# Sort the array, then duplicates must be adjacent.
# (We sort a copy so we don't modify the original.)


def contains_duplicate_sort(nums: list[int]) -> bool:
    """O(n log n) time, O(n) space for the copy."""
    sorted_nums = sorted(nums)
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1]:
            return True
    return False


# ============================================================
# PART 3: O(n) hash set, O(n) extra space
# ============================================================
# Use a set to remember what we've seen.  Fast but uses memory.


def contains_duplicate_hash(nums: list[int]) -> bool:
    """O(n) time, O(n) space — use a set."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ============================================================
# PART 4: Timing comparison
# ============================================================

print("=== Contains Duplicate: Three Approaches ===")
print()

# Quick correctness check
test_dup = [1, 2, 3, 4, 2]
test_no_dup = [1, 2, 3, 4, 5]
print("Correctness check:")
print(f"  [1,2,3,4,2] has dup?  brute={contains_duplicate_brute(test_dup)}  "
      f"sort={contains_duplicate_sort(test_dup)}  "
      f"hash={contains_duplicate_hash(test_dup)}")
print(f"  [1,2,3,4,5] has dup?  brute={contains_duplicate_brute(test_no_dup)}  "
      f"sort={contains_duplicate_sort(test_no_dup)}  "
      f"hash={contains_duplicate_hash(test_no_dup)}")
print()

# Timing with increasing sizes
# We use arrays with NO duplicates (worst case for brute force)
sizes = [1_000, 10_000, 50_000]

print(f"{'Size':>8}  {'Brute O(n^2)':>14}  {'Sort O(n lg n)':>14}  {'Hash O(n)':>14}")
print("-" * 58)

for size in sizes:
    # Create an array of unique values
    arr = list(range(size))
    random.shuffle(arr)

    # Brute force
    start = time.perf_counter()
    contains_duplicate_brute(arr)
    t_brute = time.perf_counter() - start

    # Sort
    start = time.perf_counter()
    contains_duplicate_sort(arr)
    t_sort = time.perf_counter() - start

    # Hash
    start = time.perf_counter()
    contains_duplicate_hash(arr)
    t_hash = time.perf_counter() - start

    print(f"{size:>8,}  {t_brute:>13.6f}s  {t_sort:>13.6f}s  {t_hash:>13.6f}s")

print()
print("Key takeaway: O(n^2) gets MUCH slower as n grows, while O(n)")
print("barely changes.  The hash set uses more memory, but it's worth it!")
