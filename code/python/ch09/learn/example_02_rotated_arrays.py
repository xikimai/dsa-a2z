"""
Example 2: Rotated Arrays — Visual Walkthrough
===============================================
Chapter 9: Finding Needles — The Power of Searching

Rotated sorted arrays are one of the coolest binary search applications.
This example shows how rotation works and how to search in rotated arrays.
"""


# ── Part 1: Visualize Rotation ──────────────────────────────────────

def rotate_array(arr, k):
    """Rotate array right by k positions."""
    n = len(arr)
    k = k % n
    return arr[n - k:] + arr[:n - k]


def part1_rotation_visual():
    """Show what rotation looks like for different amounts."""
    print("=" * 60)
    print("PART 1: What Does Array Rotation Look Like?")
    print("=" * 60)
    print()

    original = [1, 2, 3, 4, 5, 6, 7]
    print(f"  Original: {original}")
    print()

    for k in range(1, len(original)):
        rotated = rotate_array(original, k)
        # Find where the "break" is
        break_idx = -1
        for i in range(len(rotated) - 1):
            if rotated[i] > rotated[i + 1]:
                break_idx = i
                break

        break_str = f"  (break at index {break_idx})" if break_idx >= 0 else "  (no break — fully sorted)"
        print(f"  Rotate by {k}: {rotated}{break_str}")

    print()
    print("  Notice: A rotated sorted array has exactly ONE 'break point'")
    print("  where a bigger number is followed by a smaller one.")
    print("  The minimum element is right after the break!")
    print()


# ── Part 2: Find Min in Rotated Array ──────────────────────────────

def find_min_visual(arr):
    """Find minimum in rotated sorted array with visualization."""
    print(f"  Array: {arr}")
    print()

    lo, hi = 0, len(arr) - 1
    step = 0

    while lo < hi:
        mid = lo + (hi - lo) // 2
        step += 1

        print(f"  Step {step}: lo={lo}({arr[lo]}), mid={mid}({arr[mid]}), "
              f"hi={hi}({arr[hi]})")

        if arr[mid] > arr[hi]:
            print(f"    arr[mid]={arr[mid]} > arr[hi]={arr[hi]} "
                  f"→ min is in RIGHT half, lo = {mid + 1}")
            lo = mid + 1
        else:
            print(f"    arr[mid]={arr[mid]} <= arr[hi]={arr[hi]} "
                  f"→ min is in LEFT half (including mid), hi = {mid}")
            hi = mid
        print()

    print(f"  → Minimum value: {arr[lo]} at index {lo}")
    return arr[lo]


def part2_find_min():
    """Step through finding minimum in rotated array."""
    print("=" * 60)
    print("PART 2: Find Minimum in Rotated Sorted Array")
    print("=" * 60)
    print()

    find_min_visual([4, 5, 6, 7, 0, 1, 2])
    print()

    print("  Key insight: Compare arr[mid] with arr[hi].")
    print("  If arr[mid] > arr[hi], the break is on the right.")
    print("  Otherwise, the break is on the left (or mid IS the min).")
    print()


# ── Part 3: Search in Rotated Array ─────────────────────────────────

def search_rotated_visual(arr, target):
    """Search in rotated sorted array with visualization."""
    print(f"  Searching for {target} in {arr}")
    print()

    lo, hi = 0, len(arr) - 1
    step = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        step += 1

        print(f"  Step {step}: lo={lo}({arr[lo]}), mid={mid}({arr[mid]}), "
              f"hi={hi}({arr[hi]})")

        if arr[mid] == target:
            print(f"    Found {target} at index {mid}!")
            return mid

        # Left half is sorted
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                print(f"    Left half [{arr[lo]}..{arr[mid]}] is sorted, "
                      f"{target} is in range → go LEFT")
                hi = mid - 1
            else:
                print(f"    Left half [{arr[lo]}..{arr[mid]}] is sorted, "
                      f"{target} NOT in range → go RIGHT")
                lo = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[hi]:
                print(f"    Right half [{arr[mid]}..{arr[hi]}] is sorted, "
                      f"{target} is in range → go RIGHT")
                lo = mid + 1
            else:
                print(f"    Right half [{arr[mid]}..{arr[hi]}] is sorted, "
                      f"{target} NOT in range → go LEFT")
                hi = mid - 1
        print()

    print(f"  Target {target} not found.")
    return -1


def part3_search_rotated():
    """Step through searching in rotated array."""
    print("=" * 60)
    print("PART 3: Search in Rotated Sorted Array")
    print("=" * 60)
    print()

    search_rotated_visual([4, 5, 6, 7, 0, 1, 2], 0)
    print()

    print("  ─" * 25)
    print()

    search_rotated_visual([4, 5, 6, 7, 0, 1, 2], 5)
    print()

    print("  Key insight: At least one half is ALWAYS sorted.")
    print("  Check if the target falls in the sorted half.")
    print("  If yes, go there. If no, go to the other half.")
    print()


# ── Part 4: Peak Element Demo ───────────────────────────────────────

def find_peak_visual(arr):
    """Find peak element with visualization."""
    print(f"  Array: {arr}")
    print()

    lo, hi = 0, len(arr) - 1
    step = 0

    while lo < hi:
        mid = lo + (hi - lo) // 2
        step += 1

        left_val = arr[mid - 1] if mid > 0 else "-inf"
        right_val = arr[mid + 1] if mid < len(arr) - 1 else "-inf"

        print(f"  Step {step}: lo={lo}, mid={mid}({arr[mid]}), hi={hi}")
        print(f"    neighbors: left={left_val}, right={right_val}")

        if arr[mid] < arr[mid + 1]:
            print(f"    arr[{mid}]={arr[mid]} < arr[{mid + 1}]={arr[mid + 1]} "
                  f"→ peak must be to the RIGHT")
            lo = mid + 1
        else:
            print(f"    arr[{mid}]={arr[mid]} >= arr[{mid + 1}]={arr[mid + 1]} "
                  f"→ peak could be HERE or LEFT")
            hi = mid
        print()

    print(f"  → Peak element: {arr[lo]} at index {lo}")
    return lo


def part4_peak_element():
    """Demo peak finding on a sample array."""
    print("=" * 60)
    print("PART 4: Find Peak Element")
    print("=" * 60)
    print()

    arr = [1, 2, 1, 3, 5, 6, 4]
    find_peak_visual(arr)
    print()

    print("  Key insight: If arr[mid] < arr[mid+1], there MUST be a peak")
    print("  to the right (the values go up, so they either keep going up")
    print("  to the last element, or drop at some point — either way, peak!).")
    print()
    print("  This is like climbing a hill: if the ground slopes up to your")
    print("  right, there's definitely a peak somewhere to your right.")
    print()


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_rotation_visual()
    part2_find_min()
    part3_search_rotated()
    part4_peak_element()
