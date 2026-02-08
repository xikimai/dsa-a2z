"""
Challenge 3: Word Ladder
==========================
Chapter 19: Graphs I — Exploring Networks

PROBLEM
-------
Given a beginWord, an endWord, and a wordList, find the length of the
shortest transformation sequence from beginWord to endWord, such that:
  - Only one letter can be changed at a time.
  - Each transformed word must exist in the wordList.
Return 0 if no such sequence exists. The beginWord does NOT need to
be in the wordList. The endWord MUST be in the wordList.

INPUT FORMAT
------------
First line: beginWord.
Second line: endWord.
Third line: space-separated words in wordList.

OUTPUT FORMAT
-------------
A single integer: the length of the shortest transformation sequence
(including beginWord and endWord), or 0 if impossible.

CONSTRAINTS
-----------
- 1 <= beginWord.length <= 10
- All words have the same length
- 1 <= wordList.length <= 5000
- Words consist of lowercase English letters

EXAMPLES
--------
Input:
  hit
  cog
  hot dot dog lot log cog
Output: 5  (hit -> hot -> dot -> dog -> cog)

Input:
  hit
  cog
  hot dot dog lot log
Output: 0  (endWord "cog" is not in wordList)

HINT
----
Think of words as nodes in an implicit graph, connected if they differ
by exactly one letter. Use BFS from beginWord. For efficiency, try
all 26 letter substitutions at each position and check against a set.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(beginWord: str, endWord: str, wordList: list[str]) -> int:
    """Return length of shortest transformation sequence, or 0."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    beginWord = input().strip()
    endWord = input().strip()
    wordList = input().strip().split()
    print(solve(beginWord, endWord, wordList))
