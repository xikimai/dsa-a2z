# Johari Window: Chapter 15 — Two Pointers & Sliding Window — The Caterpillar Method

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about two pointers, sliding windows, and processing contiguous subarrays.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] How to merge two sorted arrays using two pointers (from Ch 8 merge sort)
> - [ ] That checking all pairs is O(n^2) and we want to do better
> - [ ] What a contiguous subarray/substring is
> - [ ] How prefix sums can compute range sums in O(1) (from Ch 14)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] Why two pointers on a sorted array is O(n) instead of O(n^2)
> - [ ] What "sliding window" means and how it differs from brute force
> - [ ] How to decide which pointer to move and why
> - [ ] The difference between fixed-size and variable-size windows
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to find three numbers that sum to zero efficiently
> - [ ] How to compute "trapping rain water" or "container with most water"
> - [ ] How to find the longest substring without repeating characters
> - [ ] How to find the minimum window substring containing all target characters
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
> - [ ] Converging two pointers on sorted arrays find pairs in O(n)
> - [ ] Same-direction (fast/slow) pointers partition arrays in-place in O(n)
> - [ ] Fixed-size sliding windows maintain a running computation for O(1) per slide
> - [ ] Variable-size sliding windows expand and shrink to find optimal subarrays/substrings
> - [ ] Sliding window + hash map tracks character frequencies for string problems
> - [ ] Three Sum reduces to sort + Two Sum with duplicate skipping
> - [ ] Trapping Rain Water uses two pointers with left_max and right_max tracking
> - [ ] The Dutch National Flag uses three pointers for three-way partition in one pass
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That sliding windows only work for positive arrays when tracking sums — negatives break monotonicity!
> - [ ] That Container With Most Water has such an elegant O(n) solution by moving the shorter side
> - [ ] That Three Sum needs duplicate skipping in THREE separate places
> - [ ] That every element enters and leaves the window at most once, guaranteeing O(n) total
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Recognizing whether a problem needs two pointers vs sliding window vs prefix sums
> - [ ] Getting the window boundaries right (off-by-one errors)
> - [ ] Implementing minimum window substring from scratch
> - [ ] Knowing when to sort first vs when sorting isn't needed
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can I find the maximum element in a sliding window in O(1) instead of O(k)?
> - [ ] How do slow/fast pointers work in linked lists for cycle detection?
> - [ ] What about Four Sum? Does the pattern keep generalizing?
> - [ ] When does sliding window beat prefix sums, and vice versa?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 21 (Linked Lists) — the slow/fast pointer technique from this chapter returns as the "tortoise and hare" for cycle detection!
