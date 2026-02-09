# Johari Window: Chapter 28 — Topological Sort — Ordering Dependencies

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about topological sorting, DAGs, and dependency ordering.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What a directed graph is and how to represent it (adjacency list)
> - [ ] BFS and DFS graph traversals (from Ch 19-20)
> - [ ] What a cycle is in a graph
> - [ ] How prerequisite/dependency relationships work in real life
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "topological sort" means
> - [ ] What a DAG (Directed Acyclic Graph) is
> - [ ] Why topological sort only works on DAGs
> - [ ] How build systems decide what to compile first
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] Kahn's Algorithm (BFS-based topological sort)
> - [ ] DFS-based topological sort with post-order reversal
> - [ ] Three-color cycle detection (white/gray/black)
> - [ ] How to find the longest path in a DAG
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
> - [ ] Topological sort = linear ordering where every edge u-->v has u before v
> - [ ] Kahn's Algorithm: track in-degrees, repeatedly remove zero-indegree nodes
> - [ ] DFS topo sort: reverse the post-order (finish order) gives valid ordering
> - [ ] Three-color DFS: WHITE=unvisited, GRAY=in-progress, BLACK=done; GRAY-->GRAY = cycle
> - [ ] Course Schedule [a,b] means b-->a (b must come before a) — direction matters!
> - [ ] Multiple valid topological orderings can exist for the same DAG
> - [ ] Kahn's BFS levels = minimum "semesters" = longest path + 1
> - [ ] Longest path in DAG is solvable in O(V+E) via topo sort + relaxation
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That Kahn's BFS levels naturally reveal which tasks can run in parallel!
> - [ ] That the Alien Dictionary problem is just topological sort on characters!
> - [ ] That Minimum Height Trees uses leaf removal similar to Kahn's, but on undirected graphs!
> - [ ] That longest path is NP-hard on general graphs but O(V+E) on DAGs!
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Getting the prerequisite direction right on the first try ([a,b] means b-->a)
> - [ ] Choosing between Kahn's BFS and DFS topo sort for a given problem
> - [ ] Handling edge cases in Alien Dictionary (prefix check, disconnected chars)
> - [ ] Applying topo sort to non-obvious problems (like Largest Color Value)
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does DP on DAGs combine topological sort with dynamic programming?
> - [ ] Can topological sort be used in machine learning (computation graphs)?
> - [ ] What happens if I need the lexicographically smallest topological order?
> - [ ] How do real build systems handle incremental changes efficiently?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 29 (Union-Find & MST) and Ch 31 (Advanced DP) — topological ordering is a building block for DP on DAGs and many advanced graph algorithms!
