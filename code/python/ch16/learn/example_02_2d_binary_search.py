"""
Example 02: 2D Binary Search — Searching in Matrices
=====================================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

This example demonstrates:
  - Part 1: Search in a fully sorted matrix (treat as 1D array)
  - Part 2: Row with maximum 1s (BS on each row)
  - Part 3: Comparing linear scan vs binary search timing on matrices
"""

import time


# ── Part 1: Search in Sorted Matrix ────────────────────────────────

def part1_matrix_search():
    """Search a sorted matrix by treating it as a virtual 1D array."""
    print("=" * 60)
    print("PART 1: Search in Sorted Matrix")
    print("=" * 60)

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
        [61, 62, 67, 70],
    ]

    print("  Matrix:")
    for row in matrix:
        print(f"    {row}")

    target = 30
    rows, cols = len(matrix), len(matrix[0])
    print(f"\n  Searching for {target} in {rows}x{cols} matrix")
    print(f"  Treating as 1D array of {rows * cols} elements\n")

    lo, hi = 0, rows * cols - 1
    step = 0
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        r, c = mid // cols, mid % cols
        val = matrix[r][c]
        step += 1
        print(f"  Step {step}: 1D index={mid} -> [{r}][{c}] = {val}", end="")
        if val == target:
            print(f"  == {target}  FOUND!")
            break
        elif val < target:
            print(f"  < {target}  -> search right")
            lo = mid + 1
        else:
            print(f"  > {target}  -> search left")
            hi = mid - 1

    print(f"\n  Found {target} at position [{r}][{c}] in {step} steps")


# ── Part 2: Row with Maximum 1s ───────────────────────────────────

def part2_max_ones_row():
    """Find the row with the most 1s in a binary sorted matrix."""
    print("\n" + "=" * 60)
    print("PART 2: Row with Maximum 1s")
    print("=" * 60)

    matrix = [
        [0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    print("  Binary matrix (each row sorted, 0s before 1s):")
    for i, row in enumerate(matrix):
        print(f"    Row {i}: {row}")

    cols = len(matrix[0])
    best_row, best_count = -1, 0

    print(f"\n  Binary searching for first 1 in each row:")
    for i, row in enumerate(matrix):
        lo, hi = 0, cols
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if row[mid] == 1:
                hi = mid
            else:
                lo = mid + 1
        count = cols - lo
        marker = " <-- BEST" if count > best_count else ""
        if count > best_count:
            best_count = count
            best_row = i
        print(f"    Row {i}: first 1 at index {lo}, count = {count}{marker}")

    print(f"\n  Row with maximum 1s: row {best_row} ({best_count} ones)")


# ── Part 3: Timing Comparison ──────────────────────────────────────

def part3_timing():
    """Compare linear scan vs binary search on a large sorted matrix."""
    print("\n" + "=" * 60)
    print("PART 3: Performance — Linear Scan vs Binary Search on Matrix")
    print("=" * 60)

    print(f"\n  {'Matrix Size':>15}  {'Linear (ms)':>12}  {'BS (ms)':>10}  {'Speedup':>10}")
    print(f"  {'-'*15}  {'-'*12}  {'-'*10}  {'-'*10}")

    for size in [100, 500, 1000]:
        # Create a fully sorted matrix
        flat = list(range(1, size * size + 1))
        matrix = [flat[i * size:(i + 1) * size] for i in range(size)]
        target = flat[-2]  # near the end
        rows, cols = size, size

        # Linear scan
        start = time.perf_counter()
        found_linear = None
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == target:
                    found_linear = (r, c)
                    break
            if found_linear:
                break
        linear_time = (time.perf_counter() - start) * 1000

        # Binary search
        start = time.perf_counter()
        lo, hi = 0, rows * cols - 1
        found_bs = None
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                found_bs = (mid // cols, mid % cols)
                break
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        bs_time = (time.perf_counter() - start) * 1000

        assert found_linear == found_bs, "Results don't match!"

        speedup = linear_time / bs_time if bs_time > 0 else float("inf")
        label = f"{size}x{size}"
        print(f"  {label:>15}  {linear_time:>12.4f}  {bs_time:>10.4f}  {speedup:>9.1f}x")

    print("\n  Takeaway: Binary search is O(log(r*c)) vs O(r*c) linear!")


# ── Main ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_matrix_search()
    part2_max_ones_row()
    part3_timing()
