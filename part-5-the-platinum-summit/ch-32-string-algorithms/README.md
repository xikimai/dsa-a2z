# String Algorithms — Beyond Brute Force

{% hint style="info" %}
**Welcome to Chapter 32 — Platinum territory!** String algorithms are the secret weapon of competitive programmers. Pattern matching, prefix trees, rolling hashes — these techniques transform problems that seem impossibly slow into elegant, lightning-fast solutions. USACO Platinum regularly features string problems, and this chapter gives you the full toolkit.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand why brute-force string matching is O(n*m) and why that is too slow for competitive programming
- Build a **Trie** (prefix tree) from scratch — insert, search, and prefix operations
- Count how many words share a common prefix using a Trie with prefix counters
- Implement the **KMP** (Knuth-Morris-Pratt) algorithm for O(n+m) pattern matching
- Build the KMP **failure function** (also called the prefix function) and understand what it means
- Implement the **Z-function** — another O(n+m) pattern matcher that is often easier to code
- Understand **Rabin-Karp** rolling hash for expected O(n+m) pattern matching
- Choose the right hashing parameters (base, modulus) to minimize collisions
- Know what a **suffix array** is and how it encodes all suffixes of a string
- Use the **Longest Common Prefix (LCP)** array alongside suffix arrays
- Recognize which string algorithm to use for different problem types
- Solve USACO Platinum-level string problems with confidence

---

## The Story: "The DNA Sequencer"

Maya had just started her summer internship at GenomeLab, a bioinformatics startup. Her first assignment sounded simple: find where a specific gene pattern appears in a DNA sequence.

"Here is the DNA strand," said Dr. Chen, pulling up a file on her screen. "Three billion characters. A, C, G, T. And here is the gene pattern we are looking for — about 200 characters long."

Maya wrote a quick script: start at position 0, compare the pattern character by character, slide over by one position, repeat. Her computer churned away. After ten minutes, the progress bar was at 0.01%.

"At this rate it will take about two weeks," Maya said, deflated.

Dr. Chen smiled. "There is a better way. In 1977, three computer scientists — Knuth, Morris, and Pratt — published an algorithm that solves this exact problem in a single pass through the text. No going backward, no re-checking characters you have already seen."

Maya was skeptical. "How is that possible? If there is a mismatch, don't you have to start over?"

"That is the beautiful part," said Dr. Chen. "You build a little cheat sheet from the pattern itself. It tells you exactly where to resume after a mismatch. The pattern has already taught you everything you need to know."

Maya implemented KMP. The search finished in three seconds.

Then came the hard part. "Actually," said Dr. Chen, "we need to search for 10,000 different gene patterns. Can you do that efficiently too?"

Maya needed a new data structure. Something that could store all 10,000 patterns and search for them simultaneously. She was about to discover the **Trie**.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "The Mismatch Detective"

Find all occurrences of `"AABA"` in `"AABAACAADAABAABA"`.

Start with brute force: try every starting position, compare character by character.

- At position 0: A=A, A=A, B=B, A=A. Match!
- At position 1: A=A, B=B, A=A, A!=A. No match. But wait — you just compared characters 1-3 and know they are "ABA". Do you really need to start from scratch at position 2?

{% hint style="info" %}
The answer is NO. When you hit a mismatch, the characters you have already matched tell you where to try next. Position 1 fails, but you already know position 1 starts with "A" (which matches the first character of the pattern). KMP uses this insight: the "failure function" for "AABA" is [0,1,0,1], telling you exactly how far back to "reset" in the pattern (not the text!) after each mismatch. You never go backward in the text.
{% endhint %}

### Puzzle 2: "The Prefix Oracle"

Given these words: `["apple", "app", "application", "apt", "banana"]`.

Someone asks: "How many words start with `app`?" How about `a`? How about `ban`? How about `c`?

If you had 1 million words and 100,000 queries, checking every word for every query would be way too slow. Can you organize the words into a tree-like structure where shared prefixes are stored only once?

{% hint style="info" %}
Yes! A **Trie** (prefix tree) stores words character by character in a tree. Words sharing a prefix share tree nodes. To count words with prefix "app", walk down a-p-p in the tree and read the counter. Each query takes O(length of prefix) time, regardless of how many words you have.
{% endhint %}

### Puzzle 3: "The Fingerprint Trick"

You need to check if pattern `P` (length m) appears in text `T` (length n), where both n and m can be up to 10^6.

What if you could compute a "fingerprint" (a single number) for any substring of T in O(1) time, and compare it to the fingerprint of P? You would only need to do a full character-by-character check when fingerprints match.

How would you make a fingerprint that can be updated in O(1) when you slide the window by one character?

