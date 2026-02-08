"""
Solution for Challenge 3: Combination Sum
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Sort candidates first. Use backtracking: for each candidate starting
from the current index (to avoid duplicates), if the remaining target
equals 0, we found a combination. If remaining goes negative, prune
(break, since candidates are sorted). Otherwise, recurse with the same
start index (allowing reuse of the same number).

TIME COMPLEXITY:  O(n^(t/m)) where t=target, m=min candidate — branching factor
SPACE COMPLEXITY: O(t/m) — recursion depth
"""


def solve(candidates: list[int], target: int) -> list[list[int]]:
    """Find all combinations that sum to target (numbers reusable)."""
    candidates = sorted(candidates)
    result = []

    def backtrack(start, remaining, current):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            current.append(candidates[i])
            backtrack(i, remaining - candidates[i], current)
            current.pop()

    backtrack(0, target, [])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    cands = list(map(int, input().split()))
    target = int(input())
    result = solve(cands, target)
    for combo in result:
        print(combo)
