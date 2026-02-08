# Johari Window: Chapter 11 — Hashing — The Secret Decoder Ring

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about hash tables, sets, maps, and O(1) lookups.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What a set is and how to check membership (from Ch 5)
> - [ ] What a dictionary/map is and how to store key-value pairs (from Ch 5)
> - [ ] That `x in set` is O(1) while `x in list` is O(n) (from Ch 6)
> - [ ] That memoization uses dictionaries to cache results (from Ch 10)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] How a hash table actually turns a key into an array index
> - [ ] What happens when two keys "collide" (map to the same spot)
> - [ ] Why hash lookups are O(1) on average but O(n) in the worst case
> - [ ] The difference between `HashMap` and `TreeMap` (Java) or `unordered_map` and `map` (C++)
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to solve "subarray sum" problems using hashing
> - [ ] How to group anagrams efficiently
> - [ ] What the "complement technique" is (finding pairs with a target sum in one pass)
> - [ ] How XOR can find a missing number without extra space
> - [ ] _________________________________

### Unknown (I haven't even thought about)
> Things I don't know that I don't know — leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open — Expanded (Now I truly understand)
> - [ ] A hash function converts keys to array indices for O(1) access
> - [ ] Chaining and open addressing are two ways to handle collisions
> - [ ] Hash sets answer "is X present?" in O(1) — perfect for deduplication
> - [ ] Hash maps store key→value pairs for O(1) frequency counting and lookups
> - [ ] The frequency counting pattern: iterate once, build a count map
> - [ ] The complement technique: for each element, check if target-element exists in the map
> - [ ] Prefix sum + hash map solves subarray sum problems in O(n)
> - [ ] Sorted-string keys group anagrams efficiently
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That the "Missing Number" problem has FOUR completely different approaches (sort, XOR, math, hash)!
> - [ ] That prefix sum + hash map can count subarrays with a given sum in O(n)
> - [ ] That the complement technique turns O(n²) pair-finding into O(n)
> - [ ] That hash collisions can make O(1) degrade to O(n) with adversarial inputs
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Recognizing when a problem needs hashing vs. sorting vs. two pointers
> - [ ] The prefix sum + hash map technique for subarray problems
> - [ ] Understanding when to use hash containers vs. ordered containers
> - [ ] Choosing the right data structure for the right problem
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does the hash function ACTUALLY work internally? What makes a "good" hash?
> - [ ] Can we hash more complex objects like arrays or trees?
> - [ ] What is "rolling hash" and how does it help with string matching?
> - [ ] When would O(log n) ordered containers beat O(1) hash containers?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 14 (Prefix Sums) — the prefix sum + hash map technique from this chapter becomes a whole chapter of its own!
