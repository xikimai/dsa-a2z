# Johari Window: The Art of Sorting — Putting Things in Order

Use this worksheet to track your understanding before and after studying Chapter 8.

---

## Before This Chapter

Fill this out BEFORE you read the chapter. Be completely honest — there's no wrong answer here, only honest ones.

### I Know Well (Open)
> Things I'm confident I understand and could explain to a friend.

- [ ] What "sorted" means (smallest to largest)
- [ ] How to use Python's `sorted()` or `.sort()`
- [ ] That O(n^2) is slower than O(n log n) for large inputs (from Ch 6)
- [ ] _____________________________________
- [ ] _____________________________________

### I Think I Know But I'm Not Sure (Hidden)
> Things I've heard of but couldn't confidently explain or code from scratch.

- [ ] How bubble sort works (something about swapping adjacent elements?)
- [ ] The difference between O(n^2) and O(n log n) sorting algorithms
- [ ] What "stable sort" means and why it matters
- [ ] How to sort with a custom comparator (not just smallest-to-largest)
- [ ] _____________________________________

### I Know I Don't Know (Blind Spot)
> Things I'm aware exist but haven't learned yet.

- [ ] How merge sort works (divide and conquer)
- [ ] How quick sort works (partitioning around a pivot)
- [ ] What algorithm Python/Java/C++ use internally for their built-in sort
- [ ] How to count inversions using merge sort
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

- [ ] Selection sort: find the minimum, swap to front, repeat. O(n^2) always
- [ ] Bubble sort: swap adjacent pairs, largest bubbles to end. O(n^2) worst, O(n) best with early termination
- [ ] Insertion sort: insert each element into its correct position in the sorted prefix. O(n) best case on nearly-sorted data
- [ ] Merge sort: split in half, recursively sort each half, merge. O(n log n) always, stable, needs O(n) extra space
- [ ] Quick sort: pick a pivot, partition, recursively sort each side. O(n log n) avg, O(n^2) worst
- [ ] Built-in sorts: Python uses TimSort, Java uses dual-pivot quicksort (primitives) / TimSort (objects), C++ uses IntroSort
- [ ] Custom comparators: Python `key=`, Java `Comparator.comparing()`, C++ lambda
- [ ] Counting inversions with modified merge sort in O(n log n)
- [ ] Proof by induction: base case + inductive step, like falling dominos
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

1. **Selection sort is O(n^2) because ___. Merge sort is O(n log n) because ___.**

   _____________________________________

2. **Bubble sort with early termination is O(n) on best case because ___.**

   _____________________________________

3. **Merge sort is stable but quick sort is not because ___.**

   _____________________________________

4. **Built-in sort in Python uses ___, in Java uses ___, in C++ uses ___.**

   _____________________________________

5. **The proof by induction for merge sort has base case ___ and inductive step ___.**

   _____________________________________
