# Johari Window: Chapter 23 — Dynamic Programming I — The Foundation

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about Dynamic Programming, memoization, and optimization.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What recursion is and how to write recursive functions (from Ch 10)
> - [ ] How to analyze time complexity of recursive code (from Ch 6)
> - [ ] That memoization caches function results to avoid recomputation (from Ch 10)
> - [ ] The difference between O(n) and O(2^n) — exponential is very slow
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "Dynamic Programming" actually means
> - [ ] The difference between top-down (memoization) and bottom-up (tabulation)
> - [ ] What "overlapping subproblems" and "optimal substructure" mean
> - [ ] How to decide if a problem needs DP vs. greedy vs. brute force
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to write a DP recurrence from scratch
> - [ ] How to optimize DP space from O(n) to O(1)
> - [ ] How stock buy/sell problems use state-machine DP
> - [ ] What Kadane's algorithm is
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
> - [ ] DP = solving overlapping subproblems once and storing results
> - [ ] Top-down adds a cache to recursion; bottom-up fills a table iteratively
> - [ ] The DP Recipe: state, recurrence, base case, fill order, space optimization
> - [ ] Climbing Stairs is Fibonacci in disguise: dp[n] = dp[n-1] + dp[n-2]
> - [ ] House Robber uses the take-or-skip pattern: dp[i] = max(dp[i-1], dp[i-2]+nums[i])
> - [ ] Kadane's algorithm is DP with O(1) space: extend or restart the subarray
> - [ ] Stock problems use state-machine DP with states like held/sold/rest
> - [ ] The four-stage progression: recursion, memo, tabulation, space-optimized
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That pure recursion for Fibonacci does over 40 BILLION redundant calls for n=50!
> - [ ] That the name "Dynamic Programming" was chosen to impress politicians, not describe the technique
> - [ ] That stock problems with cooldown and fees all follow the same state-machine pattern
> - [ ] That space optimization just requires tracking the last 2-3 values instead of the whole array
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Quickly identifying whether a new problem is DP, greedy, or something else
> - [ ] Writing the recurrence for unfamiliar DP problems
> - [ ] Converting top-down to bottom-up confidently
> - [ ] Choosing the right state definition for complex problems
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does DP work on 2D grids instead of 1D arrays?
> - [ ] What is the "knapsack" problem and how does DP solve it?
> - [ ] Can DP handle problems on trees or graphs, not just arrays?
> - [ ] What is bitmask DP and when would I need it?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 24 (Grid DP) and Ch 25 (Knapsack) — the patterns from this chapter extend beautifully into two dimensions!
