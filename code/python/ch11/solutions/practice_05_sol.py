"""
Solution for Practice 5: Sort Characters by Frequency
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Build a frequency map. Sort unique characters by (-frequency, character)
for descending frequency with alphabetical ascending tiebreak.
Build the result string by repeating each character by its frequency.

TIME COMPLEXITY:  O(n + k log k) where k = unique characters
SPACE COMPLEXITY: O(n) for the result string
"""


def solve(s: str) -> str:
    """Sort string characters by frequency descending, alpha ascending tiebreak."""
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Sort by (-frequency, character) so higher frequency comes first,
    # and ties are broken alphabetically
    sorted_chars = sorted(freq.keys(), key=lambda ch: (-freq[ch], ch))

    result = []
    for ch in sorted_chars:
        result.append(ch * freq[ch])
    return "".join(result)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
