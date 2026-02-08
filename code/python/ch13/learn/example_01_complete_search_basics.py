"""
Example 01: Complete Search Basics — Trying Every Possibility
=============================================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

This example demonstrates:
  - Part 1: Brute force subset generation (recursive)
  - Part 2: Bitmask subset generation
  - Part 3: Permutation generation (backtracking)
  - Part 4: Simulation — robot on a grid
"""


# ── Part 1: Recursive Subset Generation ──────────────────────────

def part1_recursive_subsets():
    """Generate all subsets using recursion (include/exclude pattern)."""
    print("=" * 60)
    print("PART 1: Recursive Subset Generation")
    print("=" * 60)

    def generate_subsets(nums, index, current, all_subsets):
        if index == len(nums):
            all_subsets.append(current[:])
            return
        # EXCLUDE nums[index]
        generate_subsets(nums, index + 1, current, all_subsets)
        # INCLUDE nums[index]
        current.append(nums[index])
        generate_subsets(nums, index + 1, current, all_subsets)
        current.pop()  # UN-CHOOSE

    nums = [1, 2, 3]
    all_subsets = []
    generate_subsets(nums, 0, [], all_subsets)

    print(f"  Input: {nums}")
    print(f"  Total subsets: {len(all_subsets)} (should be 2^{len(nums)} = {2**len(nums)})")
    for s in sorted(all_subsets, key=lambda x: (len(x), x)):
        print(f"    {s}")


# ── Part 2: Bitmask Subset Generation ────────────────────────────

def part2_bitmask_subsets():
    """Generate all subsets using bitmasks."""
    print("\n" + "=" * 60)
    print("PART 2: Bitmask Subset Generation")
    print("=" * 60)

    nums = [1, 2, 3]
    n = len(nums)
    print(f"  Input: {nums}")
    print(f"  Iterating masks 0 to {(1 << n) - 1} (binary 000 to 111):\n")

    for mask in range(1 << n):
        subset = []
        bits = ""
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
                bits += "1"
            else:
                bits += "0"
        print(f"    mask={mask}  binary={bits}  subset={subset}")


# ── Part 3: Permutation Generation ───────────────────────────────

def part3_permutations():
    """Generate all permutations using backtracking."""
    print("\n" + "=" * 60)
    print("PART 3: Backtracking Permutation Generation")
    print("=" * 60)

    def generate_permutations(nums, used, current, results):
        if len(current) == len(nums):
            results.append(current[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            current.append(nums[i])
            generate_permutations(nums, used, current, results)
            current.pop()       # UN-CHOOSE
            used[i] = False     # UN-CHOOSE

    nums = [1, 2, 3]
    results = []
    used = [False] * len(nums)
    generate_permutations(nums, used, [], results)

    print(f"  Input: {nums}")
    print(f"  Total permutations: {len(results)} (should be {len(nums)}! = ", end="")
    factorial = 1
    for i in range(1, len(nums) + 1):
        factorial *= i
    print(f"{factorial})")
    for p in results:
        print(f"    {p}")


# ── Part 4: Simulation — Robot on Grid ───────────────────────────

def part4_simulation():
    """Simulate a robot moving on a grid."""
    print("\n" + "=" * 60)
    print("PART 4: Simulation — Robot on Grid")
    print("=" * 60)

    def simulate(commands):
        x, y = 0, 0
        path = [(x, y)]
        for cmd in commands:
            if cmd == 'U':
                y += 1
            elif cmd == 'D':
                y -= 1
            elif cmd == 'L':
                x -= 1
            elif cmd == 'R':
                x += 1
            path.append((x, y))
        return path

    commands = "UURRDLL"
    path = simulate(commands)
    print(f"  Commands: {commands}")
    print(f"  Path traced:")
    for i, (x, y) in enumerate(path):
        step = commands[i] if i < len(commands) else "START"
        if i == 0:
            print(f"    Start -> ({x}, {y})")
        else:
            print(f"    '{commands[i-1]}' -> ({x}, {y})")
    print(f"  Final position: ({path[-1][0]}, {path[-1][1]})")


# ── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_recursive_subsets()
    part2_bitmask_subsets()
    part3_permutations()
    part4_simulation()
