"""
Solution for Warmup 2: Trie Prefix Count
==========================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Build a Trie with prefix counters. Each node stores how many words
pass through it. For each prefix query, walk down the trie and return
the count at the last node.

TIME COMPLEXITY:  O(sum of word lengths + sum of prefix lengths)
SPACE COMPLEXITY: O(sum of word lengths)
"""


def solve(words: list[str], prefixes: list[str]) -> list[int]:
    """Count how many words have each prefix."""

    class TrieNode:
        __slots__ = ["children", "count"]

        def __init__(self):
            self.children: dict[str, TrieNode] = {}
            self.count = 0

    root = TrieNode()

    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    results = []
    for prefix in prefixes:
        node = root
        found = True
        for ch in prefix:
            if ch not in node.children:
                found = False
                break
            node = node.children[ch]
        results.append(node.count if found else 0)
    return results


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    words = []
    for _ in range(n):
        words.append(tokens[idx]); idx += 1
    q = int(tokens[idx]); idx += 1
    prefixes = []
    for _ in range(q):
        prefixes.append(tokens[idx]); idx += 1
    result = solve(words, prefixes)
    print(" ".join(str(r) for r in result))
