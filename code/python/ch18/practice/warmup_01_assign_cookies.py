"""
Warmup 1: Assign Cookies
==========================
Chapter 18: Greedy Algorithms — The Smart Shortcut

PROBLEM
-------
You have children with greed factors and cookies with sizes.
A child is content if cookie size >= greed factor.
Maximize content children.

EXAMPLES
--------
>>> solve([1, 2, 3], [1, 1])
1
>>> solve([1, 2], [1, 2, 3])
2

CONSTRAINTS
-----------
- 0 <= len(greed), len(cookies) <= 10^4
"""


def solve(greed: list[int], cookies: list[int]) -> int:
    """Return the maximum number of content children."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    greed = list(map(int, input().strip().split()))
    cookies = list(map(int, input().strip().split()))
    print(solve(greed, cookies))
