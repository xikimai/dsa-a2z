# Johari Window: Chapter 20 --- Graphs II --- Real Problems

Use this worksheet **before** and **after** studying the chapter. Be honest --- there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about grid graphs, flood fill, and multi-source BFS.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] BFS explores level-by-level and finds shortest paths (from Ch 19)
> - [ ] DFS goes deep before backtracking (from Ch 19)
> - [ ] A 2D grid has rows and columns, and I can loop through it
> - [ ] A queue is FIFO and a deque supports both ends (from Ch 5 / Ch 19)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] How a 2D grid can be treated as a graph
> - [ ] What "flood fill" means and how it relates to the paint bucket tool
> - [ ] How BFS can start from multiple sources at the same time
> - [ ] What "connected component" means in the context of a grid
> - [ ] What 0-1 BFS is and when to use it
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to count the number of islands in a grid
> - [ ] How to find the distance from each cell to the nearest 0
> - [ ] How to determine which regions are "surrounded" vs connected to the border
> - [ ] How to use a deque for shortest paths with 0/1 edge weights
> - [ ] How to combine BFS with binary search for optimization problems
> - [ ] _________________________________

### Unknown (I haven't even thought about)
> Things I don't know that I don't know --- leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open --- Expanded (Now I truly understand)
> - [ ] A 2D grid IS a graph: each cell is a node, 4-directional neighbors are edges
> - [ ] Flood fill is BFS/DFS that colors all connected same-value cells --- used in paint bucket, counting islands, etc.
> - [ ] Number of islands = count connected components by scanning and flood-filling each new land cell
> - [ ] Multi-source BFS: enqueue ALL sources at the start, then BFS naturally processes them simultaneously
> - [ ] Rotten oranges: multi-source BFS where each level = one minute of spreading
> - [ ] 01 Matrix: multi-source BFS from all 0-cells gives distance to nearest 0
> - [ ] Surrounded regions: use the border-first trick --- BFS from border O's, then flip the rest
> - [ ] 0-1 BFS: use a deque, add cost-0 neighbors to front, cost-1 to back
> - [ ] Direction arrays (`dr/dc`) eliminate copy-pasted neighbor checks
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That multi-source BFS is exactly like single-source BFS, just with all sources enqueued at the start!
> - [ ] That the "border-first trick" flips the problem: instead of checking "is it surrounded?", check "is it connected to the border?"
> - [ ] That 0-1 BFS is O(V+E) --- faster than Dijkstra's O(E log V) for the special case of 0/1 weights
> - [ ] That Union-Find can also count islands (preview of Ch 29!)
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Remembering to check `if original == color` at the start of flood fill
> - [ ] Marking visited BEFORE enqueueing (not after popping)
> - [ ] Choosing between DFS and BFS for different grid problems
> - [ ] Setting up multi-source BFS correctly (enqueue ALL sources first)
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] What happens with weighted grid problems where weights are not just 0/1? (Hint: Dijkstra, Ch 27!)
> - [ ] Can Union-Find solve grid problems more efficiently than BFS/DFS? (Ch 29!)
> - [ ] How do I handle grids that wrap around (toroidal grids)?
> - [ ] What about 3D grids --- does the same BFS pattern work?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 27 (Shortest Paths) and Ch 29 (Union-Find) --- you'll see how the grid graph patterns from this chapter extend to weighted graphs and dynamic connectivity!
