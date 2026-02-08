# Johari Window: Chapter 13 — Bronze Battle Plan — Complete Search & Simulation

Use this worksheet **before** and **after** studying the chapter. Be honest -- there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about brute force, backtracking, and simulation.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] That recursion lets a function call itself with smaller inputs (from Ch 10)
> - [ ] That bitmasks can represent sets of elements using individual bits (from Ch 12)
> - [ ] That O(2^n) and O(n!) are very large but sometimes acceptable for small n
> - [ ] That simulation means following rules step by step
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "backtracking" actually means and how it differs from plain recursion
> - [ ] How to systematically generate all subsets or permutations
> - [ ] What "pruning" means in the context of search
> - [ ] When brute force is the RIGHT approach vs. when you need something smarter
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to solve N-Queens or Sudoku programmatically
> - [ ] The "choose, explore, un-choose" backtracking pattern
> - [ ] How bitmask subsets work (connecting Ch 12 bit ops to combinatorics)
> - [ ] How to read USACO constraints to decide on an approach
> - [ ] _________________________________

### Unknown (I haven't even thought about)
> Things I don't know that I don't know -- leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open -- Expanded (Now I truly understand)
> - [ ] Complete search means trying every candidate and checking validity
> - [ ] Backtracking = recursion + choose/explore/un-choose pattern
> - [ ] Simulation = follow the rules exactly, step by step
> - [ ] Bitmask subset generation: mask 0..2^n-1, check bits to build subsets
> - [ ] N-Queens uses column/diagonal sets for O(1) conflict checking
> - [ ] Sudoku solver: find empty cell, try 1-9, validate, recurse, backtrack
> - [ ] Pruning cuts branches that can't lead to valid solutions
> - [ ] Constraint table: n <= 20 means 2^n, n <= 10 means n!, n <= 1000 means O(n^2)
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That most USACO Bronze problems are designed for brute force!
> - [ ] That sorting before backtracking enables powerful pruning
> - [ ] That the same backtracking template works for permutations, subsets, queens, and Sudoku
> - [ ] That "overthinking" is the #1 mistake at Bronze level
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Knowing when to use backtracking vs. bitmask vs. nested loops
> - [ ] Implementing backtracking without forgetting to undo choices
> - [ ] Designing effective pruning strategies
> - [ ] Reading problem constraints to choose the right approach
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does dynamic programming relate to backtracking with memoization?
> - [ ] Can constraint propagation solve Sudoku without guessing?
> - [ ] What is "meet in the middle" for n around 25-30?
> - [ ] How do real chess engines decide which branches to prune?
> - [ ] _________________________________

---

**Milestone:** You have completed Part II: The Bronze Forge! Revisit this page after attempting your first USACO Bronze contest. How did it go?
