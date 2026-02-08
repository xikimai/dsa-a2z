# Johari Window: Chapter 21 — Linked Lists — Pointers and Connections

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about linked lists, pointers, and node-based data structures.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What an array is and how to access elements by index (from Ch 5)
> - [ ] That inserting into the middle of an array requires shifting elements (from Ch 5)
> - [ ] What recursion is and how recursive functions work (from Ch 10)
> - [ ] What a pointer/reference is (a variable that "points to" another object)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What a "linked list" is and how it differs from an array
> - [ ] Why linked lists are good for insertion but bad for random access
> - [ ] What "null pointer" means and why it crashes programs
> - [ ] How to reverse a linked list
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to detect a cycle (loop) in a linked list
> - [ ] What "slow and fast pointer" technique is
> - [ ] How to merge two sorted linked lists
> - [ ] What a doubly linked list is and when to use it
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
> - [ ] A linked list is a chain of nodes, each with a value and a "next" pointer
> - [ ] Insertion at the head is O(1) — no shifting needed (unlike arrays)
> - [ ] Access by index is O(n) — you must walk the chain from the head
> - [ ] The 3-pointer iterative reversal: prev, current, next — rewire one node at a time
> - [ ] Floyd's cycle detection: slow pointer (1 step), fast pointer (2 steps) — they meet inside a loop
> - [ ] Slow/fast pointers find the middle node in one pass
> - [ ] The dummy node trick simplifies edge cases when the head might change
> - [ ] Doubly linked lists have both next and prev pointers for O(1) deletion
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That the same slow/fast pointer setup solves BOTH cycle detection AND middle finding!
> - [ ] That reversing a linked list only needs 4 lines of code (but those 4 lines are tricky)
> - [ ] That two pointers switching lists can find the intersection in O(1) space
> - [ ] That linked lists are the foundation for stacks, queues, and hash table chaining
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Drawing pointer diagrams on paper before coding
> - [ ] Handling null checks without over-checking or under-checking
> - [ ] The recursive reversal (understanding how the call stack unwinds)
> - [ ] Knowing when to use a linked list vs. an array in practice
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does the LRU Cache use a doubly linked list + hash map together?
> - [ ] What is a skip list and can it give O(log n) search on a linked list?
> - [ ] How do real memory allocators use linked lists internally?
> - [ ] Could I implement a linked list using array indices instead of pointers?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 22 (Stacks & Queues) — you'll see how linked lists become the backbone of those data structures!
