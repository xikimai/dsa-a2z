# Johari Window: Advanced Trees & Graph Algorithms

Rate your confidence (1-5) on each topic **before** and **after** working through the chapter.

| Topic | Before | After |
|-------|--------|-------|
| I understand the LCA problem and why naive solutions are too slow | | |
| I can implement Binary Lifting (precompute 2^k ancestors) | | |
| I can answer LCA queries in O(log n) using binary lifting | | |
| I understand the Euler Tour Technique and how it flattens a tree to an array | | |
| I can use Euler Tour to convert subtree queries to range queries | | |
| I understand the concept of Heavy-Light Decomposition | | |
| I understand the concept of Centroid Decomposition | | |
| I can find bridges in a graph using Tarjan's algorithm | | |
| I understand the disc[] and low[] arrays in Tarjan's algorithm | | |
| I can find articulation points in a graph | | |
| I know the difference between bridges (strict inequality) and articulation points (non-strict) | | |
| I can find SCCs using Kosaraju's two-pass algorithm | | |
| I understand why Kosaraju's works (reverse topological order + transposed graph) | | |
| I can condense a directed graph into a DAG of SCCs | | |
| I can compute tree distances using LCA + dist from root | | |
| I know when to use binary lifting vs Euler tour vs bridges vs SCCs | | |

## Reflection

After completing the chapter, answer these questions:

1. Why does binary lifting use powers of 2 specifically? Could we use powers of 3?

2. What is the key difference between a bridge and an articulation point in terms of the inequality check?

3. Why does Kosaraju's algorithm need TWO DFS passes? What would go wrong with just one?

4. When would you use Euler Tour over HLD, and vice versa?

5. Can you think of a real-world system where finding bridges (critical connections) would be important?
