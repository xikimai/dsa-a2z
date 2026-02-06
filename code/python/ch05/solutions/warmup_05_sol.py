"""
Solution for Warmup 5: Character Frequency
============================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Iterate through each character in the string and use a dictionary to
count occurrences. The dict.get(key, default) pattern makes this clean:
for each character, set its count to the current count + 1.

TIME COMPLEXITY:  O(n) where n = len(s)
SPACE COMPLEXITY: O(k) where k = number of unique characters
"""


def solve(s: str) -> dict[str, int]:
    """Return a dict mapping each character to its frequency."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input()
    freq = solve(s)
    for key in sorted(freq.keys()):
        print(f"{key}:{freq[key]}")
