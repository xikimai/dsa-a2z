"""
Solution for Challenge 3: Word Ladder
=======================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
BFS on an implicit graph. Words are nodes. Two words are connected
if they differ by exactly one letter. Use BFS from beginWord.
For efficiency, try all 26 letter substitutions at each position
and check if the result is in the word set.

TIME COMPLEXITY:  O(M^2 * N) where M = word length, N = wordList size
SPACE COMPLEXITY: O(M * N)
"""

from collections import deque


def solve(beginWord: str, endWord: str, wordList: list[str]) -> int:
    """Return length of shortest transformation sequence, or 0."""
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == word[i]:
                    continue
                next_word = word[:i] + c + word[i + 1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))

    return 0


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    beginWord = input().strip()
    endWord = input().strip()
    wordList = input().strip().split()
    print(solve(beginWord, endWord, wordList))
