"""
Solution for Practice 5: Count Numbers with Unique Digits
==========================================================
Chapter 31: Advanced DP — Bitmask, Interval, Trees

APPROACH
--------
Digit DP. Process digits of n from left to right. Track:
- Position in the number
- Whether we are still tight (bounded by n)
- Bitmask of used digits
- Whether we have started placing non-zero digits

TIME COMPLEXITY:  O(d * 2 * 2^10 * 10) where d = number of digits
SPACE COMPLEXITY: O(d * 2 * 2^10)
"""


def solve(n: int) -> int:
    """Return count of numbers in [1, n] with all unique digits."""
    digits = list(map(int, str(n)))
    length = len(digits)

    # memo[pos][tight][mask][started]
    memo = {}

    def dp(pos, tight, mask, started):
        if pos == length:
            return 1 if started else 0

        key = (pos, tight, mask, started)
        if key in memo:
            return memo[key]

        limit = digits[pos] if tight else 9
        count = 0

        for d in range(0, limit + 1):
            if started and (mask & (1 << d)):
                continue  # digit already used

            new_tight = tight and (d == limit)
            new_started = started or (d != 0)
            new_mask = mask | (1 << d) if new_started else mask

            count += dp(pos + 1, new_tight, new_mask, new_started)

        memo[key] = count
        return count

    return dp(0, True, 0, False)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    n = int(sys.stdin.read().strip())
    print(solve(n))
