"""
Solution for Practice 5: Jump Game II
=======================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
BFS-like greedy: track current level end and farthest reachable.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(nums: list[int]) -> int:
    """Return minimum number of jumps to reach the last index."""
    if len(nums) <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    nums = list(map(int, input().strip().split()))
    print(solve(nums))
