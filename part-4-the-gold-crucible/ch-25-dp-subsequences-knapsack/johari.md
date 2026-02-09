# Johari Window: Chapter 25 — Dynamic Programming III — Subsequences & Knapsack

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about knapsack problems, subsequences, and DP on strings.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] The DP Recipe: state, recurrence, base case, fill order, space optimization (from Ch 23)
> - [ ] How to convert between top-down and bottom-up DP (from Ch 23)
> - [ ] DP on 2D grids (from Ch 24)
> - [ ] What a subsequence is (a sequence that maintains order but can skip elements)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What the "Knapsack problem" is and why it matters
> - [ ] The difference between 0/1 Knapsack and Unbounded Knapsack
> - [ ] What "Longest Common Subsequence" means
> - [ ] How edit distance relates to DP
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How to get LIS in O(n log n) instead of O(n^2)
> - [ ] What "coin change" and "subset sum" problems are
> - [ ] How to reconstruct a solution (not just its value) from a DP table
> - [ ] What wildcard matching has to do with DP
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
> - [ ] 0/1 Knapsack: iterate backwards in 1D DP so items are used at most once
> - [ ] Unbounded Knapsack: iterate forwards — that one direction change allows reuse
> - [ ] Subset Sum is Knapsack with boolean values (can we reach this sum?)
> - [ ] Coin Change (min coins) uses unbounded knapsack with min instead of max
> - [ ] Coin Change (count ways) uses coins-first loop to count combinations, not permutations
> - [ ] LCS builds a 2D table — match extends diagonal, mismatch takes max of up/left
> - [ ] Edit Distance is like LCS but with three operations: insert, delete, replace
> - [ ] LIS can be solved in O(n^2) with dp[i] = max(dp[j]+1), or O(n log n) with patience sorting
> - [ ] Many string DP problems reduce to LCS: palindromic subsequence, SCS, min insertions
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That "backwards vs. forwards iteration" is the ONLY difference between 0/1 and unbounded knapsack!
> - [ ] That Target Sum reduces to Subset Sum Count through algebra (P = (total+target)/2)
> - [ ] That minimum insertions for palindrome = len(s) - LCS(s, reverse(s))
> - [ ] That the O(n log n) LIS algorithm was discovered through a card game (patience sorting)
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Recognizing which knapsack variant a new problem maps to
> - [ ] Deciding between 0/1, unbounded, and counting versions
> - [ ] Reconstructing the actual answer (not just the optimal value) from a DP table
> - [ ] The O(n log n) LIS with binary search — conceptually clear but tricky to implement
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can DP solve problems on trees, not just arrays and strings?
> - [ ] What is bitmask DP and when would I need it?
> - [ ] How do competitive programmers decide between DP and greedy on contest problems?
> - [ ] Are there problems where knapsack is NP-hard but DP gives a pseudo-polynomial solution?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 26 (Trees) and Ch 31 (Advanced DP) — the patterns from this chapter appear in tree DP, interval DP, and bitmask DP!
