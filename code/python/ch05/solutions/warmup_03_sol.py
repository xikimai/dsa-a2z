"""
Solution for Warmup 3: Count Vowels
============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use a set of vowels for O(1) lookup. Iterate through each character in
the string, check if its lowercase version is in the vowel set, and
count matches.

TIME COMPLEXITY:  O(n) where n = len(s)
SPACE COMPLEXITY: O(1) — the vowel set is fixed size
"""


def solve(s: str) -> int:
    """Return the count of vowels in the string (case-insensitive)."""
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    print(solve(s))