{% hint style="info" %}
This is the **Rabin-Karp** idea. Treat each string as a number in some base (e.g., base 31), computed modulo a large prime. When you slide the window, subtract the contribution of the leftmost character, multiply by the base, and add the new rightmost character — all in O(1). This gives O(n+m) expected time. The catch: different strings can have the same fingerprint (hash collision), so you always verify actual matches.
{% endhint %}

---

## 32.1 The Trie (Prefix Tree)

A **Trie** (pronounced "try" — it comes from "re**trie**val") is a tree where each edge represents a character and each path from root to a node spells out a prefix.

### Why Tries Matter

Imagine storing a dictionary of 100,000 words. With a hash set, you can check if a word exists in O(length) time. But what about:
- "How many words start with `pre`?"
- "What is the longest common prefix of all words?"
- "Does any word in the dictionary START with this string?"

Hash sets cannot answer prefix questions efficiently. Tries can.

### How a Trie Works

Each node in a Trie has:
- Up to 26 children (for lowercase English letters), one per possible next character
- A boolean flag: "does a word END here?"
- (Optionally) a counter: "how many words pass through this node?"

**Inserting "cat":**
1. Start at root. Is there a child for 'c'? No. Create one. Move to it.
2. Is there a child for 'a'? No. Create one. Move to it.
3. Is there a child for 't'? No. Create one. Move to it. Mark as word-end.

**Inserting "car":**
1. Start at root. Child for 'c'? Yes (from "cat"). Move to it.
2. Child for 'a'? Yes. Move to it.
3. Child for 'r'? No. Create one. Move to it. Mark as word-end.

Now 'c' and 'ca' share nodes, but 'cat' and 'car' diverge at the third level.

{% tabs %}
{% tab title="Python" %}
```python
class TrieNode:
    def __init__(self):
        self.children = {}          # char -> TrieNode
        self.is_end = False         # True if a word ends here
        self.prefix_count = 0       # how many words pass through

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.prefix_count
```
{% endtab %}
{% tab title="Java" %}
```java
class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean isEnd = false;
    int prefixCount = 0;
}

class Trie {
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (node.children[idx] == null)
                node.children[idx] = new TrieNode();
            node = node.children[idx];
            node.prefixCount++;
        }
        node.isEnd = true;
    }

    boolean search(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            int idx = ch - 'a';
            if (node.children[idx] == null) return false;
            node = node.children[idx];
        }
        return node.isEnd;
    }

    int startsWith(String prefix) {
        TrieNode node = root;
        for (char ch : prefix.toCharArray()) {
            int idx = ch - 'a';
            if (node.children[idx] == null) return 0;
            node = node.children[idx];
        }
        return node.prefixCount;
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
struct TrieNode {
    TrieNode* children[26] = {};
    bool isEnd = false;
    int prefixCount = 0;
};

class Trie {
    TrieNode* root = new TrieNode();
public:
    void insert(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx])
                node->children[idx] = new TrieNode();
            node = node->children[idx];
            node->prefixCount++;
        }
        node->isEnd = true;
    }

    bool search(const string& word) {
        TrieNode* node = root;
        for (char ch : word) {
            int idx = ch - 'a';
            if (!node->children[idx]) return false;
            node = node->children[idx];
        }
        return node->isEnd;
    }

    int startsWith(const string& prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            int idx = ch - 'a';
            if (!node->children[idx]) return 0;
            node = node->children[idx];
        }
        return node->prefixCount;
    }
};
```
{% endtab %}
{% endtabs %}

### Language Spotlight: Trie Implementation

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Children storage | `dict` (sparse, flexible) | `TrieNode[26]` array | `TrieNode*[26]` array |
| Memory usage | Higher (dict overhead) | Fixed 26 pointers per node | Fixed 26 pointers per node |
| Alphabet flexibility | Easy (any char as key) | Need index mapping | Need index mapping |
| Null check | `ch not in children` | `children[idx] == null` | `!children[idx]` |

{% hint style="warning" %}
**Memory alert:** Each Trie node with a 26-element array uses 26 pointers regardless of how many children it actually has. For large alphabets or sparse tries, use a hash map instead of an array. In competitive programming, the 26-element array is standard because lowercase English is the most common alphabet.
{% endhint %}

### Time Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert a word of length L | O(L) | O(L) new nodes (worst case) |
| Search for a word of length L | O(L) | O(1) |
| Count words with prefix of length L | O(L) | O(1) |
| Total space for N words, average length L | — | O(N * L) worst case |

---

## 32.2 KMP — Knuth-Morris-Pratt

KMP is the gold standard for single-pattern string matching. It answers: "find all positions where pattern P occurs in text T" in O(n + m) time, where n = |T| and m = |P|.

### The Key Insight

When brute force finds a mismatch at position j of the pattern, it throws away all the work it did matching the previous j characters and starts over from the next text position. That is wasteful.

