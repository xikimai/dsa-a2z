"""
Example 02: Fast Sorts — Merge Sort, Quick Sort & Timing
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python code/python/ch08/learn/example_02_fast_sorts.py

This demo shows divide-and-conquer sorting (Merge Sort and Quick Sort),
Python's built-in sort with custom keys, and a timing comparison.
"""

import time

# ============================================================
# PART 1: Merge Sort Step-by-Step
# ============================================================
# Strategy: split the array in half, recursively sort each half,
# then merge the two sorted halves back together.

print("=== PART 1: Merge Sort ===")


def merge_sort_demo(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        print(f"{indent}Base case: {arr}")
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    print(f"{indent}Split {arr} → left={left}, right={right}")

    left = merge_sort_demo(left, depth + 1)
    right = merge_sort_demo(right, depth + 1)

    # Merge
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    print(f"{indent}Merge {left} + {right} → {merged}")
    return merged


arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Original: {arr}")
result = merge_sort_demo(arr)
print(f"Sorted:   {result}")
print()

# ============================================================
# PART 2: Quick Sort Step-by-Step
# ============================================================
# Strategy: pick a pivot, partition the array so everything
# smaller is on the left and everything larger is on the right,
# then recursively sort each side.

print("=== PART 2: Quick Sort ===")


def quick_sort_demo(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        print(f"{indent}Base case: {arr}")
        return arr

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    print(f"{indent}Pivot={pivot}: {arr} → left={left}, right={right}")

    left = quick_sort_demo(left, depth + 1)
    right = quick_sort_demo(right, depth + 1)

    result = left + [pivot] + right
    print(f"{indent}Combined: {result}")
    return result


arr = [10, 7, 8, 9, 1, 5]
print(f"Original: {arr}")
result = quick_sort_demo(arr)
print(f"Sorted:   {result}")
print()

# ============================================================
# PART 3: Built-in Sort with Custom Keys
# ============================================================
print("=== PART 3: Custom Key Sorting ===")

# Sort by string length
words = ["banana", "apple", "kiwi", "cherry", "fig"]
print(f"Original:          {words}")
print(f"By length:         {sorted(words, key=len)}")
print(f"By last letter:    {sorted(words, key=lambda w: w[-1])}")
print(f"By length, alpha:  {sorted(words, key=lambda w: (len(w), w))}")
print()

# Sort tuples
students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("Diana", 78)]
print(f"Students: {students}")
print(f"By grade (desc):   {sorted(students, key=lambda s: -s[1])}")
print(f"By grade, name:    {sorted(students, key=lambda s: (s[1], s[0]))}")
print()

# ============================================================
# PART 4: Timing Comparison
# ============================================================
print("=== PART 4: Timing Comparison ===")

import random


def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


for size in [100, 1000, 5000]:
    data = [random.randint(1, 100000) for _ in range(size)]

    start = time.time()
    bubble_sort(data)
    bubble_time = time.time() - start

    start = time.time()
    merge_sort(data)
    merge_time = time.time() - start

    start = time.time()
    sorted(data)
    builtin_time = time.time() - start

    print(f"  n={size:>5}: bubble={bubble_time:.4f}s  merge={merge_time:.4f}s  built-in={builtin_time:.6f}s")

print()
print("O(n^2) vs O(n log n) — the gap grows fast as n increases!")
