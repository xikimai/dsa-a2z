"""
Example 01: DP Basics — The Four Stages of Climbing Stairs
==========================================================
Chapter 23: Dynamic Programming I — The Foundation

This example demonstrates the four stages of DP development:
  - Stage 1: Pure recursion (O(2^n) — exponential)
  - Stage 2: Memoization / top-down (O(n))
  - Stage 3: Tabulation / bottom-up (O(n))
  - Stage 4: Space-optimized (O(n) time, O(1) space)

We also show House Robber and Kadane's algorithm as additional
examples of the DP recipe in action.
"""

import time


# ── Stage 1: Pure Recursion ───────────────────────────────────────

def climb_recursive(n):
    """Count ways to climb n stairs (1 or 2 steps). O(2^n) time."""
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)


# ── Stage 2: Memoization (Top-Down) ──────────────────────────────

def climb_memo(n, memo=None):
    """Count ways to climb n stairs with memoization. O(n) time."""
    if memo is None:
        memo = {}
    if n <= 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = climb_memo(n - 1, memo) + climb_memo(n - 2, memo)
    return memo[n]


# ── Stage 3: Tabulation (Bottom-Up) ──────────────────────────────

def climb_tabulation(n):
    """Count ways to climb n stairs with bottom-up DP. O(n) time, O(n) space."""
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# ── Stage 4: Space-Optimized ─────────────────────────────────────

def climb_optimized(n):
    """Count ways to climb n stairs. O(n) time, O(1) space."""
    if n <= 1:
        return 1
    prev2 = 1  # dp[i-2]
    prev1 = 1  # dp[i-1]
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1


# ── House Robber ──────────────────────────────────────────────────

def house_robber(nums):
    """Max money robbing non-adjacent houses. O(n) time, O(1) space."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    return prev1


# ── Kadane's Algorithm (Max Subarray) ─────────────────────────────

def max_subarray(nums):
    """Find maximum contiguous subarray sum. O(n) time, O(1) space."""
    if not nums:
        return 0
    current = nums[0]
    best = nums[0]
    for i in range(1, len(nums)):
        current = max(current + nums[i], nums[i])
        best = max(best, current)
    return best


# ── Demo ──────────────────────────────────────────────────────────

def demo_climbing_stairs():
    """Compare all four approaches side by side."""
    print("=" * 60)
    print("CLIMBING STAIRS: Four Stages of DP")
    print("=" * 60)

    # Small values — all approaches give the same answer
    for n in [1, 2, 3, 5, 10]:
        r = climb_recursive(n)
        m = climb_memo(n)
        t = climb_tabulation(n)
        o = climb_optimized(n)
        assert r == m == t == o
        print(f"  n={n:2d}: {o} ways")

    # Timing comparison: recursion vs optimized
    print(f"\n{'Approach':<20} {'n=25':>12} {'n=35':>12}")
    print(f"{'-'*20} {'-'*12} {'-'*12}")

    for n in [25, 35]:
        start = time.perf_counter()
        climb_recursive(n)
        t_rec = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        climb_optimized(n)
        t_opt = (time.perf_counter() - start) * 1000

        if n == 25:
            print(f"{'Recursive':<20} {t_rec:>10.3f}ms")
            print(f"{'Optimized':<20} {t_opt:>10.3f}ms")
        else:
            print(f"{'Recursive':<20} {'':>12} {t_rec:>10.3f}ms")
            print(f"{'Optimized':<20} {'':>12} {t_opt:>10.3f}ms")

    print("\n  Notice how recursion gets MUCH slower, but optimized stays instant!")


def demo_house_robber():
    """Demonstrate the House Robber problem."""
    print("\n" + "=" * 60)
    print("HOUSE ROBBER: Take-or-Skip DP")
    print("=" * 60)

    cases = [
        ([1, 2, 3, 1], 4, "Rob houses 0 and 2: 1+3 = 4"),
        ([2, 7, 9, 3, 1], 12, "Rob houses 0, 2, 4: 2+9+1 = 12"),
        ([2, 1, 1, 2], 4, "Rob houses 0 and 3: 2+2 = 4"),
    ]
    for nums, expected, explanation in cases:
        result = house_robber(nums)
        assert result == expected
        print(f"  {nums} -> {result}  ({explanation})")


def demo_kadane():
    """Demonstrate Kadane's algorithm."""
    print("\n" + "=" * 60)
    print("KADANE'S ALGORITHM: Maximum Subarray")
    print("=" * 60)

    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "[4,-1,2,1]"),
        ([1], 1, "[1]"),
        ([5, 4, -1, 7, 8], 23, "[5,4,-1,7,8]"),
        ([-1, -2, -3], -1, "[-1]"),
    ]
    for nums, expected, subarray in cases:
        result = max_subarray(nums)
        assert result == expected
        print(f"  {nums}")
        print(f"    -> max sum = {result}  (subarray: {subarray})")


if __name__ == "__main__":
    demo_climbing_stairs()
    demo_house_robber()
    demo_kadane()
