"""
Solution for Practice 1: Alien Dictionary
===========================================
Chapter 28: Topological Sort — Ordering Dependencies

APPROACH
--------
1. Compare consecutive words to extract character ordering edges.
2. Topologically sort the characters using Kahn's algorithm.
3. Handle edge cases: prefix conflict, cycle.

TIME COMPLEXITY:  O(C) where C = total characters across all words
SPACE COMPLEXITY: O(U) where U = number of unique characters
"""

from collections import deque, defaultdict


def solve(words: list[str]) -> str:
    """Return the alien character ordering, or '' if invalid."""
    # Collect all unique characters
    chars = set()
    for word in words:
        for c in word:
            chars.add(c)

    adj = defaultdict(set)
    in_degree = defaultdict(int)
    for c in chars:
        in_degree[c] = in_degree.get(c, 0)

    # Extract edges from consecutive word pairs
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        # Check prefix conflict: if w1 is longer and w2 is a prefix of w1
        if len(w1) > len(w2) and w1[:len(w2)] == w2:
            return ""
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    in_degree[c2] += 1
                break

    # Kahn's algorithm
    queue = deque()
    for c in chars:
        if in_degree[c] == 0:
            queue.append(c)

    result = []
    while queue:
        c = queue.popleft()
        result.append(c)
        for nxt in adj[c]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(result) != len(chars):
        return ""  # cycle
    return "".join(result)


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    words = sys.stdin.read().split()
    print(solve(words))
