"""
Solution for Warmup 1: Assign Cookies
=======================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Sort both arrays. Use two pointers to greedily assign the smallest
sufficient cookie to each child.

TIME COMPLEXITY:  O(n log n + m log m)
SPACE COMPLEXITY: O(1) extra (sorting is in-place)
"""


def solve(greed: list[int], cookies: list[int]) -> int:
    """Return the maximum number of content children."""
    greed.sort()
    cookies.sort()
    child = 0
    cookie = 0
    while child < len(greed) and cookie < len(cookies):
        if cookies[cookie] >= greed[child]:
            child += 1
        cookie += 1
    return child


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    greed = list(map(int, input().strip().split()))
    cookies = list(map(int, input().strip().split()))
    print(solve(greed, cookies))
