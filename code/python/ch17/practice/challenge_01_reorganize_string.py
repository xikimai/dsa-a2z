"""
Challenge 1: Reorganize String
==================================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given a string s, rearrange the characters so that no two adjacent
characters are the same. If not possible, return an empty string.
If multiple valid answers exist, return any one.

INPUT FORMAT
------------
A single string.

OUTPUT FORMAT
-------------
A rearranged string, or "" if impossible.

CONSTRAINTS
-----------
- 1 <= len(s) <= 500
- s consists of lowercase English letters

EXAMPLES
--------
Input: aab
Output: aba

Input: aaab
Output: ""  (impossible — 'a' appears 3 times but string has length 4)

HINT
----
Use a max-heap of (count, character). Greedily place the most frequent
character, then the next most frequent, alternating. If the most frequent
character has count > (len(s) + 1) // 2, it's impossible.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(s: str) -> str:
    """Rearrange s so no two adjacent chars are the same, or return ''."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
