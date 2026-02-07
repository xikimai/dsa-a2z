"""
Solution for Warmup 1: Count Digits
============================================
Chapter 7: Number Wizardry — Math for Programmers

APPROACH
--------
Use mod-10/div-10 loop to count digits. Handle 0 as special case (1 digit).
Use abs(n) to handle negatives.

TIME COMPLEXITY:  O(d) where d = number of digits
SPACE COMPLEXITY: O(1)
"""


def solve(n: int) -> int:
    """Return the number of digits in n."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input().strip())
    print(solve(n))