KMP asks: "Of the j characters I just matched, is there a proper prefix that is also a suffix?" If so, we can jump ahead because that prefix/suffix is already matched.

### The Failure Function (Prefix Function)

For pattern P of length m, the failure function `f[i]` is defined as:

> `f[i]` = length of the longest proper prefix of `P[0..i]` that is also a suffix of `P[0..i]`

Example for P = "AABAAAB":

| i | P[0..i] | Longest prefix = suffix | f[i] |
|---|---------|------------------------|------|
| 0 | A | (none) | 0 |
| 1 | AA | A | 1 |
| 2 | AAB | (none) | 0 |
| 3 | AABA | A | 1 |
| 4 | AABAA | AA | 2 |
| 5 | AABAAA | AA | 2 |
| 6 | AABAAAB | AAB | 3 |

### Building the Failure Function

{% tabs %}
{% tab title="Python" %}
```python
def build_failure(pattern):
    m = len(pattern)
    fail = [0] * m
    length = 0  # length of previous longest prefix-suffix
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            fail[i] = length
            i += 1
        else:
            if length > 0:
                length = fail[length - 1]  # don't increment i
            else:
                fail[i] = 0
                i += 1
    return fail
```
{% endtab %}
{% tab title="Java" %}
```java
static int[] buildFailure(String pattern) {
    int m = pattern.length();
    int[] fail = new int[m];
    int length = 0;
    int i = 1;
    while (i < m) {
        if (pattern.charAt(i) == pattern.charAt(length)) {
            fail[i++] = ++length;
        } else if (length > 0) {
            length = fail[length - 1];
        } else {
            fail[i++] = 0;
        }
    }
    return fail;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> buildFailure(const string& pattern) {
    int m = pattern.size();
    vector<int> fail(m, 0);
    int length = 0, i = 1;
    while (i < m) {
        if (pattern[i] == pattern[length]) {
            fail[i++] = ++length;
        } else if (length > 0) {
            length = fail[length - 1];
        } else {
            fail[i++] = 0;
        }
    }
    return fail;
}
```
{% endtab %}
{% endtabs %}

### KMP Search

{% tabs %}
{% tab title="Python" %}
```python
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    fail = build_failure(pattern)
    matches = []
    j = 0  # index in pattern
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = fail[j - 1]
    return matches
```
{% endtab %}
{% tab title="Java" %}
```java
static List<Integer> kmpSearch(String text, String pattern) {
    int n = text.length(), m = pattern.length();
    List<Integer> matches = new ArrayList<>();
    if (m == 0) return matches;
    int[] fail = buildFailure(pattern);
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && text.charAt(i) != pattern.charAt(j))
            j = fail[j - 1];
        if (text.charAt(i) == pattern.charAt(j)) j++;
        if (j == m) {
            matches.add(i - m + 1);
            j = fail[j - 1];
        }
    }
    return matches;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> kmpSearch(const string& text, const string& pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> matches;
    if (m == 0) return matches;
    vector<int> fail = buildFailure(pattern);
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j])
            j = fail[j - 1];
        if (text[i] == pattern[j]) j++;
        if (j == m) {
            matches.push_back(i - m + 1);
            j = fail[j - 1];
        }
    }
    return matches;
}
```
{% endtab %}
{% endtabs %}

### Why KMP is O(n + m)

Here is the critical insight for the proof:

- Building the failure function: the `length` variable can increase at most m times total (once per iteration of i), and it can decrease at most m times total (it never goes below 0). So the total work is O(m).
- Searching: the pointer `i` always moves forward (n steps total). The pointer `j` can increase at most n times and decrease at most n times. So total work is O(n).
- Combined: O(n + m).

{% hint style="info" %}
**Think of it this way:** we never go backward in the text. We only move forward, sometimes adjusting our position within the pattern. The failure function tells us exactly how much of the pattern we can "keep" after a mismatch.
{% endhint %}

---

## 32.3 The Z-Function

The Z-function is an alternative to KMP that many competitive programmers prefer because it is often easier to implement correctly.

### What is the Z-Array?

For a string S of length n, the Z-array `z[0..n-1]` is defined as:

> `z[i]` = length of the longest substring starting at position i that matches a prefix of S

By convention, `z[0] = 0` (or sometimes `n`, since the whole string is trivially a prefix of itself — we use 0 in this chapter).

Example for S = "aabxaa":

| i | Substring from i | Matches prefix | z[i] |
|---|------------------|----------------|------|
| 0 | aabxaa | (convention) | 0 |
| 1 | abxaa | a (matches "a") | 1 |
| 2 | bxaa | (no match) | 0 |
| 3 | xaa | (no match) | 0 |
| 4 | aa | aa (matches "aa") | 2 |
| 5 | a | a (matches "a") | 1 |

