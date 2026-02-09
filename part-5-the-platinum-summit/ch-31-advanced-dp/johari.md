# Johari Window: Chapter 31 — Advanced DP: Bitmask, Interval, Trees

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about advanced dynamic programming techniques.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] Basic DP: states, transitions, base cases (from Ch 23-25)
> - [ ] Bit manipulation: AND, OR, XOR, shifts (from Ch 12)
> - [ ] Tree traversal: DFS, BFS, parent-child relationships (from Ch 26)
> - [ ] Memoization vs tabulation (from Ch 23)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "bitmask DP" means and when to use it
> - [ ] What the Traveling Salesman Problem is
> - [ ] What "interval DP" means
> - [ ] How DP works on a tree (vs a 1D array or 2D grid)
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How to encode subsets as integers for DP states
> - [ ] Matrix Chain Multiplication and why parenthesization order matters
> - [ ] How to decide "pick or skip" for nodes in a tree DP
> - [ ] Digit DP and how to count numbers with specific digit properties
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
> - [ ] Bitmask DP: use an integer to represent a subset, dp[mask][...] is the state
> - [ ] The "n <= 20" rule: if n is small enough for 2^n, bitmask DP is likely the approach
> - [ ] TSP in O(2^n * n^2): state = (visited cities bitmask, current city)
> - [ ] Interval DP: dp[i][j] for subproblems on range [i..j], iterate by LENGTH
> - [ ] MCM: try all split points k, dp[i][j] = min(dp[i][k] + dp[k+1][j] + cost)
> - [ ] Burst Balloons: think about which balloon to burst LAST, not first
> - [ ] Tree DP: dp[node][0] = skip node, dp[node][1] = pick node, process leaves first
> - [ ] Digit DP: build number digit by digit, track tight constraint and state
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That TSP with bitmask DP is only O(2^n * n^2) instead of O(n!)
> - [ ] That the loop order in interval DP is critical — length first, not endpoints!
> - [ ] That "think about what happens LAST" is a powerful technique for interval DP
> - [ ] That Knuth's optimization can reduce interval DP from O(n^3) to O(n^2)
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Recognizing when a problem needs bitmask DP vs standard DP
> - [ ] Setting up the interval DP loop correctly without off-by-one errors
> - [ ] Implementing tree DP iteratively (to avoid recursion limit issues in Python)
> - [ ] Digit DP tight constraint handling — when to cap the digit and when not to
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can bitmask DP be combined with other techniques (like graphs or segment trees)?
> - [ ] What about "profile DP" where the bitmask represents a row of a grid?
> - [ ] Are there problems that need BOTH interval DP and tree DP?
> - [ ] How does the Convex Hull Trick actually work in detail?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 33 (Advanced Trees) — tree DP concepts get extended to Heavy-Light Decomposition and Euler Tour techniques!
