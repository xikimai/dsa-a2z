# Johari Window: Chapter 27 — Shortest Paths — Finding the Best Route

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about shortest path algorithms and weighted graphs.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] BFS finds shortest paths in unweighted graphs (from Ch 19-20)
> - [ ] Adjacency lists and how to build them from edge lists (from Ch 19)
> - [ ] How a priority queue / min-heap works (from Ch 17)
> - [ ] The greedy paradigm — make the locally best choice (from Ch 18)
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What Dijkstra's algorithm does and why it is important
> - [ ] Why Dijkstra fails on graphs with negative edge weights
> - [ ] What "relaxation" of an edge means
> - [ ] The difference between single-source and all-pairs shortest paths
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] Bellman-Ford algorithm and how it handles negative weights
> - [ ] Floyd-Warshall algorithm for all-pairs shortest paths
> - [ ] 0-1 BFS and when to use a deque instead of a priority queue
> - [ ] How to detect negative cycles in a graph
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
> - [ ] Dijkstra's algorithm: greedy + min-heap, always pop closest node, relax neighbors
> - [ ] Why Dijkstra needs non-negative weights: the greedy "finalize on pop" trick fails with negatives
> - [ ] Bellman-Ford: relax ALL edges V-1 times, handles negative weights, detects negative cycles on round V
> - [ ] Floyd-Warshall: all-pairs in O(V^3), the k-loop MUST be outermost
> - [ ] 0-1 BFS: deque trick — push weight-0 edges to front, weight-1 edges to back, O(V+E)
> - [ ] Grid shortest paths: BFS for unweighted, Dijkstra for weighted, 0-1 BFS for binary
> - [ ] Decision flowchart: unweighted→BFS, 0/1→0-1 BFS, non-negative→Dijkstra, negative→Bellman-Ford, all-pairs→Floyd-Warshall
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That Dijkstra invented the algorithm in 20 minutes at a cafe — without a computer!
> - [ ] That stale priority queue entries are a real performance trap (always check d > dist[u])
> - [ ] That "minimum effort path" and "swim in rising water" are DISGUISED Dijkstra problems
> - [ ] That 0-1 BFS is just as fast as regular BFS — O(V+E) — by using a deque instead of a priority queue
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Choosing the right algorithm quickly when faced with a new problem
> - [ ] Recognizing disguised shortest path problems (grid → graph reduction)
> - [ ] Implementing Dijkstra correctly on the first try without bugs (stale entries, INF overflow)
> - [ ] Floyd-Warshall path reconstruction (not just the distance matrix)
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does A* improve on Dijkstra using heuristics?
> - [ ] Can shortest paths be computed in parallel for massive graphs?
> - [ ] How do real GPS systems handle dynamic traffic (changing edge weights)?
> - [ ] What is the fastest shortest path algorithm for planar graphs?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 28 (Topological Sort) and Ch 29 (Union-Find & MST) — shortest path patterns reappear in DAG relaxation and MST algorithms!