### Building the Z-Array Efficiently

The naive approach computes each z[i] independently — O(n^2). The clever approach maintains a "Z-box" [l, r] representing the rightmost interval that matches a prefix, and reuses previous computations.

{% tabs %}
{% tab title="Python" %}
```python
def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0  # [l, r) is the rightmost Z-box
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z
```
{% endtab %}
{% tab title="Java" %}
```java
static int[] zFunction(String s) {
    int n = s.length();
    int[] z = new int[n];
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = Math.min(r - i, z[i - l]);
        while (i + z[i] < n && s.charAt(z[i]) == s.charAt(i + z[i]))
            z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> zFunction(const string& s) {
    int n = s.size();
    vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}
```
{% endtab %}
{% endtabs %}

### Using Z-Function for Pattern Matching

To find pattern P in text T:
1. Create the combined string `S = P + "$" + T` (where "$" is a character not in P or T)
2. Compute the Z-array of S
3. Any position i where `z[i] == len(P)` corresponds to a match at position `i - len(P) - 1` in T

{% hint style="info" %}
The separator "$" prevents the Z-values from extending across the boundary between P and T. Without it, you might get z-values larger than |P| which would give false matches.
{% endhint %}

### Z-Function vs KMP: Which to Use?

| Aspect | KMP | Z-Function |
|--------|-----|------------|
| Time complexity | O(n + m) | O(n + m) |
| Space | O(m) for failure array | O(n + m) for Z-array |
| Implementation | Slightly tricky (off-by-one) | Often cleaner |
| Output | Failure function (prefix info) | Z-array (direct match lengths) |
| Pattern matching | Natural fit | Requires concatenation trick |
| Best for | Streaming text, longest prefix=suffix | Multiple applications, easier to debug |

---

## 32.4 Rabin-Karp — Rolling Hash

Rabin-Karp takes a completely different approach: instead of clever pointer manipulation, it uses **hashing** to compare substrings in O(1) time.

### The Idea

Treat each string as a number in some base (like base 31 for lowercase letters). Compute the hash of the pattern. Then slide a window across the text, updating the hash in O(1) as you go.

Hash of string `s[0..m-1]` with base B and modulus M:

```
hash(s) = (s[0] * B^(m-1) + s[1] * B^(m-2) + ... + s[m-1] * B^0) mod M
```

When sliding from position i to i+1:

```
new_hash = ((old_hash - s[i] * B^(m-1)) * B + s[i+m]) mod M
```

This is O(1)! We remove the leftmost character's contribution and add the new rightmost character.

### Choosing Good Parameters

- **Base B**: Choose a prime larger than the alphabet size. Common choices: 31, 37, 131, 1000000007.
- **Modulus M**: Choose a large prime. Common choices: 10^9 + 7, 10^9 + 9.
- **Double hashing**: Use two different (base, mod) pairs and only consider a match when BOTH hashes agree. This makes collisions astronomically unlikely.

{% tabs %}
{% tab title="Python" %}
```python
def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []
    if m == 0:
        return []

    BASE, MOD = 31, 10**9 + 7
    matches = []

    # Compute hash of pattern and first window
    p_hash = 0
    t_hash = 0
    power = 1  # BASE^(m-1) mod MOD
    for i in range(m - 1):
        power = power * BASE % MOD

    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD

    # Slide the window
    for i in range(n - m + 1):
        if p_hash == t_hash:
            # Verify (avoid false positives from hash collisions)
            if text[i:i + m] == pattern:
                matches.append(i)
        if i < n - m:
            # Remove leftmost, add next character
            t_hash = ((t_hash - ord(text[i]) * power) * BASE
                      + ord(text[i + m])) % MOD
    return matches
```
{% endtab %}
{% tab title="Java" %}
```java
static List<Integer> rabinKarp(String text, String pattern) {
    int n = text.length(), m = pattern.length();
    List<Integer> matches = new ArrayList<>();
    if (m > n || m == 0) return matches;

    long BASE = 31, MOD = 1_000_000_007;
    long pHash = 0, tHash = 0, power = 1;
    for (int i = 0; i < m - 1; i++) power = power * BASE % MOD;

    for (int i = 0; i < m; i++) {
        pHash = (pHash * BASE + pattern.charAt(i)) % MOD;
        tHash = (tHash * BASE + text.charAt(i)) % MOD;
    }

    for (int i = 0; i <= n - m; i++) {
        if (pHash == tHash && text.substring(i, i + m).equals(pattern))
            matches.add(i);
        if (i < n - m)
            tHash = ((tHash - text.charAt(i) * power % MOD + MOD)
                     * BASE + text.charAt(i + m)) % MOD;
    }
    return matches;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> rabinKarp(const string& text, const string& pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> matches;
    if (m > n || m == 0) return matches;

    long long BASE = 31, MOD = 1e9 + 7;
    long long pHash = 0, tHash = 0, power = 1;
    for (int i = 0; i < m - 1; i++) power = power * BASE % MOD;

    for (int i = 0; i < m; i++) {
        pHash = (pHash * BASE + pattern[i]) % MOD;
        tHash = (tHash * BASE + text[i]) % MOD;
    }

    for (int i = 0; i <= n - m; i++) {
        if (pHash == tHash && text.substr(i, m) == pattern)
            matches.push_back(i);
        if (i < n - m)
            tHash = ((tHash - text[i] * power % MOD + MOD)
                     * BASE + text[i + m]) % MOD;
    }
    return matches;
}
```
{% endtab %}
{% endtabs %}

