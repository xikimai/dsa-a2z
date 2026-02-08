"""
Solution for Warmup 4: Check Palindrome
============================================
Chapter 10: The Magic of Recursion

APPROACH
--------
Base case: strings of length 0 or 1 are palindromes.
Compare the first and last characters. If they differ, not a palindrome.
Otherwise, check if the middle substring is a palindrome.

TIME COMPLEXITY:  O(n) — each call shrinks string by 2
SPACE COMPLEXITY: O(n) — recursion depth n/2, plus string slicing
"""


def solve(s: str) -> bool:
    """Check if the string is a palindrome, recursively."""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return solve(s[1:-1])


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
