# Johari Window: Chapter 14 — Prefix Sums — The Running Total Trick

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about prefix sums, range queries, and subarray problems.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What a "running total" means (add numbers as you go)
> - [ ] That summing a range by looping is O(n) per query (from Ch 6)
> - [ ] That hash maps give O(1) lookups (from Ch 11)
> - [ ] The prefix sum + hash map technique from Ch 11 section 11.6
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] Why prefix sums need an array of length n+1 (not n)
> - [ ] How to get the sum of a range from two prefix values
> - [ ] What a "difference array" is and how it relates to prefix sums
> - [ ] How Kadane's algorithm works for maximum subarray sum
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to do prefix sums on a 2D grid (matrix)
> - [ ] How to apply range updates in O(1) per update
> - [ ] The inclusion-exclusion formula for 2D rectangle queries
> - [ ] How to count subarrays divisible by K using prefix sums
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
> - [ ] prefix[i] stores the sum of arr[0..i-1], and prefix[0] = 0 as a sentinel
> - [ ] Range sum formula: sum(l, r) = prefix[r+1] - prefix[l]
> - [ ] Building prefix sums is O(n) precomputation for O(1) queries — "trade space for time"
> - [ ] Difference arrays are the INVERSE of prefix sums — mark start/end, then prefix-sum to reconstruct
> - [ ] Kadane's: extend or restart — if running sum goes negative, start fresh
> - [ ] 2D prefix sums use inclusion-exclusion: add, subtract overlaps, add back double-subtracted corner
> - [ ] Prefix sum + hash map counts subarrays with sum K in O(n) — a Silver-level technique
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That difference arrays let you do range updates in O(1) per update, then reconstruct in O(n)!
> - [ ] That Kadane's algorithm is secretly dynamic programming (extend or restart recurrence)
> - [ ] That the maximum subarray problem has solutions from O(n^3) to O(n) — three levels of insight
> - [ ] That 2D prefix sums can answer rectangle sum queries in O(1) after O(rows * cols) preprocessing
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Getting the off-by-one indexing right every time (prefix[r+1] vs prefix[r])
> - [ ] Building 2D prefix sums without bugs in the inclusion-exclusion formula
> - [ ] Remembering to use long/long long instead of int for prefix sums
> - [ ] Recognizing when to use prefix sum + hash map vs plain prefix sum
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] What if the array changes between queries? (Hint: Segment Trees, Ch 30!)
> - [ ] Can Kadane's be modified for circular subarrays?
> - [ ] How do prefix sums extend to 3D or higher dimensions?
> - [ ] Can difference arrays handle multiplicative updates, not just additive?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 15 (Two Pointers) — sliding window builds directly on the range-query intuition from this chapter!
