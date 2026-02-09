"""
Example 01: Trie Basics — Building a Prefix Tree
=================================================
Chapter 32: String Algorithms — Beyond Brute Force

This example demonstrates the Trie (prefix tree) data structure:
  - Inserting words
  - Searching for exact words
  - Counting words with a given prefix
  - Finding the longest common prefix
"""


# ── Trie Node ────────────────────────────────────────────────

class TrieNode:
    """A single node in the Trie."""

    def __init__(self):
        self.children = {}       # char -> TrieNode
        self.is_end = False      # True if a word ends at this node
        self.prefix_count = 0    # how many words pass through this node


# ── Trie ─────────────────────────────────────────────────────

class Trie:
    """A prefix tree supporting insert, search, and prefix operations."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.is_end = True

    def search(self, word):
        """Return True if the word exists in the trie."""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        """Return count of words that start with the given prefix."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count

    def longest_common_prefix(self):
        """Find the longest prefix shared by ALL words in the trie."""
        prefix = []
        node = self.root
        while len(node.children) == 1 and not node.is_end:
            ch = next(iter(node.children))
            prefix.append(ch)
            node = node.children[ch]
        return "".join(prefix)


# ── Main ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("TRIE BASICS: Insert, Search, Prefix Operations")
    print("=" * 60)

    trie = Trie()
    words = ["apple", "app", "application", "apt", "banana"]

    print(f"\n  Inserting words: {words}")
    for w in words:
        trie.insert(w)

    # Search for words
    print("\n  Search results:")
    for query in ["app", "apple", "ban", "banana", "apply"]:
        print(f"    '{query}' -> {trie.search(query)}")

    # Prefix count
    print("\n  Prefix counts:")
    for prefix in ["app", "a", "ban", "c", "ap"]:
        print(f"    '{prefix}' -> {trie.starts_with(prefix)} words")

    # Longest common prefix
    trie2 = Trie()
    words2 = ["flower", "flow", "flight"]
    for w in words2:
        trie2.insert(w)
    print(f"\n  Words: {words2}")
    print(f"  Longest common prefix: '{trie2.longest_common_prefix()}'")

    trie3 = Trie()
    words3 = ["interstellar", "internet", "internal"]
    for w in words3:
        trie3.insert(w)
    print(f"\n  Words: {words3}")
    print(f"  Longest common prefix: '{trie3.longest_common_prefix()}'")
