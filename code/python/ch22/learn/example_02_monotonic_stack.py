"""
Example 02: Monotonic Stack — Solving "Next Greater Element" Step by Step
=========================================================================
Chapter 22: Stacks & Queues — Order Matters

This example demonstrates:
  - Part 1: Next Greater Element with brute force (O(n^2))
  - Part 2: Next Greater Element with monotonic stack (O(n)) — step-by-step
  - Part 3: Largest Rectangle in Histogram — monotonic stack trace
  - Part 4: Sliding Window Maximum with deque — step-by-step
"""

from collections import deque


# ── Part 1: Next Greater Element — Brute Force ──────────────────────

def part1_nge_brute():
    """Brute force: for each element, scan right for the first larger one."""
    print("=" * 60)
    print("PART 1: Next Greater Element — Brute Force O(n^2)")
    print("=" * 60)

    arr = [4, 5, 2, 10, 8]
    print(f"  Input: {arr}\n")

    result = [-1] * len(arr)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                print(f"  arr[{i}]={arr[i]}: scanning right... arr[{j}]={arr[j]} > {arr[i]} -> NGE = {arr[j]}")
                break
        else:
            print(f"  arr[{i}]={arr[i]}: scanning right... no greater element found -> NGE = -1")

    print(f"\n  Result: {result}")


# ── Part 2: Next Greater Element — Monotonic Stack ──────────────────

def part2_nge_stack():
    """Monotonic stack approach: process right to left, maintain decreasing stack."""
    print("\n" + "=" * 60)
    print("PART 2: Next Greater Element — Monotonic Stack O(n)")
    print("=" * 60)

    arr = [4, 5, 2, 10, 8]
    n = len(arr)
    print(f"  Input: {arr}")
    print(f"  Processing right to left...\n")

    result = [-1] * n
    stack = []  # indices

    for i in range(n - 1, -1, -1):
        # Pop elements not greater than arr[i]
        popped = []
        while stack and arr[stack[-1]] <= arr[i]:
            popped.append(arr[stack.pop()])

        if popped:
            print(f"  i={i}, arr[{i}]={arr[i]}: popped {popped} (not greater)")
        else:
            print(f"  i={i}, arr[{i}]={arr[i]}: nothing to pop")

        if stack:
            result[i] = arr[stack[-1]]
            print(f"    Stack top = arr[{stack[-1]}] = {arr[stack[-1]]} -> NGE = {result[i]}")
        else:
            print(f"    Stack empty -> NGE = -1")

        stack.append(i)
        print(f"    Push index {i} -> stack (as values) = {[arr[s] for s in stack]}")
        print()

    print(f"  Result: {result}")


# ── Part 3: Largest Rectangle in Histogram ───────────────────────────

def part3_histogram():
    """Trace the monotonic stack algorithm for largest rectangle in histogram."""
    print("\n" + "=" * 60)
    print("PART 3: Largest Rectangle in Histogram — Monotonic Stack")
    print("=" * 60)

    heights = [2, 1, 5, 6, 2, 3]
    print(f"  Heights: {heights}\n")

    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        curr = heights[i] if i < n else 0
        print(f"  i={i}, current height = {curr}")

        while stack and heights[stack[-1]] > curr:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            area = h * w
            max_area = max(max_area, area)
            print(f"    Pop height {h}: width = {w}, area = {h}x{w} = {area}"
                  f"  (max_area = {max_area})")

        stack.append(i)
        print(f"    Push index {i} -> stack = {stack}")
        print()

    print(f"  Answer: {max_area}")
    print(f"  (Rectangle of height 5, width 2 at indices 2-3)")


# ── Part 4: Sliding Window Maximum ───────────────────────────────────

def part4_sliding_window_max():
    """Trace the deque algorithm for sliding window maximum."""
    print("\n" + "=" * 60)
    print("PART 4: Sliding Window Maximum — Deque O(n)")
    print("=" * 60)

    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"  Input: {nums}, k = {k}\n")

    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove expired indices
        while dq and dq[0] < i - k + 1:
            expired = dq.popleft()
            print(f"  i={i}: Remove expired index {expired} from front")

        # Remove smaller elements
        while dq and nums[dq[-1]] <= nums[i]:
            removed = dq.pop()
            print(f"  i={i}: Remove index {removed} (val={nums[removed]}) from back (<= {nums[i]})")

        dq.append(i)
        print(f"  i={i}: Add index {i} (val={nums[i]}). Deque indices: {list(dq)}, "
              f"values: {[nums[j] for j in dq]}")

        if i >= k - 1:
            result.append(nums[dq[0]])
            window = nums[i - k + 1:i + 1]
            print(f"    Window {window} -> max = {nums[dq[0]]}")
        print()

    print(f"  Result: {result}")


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_nge_brute()
    part2_nge_stack()
    part3_histogram()
    part4_sliding_window_max()
