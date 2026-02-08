"""
Example 02: Backtracking Patterns — Choose, Explore, Un-choose
===============================================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

This example demonstrates:
  - Part 1: N-Queens step-by-step with visual board
  - Part 2: Subset sum with pruning
  - Part 3: Backtracking vs brute force timing comparison
"""


# ── Part 1: N-Queens Visualized ──────────────────────────────────

def part1_n_queens_visual():
    """Solve N-Queens with step-by-step visualization."""
    print("=" * 60)
    print("PART 1: N-Queens (N=4) — Step-by-Step")
    print("=" * 60)

    n = 4
    solutions = []
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    queens = []    # list of (row, col)
    step = [0]

    def print_board():
        board = [['.' for _ in range(n)] for _ in range(n)]
        for r, c in queens:
            board[r][c] = 'Q'
        for row in board:
            print("    " + " ".join(row))

    def backtrack(row):
        if row == n:
            step[0] += 1
            print(f"\n  SOLUTION #{step[0]} FOUND:")
            print_board()
            solutions.append([c for _, c in queens])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # CHOOSE
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            queens.append((row, col))

            backtrack(row + 1)

            # UN-CHOOSE
            queens.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    print(f"\n  Total solutions for {n}-Queens: {len(solutions)}")

    # Count for various N
    print("\n  N-Queens solution counts:")
    for test_n in range(1, 9):
        count = [0]
        c2 = set()
        d1 = set()
        d2 = set()

        def count_queens(row):
            if row == test_n:
                count[0] += 1
                return
            for col in range(test_n):
                if col in c2 or (row - col) in d1 or (row + col) in d2:
                    continue
                c2.add(col)
                d1.add(row - col)
                d2.add(row + col)
                count_queens(row + 1)
                c2.remove(col)
                d1.remove(row - col)
                d2.remove(row + col)

        count_queens(0)
        print(f"    N={test_n}: {count[0]} solutions")


# ── Part 2: Subset Sum with Pruning ──────────────────────────────

def part2_subset_sum_pruning():
    """Demonstrate pruning by solving subset sum."""
    print("\n" + "=" * 60)
    print("PART 2: Subset Sum with Pruning")
    print("=" * 60)

    nums = [3, 7, 1, 8, 4]
    target = 11

    # Without pruning: check all 2^n subsets
    all_subsets_checked = [0]
    results_brute = []

    def brute_force(index, current, current_sum):
        all_subsets_checked[0] += 1
        if index == len(nums):
            if current_sum == target:
                results_brute.append(current[:])
            return
        # Exclude
        brute_force(index + 1, current, current_sum)
        # Include
        current.append(nums[index])
        brute_force(index + 1, current, current_sum + nums[index])
        current.pop()

    brute_force(0, [], 0)
    print(f"  Input: {nums}, target: {target}")
    print(f"  Brute force: checked {all_subsets_checked[0]} nodes")
    print(f"  Found: {results_brute}")

    # With pruning
    sorted_nums = sorted(nums)
    pruned_nodes = [0]
    results_pruned = []

    def pruned_search(index, current, current_sum):
        pruned_nodes[0] += 1
        if current_sum == target:
            results_pruned.append(current[:])
            return
        if current_sum > target:
            return
        for i in range(index, len(sorted_nums)):
            if current_sum + sorted_nums[i] > target:
                break  # Prune: all remaining too big
            current.append(sorted_nums[i])
            pruned_search(i + 1, current, current_sum + sorted_nums[i])
            current.pop()

    pruned_search(0, [], 0)
    print(f"\n  Sorted input: {sorted_nums}")
    print(f"  Pruned search: checked {pruned_nodes[0]} nodes")
    print(f"  Found: {results_pruned}")
    print(f"\n  Pruning reduced nodes from {all_subsets_checked[0]} to {pruned_nodes[0]}"
          f" ({100 * (1 - pruned_nodes[0]/all_subsets_checked[0]):.0f}% reduction)")


# ── Part 3: Timing Comparison ────────────────────────────────────

def part3_timing():
    """Compare brute force vs pruned backtracking speed."""
    print("\n" + "=" * 60)
    print("PART 3: Timing — Brute Force vs Pruned")
    print("=" * 60)

    import time

    # Generate a test case
    nums = list(range(1, 21))  # [1, 2, ..., 20]
    target = 50

    # Brute force: all 2^20 subsets
    start = time.perf_counter()
    count_brute = [0]

    def bf(idx, s):
        if idx == len(nums):
            if s == target:
                count_brute[0] += 1
            return
        bf(idx + 1, s)
        bf(idx + 1, s + nums[idx])

    bf(0, 0)
    brute_time = time.perf_counter() - start

    # Pruned search
    start = time.perf_counter()
    count_pruned = [0]
    sorted_nums = sorted(nums)

    def ps(idx, s):
        if s == target:
            count_pruned[0] += 1
            return
        if s > target:
            return
        for i in range(idx, len(sorted_nums)):
            if s + sorted_nums[i] > target:
                break
            ps(i + 1, s + sorted_nums[i])

    ps(0, 0)
    pruned_time = time.perf_counter() - start

    print(f"  Finding subsets of [1..20] that sum to {target}")
    print(f"  Brute force: {count_brute[0]} solutions in {brute_time:.4f}s")
    print(f"  Pruned:      {count_pruned[0]} solutions in {pruned_time:.4f}s")
    if pruned_time > 0:
        print(f"  Speedup: {brute_time / pruned_time:.1f}x")


# ── Main ────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_n_queens_visual()
    part2_subset_sum_pruning()
    part3_timing()
