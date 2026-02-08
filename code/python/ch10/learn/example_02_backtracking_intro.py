"""
Example 2: Backtracking — Introduction
=======================================
Chapter 10: The Magic of Recursion

This example shows HOW backtracking works: make a choice, explore,
then UNDO the choice and try something else.
"""


# ── Part 1: Generate All Subsets with Decision Tree ──────────────────

def subsets_traced(nums):
    """Generate all subsets of nums, printing the decision tree."""
    result = []

    def helper(index, current, depth=0):
        indent = "  " * depth
        if index == len(nums):
            print(f"{indent}→ Reached end, subset = {current}")
            result.append(current[:])
            return

        elem = nums[index]

        # Choice 1: INCLUDE this element
        print(f"{indent}Include {elem}")
        current.append(elem)
        helper(index + 1, current, depth + 1)
        current.pop()  # undo (backtrack)

        # Choice 2: EXCLUDE this element
        print(f"{indent}Exclude {elem}")
        helper(index + 1, current, depth + 1)

    helper(0, [])
    return result


def part1_subsets():
    """Show subset generation with decision tree trace."""
    print("=" * 60)
    print("PART 1: All Subsets of [1, 2, 3]")
    print("=" * 60)
    print()
    print("  At each element, we choose: INCLUDE or EXCLUDE.")
    print("  That's 2 choices × 3 elements = 2^3 = 8 subsets.")
    print()

    subsets = subsets_traced([1, 2, 3])

    print()
    print(f"  All {len(subsets)} subsets: {subsets}")
    print()


# ── Part 2: Generate All Permutations with Swap Trace ────────────────

def permutations_traced(nums):
    """Generate all permutations using swap-based approach with trace."""
    result = []
    arr = nums[:]

    def helper(start, depth=0):
        indent = "  " * depth
        if start == len(arr):
            print(f"{indent}→ Permutation found: {arr}")
            result.append(arr[:])
            return

        for i in range(start, len(arr)):
            if i != start:
                print(f"{indent}Swap arr[{start}]={arr[start]} ↔ arr[{i}]={arr[i]}")
            else:
                print(f"{indent}Keep arr[{start}]={arr[start]} in place")

            arr[start], arr[i] = arr[i], arr[start]
            helper(start + 1, depth + 1)
            arr[start], arr[i] = arr[i], arr[start]  # undo (backtrack)

    helper(0)
    return result


def part2_permutations():
    """Show permutation generation with swap trace."""
    print("=" * 60)
    print("PART 2: All Permutations of [1, 2, 3]")
    print("=" * 60)
    print()
    print("  At each position, we try every remaining element.")
    print("  That's 3 × 2 × 1 = 3! = 6 permutations.")
    print()

    perms = permutations_traced([1, 2, 3])

    print()
    print(f"  All {len(perms)} permutations:")
    for p in perms:
        print(f"    {p}")
    print()


# ── Part 3: N-Queens 4×4 Demo ────────────────────────────────────────

def solve_nqueens_4():
    """Solve the 4-Queens problem with backtracking, printing the board."""
    n = 4
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        """Check if placing a queen at (row, col) is safe."""
        # Check column above
        for r in range(row):
            if board[r][col] == "Q":
                return False
        # Check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        # Check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        return True

    def place_queen(row, attempt_count):
        if row == n:
            solution = ["".join(r) for r in board]
            solutions.append(solution)
            return attempt_count

        for col in range(n):
            attempt_count += 1
            if is_safe(row, col):
                board[row][col] = "Q"
                attempt_count = place_queen(row + 1, attempt_count)
                board[row][col] = "."  # backtrack!
        return attempt_count

    attempts = place_queen(0, 0)
    return solutions, attempts


def part3_nqueens():
    """Demo the 4-Queens problem."""
    print("=" * 60)
    print("PART 3: N-Queens on a 4×4 Board")
    print("=" * 60)
    print()
    print("  Goal: Place 4 queens so none attacks another.")
    print("  Queens attack in rows, columns, and diagonals.")
    print()

    solutions, attempts = solve_nqueens_4()

    for i, sol in enumerate(solutions):
        print(f"  Solution {i + 1}:")
        for row in sol:
            print(f"    {' '.join(row)}")
        print()

    print(f"  Found {len(solutions)} solutions after {attempts} placement attempts.")
    print()
    print("  Without backtracking, we'd try 4^4 = 256 placements.")
    print(f"  Backtracking pruned it down to just {attempts} attempts!")
    print()


# ── Part 4: Backtracking Template ────────────────────────────────────

def part4_template():
    """Print the universal backtracking template."""
    print("=" * 60)
    print("PART 4: The Backtracking Template")
    print("=" * 60)
    print()
    print("  Every backtracking problem follows this pattern:")
    print()
    print("    def backtrack(state):")
    print("        if is_solution(state):")
    print("            record(state)")
    print("            return")
    print()
    print("        for choice in choices(state):")
    print("            if is_valid(choice, state):")
    print("                make(choice, state)       # choose")
    print("                backtrack(state)           # explore")
    print("                undo(choice, state)        # un-choose")
    print()
    print("  Three key steps: CHOOSE → EXPLORE → UN-CHOOSE")
    print()
    print("  Examples we just saw:")
    print("    Subsets:      include/exclude each element")
    print("    Permutations: swap each remaining element into position")
    print("    N-Queens:     try each column, check safety, backtrack")
    print()
    print("  The magic is in the UNDO step — it lets us explore ALL paths!")
    print()


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_subsets()
    part2_permutations()
    part3_nqueens()
    part4_template()
