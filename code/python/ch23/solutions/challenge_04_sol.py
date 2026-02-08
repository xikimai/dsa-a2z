"""
Solution for Challenge 4: House Robber III (Binary Tree)
==========================================================
Chapter 23: Dynamic Programming I — The Foundation

APPROACH
--------
Build tree from level-order array. DFS returns (rob_this, skip_this) for
each node. rob_this = val + skip_left + skip_right.
skip_this = max(rob_left, skip_left) + max(rob_right, skip_right).

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n) for tree and recursion
"""


def solve(tree: list[int]) -> int:
    """Return maximum money from tree-shaped houses without robbing adjacent."""
    if not tree:
        return 0

    def dfs(idx):
        """Return (rob_this_node, skip_this_node)."""
        if idx >= len(tree) or tree[idx] == -1:
            return (0, 0)
        left = dfs(2 * idx + 1)
        right = dfs(2 * idx + 2)
        rob = tree[idx] + left[1] + right[1]
        skip = max(left[0], left[1]) + max(right[0], right[1])
        return (rob, skip)

    result = dfs(0)
    return max(result[0], result[1])


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    tree = list(map(int, input().split()))
    print(solve(tree))