### Language Spotlight: Rabin-Karp

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Big integers | Native (no overflow) | Need `long` + careful mod | Need `long long` + careful mod |
| Negative modulo | `%` always non-negative | `%` can be negative (add MOD) | `%` can be negative (add MOD) |
| Substring compare | `text[i:i+m] == pattern` | `.substring().equals()` | `.substr(i, m) == pattern` |
| Character to int | `ord(c)` | `(int) c` | Implicit char-to-int |

{% hint style="danger" %}
**The biggest Rabin-Karp pitfall:** In Java and C++, the modulo of a negative number can be negative! Always add MOD before taking mod: `((x % MOD) + MOD) % MOD`. In Python, `%` always returns a non-negative result, so this is not an issue.
{% endhint %}

---

## 32.5 Suffix Arrays (Concept)

A **suffix array** is a sorted array of all suffixes of a string. It is one of the most powerful string data structures, but constructing it efficiently is quite involved.

### What is a Suffix Array?

For string S = "banana":

| Index | Suffix |
|-------|--------|
| 0 | banana |
| 1 | anana |
| 2 | nana |
| 3 | ana |
| 4 | na |
| 5 | a |

Sorted alphabetically:

| Rank | Suffix | Original Index |
|------|--------|---------------|
| 0 | a | 5 |
| 1 | ana | 3 |
| 2 | anana | 1 |
| 3 | banana | 0 |
| 4 | na | 4 |
| 5 | nana | 2 |

The suffix array is: `[5, 3, 1, 0, 4, 2]`

### The LCP Array

The **Longest Common Prefix** (LCP) array stores the length of the longest common prefix between consecutive suffixes in the sorted order:

| Pair | LCP |
|------|-----|
| a, ana | 1 |
| ana, anana | 3 |
| anana, banana | 0 |
| banana, na | 0 |
| na, nana | 2 |

LCP array: `[1, 3, 0, 0, 2]`

### Why Suffix Arrays Matter

With a suffix array and LCP array, you can:
- Find any pattern in O(m log n) using binary search
- Count distinct substrings: total substrings = n*(n+1)/2, subtract sum of LCP values
- Find the longest repeated substring: the maximum value in the LCP array

### Construction

The naive approach (sort all suffixes) is O(n^2 log n). The O(n log n) approach uses repeated doubling — sort by first 1 character, then first 2, then first 4, etc. The O(n) construction (SA-IS algorithm) exists but is complex.

For competitive programming, the O(n log n) construction is usually sufficient:

