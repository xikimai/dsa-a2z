"""
Solution for Warmup 4: Lemonade Change
========================================
Chapter 18: Greedy Algorithms — The Smart Shortcut

APPROACH
--------
Track count of $5 and $10 bills. For $10, give back $5. For $20,
prefer giving $10+$5 (saves fives), else give three $5s.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(1)
"""


def solve(bills: list[int]) -> bool:
    """Return True if you can make change for every customer."""
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # bill == 20
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    bills = list(map(int, input().strip().split()))
    print(solve(bills))
