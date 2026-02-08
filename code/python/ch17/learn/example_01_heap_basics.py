"""
Example 01: Heap Basics — See the Heap in Action
==================================================
Chapter 17: Heaps & Priority Queues — The VIP Line

This example demonstrates:
  - Part 1: Building a min-heap from an array using heapify
  - Part 2: Insert (heappush) and extract (heappop) operations
  - Part 3: Visualizing the heap as a tree (array → tree diagram)
  - Part 4: Building a heap manually with bubble-up
"""

import heapq


# ── Part 1: Heapify — Build a Heap in O(n) ─────────────────────────

def part1_heapify():
    """Show how heapify converts an unsorted list into a min-heap."""
    print("=" * 60)
    print("PART 1: Heapify — O(n) Heap Construction")
    print("=" * 60)

    data = [9, 5, 6, 2, 3, 8, 1, 7, 4]
    print(f"  Original array: {data}")

    heapq.heapify(data)
    print(f"  After heapify:  {data}")
    print(f"  Minimum (root): {data[0]}")
    print()
    print("  Note: The array is NOT fully sorted!")
    print("  It only satisfies the heap property: parent <= children.")
    print()

    # Show the tree structure
    print("  As a tree:")
    print_heap_tree(data)


# ── Part 2: Push and Pop Operations ─────────────────────────────────

def part2_push_pop():
    """Demonstrate insert and extract on a min-heap."""
    print("\n" + "=" * 60)
    print("PART 2: Push and Pop Operations")
    print("=" * 60)

    heap = []
    values_to_push = [5, 3, 8, 1, 2, 9, 4]

    print("  Pushing values one by one:")
    for val in values_to_push:
        heapq.heappush(heap, val)
        print(f"    Push {val} → heap = {heap}  (min = {heap[0]})")

    print(f"\n  Final heap: {heap}")
    print(f"\n  Popping all values (extracts in sorted order):")

    sorted_output = []
    while heap:
        val = heapq.heappop(heap)
        sorted_output.append(val)
        print(f"    Pop → {val}  heap = {heap}")

    print(f"\n  Extracted in order: {sorted_output}")
    print("  This IS heapsort!")


# ── Part 3: Visualize Heap as Tree ──────────────────────────────────

def print_heap_tree(heap):
    """Print a heap array as a visual tree."""
    if not heap:
        print("    (empty)")
        return

    n = len(heap)
    level = 0
    idx = 0
    while idx < n:
        level_size = 2 ** level
        level_vals = []
        for _ in range(level_size):
            if idx < n:
                level_vals.append(str(heap[idx]))
                idx += 1
        indent = " " * (2 ** (4 - level))
        spacing = " " * (2 ** (5 - level))
        print(f"    {indent}{spacing.join(level_vals)}")
        level += 1


def part3_visualize():
    """Visualize a heap as both array and tree."""
    print("\n" + "=" * 60)
    print("PART 3: Array ↔ Tree Visualization")
    print("=" * 60)

    data = [1, 3, 2, 7, 6, 5, 4, 8]
    print(f"\n  Array: {data}")
    print(f"  Index: {list(range(len(data)))}")
    print()
    print("  Tree view:")
    print_heap_tree(data)

    print("\n  Parent-child relationships (0-indexed):")
    for i in range(len(data)):
        parent = (i - 1) // 2 if i > 0 else None
        left = 2 * i + 1 if 2 * i + 1 < len(data) else None
        right = 2 * i + 2 if 2 * i + 2 < len(data) else None
        parent_str = f"parent={data[parent]}(idx {parent})" if parent is not None else "ROOT"
        left_str = f"left={data[left]}(idx {left})" if left is not None else "none"
        right_str = f"right={data[right]}(idx {right})" if right is not None else "none"
        print(f"    node {data[i]} (idx {i}): {parent_str}, {left_str}, {right_str}")


# ── Part 4: Manual Heap with Bubble-Up ──────────────────────────────

def part4_manual_heap():
    """Build a min-heap from scratch to see bubble-up in action."""
    print("\n" + "=" * 60)
    print("PART 4: Manual Heap — Bubble Up Step by Step")
    print("=" * 60)

    heap = []

    def manual_push(val):
        heap.append(val)
        i = len(heap) - 1
        steps = []
        while i > 0:
            parent = (i - 1) // 2
            if heap[i] < heap[parent]:
                steps.append(f"swap {heap[i]} with parent {heap[parent]}")
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break
        return steps

    values = [5, 3, 8, 1, 2]
    for val in values:
        steps = manual_push(val)
        if steps:
            print(f"  Push {val}: {' → '.join(steps)} → heap = {heap}")
        else:
            print(f"  Push {val}: no swaps needed → heap = {heap}")

    print(f"\n  Final min-heap: {heap}")
    print(f"  Minimum: {heap[0]}")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_heapify()
    part2_push_pop()
    part3_visualize()
    part4_manual_heap()
