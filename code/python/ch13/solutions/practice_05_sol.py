"""
Solution for Practice 5: Combination Sum
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Sort candidates. Backtrack: for each candidate (starting from current
index to avoid duplicates), add it if sum doesn't exceed target. Allow
reuse by starting from same index.

TIME COMPLEXITY:  O(n^(t/m)) — n candidates, t=target, m=min candidate
SPACE COMPLEXITY: O(t/m) — recursion depth
"""


def solve(candidates: list[int], target: int) -> list[list[int]]:
    """Return all unique combinations summing to target."""
    candidates.sort()
    results = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            results.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # Pruning: sorted, so all future too big
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i, not i+1: allow reuse
            current.pop()

    backtrack(0, [], target)
    return results


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    candidates = list(map(int, input().split()))
    target = int(input())
    result = solve(candidates, target)
    for combo in result:
        print(combo)
