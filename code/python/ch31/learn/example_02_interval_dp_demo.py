"""
Example 02: Interval DP Demo — MCM & Burst Balloons
====================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

This example demonstrates:
  - Matrix Chain Multiplication (interval DP)
  - Burst Balloons (interval DP, think about last action)
  - The critical importance of loop order (iterate by length!)
"""


# ── Matrix Chain Multiplication ──────────────────────────────

def mcm(dims):
    """
    Find minimum number of scalar multiplications to multiply a chain
    of matrices with given dimensions.
    dims has length n+1: matrix i has dimensions dims[i] x dims[i+1].
    Time: O(n^3), Space: O(n^2)
    """
    n = len(dims) - 1  # number of matrices
    if n <= 1:
        return 0

    dp = [[0] * n for _ in range(n)]

    # Fill by increasing interval length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# ── Burst Balloons ───────────────────────────────────────────

def burst_balloons(nums):
    """
    Burst all balloons to maximize coins.
    Bursting balloon i earns nums[i-1] * nums[i] * nums[i+1].
    Boundaries treated as 1.
    Time: O(n^3), Space: O(n^2)
    """
    # Add boundary 1s
    vals = [1] + nums + [1]
    n = len(vals)
    dp = [[0] * n for _ in range(n)]

    # length of the interval (excluding boundaries)
    for length in range(1, n - 1):
        for left in range(1, n - length):
            right = left + length - 1
            for k in range(left, right + 1):
                # k is the LAST balloon burst in [left, right]
                coins = vals[left - 1] * vals[k] * vals[right + 1]
                coins += dp[left][k - 1] + dp[k + 1][right]
                dp[left][right] = max(dp[left][right], coins)

    return dp[1][n - 2]


# ── Main ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("MATRIX CHAIN MULTIPLICATION")
    print("=" * 60)

    dims1 = [10, 30, 5, 60]
    print(f"\n  Dimensions: {dims1}")
    print(f"  3 matrices: 10x30, 30x5, 5x60")
    print(f"  Minimum multiplications: {mcm(dims1)}")  # 4500

    dims2 = [40, 20, 30, 10, 30]
    print(f"\n  Dimensions: {dims2}")
    print(f"  4 matrices: 40x20, 20x30, 30x10, 10x30")
    print(f"  Minimum multiplications: {mcm(dims2)}")  # 26000

    print("\n" + "=" * 60)
    print("BURST BALLOONS")
    print("=" * 60)

    nums1 = [3, 1, 5, 8]
    print(f"\n  Balloons: {nums1}")
    print(f"  Maximum coins: {burst_balloons(nums1)}")  # 167

    nums2 = [1, 5]
    print(f"\n  Balloons: {nums2}")
    print(f"  Maximum coins: {burst_balloons(nums2)}")  # 10
