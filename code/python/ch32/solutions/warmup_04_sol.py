"""
Solution for Warmup 4: Z-Function
===================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Use the Z-box optimization:
- Maintain [l, r) as the rightmost interval matching a prefix.
- For each position i, seed z[i] from previous results if inside the Z-box.
- Extend greedily, then update the Z-box if we went further right.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str) -> list[int]:
    """Return the Z-array of s."""
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    s = sys.stdin.read().strip()
    result = solve(s)
    print(" ".join(str(r) for r in result))
