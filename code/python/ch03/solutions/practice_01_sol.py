"""
Solution for Practice 01: FizzBuzz
============================================
Chapter 3: Decisions and Loops

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Loop from 1 to n. For each number, check divisibility by 15 first
(both 3 and 5), then by 3, then by 5, then default to the number.
ORDER MATTERS: check 15 before 3 or 5, otherwise "FizzBuzz" never appears.

TIME COMPLEXITY:  O(n) — one pass through all numbers
SPACE COMPLEXITY: O(n) — the result list
"""


def solve(n: int) -> list[str]:
    """Return the FizzBuzz sequence from 1 to n."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    n = int(input())
    for item in solve(n):
        print(item)
