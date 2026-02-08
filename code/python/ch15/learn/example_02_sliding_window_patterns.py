"""
Example 02: Sliding Window Patterns — Fixed and Variable Windows
================================================================
Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method

This example demonstrates:
  - Part 1: Fixed-size window — max sum of k consecutive elements
  - Part 2: Variable-size window — longest subarray with sum <= target
  - Part 3: Window + hash map — longest substring without repeating chars
  - Part 4: The caterpillar visualization
"""


# ── Part 1: Fixed-Size Window ────────────────────────────────────────

def part1_fixed_window():
    """Max sum of k consecutive elements."""
    print("=" * 60)
    print("PART 1: Fixed-Size Sliding Window — Max Sum of k Elements")
    print("=" * 60)

    arr = [2, 1, 5, 1, 3, 2, 8, 1]
    k = 3

    print(f"  Array: {arr}")
    print(f"  k = {k}\n")

    # Build first window
    window_sum = sum(arr[:k])
    best = window_sum
    best_start = 0

    print(f"  Window [0..{k-1}] = {arr[:k]}, sum = {window_sum}")

    # Slide
    for i in range(k, len(arr)):
        removed = arr[i - k]
        added = arr[i]
        window_sum += added - removed
        window_str = arr[i - k + 1:i + 1]
        print(f"  Window [{i-k+1}..{i}] = {window_str}, sum = {window_sum}"
              f"  (removed {removed}, added {added})", end="")

        if window_sum > best:
            best = window_sum
            best_start = i - k + 1
            print("  ← new best!")
        else:
            print()

    print(f"\n  Best sum = {best} at window [{best_start}..{best_start+k-1}] = {arr[best_start:best_start+k]}")


# ── Part 2: Variable-Size Window ─────────────────────────────────────

def part2_variable_window():
    """Longest subarray with sum <= target (positive elements only)."""
    print("\n" + "=" * 60)
    print("PART 2: Variable-Size Sliding Window — Longest Subarray with Sum <= K")
    print("=" * 60)

    arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    target = 8

    print(f"  Array:  {arr}")
    print(f"  Target: sum <= {target}\n")

    left = 0
    current_sum = 0
    best_len = 0
    best_window = []

    for right in range(len(arr)):
        current_sum += arr[right]
        action = f"  Expand: add arr[{right}]={arr[right]}, sum={current_sum}"

        while current_sum > target:
            current_sum -= arr[left]
            action += f" → shrink: remove arr[{left}]={arr[left]}"
            left += 1

        window = arr[left:right + 1]
        length = right - left + 1

        if length > best_len:
            best_len = length
            best_window = window[:]
            action += f"  ← new best (len={length})"

        print(f"{action}")
        print(f"           window = {window}, sum = {current_sum}")

    print(f"\n  Longest subarray with sum <= {target}: {best_window} (length {best_len})")


# ── Part 3: Window + Hash Map ────────────────────────────────────────

def part3_window_hashmap():
    """Longest substring without repeating characters."""
    print("\n" + "=" * 60)
    print("PART 3: Window + Hash Map — Longest Substring Without Repeating")
    print("=" * 60)

    s = "abcabcbb"
    print(f"  String: \"{s}\"\n")

    char_index = {}
    left = 0
    best = 0
    best_start = 0

    for right in range(len(s)):
        ch = s[right]
        old_left = left

        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
            print(f"  right={right}: '{ch}' duplicate at {char_index[ch]} "
                  f"→ left jumps {old_left} → {left}")
        else:
            print(f"  right={right}: '{ch}' new", end="")

        char_index[ch] = right
        length = right - left + 1

        if length > best:
            best = length
            best_start = left
            print(f"  window=\"{s[left:right+1]}\" len={length} ← new best!")
        else:
            print(f"  window=\"{s[left:right+1]}\" len={length}")

    print(f"\n  Longest substring without repeating: \"{s[best_start:best_start+best]}\" (length {best})")


# ── Part 4: The Caterpillar ──────────────────────────────────────────

def part4_caterpillar_visualization():
    """Visual metaphor: the caterpillar stretching and shrinking."""
    print("\n" + "=" * 60)
    print("PART 4: The Caterpillar Visualization")
    print("=" * 60)

    arr = [1, 3, 2, 5, 1, 1, 2, 3]
    target = 7

    print(f"  Array:  {arr}")
    print(f"  Goal: longest subarray with sum <= {target}")
    print(f"  The caterpillar stretches (right++) and shrinks (left++)\n")

    left = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > target:
            current_sum -= arr[left]
            left += 1

        # Draw the caterpillar
        line = "  "
        for i in range(len(arr)):
            if i == left and i == right:
                line += "[" + str(arr[i]) + "]"
            elif i == left:
                line += "[" + str(arr[i])
            elif i == right:
                line += " " + str(arr[i]) + "]"
            elif left < i < right:
                line += " " + str(arr[i])
            else:
                line += "  "

        line += f"   sum={current_sum}, len={right - left + 1}"
        print(line)

    print("\n  The caterpillar never backtracks — it only moves forward!")
    print("  Total work: each element added once, removed at most once → O(n)")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_fixed_window()
    part2_variable_window()
    part3_window_hashmap()
    part4_caterpillar_visualization()
