# Johari Window: Chapter 32 — String Algorithms

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about string algorithms, pattern matching, and text processing.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] Strings are sequences of characters (from Ch 5)
> - [ ] Hash maps can store and look up values in O(1) average time (from Ch 11)
> - [ ] Brute-force string search: check every position (from Ch 9)
> - [ ] Recursion and recursive data structures (from Ch 10)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What a "Trie" or "prefix tree" is
> - [ ] How pattern matching can be faster than checking every position
> - [ ] What "rolling hash" means
> - [ ] Why KMP is called "Knuth-Morris-Pratt"
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How the KMP failure function works
> - [ ] What the Z-function / Z-array is
> - [ ] How Rabin-Karp uses hashing for string matching
> - [ ] What a suffix array is and what it is used for
> - [ ] _________________________________

### Unknown (I have not even thought about)
> Things I don't know that I don't know — leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open — Expanded (Now I truly understand)
> - [ ] Tries store words character-by-character in a tree; shared prefixes share nodes
> - [ ] KMP's failure function tells you where to resume matching after a mismatch
> - [ ] Z-function computes the longest prefix match at every position in O(n)
> - [ ] Rabin-Karp computes a rolling hash that can be updated in O(1) per slide
> - [ ] Hash collisions are possible — always verify Rabin-Karp matches
> - [ ] KMP and Z-function both achieve O(n+m) guaranteed time
> - [ ] Suffix arrays sort all suffixes; LCP array measures shared prefixes between neighbors
> - [ ] The decision table: Trie for prefixes, KMP/Z for matching, hashing for quick coding
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That KMP's failure function and the Z-array encode the SAME information differently!
> - [ ] That you never go backward in the text during KMP — only in the pattern
> - [ ] That Trie memory can blow up fast (26 pointers per node)
> - [ ] That Python's `%` is always non-negative but Java/C++ `%` can be negative
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Building the KMP failure function without off-by-one errors
> - [ ] Choosing the right base and modulus for Rabin-Karp
> - [ ] Knowing when to use a Trie vs hashing vs KMP
> - [ ] Suffix array construction (the doubling trick is complex)
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does Aho-Corasick extend tries for multi-pattern matching?
> - [ ] Can suffix arrays solve problems that KMP/Z-function cannot?
> - [ ] What is a suffix automaton and how does it compare to suffix arrays?
> - [ ] How do real search engines handle pattern matching at massive scale?
> - [ ] _________________________________

---

**Tip:** Revisit this page after attempting USACO Platinum string problems — you will be amazed how much these algorithms simplify seemingly impossible tasks!
