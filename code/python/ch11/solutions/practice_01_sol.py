"""
Solution for Practice 1: Group Anagrams
============================================
Chapter 11: Hashing — The Secret Decoder Ring

APPROACH
--------
Sort each string's characters to create a canonical key.
Group strings with the same key in a dictionary.
Sort each group alphabetically, then sort outer list by first element.

TIME COMPLEXITY:  O(n * k log k) where k = max string length
SPACE COMPLEXITY: O(n * k) for the groups
"""


def solve(strs: list[str]) -> list[list[str]]:
    """Group strings by anagram equivalence."""
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    result = []
    for group in groups.values():
        result.append(sorted(group))
    result.sort(key=lambda g: g[0])
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    line = input().strip()
    if line:
        strs = line.split()
    else:
        strs = []
    print(solve(strs))
