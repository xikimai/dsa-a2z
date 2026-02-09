"""
Solution for Challenge 4: Longest String Chain
=================================================
Chapter 25: Dynamic Programming III — Subsequences & Knapsack

APPROACH
--------
Sort words by length. For each word, try removing each character
to form a predecessor and look it up in a hash map.
dp[word] = length of longest chain ending at word.

TIME COMPLEXITY:  O(n * L^2) where L = max word length
SPACE COMPLEXITY: O(n * L)
"""


def solve(words: list[str]) -> int:
    """Return the length of the longest string chain."""
    words.sort(key=len)
    dp: dict[str, int] = {}
    best = 1
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            pred = word[:i] + word[i + 1:]
            if pred in dp:
                dp[word] = max(dp[word], dp[pred] + 1)
        best = max(best, dp[word])
    return best


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    words = input().strip().split()
    print(solve(words))
