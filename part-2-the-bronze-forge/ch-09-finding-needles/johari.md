# Johari Window: Finding Needles — The Power of Searching

Use this worksheet to track your understanding before and after studying Chapter 9.

---

## Before This Chapter

Fill this out BEFORE you read the chapter. Be completely honest — there's no wrong answer here, only honest ones.

### I Know Well (Open)
> Things I'm confident I understand and could explain to a friend.

- [ ] What "searching" means (looking for something in a collection)
- [ ] How to use Python's `in` operator or Java's `.contains()`
- [ ] That sorted data is useful for finding things faster (from Ch 8)
- [ ] _____________________________________
- [ ] _____________________________________

### I Think I Know But I'm Not Sure (Hidden)
> Things I've heard of but couldn't confidently explain or code from scratch.

- [ ] How binary search works (something about halving the search space?)
- [ ] Why O(log n) is so much faster than O(n) for searching
- [ ] What "lower bound" and "upper bound" mean
- [ ] How to handle a sorted array that's been "rotated"
- [ ] _____________________________________

### I Know I Don't Know (Blind Spot)
> Things I'm aware exist but haven't learned yet.

- [ ] How to implement binary search from scratch (without bugs!)
- [ ] How to find the first/last occurrence of a repeated element
- [ ] How binary search works on rotated sorted arrays
- [ ] What a "peak element" is and how to find it efficiently
- [ ] _____________________________________

### I Haven't Even Thought About (Unknown)
> Leave this blank for now. You'll fill it in after the chapter when you discover things you didn't even know existed!

- [ ] _____________________________________
- [ ] _____________________________________
- [ ] _____________________________________

---

## After This Chapter

Fill this out AFTER you complete the chapter. Compare with your "Before" answers!

### Now I Truly Understand (Open — Expanded)
> Things that moved from "Hidden" or "Blind Spot" to genuine understanding.

- [ ] Linear search: check each element, O(n). Simple but slow for large data
- [ ] Binary search: pick the middle, compare, eliminate half. O(log n) on sorted data
- [ ] First/Last occurrence: modify binary search to keep going left/right after finding the target
- [ ] Lower bound: first index where arr[i] >= target. Upper bound: first index where arr[i] > target
- [ ] Floor and ceil: largest element <= target and smallest element >= target
- [ ] Rotated sorted array: one half is ALWAYS sorted — use that to decide which half to search
- [ ] Peak element: binary search works even on unsorted data when there's a monotonic property
- [ ] Single element in sorted array: binary search on pair parity (even/odd index pattern)
- [ ] Proof by contradiction: assume the opposite, show it leads to impossibility
- [ ] _____________________________________

### Surprised Me! (Was Unknown/Blind, Now Open)
> Things you didn't expect to learn or that changed how you think about coding.

- _____________________________________
- _____________________________________
- _____________________________________

### Still Working On (Honest Self-Assessment)
> Things you understand in theory but need more practice with.

- _____________________________________
- _____________________________________
- _____________________________________

### Questions I Now Have (New Curiosity)
> New questions that popped up while studying. These are GREAT — they mean you're thinking deeply!

- _____________________________________
- _____________________________________
- _____________________________________

---

## Reflection

1. **Linear search is O(n) because ___. Binary search is O(log n) because ___.**

   _____________________________________

2. **Binary search requires sorted data because ___.**

   _____________________________________

3. **The mid-point formula uses `lo + (hi - lo) / 2` instead of `(lo + hi) / 2` because ___.**

   _____________________________________

4. **In a rotated sorted array, you can still use binary search because ___.**

   _____________________________________

5. **The proof by contradiction for binary search says: "If the target were in the array, then ___."**

   _____________________________________
