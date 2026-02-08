# Johari Window: Chapter 17 — Heaps & Priority Queues — The VIP Line

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about heaps, priority queues, and the idea of "always processing the most important item first."

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What a binary tree looks like (parent, left child, right child)
> - [ ] That sorting gives you ordered access but costs O(n log n) up front
> - [ ] How arrays store elements by index in O(1) (from Ch 5)
> - [ ] That different data structures have different strengths (from Ch 6)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What a "heap" is and how it differs from a sorted array
> - [ ] What "priority queue" means and when you'd use one
> - [ ] How a tree can be stored inside a flat array
> - [ ] Why Python's `heapq` only does min-heap (and how to get max-heap)
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to insert into a heap and maintain the heap property
> - [ ] How to efficiently find the Kth largest element without fully sorting
> - [ ] How to merge K sorted arrays efficiently
> - [ ] How to find a running median from a stream of numbers
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
> - [ ] A heap is a complete binary tree where every parent beats its children (min or max)
> - [ ] Heaps are stored as arrays: parent at i, children at 2i+1 and 2i+2
> - [ ] Insert = add at end, bubble UP; Extract = remove root, bubble DOWN
> - [ ] Building a heap from scratch is O(n), not O(n log n)!
> - [ ] Python heapq is min-heap only; negate values for max-heap
> - [ ] Java PriorityQueue is min-heap; use Collections.reverseOrder() for max
> - [ ] C++ priority_queue is max-heap; use greater<int> for min
> - [ ] A heap of size k gives you the Kth largest/smallest in O(n log k)
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That you can find the Kth largest element in O(n) average time with quickselect!
> - [ ] That the "two-heap" trick (max-heap + min-heap) finds a running median in O(log n) per insert
> - [ ] That you can merge K sorted arrays in O(N log K) using a min-heap of size K
> - [ ] That heaps are behind Dijkstra's algorithm, Huffman coding, and operating system schedulers
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Knowing when to use a heap vs. sorting vs. a balanced BST
> - [ ] The "lazy deletion" technique for heaps
> - [ ] Implementing heap operations from scratch (not just using library functions)
> - [ ] The two-heap median technique — it's clever but tricky to get right
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does Dijkstra's shortest path algorithm use a priority queue? (Ch 27)
> - [ ] What are Fibonacci heaps and why do they have better amortized bounds?
> - [ ] How do operating systems use priority queues for process scheduling?
> - [ ] Can heaps help with greedy algorithms? (Spoiler: yes — Ch 18!)
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 18 (Greedy Algorithms) — many greedy problems use heaps as their core data structure! And again after Ch 27 (Shortest Paths), where Dijkstra's algorithm brings heaps to life.
