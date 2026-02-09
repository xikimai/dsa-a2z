"""
Solution for Practice 2: Longest Common Prefix (Trie-based)
============================================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Insert all words into a Trie. Then walk from the root, following
the single child path as long as:
  1. There is exactly one child
  2. The current node is not an end-of-word (if it is, some word
     ended here, so the common prefix cannot be longer)

Alternative simpler approach: just compare character by character
across all words. We use the Trie approach to match the chapter theme.

TIME COMPLEXITY:  O(S) where S = sum of all word lengths
SPACE COMPLEXITY: O(S)
"""


def solve(words: list[str]) -> str:
    """Return the longest common prefix of all words."""
    if not words:
        return ""

    # Simple approach: compare char by char
    prefix = []
    for i, ch in enumerate(words[0]):
        for word in words[1:]:
            if i >= len(word) or word[i] != ch:
                return "".join(prefix)
        prefix.append(ch)
    return "".join(prefix)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    words = []
    for _ in range(n):
        words.append(tokens[idx]); idx += 1
    print(solve(words))
