"""
Solution for Challenge 4: Candy Distribution
==============================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Two passes: left-to-right (satisfy right neighbors), then
right-to-left (satisfy left neighbors). Take max at each position.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(ratings: list[int]) -> int:
    """Return minimum total candies needed."""
    n = len(ratings)
    if n == 0:
        return 0
    candies = [1] * n
    # Left to right: if rating[i] > rating[i-1], give more than left neighbor
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    # Right to left: if rating[i] > rating[i+1], must be more than right neighbor
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    ratings = list(map(int, input().strip().split()))
    print(solve(ratings))
