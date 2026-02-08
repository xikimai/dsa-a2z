"""
Example 02: Prefix Sum Patterns — 2D Prefix Sums and Kadane's
==============================================================
Chapter 14: Prefix Sums — The Running Total Trick

This example demonstrates:
  - Part 1: 2D prefix sum construction and rectangle queries
  - Part 2: Kadane's algorithm step-by-step trace
  - Part 3: Prefix sum + hash map for subarray sum equals K
"""


# ── Part 1: 2D Prefix Sums ───────────────────────────────────────

def part1_2d_prefix():
    """Build a 2D prefix sum and answer rectangle queries."""
    print("=" * 60)
    print("PART 1: 2D Prefix Sums and Rectangle Queries")
    print("=" * 60)

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rows, cols = len(matrix), len(matrix[0])
    print("  Matrix:")
    for r in range(rows):
        print(f"    {matrix[r]}")
    print()

    # Build 2D prefix sum
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (prefix[i-1][j] + prefix[i][j-1]
                           - prefix[i-1][j-1] + matrix[i-1][j-1])

    print("  2D Prefix Sum:")
    for r in range(rows + 1):
        print(f"    {prefix[r]}")
    print()

    # Answer rectangle queries
    queries = [(0, 0, 2, 2), (1, 1, 2, 2), (0, 0, 0, 2), (0, 0, 2, 0), (1, 0, 2, 1)]
    for r1, c1, r2, c2 in queries:
        result = (prefix[r2+1][c2+1] - prefix[r1][c2+1]
                  - prefix[r2+1][c1] + prefix[r1][c1])
        # Verify
        actual = sum(matrix[r][c] for r in range(r1, r2+1) for c in range(c1, c2+1))
        print(f"  rect_sum({r1},{c1}) to ({r2},{c2}) = {result}  (verify: {actual})")


# ── Part 2: Kadane's Algorithm Trace ──────────────────────────────

def part2_kadanes_trace():
    """Show Kadane's algorithm step by step."""
    print("\n" + "=" * 60)
    print("PART 2: Kadane's Algorithm — Step-by-Step Trace")
    print("=" * 60)

    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"  Input: {arr}\n")

    current_sum = arr[0]
    max_sum = arr[0]
    best_start = 0
    best_end = 0
    current_start = 0

    print(f"  i=0: arr[0]={arr[0]:>3}  current_sum={current_sum:>3}  max_sum={max_sum:>3}")

    for i in range(1, len(arr)):
        if current_sum + arr[i] >= arr[i]:
            current_sum = current_sum + arr[i]
            action = "extend"
        else:
            current_sum = arr[i]
            current_start = i
            action = "RESTART"

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = current_start
            best_end = i

        marker = " <-- NEW MAX!" if action != "RESTART" and current_sum == max_sum else ""
        print(f"  i={i}: arr[{i}]={arr[i]:>3}  current_sum={current_sum:>3}  "
              f"max_sum={max_sum:>3}  ({action}){marker}")

    print(f"\n  Maximum subarray sum: {max_sum}")
    print(f"  Subarray: {arr[best_start:best_end+1]} (indices {best_start} to {best_end})")

    # Also test all-negative
    print("\n  --- All-Negative Case ---")
    arr2 = [-5, -3, -1, -4, -2]
    print(f"  Input: {arr2}")
    current_sum = arr2[0]
    max_sum = arr2[0]
    for i in range(1, len(arr2)):
        current_sum = max(current_sum + arr2[i], arr2[i])
        max_sum = max(max_sum, current_sum)
    print(f"  Maximum subarray sum: {max_sum} (single element -1)")


# ── Part 3: Prefix Sum + Hash Map ─────────────────────────────────

def part3_prefix_hashmap():
    """Count subarrays with sum equals K using prefix sum + hash map."""
    print("\n" + "=" * 60)
    print("PART 3: Prefix Sum + Hash Map (Subarray Sum = K)")
    print("=" * 60)

    arr = [1, 2, 3, -2, 5]
    k = 3
    print(f"  Input: arr={arr}, k={k}")
    print(f"  Goal: Count subarrays with sum = {k}\n")

    prefix_count = {0: 1}
    current_sum = 0
    count = 0

    for i, x in enumerate(arr):
        current_sum += x
        complement = current_sum - k
        found = prefix_count.get(complement, 0)
        count += found

        if found > 0:
            print(f"  i={i}: arr[{i}]={x:>3}  sum={current_sum:>3}  "
                  f"need={complement:>3}  FOUND {found} time(s)!  count={count}")
        else:
            print(f"  i={i}: arr[{i}]={x:>3}  sum={current_sum:>3}  "
                  f"need={complement:>3}  not found           count={count}")

        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        print(f"        prefix_count = {dict(prefix_count)}")

    print(f"\n  Total subarrays with sum = {k}: {count}")
    # Verify by brute force
    brute_count = 0
    for l in range(len(arr)):
        for r in range(l, len(arr)):
            if sum(arr[l:r+1]) == k:
                brute_count += 1
                print(f"    Subarray [{l}:{r}] = {arr[l:r+1]} sum = {sum(arr[l:r+1])}")
    print(f"  Brute force verification: {brute_count}")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_2d_prefix()
    part2_kadanes_trace()
    part3_prefix_hashmap()
