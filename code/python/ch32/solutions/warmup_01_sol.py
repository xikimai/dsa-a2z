"""
Solution for Warmup 1: Trie Insert and Search
===============================================
Chapter 32: String Algorithms — Beyond Brute Force

APPROACH
--------
Build a Trie. Insert all words, marking end-of-word nodes.
For each query, walk down the trie; return True only if we reach
a node marked as end-of-word.

TIME COMPLEXITY:  O(sum of word lengths + sum of query lengths)
SPACE COMPLEXITY: O(sum of word lengths)
"""


def solve(words: list[str], queries: list[str]) -> list[bool]:
    """Insert all words into a trie, return whether each query is a complete word."""
    # Build trie using nested dicts
    root: dict = {}
    END = "#"

    for word in words:
        node = root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[END] = True

    results = []
    for query in queries:
        node = root
        found = True
        for ch in query:
            if ch not in node:
                found = False
                break
            node = node[ch]
        results.append(found and END in node)
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
    queries = []
    for _ in range(q):
        queries.append(tokens[idx]); idx += 1
    result = solve(words, queries)
    print(" ".join(str(r) for r in result))
