"""
Example 01: Basic Sorts — Visual Demos
==============================
Chapter 8: The Art of Sorting — Putting Things in Order

Run with:
    python code/python/ch08/learn/example_01_basic_sorts.py

This demo walks through Selection Sort, Bubble Sort, and Insertion Sort
step by step so you can SEE how each algorithm moves elements around.
"""

# ============================================================
# PART 1: Selection Sort
# ============================================================
# Strategy: find the minimum element in the unsorted portion,
# then swap it into the correct position at the front.

print("=== PART 1: Selection Sort ===")
arr = [64, 25, 12, 22, 11]
print(f"Original: {arr}")

for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(f"  Pass {i + 1}: min found = {arr[i]}, swapped into position {i} → {arr}")

print(f"Sorted:   {arr}")
print()

# ============================================================
# PART 2: Bubble Sort
# ============================================================
# Strategy: repeatedly walk through the array, swapping adjacent
# elements that are out of order. Largest elements "bubble up"
# to the end. If no swaps happen in a pass, we're done early!

print("=== PART 2: Bubble Sort ===")
arr = [5, 1, 4, 2, 8]
print(f"Original: {arr}")

n = len(arr)
for i in range(n):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    print(f"  Pass {i + 1}: {arr} {'(swaps happened)' if swapped else '(no swaps — done early!)'}")
    if not swapped:
        break

print(f"Sorted:   {arr}")
print()

# Demonstrate early termination on already-sorted input
print("  Early termination demo on already-sorted [1, 2, 3, 4, 5]:")
arr2 = [1, 2, 3, 4, 5]
swapped = False
for j in range(len(arr2) - 1):
    if arr2[j] > arr2[j + 1]:
        arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
        swapped = True
print(f"  After 1 pass: {arr2}, swapped = {swapped} → stops immediately!")
print()

# ============================================================
# PART 3: Insertion Sort
# ============================================================
# Strategy: build the sorted array one element at a time.
# Pick the next element and insert it into the correct position
# among the already-sorted elements on the left.

print("=== PART 3: Insertion Sort ===")
arr = [12, 11, 13, 5, 6]
print(f"Original: {arr}")

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(f"  Insert {key}: shifted elements right, placed at index {j + 1} → {arr}")

print(f"Sorted:   {arr}")
print()

# ============================================================
# PART 4: Comparison — Count comparisons for each algorithm
# ============================================================
print("=== PART 4: Comparison Count ===")
test_arr = [8, 4, 7, 3, 1, 9, 6, 2, 5, 10]
print(f"Array: {test_arr}")


def selection_sort_count(arr):
    arr = arr[:]
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparisons


def bubble_sort_count(arr):
    arr = arr[:]
    comparisons = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, comparisons


def insertion_sort_count(arr):
    arr = arr[:]
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparisons


_, sel_comps = selection_sort_count(test_arr)
_, bub_comps = bubble_sort_count(test_arr)
_, ins_comps = insertion_sort_count(test_arr)

print(f"  Selection sort: {sel_comps} comparisons")
print(f"  Bubble sort:    {bub_comps} comparisons")
print(f"  Insertion sort: {ins_comps} comparisons")
print()
print("All three are O(n^2) in the worst case, but the constant factors differ!")
