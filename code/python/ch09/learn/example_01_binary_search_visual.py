"""
Example 1: Binary Search — Visual Walkthrough
==============================================
Chapter 9: Finding Needles — The Power of Searching

This example shows HOW searching algorithms work step by step.
Run it and watch the searches unfold!
"""


# ── Part 1: Linear Search — Step Counter ────────────────────────────

def linear_search_counted(arr, target):
    """Linear search that counts how many comparisons it makes."""
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps


def part1_linear_step_counter():
    """Show how linear search steps grow with array size."""
    print("=" * 60)
    print("PART 1: Linear Search — How Steps Grow")
    print("=" * 60)
    print()

    sizes = [10, 100, 1_000, 10_000, 100_000]
    for n in sizes:
        arr = list(range(n))
        # Worst case: target is the last element
        target = n - 1
        _, steps = linear_search_counted(arr, target)
        print(f"  Array size {n:>7,}  →  {steps:>7,} comparisons (worst case)")

    print()
    print("  Notice: Linear search checks EVERY element in the worst case.")
    print("  Double the array → double the work. That's O(n).")
    print()


# ── Part 2: Binary Search — Lo/Hi/Mid Trace ────────────────────────

def binary_search_visual(arr, target):
    """Binary search with step-by-step visualization."""
    lo, hi = 0, len(arr) - 1
    step = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        step += 1

        arr_str = "  ".join(f"{x:>2}" for x in arr)

        print(f"  Step {step}: lo={lo} hi={hi} mid={mid}, arr[{mid}] = {arr[mid]}")
        print(f"    [{arr_str}]")

        if arr[mid] == target:
            print(f"    Found {target} at index {mid}!")
            return mid, step
        elif arr[mid] < target:
            print(f"    {arr[mid]} < {target}, search RIGHT half")
            lo = mid + 1
        else:
            print(f"    {arr[mid]} > {target}, search LEFT half")
            hi = mid - 1
        print()

    print(f"  Target {target} not found after {step} steps.")
    return -1, step


def part2_binary_search_trace():
    """Trace binary search on a sample array."""
    print("=" * 60)
    print("PART 2: Binary Search — Step-by-Step Trace")
    print("=" * 60)
    print()

    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    print(f"  Searching for {target} in {arr}")
    print()
    idx, steps = binary_search_visual(arr, target)
    print()
    print(f"  Result: index {idx} in {steps} steps")
    print(f"  Linear search would need up to {len(arr)} steps!")
    print()


# ── Part 3: First/Last Occurrence Visualization ────────────────────

def first_occurrence_visual(arr, target):
    """Find first occurrence with visualization."""
    print(f"  Finding FIRST occurrence of {target} in {arr}")
    lo, hi = 0, len(arr) - 1
    result = -1
    step = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        step += 1
        if arr[mid] == target:
            result = mid
            print(f"    Step {step}: arr[{mid}]={arr[mid]} == {target}, "
                  f"save result={mid}, search LEFT (hi={mid - 1})")
            hi = mid - 1
        elif arr[mid] < target:
            print(f"    Step {step}: arr[{mid}]={arr[mid]} < {target}, "
                  f"search RIGHT (lo={mid + 1})")
            lo = mid + 1
        else:
            print(f"    Step {step}: arr[{mid}]={arr[mid]} > {target}, "
                  f"search LEFT (hi={mid - 1})")
            hi = mid - 1

    print(f"  → First occurrence at index {result}")
    return result


def last_occurrence_visual(arr, target):
    """Find last occurrence with visualization."""
    print(f"  Finding LAST occurrence of {target} in {arr}")
    lo, hi = 0, len(arr) - 1
    result = -1
    step = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        step += 1
        if arr[mid] == target:
            result = mid
            print(f"    Step {step}: arr[{mid}]={arr[mid]} == {target}, "
                  f"save result={mid}, search RIGHT (lo={mid + 1})")
            lo = mid + 1
        elif arr[mid] < target:
            print(f"    Step {step}: arr[{mid}]={arr[mid]} < {target}, "
                  f"search RIGHT (lo={mid + 1})")
            lo = mid + 1
        else:
            print(f"    Step {step}: arr[{mid}]={arr[mid]} > {target}, "
                  f"search LEFT (hi={mid - 1})")
            hi = mid - 1

    print(f"  → Last occurrence at index {result}")
    return result


def part3_first_last():
    """Visualize first and last occurrence searches."""
    print("=" * 60)
    print("PART 3: First & Last Occurrence")
    print("=" * 60)
    print()

    arr = [1, 2, 2, 2, 3, 4]
    target = 2
    first_occurrence_visual(arr, target)
    print()
    last_occurrence_visual(arr, target)
    print()
    print("  Key insight: When you find the target, DON'T stop!")
    print("  Keep searching left (for first) or right (for last).")
    print()


# ── Part 4: Linear vs Binary Comparison ────────────────────────────

def part4_comparison():
    """Compare linear vs binary search steps."""
    print("=" * 60)
    print("PART 4: Linear vs Binary — Steps Comparison")
    print("=" * 60)
    print()

    import math

    print(f"  {'Array Size':>12}  {'Linear (worst)':>15}  {'Binary (worst)':>15}")
    print(f"  {'─' * 12}  {'─' * 15}  {'─' * 15}")

    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]
    for n in sizes:
        linear_steps = n
        binary_steps = math.floor(math.log2(n)) + 1
        print(f"  {n:>12,}  {linear_steps:>15,}  {binary_steps:>15,}")

    print()
    print("  Binary search is DRAMATICALLY faster on large arrays!")
    print("  1 million elements → only ~20 steps with binary search.")
    print("  That's the power of O(log n) vs O(n).")
    print()


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_linear_step_counter()
    part2_binary_search_trace()
    part3_first_last()
    part4_comparison()