{% tabs %}
{% tab title="Python" %}
```python
def build_suffix_array(s):
    """O(n log^2 n) suffix array construction."""
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    k = 1
    while k < n:
        def cmp_key(i):
            return (rank[i], rank[i + k] if i + k < n else -1)
        sa.sort(key=cmp_key)
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i-1]]
            if cmp_key(sa[i]) != cmp_key(sa[i-1]):
                tmp[sa[i]] += 1
        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        k *= 2
    return sa
```
{% endtab %}
{% tab title="Java" %}
```java
// Suffix array construction is typically done with arrays of pairs
// For USACO, you can often use simpler O(n log^2 n) approach
// or use the Z-function / KMP for the specific problem at hand.
```
{% endtab %}
{% tab title="C++" %}
```cpp
// O(n log^2 n) suffix array construction
vector<int> buildSuffixArray(const string& s) {
    int n = s.size();
    vector<int> sa(n), rank(n), tmp(n);
    iota(sa.begin(), sa.end(), 0);
    for (int i = 0; i < n; i++) rank[i] = s[i];
    for (int k = 1; k < n; k <<= 1) {
        auto cmp = [&](int a, int b) {
            if (rank[a] != rank[b]) return rank[a] < rank[b];
            int ra = a + k < n ? rank[a + k] : -1;
            int rb = b + k < n ? rank[b + k] : -1;
            return ra < rb;
        };
        sort(sa.begin(), sa.end(), cmp);
        tmp[sa[0]] = 0;
        for (int i = 1; i < n; i++)
            tmp[sa[i]] = tmp[sa[i-1]] + (cmp(sa[i-1], sa[i]) ? 1 : 0);
        rank = tmp;
        if (rank[sa.back()] == n - 1) break;
    }
    return sa;
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**For USACO Platinum:** You rarely need to implement suffix arrays from scratch. Most string problems can be solved with KMP, Z-function, or hashing. Suffix arrays are most useful for problems about distinct substrings or longest repeated substrings. If you need one, C++ has the cleanest implementation.
{% endhint %}

---

## 32.6 When to Use What

Here is your decision table for string algorithm problems:

| Problem Type | Best Algorithm | Why |
|-------------|----------------|-----|
| Find pattern in text (single pattern) | KMP or Z-function | O(n+m) guaranteed |
| Find pattern in text (quick to code) | Rabin-Karp | Simplest to implement; O(n+m) expected |
| Multiple patterns, prefix queries | Trie | O(L) per query, L = query length |
| Find all words from dictionary in text | Trie + Aho-Corasick | Multi-pattern matching (beyond this chapter) |
| Longest prefix that is also a suffix | KMP failure function | Direct application of the failure array |
| Count distinct substrings | Suffix Array + LCP | Formula: n(n+1)/2 - sum(LCP) |
| Longest repeated substring | Suffix Array + LCP | Max value in LCP array |
| Substring equality queries | Hashing (Rabin-Karp) | O(1) per query after O(n) preprocessing |
| Word search in a grid (multiple words) | Trie + backtracking | Trie prunes impossible paths early |

{% hint style="warning" %}
**Adversarial inputs:** Rabin-Karp with a single hash can be broken by an adversary who constructs inputs causing many collisions. In competitive programming, use double hashing (two different mod/base pairs) or switch to KMP/Z-function for guaranteed O(n+m).
{% endhint %}

---

## Five-Lens Framework: Pattern Matching

Let us apply the Five-Lens Framework to the classic pattern matching problem.

### Lens 1: Constraints

- Text length n, pattern length m, both up to 10^6
- Time limit: typically 1-2 seconds
- 10^6 * 10^6 = 10^12 operations would take minutes. We need O(n + m).

### Lens 2: Brute Force

Try every starting position i in the text (n - m + 1 positions). For each, compare m characters. Worst case: O(n * m). For n = m = 10^6, that is 10^12 — way too slow.

### Lens 3: Pattern

When brute force finds a mismatch at position j in the pattern, it has already verified that `text[i..i+j-1] == pattern[0..j-1]`. The failure function captures this: "what is the longest proper prefix of `pattern[0..j-1]` that is also a suffix?" We can jump pattern pointer to that position instead of starting over.

### Lens 4: Optimization

KMP processes each text character exactly once (pointer `i` only moves forward). The pattern pointer `j` moves forward and backward, but the total number of backward moves across the entire search is bounded by n (it can only go back as many times as it went forward). Result: O(n + m).

### Lens 5: Proof

**Claim:** KMP runs in O(n + m) time.

**Proof (amortized analysis):** Define a potential function Phi = j (the current position in the pattern). Each step of the main loop either:
- Advances i by 1 and j by at most 1 (Phi increases by at most 1)
- Decreases j by using the failure function (Phi decreases)

Since i advances n times and Phi starts at 0 and stays non-negative, the total increase in Phi is at most n. Since each decrease operation reduces Phi, the total number of decrease operations is also at most n. Therefore, total operations are O(n). Building the failure function uses the same argument for O(m). Total: O(n + m).

---

## Think Like a Pro

{% hint style="info" %}
**Neal Wu** (USACO Platinum, IOI Gold): "For competitive programming, I use hashing first because it is the fastest to code. If I need guaranteed worst-case complexity or the problem involves adversarial inputs, I switch to KMP or Z-function. Tries are my go-to when the problem involves multiple patterns or prefix operations. The key is not to memorize all the algorithms — it is to recognize WHICH type of string problem you are facing and pick the right tool."
{% endhint %}

---

## AOPS Showcase: Pattern Matching — Three Ways

**Problem:** Given text T and pattern P, find all starting positions where P occurs in T.

### Solution 1: Brute Force — O(n * m)

{% tabs %}
{% tab title="Python" %}
```python
def brute_force_match(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            matches.append(i)
    return matches
```
{% endtab %}
{% tab title="Java" %}
```java
static List<Integer> bruteForceMatch(String text, String pattern) {
    List<Integer> matches = new ArrayList<>();
    int n = text.length(), m = pattern.length();
    for (int i = 0; i <= n - m; i++)
        if (text.substring(i, i + m).equals(pattern))
            matches.add(i);
    return matches;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> bruteForceMatch(const string& text, const string& pattern) {
    vector<int> matches;
    int n = text.size(), m = pattern.size();
    for (int i = 0; i <= n - m; i++)
        if (text.substr(i, m) == pattern)
            matches.push_back(i);
    return matches;
}
```
{% endtab %}
{% endtabs %}

**Analysis:** Simple, but O(n * m) worst case. Fails on inputs like text = "AAAA...A" (10^6 A's), pattern = "AAA...AB" (almost all A's then a B).

### Solution 2: KMP — O(n + m) guaranteed

{% tabs %}
{% tab title="Python" %}
```python
def kmp_match(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    # Build failure function
    fail = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            fail[i] = length
            i += 1
        elif length > 0:
            length = fail[length - 1]
        else:
            i += 1
    # Search
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = fail[j - 1]
    return matches
```
{% endtab %}
{% tab title="Java" %}
```java
// (See Section 32.2 for full implementation)
```
{% endtab %}
{% tab title="C++" %}
```cpp
// (See Section 32.2 for full implementation)
```
{% endtab %}
{% endtabs %}

**Analysis:** O(n + m) guaranteed. No worst-case degradation.

### Solution 3: Rabin-Karp — O(n + m) expected

{% tabs %}
{% tab title="Python" %}
```python
def rabin_karp_match(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    BASE, MOD = 131, 10**9 + 7
    p_hash = t_hash = 0
    power = pow(BASE, m - 1, MOD)
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
    matches = []
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * power) * BASE
                      + ord(text[i + m])) % MOD
    return matches
```
{% endtab %}
{% tab title="Java" %}
```java
// (See Section 32.4 for full implementation)
```
{% endtab %}
{% tab title="C++" %}
```cpp
// (See Section 32.4 for full implementation)
```
{% endtab %}
{% endtabs %}

**Analysis:** O(n + m) expected. O(n * m) worst case if many hash collisions, but with good parameters this is extremely unlikely. Easiest to code.

### Comparison

| | Brute Force | KMP | Rabin-Karp |
|-|-------------|-----|------------|
| Time | O(n*m) worst | O(n+m) always | O(n+m) expected |
| Space | O(1) | O(m) | O(1) |
| Coding time | 2 min | 8 min | 5 min |
| Best for | Small inputs | Guaranteed speed | Quick implementation |
| USACO safe? | Bronze only | Gold/Platinum | Gold (double hash for Platinum) |

---

## Legend's Corner

{% hint style="info" %}
**Petr Mitrichev** (two-time IOI Gold, Google Code Jam champion): "String algorithms were my weak point for years. The breakthrough was realizing that KMP's failure function and the Z-array encode the SAME information in different forms. Once you understand one deeply, you can derive the other. That connection made string problems much less scary. My advice: pick ONE of KMP or Z-function, master it completely, and only learn the other when you need its specific properties."
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**1. Rabin-Karp hash collisions:** NEVER trust a hash match without verifying. Two different strings can have the same hash. Always do `text[i:i+m] == pattern` when hashes match. Skipping this step will give wrong answers on adversarial test cases.

**2. KMP failure function off-by-one:** The most common bug is confusing 0-indexed and 1-indexed. In our implementation, `fail[i]` is the length of the longest proper prefix-suffix of `pattern[0..i]`. When you use it: `j = fail[j - 1]` (go to the previous position's failure value). Getting this wrong produces silent incorrect answers.

**3. Trie memory explosion:** Each TrieNode with a 26-element array allocates 26 pointers/references. If you insert 10^5 words of average length 10, you create up to 10^6 nodes, each with 26 pointers. That is 26 million pointers. For problems with large alphabets, use a hash map instead of an array.

**4. Modular arithmetic in hashing:** In Java and C++, `(a - b) % M` can be negative! Always use `((a - b) % M + M) % M`. Forgetting this causes sporadic wrong answers that are extremely hard to debug.

**5. Z-function vs KMP for the same problem:** Z-function requires concatenating pattern + separator + text, creating a string of length n + m + 1. For very large inputs where memory is tight, KMP might be preferable since it only needs O(m) extra space for the failure function.

**6. Empty pattern edge case:** Both KMP and Rabin-Karp must handle empty pattern specially. An empty pattern "matches everywhere" or "matches nowhere" depending on the problem statement. Always check.

**7. Overlapping matches:** Make sure your algorithm handles overlapping matches. "AA" appears in "AAAA" at positions [0, 1, 2], not just [0, 2]. KMP handles this correctly via `j = fail[j-1]` after a match.
{% endhint %}

---

## Practice Problems

Here are 12 problems organized in three tiers. Each problem has skeleton files in your `code/` directory with test cases.

### Warmup (W1-W4)

| # | Problem | Key Idea | Difficulty |
|---|---------|----------|------------|
| W1 | Trie Insert and Search | Build trie, check word existence | Easy |
| W2 | Trie Prefix Count | Count words sharing a prefix | Easy |
| W3 | KMP Pattern Search | Find all occurrences of pattern in text | Medium |
| W4 | Z-Function | Compute the Z-array | Medium |

### Practice (P1-P5)

| # | Problem | Key Idea | Difficulty |
|---|---------|----------|------------|
| P1 | Rabin-Karp Pattern Search | Rolling hash for pattern matching | Medium |
| P2 | Longest Common Prefix (Trie) | All words' longest shared prefix | Medium |
| P3 | Count Distinct Substrings | Use set or hashing | Medium-Hard |
| P4 | Repeated String Match | Minimum repeats for substring containment | Medium |
| P5 | Longest Happy Prefix | KMP failure function application | Medium-Hard |

### Challenge (C1-C3)

| # | Problem | Key Idea | Difficulty |
|---|---------|----------|------------|
| C1 | Word Search II | Trie + grid backtracking | Hard |
| C2 | Shortest Palindrome | KMP on reversed string | Hard |
| C3 | Distinct Substrings of Length K | Rolling hash for fixed-length substrings | Hard |

---

## Language Idioms

### Python
- `ord(c)` converts character to integer (needed for hashing)
- String slicing `s[i:j]` creates a new string (O(j-i) time and space)
- `dict` is the natural choice for Trie children (flexible, any hashable key)
- Python's native `in` operator uses optimized C-level string search internally

### Java
- `String.charAt(i)` is O(1); `String.substring(i, j)` creates a new String object
- Use `long` for hash computations to avoid integer overflow
- `StringBuilder` is faster than `String` concatenation in loops
- Arrays of objects in Java need explicit initialization (each element is `null`)

### C++
- `string::substr(i, len)` creates a new string (O(len))
- Use `long long` for hash computations
- `string::operator[]` is O(1) with no bounds checking (use `.at()` for safety)
- `struct` with arrays is fastest for Trie nodes in C++

---

## Breadcrumbs

{% hint style="info" %}
**Looking back:**
- **Ch 5 (Collections):** You first worked with strings as sequences of characters. Now you are seeing them as objects with deep internal structure.
- **Ch 11 (Hashing):** Rabin-Karp is a direct application of the hashing ideas from Ch 11. The "rolling" part is new, but the core concept — map data to a number for fast comparison — is the same.
- **Ch 10 (Recursion):** The Trie is a recursive data structure. Each subtrie is itself a valid trie.

**Looking ahead:**
- **Ch 33 (Advanced Trees):** Suffix trees are a compressed version of tries built from all suffixes. They solve many problems that suffix arrays solve but with different tradeoffs.
- **USACO Platinum:** String problems appear regularly. The most common patterns: KMP/Z-function for pattern matching, tries for multiple patterns, hashing for substring comparison.
- **Aho-Corasick (beyond this book):** Combines tries with KMP-style failure links to search for MANY patterns simultaneously in O(n + m1 + m2 + ... + mk + matches).
{% endhint %}

---

## Johari Window: After

Now that you have completed this chapter, return to your [Johari Window worksheet](johari.md) and fill in the "After" section. Compare what you knew before with what you know now. What surprised you? What is still fuzzy?

---

## Open Questions Beyond

1. **"What if you need to search for many patterns at once?"** The Aho-Corasick algorithm builds a trie of all patterns and adds "failure links" (like KMP's failure function, but between trie nodes). It finds all occurrences of all patterns in a single pass through the text — O(n + total_pattern_length + matches). Used in network intrusion detection, DNA analysis, and plagiarism detection.

2. **"Can you build a suffix array in O(n) time?"** Yes! The SA-IS (Suffix Array by Induced Sorting) algorithm does it. It is based on classifying suffixes as "S-type" or "L-type" and using induced sorting. The algorithm is elegant but complex. For competitive programming, O(n log n) is usually fast enough.

3. **"What about approximate string matching?"** All algorithms in this chapter find EXACT matches. What if you want to find strings that are "close" to the pattern (e.g., at most k characters different)? This leads to edit distance (Ch 25 DP), bitap algorithm, and more advanced techniques used in spell checkers and bioinformatics.

---

## What's Next

{% hint style="info" %}
You have mastered the core string algorithms toolkit: Tries for prefix operations, KMP and Z-function for exact matching, Rabin-Karp for hash-based matching, and suffix arrays for advanced substring queries.

In **Chapter 33: Advanced Trees**, we will explore balanced BSTs (AVL, Red-Black), B-Trees, and advanced tree techniques like Heavy-Light Decomposition and Euler Tour that appear in the hardest USACO Platinum problems. The summit is almost within reach!
{% endhint %}
