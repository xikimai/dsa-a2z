"""
Solution for Warmup 3: Sum of Digits
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Use abs(n), then extract digits with mod-10 and accumulate.

TIME COMPLEXITY:  O(d) where d = number of digits
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the sum of digits of n."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
