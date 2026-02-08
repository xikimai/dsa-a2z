# Johari Window: Chapter 22 — Stacks & Queues — Order Matters

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about stacks, queues, and related data structures.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What LIFO means (Last In, First Out)
> - [ ] What FIFO means (First In, First Out)
> - [ ] That BFS uses a queue (from Ch 19)
> - [ ] That recursion uses a call stack internally (from Ch 10)
> - [ ] Using lists/arrays to store collections of data (from Ch 5)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] How a stack is different from a regular list/array
> - [ ] What a monotonic stack is and when to use it
> - [ ] How a deque differs from a regular queue
> - [ ] Why stacks are used to evaluate mathematical expressions
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to use a monotonic stack for "next greater element" problems
> - [ ] How to find the largest rectangle in a histogram
> - [ ] How to implement a Min Stack with O(1) getMin
> - [ ] What an LRU Cache is and how to build one
> - [ ] How to implement a queue using only stacks
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
> - [ ] A stack supports push/pop/peek — all O(1) — accessing only the top element
> - [ ] A queue supports enqueue/dequeue/peek — all O(1) — accessing only the front element
> - [ ] Balanced parentheses checking is a classic stack problem: push openers, pop on closers
> - [ ] A monotonic stack maintains sorted order and solves "next greater/smaller" in O(n)
> - [ ] A deque allows O(1) operations at both ends — perfect for sliding window problems
> - [ ] Postfix (RPN) expressions are evaluated naturally with a stack: push numbers, pop for operators
> - [ ] A Min Stack tracks the running minimum using an auxiliary stack — O(1) getMin
> - [ ] A queue can be built from two stacks with amortized O(1) operations
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That monotonic stacks solve problems in O(n) that seem to need O(n^2)!
> - [ ] That the "sentinel" trick in the histogram problem eliminates cleanup code
> - [ ] That C++ stack::pop() returns void — you MUST call top() first
> - [ ] That Python's `//` and `int(a/b)` give different results for negative division
> - [ ] That an LRU Cache combines a doubly linked list with a hash map for O(1) everything
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Knowing when to use a stack vs. queue vs. deque in a new problem
> - [ ] The monotonic stack pattern — which direction to iterate, what to pop
> - [ ] Implementing LRU Cache cleanly without bugs
> - [ ] Expression conversion between infix, prefix, and postfix
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How do real compilers use stacks to parse expressions and manage function calls?
> - [ ] Can monotonic stacks be combined with dynamic programming?
> - [ ] What is a "monotonic queue" and how is it different from the deque technique we learned?
> - [ ] How would I implement a browser's back/forward buttons using stacks?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 23 (DP I) — the monotonic stack optimization technique from this chapter appears again in advanced DP problems!
