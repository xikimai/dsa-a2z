# Johari Window: Chapter 29 — Union-Find & Minimum Spanning Trees

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about connectivity, Union-Find, and spanning trees.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What a connected component is in a graph (from Ch 19-20)
> - [ ] BFS/DFS can check if two nodes are connected (from Ch 19-20)
> - [ ] What a tree is: a connected graph with n-1 edges and no cycles (from Ch 26)
> - [ ] Greedy algorithms and when they work (from Ch 18)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "Union-Find" or "Disjoint Set Union" means
> - [ ] What a "spanning tree" is
> - [ ] Why Kruskal's or Prim's algorithm gives the cheapest network
> - [ ] What "path compression" does and why it matters
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How to implement Union-Find with both path compression and union by rank
> - [ ] The inverse Ackermann function and amortized analysis of Union-Find
> - [ ] How Kruskal's algorithm uses Union-Find internally
> - [ ] The "cut property" that proves MST correctness
> - [ ] _________________________________

### Unknown (I have not even thought about)
> Things I don't know that I don't know — leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open — Expanded (Now I truly understand)
> - [ ] Union-Find: parent array + find (with path compression) + union (with rank)
> - [ ] Path compression makes every node point directly to the root — flattens the tree
> - [ ] Union by rank attaches the shorter tree under the taller tree — keeps things balanced
> - [ ] Together they give amortized O(alpha(n)) per operation — effectively O(1)
> - [ ] Kruskal's: sort edges by weight, add if no cycle (use Union-Find to check)
> - [ ] Prim's: grow MST from a start vertex using a min-heap, always pick cheapest edge
> - [ ] MST has exactly n-1 edges for n vertices
> - [ ] Cut property: the lightest crossing edge for any cut is in some MST
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That Union-Find with both optimizations is practically O(1) per operation!
> - [ ] That Kruskal's and Prim's were published in the SAME YEAR (1956) as Dijkstra's algorithm
> - [ ] That cycle detection in undirected graphs is trivial with Union-Find
> - [ ] That so many seemingly different problems (accounts merge, stones, equations) are really Union-Find
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Recognizing when a problem is really a connectivity/Union-Find problem in disguise
> - [ ] Choosing between Kruskal's and Prim's for a given problem
> - [ ] Handling 1-indexed vs 0-indexed nodes without bugs
> - [ ] The exchange argument proof — I get the intuition but the formal proof is tricky
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can Union-Find support "undo" operations (rollback)?
> - [ ] What is the second minimum spanning tree and how do you find it?
> - [ ] How do segment trees (Ch 30) compare to Union-Find for different query types?
> - [ ] Are there problems where you need BOTH Union-Find AND shortest paths?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 30 (Segment Trees) and Part V — Union-Find concepts reappear in advanced graph algorithms and offline query processing!
