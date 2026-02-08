"""
Example 01: Two-Pointer Basics — See Converging & Same-Direction Pointers
=========================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

This example demonstrates:
  - Part 1: Converging two pointers to find a pair in a sorted array
  - Part 2: Same-direction pointers to move zeros to the end
  - Part 3: Comparing brute force O(n^2) vs two-pointer O(n) timing
"""


# ── Part 1: Converging Two Pointers ──────────────────────────────────

def part1_converging_pointers():
    """Find a pair in a sorted array that sums to a target."""
    print("=" * 60)
    print("PART 1: Converging Two Pointers — Pair Sum")
    print("=" * 60)

    arr = [1, 3, 5, 8, 12, 15, 20]
    target = 13

    print(f"  Array:  {arr}")
    print(f"  Target: {target}\n")

    left, right = 0, len(arr) - 1
    step = 0

    while left < right:
        step += 1
        current = arr[left] + arr[right]
        print(f"  Step {step}: arr[{left}]={arr[left]} + arr[{right}]={arr[right]} = {current}", end="")

        if current == target:
            print(f"  == {target}  FOUND!")
            break
        elif current < target:
            print(f"  < {target}  → move left pointer right")
            left += 1
        else:
            print(f"  > {target}  → move right pointer left")
            right -= 1
    else:
        print("  No pair found!")

    print(f"\n  Result: [{arr[left]}, {arr[right]}] in {step} steps (vs {len(arr)*(len(arr)-1)//2} brute-force pairs)")


# ── Part 2: Same-Direction Pointers ──────────────────────────────────

def part2_same_direction():
    """Move zeros to the end using slow/fast pointers."""
    print("\n" + "=" * 60)
    print("PART 2: Same-Direction Pointers — Move Zeros")
    print("=" * 60)

    arr = [0, 1, 0, 3, 12, 0, 5]
    print(f"  Input:  {arr}\n")

    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            print(f"  fast={fast}, arr[fast]={arr[fast]} != 0 → swap with slow={slow} → {arr}")
            slow += 1
        else:
            print(f"  fast={fast}, arr[fast]=0 → skip")

    print(f"\n  Result: {arr}")
    print(f"  All zeros are at the end!")


# ── Part 3: Timing Comparison ────────────────────────────────────────

def part3_timing():
    """Compare brute-force pair search vs two-pointer."""
    import time

    print("\n" + "=" * 60)
    print("PART 3: Performance — Brute Force vs Two Pointers")
    print("=" * 60)

    print(f"\n  {'Size':>10}  {'Brute O(n^2)':>14}  {'Two-Ptr O(n)':>14}  {'Speedup':>10}")
    print(f"  {'-'*10}  {'-'*14}  {'-'*14}  {'-'*10}")

    for size in [100, 1_000, 10_000]:
        arr = list(range(size))
        target = arr[-2] + arr[-1]  # last two elements

        # Brute force
        start = time.perf_counter()
        found_brute = False
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    found_brute = True
                    break
            if found_brute:
                break
        brute_time = (time.perf_counter() - start) * 1000

        # Two pointers
        start = time.perf_counter()
        left, right = 0, len(arr) - 1
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                break
            elif s < target:
                left += 1
            else:
                right -= 1
        tp_time = (time.perf_counter() - start) * 1000

        speedup = brute_time / tp_time if tp_time > 0 else float("inf")
        print(f"  {size:>10,}  {brute_time:>14.4f}  {tp_time:>14.4f}  {speedup:>9.1f}x")

    print("\n  Takeaway: Two pointers is O(n) — dramatically faster than O(n^2)!")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_converging_pointers()
    part2_same_direction()
    part3_timing()
