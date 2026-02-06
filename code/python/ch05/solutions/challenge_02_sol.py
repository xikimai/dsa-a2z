"""
Solution for Challenge 2: Group Anagrams
==========================================
Chapter 5: Collections

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Key insight: two strings are anagrams if and only if they have the same
sorted characters. So "eat" and "tea" both become "aet" when sorted.

1. For each string, sort its characters to create a key.
2. Use a dictionary to group strings by their sorted key.
3. Sort each inner group alphabetically.
4. Sort the outer list by the first element of each group.

TIME COMPLEXITY:  O(n * k * log(k)) where n = number of strings, k = max string length
SPACE COMPLEXITY: O(n * k) for the groups dictionary
"""


def solve(strs: list[str]) -> list[list[str]]:
    """Group anagrams together. Inner sorted, outer sorted by first element."""
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)

    # Sort each group internally, then sort groups by their first element
    result = []
    for group in groups.values():
        result.append(sorted(group))
    result.sort(key=lambda g: g[0])

    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    strs = input().split()
    groups = solve(strs)
    for group in groups:
        print(" ".join(group))
