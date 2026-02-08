# Johari Window: Chapter 19 — Graphs I — Exploring Networks

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about graphs, BFS, DFS, and network-style problems.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What a "network" or "graph" looks like informally (nodes and connections)
> - [ ] That a queue is FIFO and a stack is LIFO (from Ch 5 / Ch 22)
> - [ ] How recursion works — functions calling themselves (from Ch 10)
> - [ ] That hash sets give O(1) membership testing (from Ch 11)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] The difference between directed and undirected graphs
> - [ ] What "adjacency list" and "adjacency matrix" mean
> - [ ] How BFS uses a queue to explore level by level
> - [ ] How DFS uses recursion (or a stack) to go deep first
> - [ ] What a "connected component" is
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How to detect cycles in a graph
> - [ ] What "bipartite" means and how to check it
> - [ ] How to find shortest paths in an unweighted graph
> - [ ] Why DFS is WRONG for shortest paths but BFS is correct
> - [ ] How to represent a graph as code (adjacency list vs matrix)
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
> - [ ] A graph G = (V, E) is just vertices and edges — directed or undirected, weighted or unweighted
> - [ ] Adjacency list is the go-to representation: O(V+E) space, fast neighbor iteration
> - [ ] BFS uses a queue and explores level-by-level — guarantees shortest paths in unweighted graphs
> - [ ] DFS uses recursion/stack and goes deep before backtracking — does NOT guarantee shortest paths
> - [ ] Connected components = "islands" in the graph, found by BFS/DFS from each unvisited node
> - [ ] Mark visited BEFORE enqueueing in BFS (not after dequeueing) to avoid duplicate entries
> - [ ] Cycle detection in undirected graphs: if we visit a neighbor that's already visited and isn't our parent, there's a cycle
> - [ ] Bipartite check: try to 2-color the graph with BFS/DFS; if any edge has same-color endpoints, not bipartite
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That DFS gives WRONG shortest paths — it might find a long path before discovering a short one!
> - [ ] That many problems are secretly graph problems (word ladders, course schedules, mazes)
> - [ ] That cloning a graph requires a hash map to track original-to-clone mapping
> - [ ] That cycle detection in directed graphs needs THREE states (unvisited, in-progress, done), not just two
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Remembering to mark visited before enqueueing (the #1 BFS bug)
> - [ ] Choosing between BFS and DFS for different problem types
> - [ ] Converting a word problem into a graph (identifying vertices and edges)
> - [ ] Implementing iterative DFS without recursion (for large graphs)
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] What happens when edges have weights? (Hint: Dijkstra's algorithm, Ch 27!)
> - [ ] How do you find shortest paths with negative edge weights? (Bellman-Ford)
> - [ ] Can Union-Find track connected components faster than BFS/DFS? (Ch 29!)
> - [ ] How does topological sort work for ordering dependencies? (Ch 28!)
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 20 (Graphs II) — you'll apply BFS and DFS to grids, flood fill, and real contest problems!
