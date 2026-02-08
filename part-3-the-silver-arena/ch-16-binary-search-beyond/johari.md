# Johari Window: Chapter 16 — Binary Search Beyond Arrays — Searching on Answers

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about binary search beyond simple array lookups.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] Binary search on a sorted array to find a target element (from Ch 9)
> - [ ] That binary search runs in O(log n) time
> - [ ] The concept of "sorted" meaning elements are in order
> - [ ] How to compute floor/ceiling of division
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "binary search on the answer" means
> - [ ] How to handle rotated sorted arrays
> - [ ] What a "monotonic predicate" is and why it matters for binary search
> - [ ] How a 2D matrix can be treated as a 1D sorted array
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to find the minimum eating speed (Koko's Bananas problem)
> - [ ] How to maximize the minimum distance between objects (Aggressive Cows)
> - [ ] How to find the median of two sorted arrays in O(log n) time
> - [ ] How to minimize the maximum workload across workers (Painter's Partition)
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
> - [ ] Binary search works on ANY monotonic predicate, not just sorted arrays
> - [ ] "BS on answers" converts optimization problems into decision problems
> - [ ] The feasibility function returns True/False, and binary search finds the boundary
> - [ ] "Find minimum feasible" uses `hi = mid`; "find maximum feasible" uses `lo = mid` with round-up
> - [ ] Koko's Bananas, Ship Packages, and Painter's Partition all share the same template
> - [ ] Aggressive Cows is "maximize the minimum" — the dual of "minimize the maximum"
> - [ ] A fully sorted matrix maps to a 1D array via `row = idx // cols, col = idx % cols`
> - [ ] Median of Two Sorted Arrays uses binary search on the partition point of the shorter array
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That "minimize the maximum" and "maximize the minimum" are essentially the same technique with different templates!
> - [ ] That the ceiling division trick `(a + b - 1) / b` avoids floating-point entirely
> - [ ] That the infinite-loop bug with `lo = mid` is fixed by rounding mid UP — such a subtle detail!
> - [ ] That Painter's Partition and Ship Packages are structurally identical problems
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Writing the feasibility function correctly on first attempt
> - [ ] Choosing the right search space bounds (lo and hi)
> - [ ] Remembering when to round mid up vs down
> - [ ] Understanding the median of two sorted arrays partition approach
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can binary search on answers work with floating-point answers, not just integers?
> - [ ] What if the feasibility function itself is expensive — like O(n^2)? Is BS on answers still worth it?
> - [ ] Are there problems where the predicate looks monotonic but isn't?
> - [ ] How does binary search relate to ternary search for unimodal functions?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 25 (DP — Subsequences & Knapsack) — the Longest Increasing Subsequence uses binary search internally to achieve O(n log n), combining ideas from this chapter with dynamic programming!
