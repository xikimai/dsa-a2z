# Johari Window: Chapter 30 — Segment Trees & Range Queries

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about range queries, segment trees, and Fenwick trees.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] Prefix sums can answer range sum queries in O(1) (from Ch 14)
> - [ ] Binary trees: parent/child relationships, tree height is O(log n) (from Ch 26)
> - [ ] Heaps store elements in a tree backed by an array (from Ch 17)
> - [ ] Why O(n) per query is too slow when Q is large
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What a "segment tree" is and why it is called that
> - [ ] How a segment tree handles both queries and updates efficiently
> - [ ] What "lazy propagation" means
> - [ ] What a "Fenwick tree" or "Binary Indexed Tree" is
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How to build a segment tree from an array in O(n) time
> - [ ] How to implement lazy propagation for range updates
> - [ ] When to use a Fenwick tree vs a segment tree
> - [ ] How to handle non-invertible operations (like min/max) with range queries
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
> - [ ] A segment tree is a balanced binary tree where each node stores the aggregate of a range
> - [ ] Build is O(n), query and point update are both O(log n)
> - [ ] Lazy propagation defers range updates — push down only when children are visited
> - [ ] Fenwick tree (BIT) uses clever bit manipulation: add/query in O(log n) with tiny code
> - [ ] BIT works for invertible operations (sum, XOR); segment tree works for everything (min, max, GCD)
> - [ ] Segment tree array needs size 4*n to be safe (not 2*n)
> - [ ] Merge sort tree answers "count in range [lo, hi]" queries offline
> - [ ] Maximum subarray in a range needs four values per node: total, prefix max, suffix max, answer
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That the segment tree is just a recursive divide-and-conquer structure stored in an array!
> - [ ] That Fenwick trees use the "lowest set bit" trick (x & -x) — so elegant!
> - [ ] That lazy propagation is basically "procrastination that works" — defer work until needed
> - [ ] That you can put almost ANY associative operation into a segment tree (sum, min, max, GCD, XOR...)
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Getting the indexing right (0-indexed vs 1-indexed, inclusive vs exclusive ranges)
> - [ ] Remembering to push down lazy values before querying children
> - [ ] Choosing between BIT and segment tree for a given problem
> - [ ] Implementing the maximum subarray range query (four values per node is tricky)
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can you make a segment tree "persistent" so it remembers all previous versions?
> - [ ] How does a 2D segment tree work for 2D range queries?
> - [ ] Can segment trees be used to optimize DP transitions? (Ch 31 hint!)
> - [ ] What is the "Euler tour" trick that turns subtree queries into range queries? (Ch 33 hint!)
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 31 (Advanced DP) and Ch 33 (Advanced Trees) — segment trees are the backbone of many Platinum-level optimizations!
