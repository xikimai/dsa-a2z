"""
Example 01: Greedy Basics — Activity Selection Step by Step
============================================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

This example demonstrates:
  - Part 1: Activity Selection — sort by end time, pick greedily
  - Part 2: Visual trace of greedy decisions
  - Part 3: Comparing greedy vs brute force on the same input
  - Part 4: When greedy fails — 0/1 Knapsack counterexample
"""


# ── Part 1: Activity Selection ─────────────────────────────────────

def part1_activity_selection():
    """Show activity selection step by step."""
    print("=" * 60)
    print("PART 1: Activity Selection — Sort by End Time")
    print("=" * 60)

    activities = [
        ("A", 9, 10),   # (name, start, end)
        ("B", 9, 12),
        ("C", 10, 11),
        ("D", 11, 14),
        ("E", 11, 12),
        ("F", 13, 15),
    ]

    print("  Original activities:")
    for name, start, end in activities:
        print(f"    {name}: [{start}, {end})")

    # Sort by end time
    activities.sort(key=lambda x: x[2])
    print("\n  Sorted by end time:")
    for name, start, end in activities:
        print(f"    {name}: [{start}, {end})")

    # Greedy selection
    selected = []
    last_end = 0
    print("\n  Greedy selection:")

    for name, start, end in activities:
        if start >= last_end:
            selected.append(name)
            last_end = end
            print(f"    PICK {name} [{start}, {end}) — start {start} >= last_end {start}")
        else:
            print(f"    SKIP {name} [{start}, {end}) — start {start} < last_end {last_end}")

    print(f"\n  Selected: {selected} ({len(selected)} activities)")


# ── Part 2: Visual Trace ───────────────────────────────────────────

def part2_visual_trace():
    """Show a timeline visualization of activity selection."""
    print("\n" + "=" * 60)
    print("PART 2: Visual Timeline Trace")
    print("=" * 60)

    activities = [
        ("Meeting",  1, 3),
        ("Lunch",    2, 5),
        ("Workshop", 4, 7),
        ("Talk",     6, 8),
        ("Social",   5, 9),
        ("Dinner",   8, 10),
    ]

    activities.sort(key=lambda x: x[1])  # Sort by end time

    # Print timeline header
    print("\n  Time:  ", end="")
    for t in range(11):
        print(f"{t:>3}", end="")
    print()
    print("         " + "---" * 11)

    # Print each activity as a bar
    selected = []
    last_end = 0
    for name, start, end in sorted(activities, key=lambda x: x[1]):
        bar = "   " * start + "===" * (end - start)
        picked = start >= last_end
        if picked:
            selected.append(name)
            last_end = end
            marker = " <-- PICK"
        else:
            marker = "     skip"
        print(f"  {name:>8}: {bar}{marker}")

    print(f"\n  Maximum non-overlapping: {len(selected)} activities")


# ── Part 3: Brute Force vs Greedy ──────────────────────────────────

def part3_brute_vs_greedy():
    """Compare brute force and greedy on the same input."""
    print("\n" + "=" * 60)
    print("PART 3: Brute Force vs Greedy Comparison")
    print("=" * 60)

    activities = [(1, 3), (2, 5), (4, 7), (6, 8), (5, 9), (8, 10)]

    # Brute force: try all subsets
    n = len(activities)
    best_brute = 0
    best_subset = []

    for mask in range(1 << n):
        subset = [activities[i] for i in range(n) if mask & (1 << i)]
        subset.sort()
        valid = True
        for i in range(1, len(subset)):
            if subset[i][0] < subset[i - 1][1]:
                valid = False
                break
        if valid and len(subset) > best_brute:
            best_brute = len(subset)
            best_subset = subset[:]

    print(f"  Brute force: {best_brute} activities {best_subset}")

    # Greedy
    sorted_acts = sorted(activities, key=lambda x: x[1])
    selected = []
    last_end = 0
    for start, end in sorted_acts:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    print(f"  Greedy:      {len(selected)} activities {selected}")
    print(f"  Match: {best_brute == len(selected)}")


# ── Part 4: When Greedy Fails ──────────────────────────────────────

def part4_greedy_fails():
    """Show counterexample where greedy gives wrong answer."""
    print("\n" + "=" * 60)
    print("PART 4: When Greedy Fails — Coin Change")
    print("=" * 60)

    # US coins: greedy works!
    coins_us = [25, 10, 5, 1]
    target = 41
    count = 0
    remaining = target
    used = []
    for coin in coins_us:
        while remaining >= coin:
            remaining -= coin
            count += 1
            used.append(coin)
    print(f"  US coins {coins_us}, target {target}:")
    print(f"    Greedy: {used} = {count} coins (OPTIMAL)")

    # Arbitrary coins: greedy FAILS!
    coins_bad = [4, 3, 1]
    target = 6
    count = 0
    remaining = target
    used = []
    for coin in coins_bad:
        while remaining >= coin:
            remaining -= coin
            count += 1
            used.append(coin)
    print(f"\n  Coins {coins_bad}, target {target}:")
    print(f"    Greedy: {used} = {count} coins")
    print(f"    Optimal: [3, 3] = 2 coins")
    print(f"    Greedy is WRONG! (3 vs 2 coins)")
    print(f"\n  Lesson: always check if greedy actually works for your problem!")


# ── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_activity_selection()
    part2_visual_trace()
    part3_brute_vs_greedy()
    part4_greedy_fails()
