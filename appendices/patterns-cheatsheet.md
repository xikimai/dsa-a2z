# Appendix B: Patterns Cheatsheet

---

## B.1 How to Use This Cheatsheet

This is your **lookup table** for problem-solving. When you are stuck on a problem, come here.

**Three ways to use it:**

1. **Scan the "When to Use" column.** Read through the technique table until something matches the problem you are working on.
2. **Use the Decision Flowchart** (Section B.3). Answer questions about your problem and follow the arrows.
3. **Check the Constraint Table** (Section B.4). Look at the input size `n` and work backwards to find which complexity — and therefore which technique — fits.

Each entry in the master table gives you: the technique name, when to reach for it, its time and space complexity, and which chapter in this book covers it.

{% hint style="info" %}
**Bookmark this page.** Seriously. You will come back to it more than any other page in the book. Tape it to your wall if you have to.
{% endhint %}

---

## B.2 The Master Technique Table

### Sorting & Ordering (Ch 8)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Selection Sort | Teaching purposes; find min/max repeatedly | O(n^2) | O(1) | 8 |
| Bubble Sort | Teaching purposes; detect nearly-sorted data | O(n^2) | O(1) | 8 |
| Insertion Sort | Small arrays or nearly sorted data | O(n^2) | O(1) | 8 |
| Merge Sort | Need guaranteed O(n log n); need stability | O(n log n) | O(n) | 8 |
| Quick Sort | General-purpose fast sort; average case king | O(n log n) avg, O(n^2) worst | O(log n) | 8 |
| Counting Sort | Integers in a small known range | O(n + k) | O(k) | 8 |

{% hint style="info" %}
**In contests, you almost never code your own sort.** Use the built-in: Python `sorted()`, Java `Arrays.sort()`, C++ `std::sort()`. Know the algorithms so you understand WHY sorting helps — the built-in handles the HOW.
{% endhint %}

---

### Searching (Ch 9, 16)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Linear Search | Unsorted data; small input; no better option | O(n) | O(1) | 9 |
| Binary Search | Sorted data; find exact value or insertion point | O(log n) | O(1) | 9 |
| Binary Search on Answers | "Find the minimum/maximum value that satisfies condition X" — search the answer space | O(log(range) * check) | O(1) | 16 |
| 2D Binary Search | Sorted matrix; search rows then columns | O(log(m) + log(n)) or O(m + n) | O(1) | 16 |

{% hint style="warning" %}
**Binary Search on Answers** is one of the most powerful Silver/Gold techniques. The key insight: if the answer is monotonic (if X works, then X+1 also works), you can binary search for the boundary.
{% endhint %}

---

### Math & Number Theory (Ch 7)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| GCD (Euclidean) | Find greatest common divisor of two numbers | O(log(min(a,b))) | O(1) | 7 |
| LCM | Find least common multiple: `lcm(a,b) = a*b / gcd(a,b)` | O(log(min(a,b))) | O(1) | 7 |
| Sieve of Eratosthenes | Find all primes up to N | O(n log log n) | O(n) | 7 |
| Prime Factorization | Break a number into prime factors | O(sqrt(n)) | O(log n) | 7 |
| Modular Arithmetic | Large numbers; "answer mod 10^9+7" | O(1) per op | O(1) | 7 |
| Extended GCD | Find x, y such that ax + by = gcd(a,b) | O(log(min(a,b))) | O(log(min(a,b))) | 7 |
| Fast Exponentiation | Compute a^b mod m efficiently | O(log b) | O(1) | 7 |

---

### Bit Manipulation (Ch 12)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Check i-th bit | Test if bit i is set: `(n >> i) & 1` | O(1) | O(1) | 12 |
| Set / Clear bit | Turn a specific bit on or off | O(1) | O(1) | 12 |
| Count set bits | Count 1-bits (popcount) | O(bits) | O(1) | 12 |
| XOR tricks | Find the unique element; swap without temp | O(n) | O(1) | 12 |
| Bitmask as set | Represent a subset of N items as an N-bit integer | O(1) per op | O(1) | 12 |
| Enumerate subsets | Iterate over all subsets of a bitmask | O(2^k) for k bits | O(1) | 12 |

{% hint style="info" %}
**XOR golden rule:** `a ^ a = 0` and `a ^ 0 = a`. If every element appears twice except one, XOR them all to find the loner.
{% endhint %}

---

### Recursion & Backtracking (Ch 10, 13)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Recursion | Problem has self-similar sub-structure; "solve smaller version of same problem" | Varies | O(depth) stack | 10 |
| Generate All Subsets | Need every subset of a set (power set) | O(2^n) | O(n) | 10 |
| Generate Permutations | Need every ordering of a set | O(n!) | O(n) | 10 |
| N-Queens | Place items on grid with constraints | O(n!) pruned | O(n) | 13 |
| Sudoku Solver | Fill grid satisfying row/col/box constraints | O(9^(empty cells)) pruned | O(81) | 13 |
| Complete Search | "Try everything" — enumerate all candidates | O(2^n) or O(n!) | O(n) | 13 |

{% hint style="warning" %}
**Recursion depth limit.** Python defaults to 1000. For deep recursion, add `sys.setrecursionlimit(...)` or convert to an iterative approach. Java and C++ have larger stack limits but can still overflow on very deep trees.
{% endhint %}

---

### Hashing (Ch 11)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Hash Map (dict) | Need O(1) lookup/insert by key | O(1) avg | O(n) | 11 |
| Hash Set | Need O(1) membership test; remove duplicates | O(1) avg | O(n) | 11 |
| Frequency Counting | Count occurrences of each element | O(n) | O(k) distinct | 11 |
| Two Sum pattern | "Do two elements sum to target?" — store complements in a map | O(n) | O(n) | 11 |
| Anagram Detection | Check if two strings are anagrams — compare frequency maps | O(n) | O(1) fixed alphabet | 11 |
| Group by key | Group elements sharing a property (anagrams, same frequency, etc.) | O(n) | O(n) | 11 |

---

### Prefix Sums & Range Queries (Ch 14)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| 1D Prefix Sum | Many range sum queries on a static array | O(n) build, O(1) query | O(n) | 14 |
| 2D Prefix Sum | Sum of submatrix queries on a static grid | O(mn) build, O(1) query | O(mn) | 14 |
| Difference Array | Many range increment/decrement updates, then query final state | O(n) build + O(1) update | O(n) | 14 |
| Kadane's Algorithm | Find the maximum subarray sum (contiguous) | O(n) | O(1) | 14 |

{% hint style="info" %}
**Prefix sums are the "space-for-time" pattern in its purest form.** You invest O(n) space once and get O(1) per query forever after. Any time you see "many queries on a static array," think prefix sums first.
{% endhint %}

---

### Two Pointers & Sliding Window (Ch 15)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Two Pointers (sorted) | Pair/triplet search in sorted data; merging two sorted lists | O(n) | O(1) | 15 |
| Two Pointers (opposite ends) | Palindrome check; container with most water | O(n) | O(1) | 15 |
| Three Sum | Find three elements that sum to target — sort + two pointers | O(n^2) | O(1) | 15 |
| Sliding Window (fixed) | Subarray/substring of exactly size k | O(n) | O(1) or O(k) | 15 |
| Sliding Window (variable) | Smallest/longest subarray satisfying a condition | O(n) | O(1) or O(k) | 15 |

{% hint style="warning" %}
**Two pointers only work when the search space shrinks monotonically.** For sorted arrays, if `a[l] + a[r] < target`, increasing `l` cannot make it worse. This monotonicity is what lets you skip checking all pairs.
{% endhint %}

---

### Heaps & Priority Queues (Ch 17)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Min-Heap | Repeatedly extract the minimum; Dijkstra; merge K sorted | O(log n) push/pop | O(n) | 17 |
| Max-Heap | Repeatedly extract the maximum | O(log n) push/pop | O(n) | 17 |
| Kth Largest / Smallest | Keep a heap of size k; stream of elements | O(n log k) | O(k) | 17 |
| Merge K Sorted Lists | Use a min-heap of size k to merge | O(N log k), N total elements | O(k) | 17 |
| Top K Frequent | Frequency map + heap of size k | O(n log k) | O(n) | 17 |
| Heapify | Build a heap from an array | O(n) | O(1) in-place | 17 |

---

### Greedy Algorithms (Ch 18)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Activity Selection | Maximum non-overlapping intervals — sort by end time | O(n log n) | O(1) | 18 |
| Fractional Knapsack | Maximize value with fractional items allowed — sort by value/weight | O(n log n) | O(1) | 18 |
| Jump Game | Can you reach the end? Track farthest reachable index | O(n) | O(1) | 18 |
| Interval Merging | Merge overlapping intervals — sort by start | O(n log n) | O(n) | 18 |
| Job Sequencing | Schedule jobs with deadlines to maximize profit | O(n log n) | O(n) | 18 |

{% hint style="warning" %}
**Greedy is easy to code but hard to prove correct.** Before coding a greedy solution, convince yourself: "If I make the locally optimal choice at each step, does it lead to the globally optimal answer?" Use exchange argument or proof by contradiction (see Ch 18).
{% endhint %}

---

### Linked Lists (Ch 21)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Traversal | Visit every node; find length; search | O(n) | O(1) | 21 |
| Reversal | Reverse a linked list (iterative or recursive) | O(n) | O(1) iter, O(n) rec | 21 |
| Floyd's Cycle Detection | Detect cycle — slow + fast pointer | O(n) | O(1) | 21 |
| Find Middle Node | Slow + fast pointer — slow lands at middle | O(n) | O(1) | 21 |
| Merge Two Sorted Lists | Two-pointer merge (like merge sort merge step) | O(n + m) | O(1) | 21 |

---

### Stacks & Queues (Ch 22)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Stack (balanced parentheses) | Matching brackets; undo operations; expression evaluation | O(n) | O(n) | 22 |
| Monotonic Stack | "Next greater/smaller element" — maintain sorted invariant on stack | O(n) | O(n) | 22 |
| Queue (BFS) | Level-order traversal; process in FIFO order | O(n) | O(n) | 22 |
| Deque | Sliding window max/min; double-ended operations | O(n) total | O(k) window | 22 |
| Min Stack | Stack with O(1) getMin — store min alongside each element | O(1) all ops | O(n) | 22 |

{% hint style="info" %}
**Monotonic stack pattern:** whenever a problem asks about "the next element that is bigger/smaller," you almost certainly want a monotonic stack. It turns an obvious O(n^2) into O(n).
{% endhint %}

---

### Graphs -- Basics (Ch 19-20)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| BFS (Breadth-First Search) | Shortest path in unweighted graph; level-order exploration | O(V + E) | O(V) | 19 |
| DFS (Depth-First Search) | Explore all reachable nodes; detect cycles; connected components | O(V + E) | O(V) | 19 |
| Connected Components | Count/label separate groups in undirected graph | O(V + E) | O(V) | 19 |
| Flood Fill | Fill connected region on a grid (BFS or DFS) | O(rows * cols) | O(rows * cols) | 20 |
| Cycle Detection (undirected) | DFS with parent tracking; or Union-Find | O(V + E) | O(V) | 20 |
| Cycle Detection (directed) | DFS with three-color marking (white/gray/black) | O(V + E) | O(V) | 20 |
| Bipartite Check | 2-color BFS/DFS; check if graph is 2-colorable | O(V + E) | O(V) | 20 |

{% hint style="info" %}
**BFS vs DFS rule of thumb:** BFS finds shortest paths in unweighted graphs and explores "level by level." DFS explores "as deep as possible first" and is better for cycle detection, topological sort, and connected components.
{% endhint %}

---

### Dynamic Programming (Ch 23-25)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Climbing Stairs / Fibonacci | Count ways; linear recurrence | O(n) | O(1) with space opt | 23 |
| House Robber | Max sum of non-adjacent elements | O(n) | O(1) with space opt | 23 |
| Best Time Buy/Sell Stock | Max profit from one transaction; state machine for multiple | O(n) | O(1) | 23 |
| Grid DP (unique paths) | Count paths / min cost in a grid; move right or down | O(mn) | O(n) with space opt | 24 |
| 0/1 Knapsack | Choose items (take or skip) to maximize value within weight limit | O(nW) | O(W) with space opt | 25 |
| Unbounded Knapsack | Like 0/1 but can reuse items (coin change, rod cutting) | O(nW) | O(W) | 25 |
| Longest Common Subsequence | Compare two sequences; diff tool; edit distance variant | O(mn) | O(min(m,n)) opt | 25 |
| Longest Increasing Subsequence | Longest subsequence in strictly increasing order | O(n log n) with patience sort | O(n) | 25 |
| Edit Distance | Minimum insertions/deletions/replacements to transform string A to B | O(mn) | O(min(m,n)) opt | 25 |
| Coin Change | Minimum coins to make amount (unbounded knapsack variant) | O(n * amount) | O(amount) | 25 |
| Subset Sum | Can a subset sum to target? (0/1 knapsack variant) | O(n * target) | O(target) | 25 |

{% hint style="warning" %}
**The two signs of a DP problem:** (1) overlapping subproblems -- the same subproblem gets solved multiple times, and (2) optimal substructure -- the optimal solution uses optimal solutions to subproblems. If you see both, it is almost certainly DP.
{% endhint %}

---

### Trees (Ch 26)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Inorder Traversal | BST: visits nodes in sorted order | O(n) | O(h) | 26 |
| Preorder Traversal | Serialize a tree; copy a tree | O(n) | O(h) | 26 |
| Postorder Traversal | Delete a tree; evaluate expression tree | O(n) | O(h) | 26 |
| Level-Order (BFS) | Process level by level; find width; zigzag traversal | O(n) | O(w) max width | 26 |
| Height / Diameter | Find tree height or longest path between any two nodes | O(n) | O(h) | 26 |
| Balanced Check | Is the tree height-balanced? (recursive height check) | O(n) | O(h) | 26 |
| BST Search / Insert / Delete | Sorted dictionary operations on a BST | O(h), O(log n) if balanced | O(h) | 26 |
| Lowest Common Ancestor (LCA) | Find the deepest node that is an ancestor of both p and q | O(n) naive, O(log n) with lifting | O(h) | 26 |
| Serialize / Deserialize | Convert tree to string and back | O(n) | O(n) | 26 |

---

### Shortest Paths (Ch 27)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Dijkstra's Algorithm | Single-source shortest path; **non-negative** weights | O((V + E) log V) with heap | O(V + E) | 27 |
| Bellman-Ford | Single-source shortest path; handles **negative** weights; detect negative cycles | O(VE) | O(V) | 27 |
| Floyd-Warshall | **All-pairs** shortest paths; small graphs (V <= 500) | O(V^3) | O(V^2) | 27 |
| 0-1 BFS | Shortest path when edge weights are **only 0 or 1** — use deque | O(V + E) | O(V) | 27 |
| DAG Shortest Path | Shortest path in a **DAG** — topological sort + relax | O(V + E) | O(V) | 27 |

{% hint style="info" %}
**Choosing a shortest path algorithm:**
- All weights non-negative? **Dijkstra.**
- Negative weights possible? **Bellman-Ford.**
- Need all pairs? **Floyd-Warshall.**
- Weights are only 0 and 1? **0-1 BFS.**
- Graph is a DAG? **Topo sort + relax.**
{% endhint %}

---

### Topological Sort (Ch 28)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Kahn's Algorithm (BFS) | Topological ordering via indegree counting + queue | O(V + E) | O(V + E) | 28 |
| DFS-based Topo Sort | Topological ordering via DFS finish-time reversal | O(V + E) | O(V + E) | 28 |
| Course Schedule | Can you finish all courses? (cycle detection in directed graph) | O(V + E) | O(V + E) | 28 |
| Alien Dictionary | Derive ordering of characters from sorted word list | O(total chars) | O(alphabet) | 28 |

{% hint style="info" %}
**Topological sort only works on DAGs** (Directed Acyclic Graphs). If the graph has a cycle, no valid ordering exists. Both Kahn's and DFS-based approaches can detect this: Kahn's produces fewer than V nodes; DFS finds a back edge.
{% endhint %}

---

### Union-Find & MST (Ch 29)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Union-Find (DSU) | Dynamic connectivity; "are X and Y in the same group?" | O(alpha(n)) ~= O(1) amortized | O(n) | 29 |
| Kruskal's Algorithm | MST — sort edges by weight, add if no cycle (uses Union-Find) | O(E log E) | O(V + E) | 29 |
| Prim's Algorithm | MST — grow tree from a vertex using a min-heap | O((V + E) log V) | O(V + E) | 29 |

{% hint style="info" %}
**Union-Find with path compression + union by rank** gives nearly O(1) per operation. The inverse Ackermann function alpha(n) is less than 5 for any practical input size. It is one of the most useful data structures in competitive programming.
{% endhint %}

---

### Segment Trees & Range Queries (Ch 30)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Segment Tree (Build) | Preprocess array for range queries with point updates | O(n) build | O(4n) | 30 |
| Segment Tree (Query) | Range min, max, sum, GCD, etc. | O(log n) | -- | 30 |
| Segment Tree (Update) | Point update (change one element) | O(log n) | -- | 30 |
| Lazy Propagation | **Range updates** (update an entire range at once) + range queries | O(log n) per op | O(4n) | 30 |
| Fenwick Tree (BIT) | Prefix sums with point updates; simpler + faster constant than segment tree | O(log n) query/update | O(n) | 30 |

{% hint style="warning" %}
**Segment Tree vs Fenwick Tree:** Fenwick is simpler and faster for prefix sum + point update problems. Segment tree is more general -- it handles range min/max, lazy propagation, and other operations Fenwick cannot do.
{% endhint %}

---

### Advanced DP (Ch 31)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Bitmask DP | State includes "which items are chosen" from a small set (n <= 20) | O(2^n * n) | O(2^n) | 31 |
| Interval DP (MCM) | Optimal way to split a range; matrix chain, burst balloons, palindrome partition | O(n^3) | O(n^2) | 31 |
| Tree DP | DP on tree structure; answer depends on subtree computations | O(n) typical | O(n) | 31 |
| Digit DP | "Count numbers from 0 to N with property X" | O(digits * states * 2) | O(digits * states) | 31 |

{% hint style="info" %}
**Bitmask DP constraint check:** if the problem says n <= 15 or n <= 20, and you need to track "which subset is used," bitmask DP is almost certainly the intended approach. 2^20 = ~10^6, which fits comfortably.
{% endhint %}

---

### String Algorithms (Ch 32)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Trie (Prefix Tree) | Prefix search; autocomplete; dictionary of words; XOR maximum | O(L) per op, L = string length | O(total chars) | 32 |
| KMP (Knuth-Morris-Pratt) | Find pattern in text; compute failure/prefix function | O(n + m) | O(m) | 32 |
| Z-Function | Find all occurrences of pattern in text; period of a string | O(n + m) | O(n + m) | 32 |
| Rabin-Karp | Pattern matching via rolling hash; multiple pattern search | O(n + m) avg, O(nm) worst | O(1) | 32 |
| Suffix Array | All suffixes sorted; substring search; LCP array applications | O(n log n) build | O(n) | 32 |

---

### Advanced Graphs (Ch 33)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Binary Lifting (LCA) | LCA queries in O(log n); k-th ancestor queries | O(n log n) build, O(log n) query | O(n log n) | 33 |
| Euler Tour | Flatten tree into array for range queries (subtree sums, LCA via RMQ) | O(n) | O(n) | 33 |
| Bridges (Tarjan's) | Find edges whose removal disconnects the graph | O(V + E) | O(V) | 33 |
| Articulation Points | Find vertices whose removal disconnects the graph | O(V + E) | O(V) | 33 |
| SCC (Kosaraju's) | Find strongly connected components in a directed graph | O(V + E) | O(V + E) | 33 |

---

### Computational Geometry (Ch 34)

| Technique | When to Use | Time | Space | Ch |
|---|---|---|---|---|
| Cross Product | Determine left/right turn; area of triangle; collinearity test | O(1) | O(1) | 34 |
| Convex Hull | Find the outer boundary of a set of points | O(n log n) | O(n) | 34 |
| Closest Pair of Points | Find two closest points — divide and conquer | O(n log n) | O(n) | 34 |
| Sweep Line | Process events left-to-right; segment intersections; rectangle union area | O(n log n) | O(n) | 34 |
| Point in Polygon | Test if a point lies inside a polygon — ray casting | O(n) per query | O(1) | 34 |

---

## B.3 Pattern Recognition Decision Flowchart

When you are stuck on a problem, walk through this decision tree. Start at the top.

```
What type of problem is this?
|
+-- Is the data SORTED (or can sorting help)?
|   |
|   +-- Looking for a specific value?
|   |   --> Binary Search (Ch 9)
|   |
|   +-- Looking for a pair/triplet that satisfies a condition?
|   |   --> Two Pointers (Ch 15)
|   |
|   +-- Looking for the min/max value that satisfies a condition?
|   |   --> Binary Search on Answers (Ch 16)
|   |
|   +-- Need to merge intervals or select non-overlapping ones?
|       --> Greedy after sorting (Ch 18)
|
+-- Does the problem involve a GRAPH or NETWORK?
|   |
|   +-- Shortest path?
|   |   |
|   |   +-- All weights non-negative? --> Dijkstra (Ch 27)
|   |   +-- Negative weights? --> Bellman-Ford (Ch 27)
|   |   +-- All pairs? --> Floyd-Warshall (Ch 27)
|   |   +-- Unweighted? --> BFS (Ch 19)
|   |   +-- Weights 0 or 1? --> 0-1 BFS (Ch 27)
|   |
|   +-- Connectivity / "are they in the same group?"
|   |   --> Union-Find (Ch 29) or BFS/DFS (Ch 19)
|   |
|   +-- Ordering with dependencies?
|   |   --> Topological Sort (Ch 28)
|   |
|   +-- Minimum spanning tree?
|   |   --> Kruskal's or Prim's (Ch 29)
|   |
|   +-- Find bridges / articulation points / SCCs?
|   |   --> Tarjan's / Kosaraju's (Ch 33)
|   |
|   +-- Just need to explore / traverse?
|       --> BFS or DFS (Ch 19)
|
+-- Does the problem involve a TREE?
|   |
|   +-- Need LCA or ancestor queries?
|   |   --> Binary Lifting (Ch 33) or Euler Tour + RMQ (Ch 33)
|   |
|   +-- Need subtree queries?
|   |   --> Euler Tour + Segment Tree (Ch 33 + 30)
|   |
|   +-- DP on the tree?
|   |   --> Tree DP (Ch 31)
|   |
|   +-- Just need traversals?
|       --> DFS / BFS (Ch 26)
|
+-- Does the problem ask for RANGE QUERIES or RANGE UPDATES?
|   |
|   +-- Static array, many sum queries?
|   |   --> Prefix Sums (Ch 14)
|   |
|   +-- Point updates + range queries?
|   |   --> Fenwick Tree (Ch 30) or Segment Tree (Ch 30)
|   |
|   +-- Range updates + range queries?
|       --> Segment Tree with Lazy Propagation (Ch 30)
|
+-- Does the problem have OVERLAPPING SUBPROBLEMS?
|   |
|   +-- Linear (1D) state?
|   |   --> 1D DP (Ch 23)
|   |
|   +-- Grid / two-sequence state?
|   |   --> Grid DP (Ch 24) or LCS / Edit Distance (Ch 25)
|   |
|   +-- Knapsack / subset selection?
|   |   --> 0/1 or Unbounded Knapsack (Ch 25)
|   |
|   +-- State is a subset (n <= 20)?
|   |   --> Bitmask DP (Ch 31)
|   |
|   +-- State is an interval / range?
|   |   --> Interval DP (Ch 31)
|   |
|   +-- State is on a tree?
|       --> Tree DP (Ch 31)
|
+-- Does the problem involve STRINGS or PATTERN MATCHING?
|   |
|   +-- Find pattern in text?
|   |   --> KMP or Z-Function (Ch 32)
|   |
|   +-- Multiple patterns / prefix queries?
|   |   --> Trie (Ch 32)
|   |
|   +-- Need substring hashing?
|       --> Rabin-Karp (Ch 32)
|
+-- Is the problem about making LOCALLY OPTIMAL choices?
|   |
|   +-- Can you prove greedy works (exchange argument)?
|       --> Greedy (Ch 18)
|
+-- Do you need to TRY ALL POSSIBILITIES?
|   |
|   +-- n <= 20? --> Bitmask enumeration (Ch 12) or Bitmask DP (Ch 31)
|   +-- n <= 10-12? --> Backtracking / Complete Search (Ch 10, 13)
|   +-- Constraint satisfaction (place items with rules)?
|       --> Backtracking with pruning (Ch 13)
|
+-- Does the problem involve GEOMETRY?
|   |
|   +-- Convex hull / farthest points?
|   |   --> Convex Hull (Ch 34)
|   |
|   +-- Closest pair of points?
|   |   --> Divide and conquer or Sweep Line (Ch 34)
|   |
|   +-- Events happening at positions?
|       --> Sweep Line (Ch 34)
|
+-- Still stuck?
    |
    +-- Try brute force first. Optimize later.
    +-- Look at constraints (Section B.4) to narrow the approach.
    +-- Re-read the problem. The answer is often in a sentence you skipped.
```

---

## B.4 Complexity Quick Reference

### The Constraint-to-Complexity Table

This is one of the most important tables in competitive programming. Look at the input constraint `n` and determine which time complexities are feasible. A modern computer does roughly **10^8 simple operations per second** (with a safety margin -- USACO gives 2-4 seconds).

| Constraint on n | Max Feasible Complexity | Typical Techniques |
|---|---|---|
| n <= 10 | O(n!) or O(2^n * n) | Brute force, permutations, backtracking |
| n <= 20 | O(2^n) or O(2^n * n) | Bitmask DP, bitmask enumeration |
| n <= 100 | O(n^3) | Floyd-Warshall, interval DP, Gaussian elimination |
| n <= 500 | O(n^3) (tight) | Floyd-Warshall, 3-nested-loop DP |
| n <= 5,000 | O(n^2) | Simple DP, pairwise comparisons |
| n <= 10^5 | O(n sqrt(n)) or O(n log^2 n) | Sqrt decomposition, heavy processing per element |
| n <= 5 * 10^5 | O(n log n) | Sorting, segment tree, merge sort, binary search |
| n <= 10^6 | O(n log n) or O(n) | Sorting, hashing, two pointers, prefix sums |
| n <= 10^7 | O(n) | Linear scan, sieve, prefix sums |
| n <= 10^8 | O(n) (tight) | Very simple linear pass |
| n <= 10^18 | O(log n) or O(sqrt(n)) | Binary search, math, fast exponentiation |

{% hint style="warning" %}
**Read constraints FIRST.** Before you think about the algorithm, look at n. If n = 10^5, you CANNOT use O(n^2). This single check eliminates half the possible approaches instantly.
{% endhint %}

### "Feels Like" Guide to Common Complexities

| Complexity | What It Feels Like | Example |
|---|---|---|
| O(1) | Instant. Lookup by index, math formula. | Hash map lookup |
| O(log n) | Halving each step. Very fast. | Binary search |
| O(sqrt(n)) | The "forgotten middle child." | Trial division for primality |
| O(n) | Touch every element once. | Linear scan, prefix sum build |
| O(n log n) | Sort it, then do something smart. | Merge sort, Dijkstra |
| O(n^2) | All pairs. Gets slow around n = 10,000. | Bubble sort, 2D DP |
| O(n^3) | All triples. Painful above n = 500. | Floyd-Warshall, matrix multiply |
| O(2^n) | All subsets. Dies above n = 25. | Bitmask DP, power set |
| O(n!) | All permutations. Dies above n = 12. | Brute force permutations |

---

## B.5 Common Gotchas Reference

Twenty mistakes that have cost countless contest points. Learn them here so you do not learn them the hard way.

### Off-by-One and Boundaries

| # | Gotcha | What Goes Wrong | Fix |
|---|---|---|---|
| 1 | **Off-by-one in binary search** | Infinite loop or miss the answer | Use `lo < hi` vs `lo <= hi` deliberately. Test edge cases: array of size 0, 1, 2. |
| 2 | **Off-by-one in prefix sums** | Sum of range [l, r] is `prefix[r+1] - prefix[l]`, not `prefix[r] - prefix[l-1]` (depends on convention) | Pick ONE convention (0-indexed or 1-indexed) and stick to it. Write it down. |
| 3 | **Empty input / edge cases** | Crash on n=0, empty string, single node tree | Always handle n=0 and n=1 before the main logic. |

### Integer Overflow

| # | Gotcha | What Goes Wrong | Fix |
|---|---|---|---|
| 4 | **Integer overflow in C++/Java** | `a * b` overflows 32-bit int when a, b > 46340 | Use `long long` in C++, `long` in Java. Cast BEFORE multiplication: `(long long)a * b`. |
| 5 | **LCM overflow** | `a * b / gcd(a,b)` can overflow even if the result fits | Compute `a / gcd(a,b) * b` -- divide first, then multiply. |
| 6 | **Forgetting mod** | "Answer mod 10^9 + 7" but you forget to mod intermediate results | Mod after EVERY addition and multiplication. `(a + b) % MOD`, `(a * b) % MOD`. |

### Language-Specific Traps

| # | Gotcha | What Goes Wrong | Fix |
|---|---|---|---|
| 7 | **Python integer division** | `-7 // 2 = -4` in Python (floors), but `-7 / 2 = -3` in C++/Java (truncates toward zero) | Use `int(a / b)` in Python if you want C++/Java behavior. |
| 8 | **Python recursion limit** | `RecursionError` on deep recursion (default limit 1000) | `sys.setrecursionlimit(300000)` or convert to iterative. |
| 9 | **C++ uninitialized variables** | Random garbage values; different results each run | Always initialize: `int x = 0;`, `vector<int> v(n, 0);`, `memset(arr, 0, sizeof(arr));`. |
| 10 | **Java `==` vs `.equals()`** | `==` compares references for objects (Integer, String), not values | Use `.equals()` for objects. Or unbox to primitives. |
| 11 | **C++ `#include <climits>` missing** | `INT_MIN`, `INT_MAX` undefined on some compilers | Always include `<climits>` explicitly. Do not rely on transitive includes. |

### Algorithm-Specific Mistakes

| # | Gotcha | What Goes Wrong | Fix |
|---|---|---|---|
| 12 | **Dijkstra with negative edges** | Wrong answers -- Dijkstra assumes shortest path to a visited node is final | Use Bellman-Ford for negative edges. Check problem for "weights >= 0" guarantee. |
| 13 | **Forgetting visited check in BFS/DFS** | Infinite loop on cyclic graphs; TLE | Mark visited WHEN ADDING to queue (BFS) or WHEN ENTERING (DFS), not when popping. |
| 14 | **DP base case wrong** | Entire DP table is wrong because the foundation is wrong | Write out base cases by hand for small inputs. Verify dp[0], dp[1] match expected values. |
| 15 | **Greedy without proof** | "Seems greedy" but the greedy choice is wrong | Try a counterexample. If you cannot find one, attempt an exchange argument proof. |
| 16 | **Segment tree array too small** | Out-of-bounds access; segfault or wrong answer | Always allocate `4 * n` nodes, not `2 * n`. |

### Input/Output and Contest Logistics

| # | Gotcha | What Goes Wrong | Fix |
|---|---|---|---|
| 17 | **Slow I/O in C++** | TLE even with correct algorithm | Add `ios_base::sync_with_stdio(false); cin.tie(NULL);` at the start of main. |
| 18 | **Slow I/O in Java** | TLE due to Scanner | Use `BufferedReader` + `StringTokenizer` instead of `Scanner`. |
| 19 | **Slow I/O in Python** | TLE due to `input()` | Use `sys.stdin.readline()` or read all input at once with `sys.stdin.read()`. |
| 20 | **Reading wrong input format** | Read n when it expected n and m on the same line; everything after is shifted | Read the input specification character by character. Print what you read to stderr to verify. |

{% hint style="danger" %}
**The single most common reason for wrong answers in contests is not a wrong algorithm -- it is a wrong implementation.** Edge cases, overflow, off-by-one, and I/O mistakes cause more failures than picking the wrong approach. Always test with edge cases before submitting.
{% endhint %}

---

## B.6 The Six Cross-Chapter Threads

These six patterns appear repeatedly throughout the book. They are not techniques you apply to a single problem -- they are **ways of thinking** that connect many techniques together.

---

### Thread 1: Sort First, Think Later

**Chapters:** 5, 8, 9, 13, 15, 18

Sorting transforms a chaotic problem into an orderly one. After sorting, binary search works, two pointers work, greedy strategies become obvious, and duplicates cluster together.

**Where you see it:**

- **Ch 5:** Sorting a collection to find medians, remove duplicates.
- **Ch 8:** The sorting algorithms themselves -- understanding how order is created.
- **Ch 9:** Binary search requires sorted input. Sorting is the preprocessing step that unlocks logarithmic search.
- **Ch 13:** Complete search is often faster on sorted input because you can prune earlier.
- **Ch 15:** Two pointers and Three Sum only work on sorted arrays. Sorting is the key insight, not the pointers.
- **Ch 18:** Greedy algorithms almost always start by sorting (by end time, by value/weight ratio, by deadline).

**The lesson:** When stuck, ask yourself: "What if I sorted the input first?"

---

### Thread 2: Trade Space for Time

**Chapters:** 6, 11, 14, 23-25, 30

The most universal optimization strategy in computer science. Store precomputed results so you do not recompute them.

**Where you see it:**

- **Ch 6:** The concept -- understanding that O(n^2) to O(n) often costs O(n) extra space.
- **Ch 11:** Hash maps trade O(n) space for O(1) lookup. Two Sum is the classic example.
- **Ch 14:** Prefix sums trade O(n) space for O(1) range queries.
- **Ch 23-25:** DP tables trade O(n), O(n^2), or O(2^n) space for avoiding recomputation of overlapping subproblems.
- **Ch 30:** Segment trees and Fenwick trees trade O(n) space for O(log n) range queries with updates.

**The lesson:** If your solution is too slow, ask: "What can I precompute and store?"

---

### Thread 3: Reduce to a Known Problem

**Chapters:** 9, 13, 16, 19-20, 28

Many "new" problems are old problems in disguise. Recognizing the transformation is the real skill.

**Where you see it:**

- **Ch 9:** "Find the missing number" reduces to sum or XOR.
- **Ch 13:** Many USACO Bronze problems reduce to simulation or complete search once you see the structure.
- **Ch 16:** "Minimum time to do X" reduces to binary search on answers -- transform an optimization problem into a decision problem.
- **Ch 19-20:** Grid problems reduce to graph problems (each cell is a node, adjacent cells are edges).
- **Ch 28:** "Can you finish all courses?" reduces to cycle detection in a directed graph.

**The lesson:** When you see a new problem, ask: "What known problem does this look like?"

---

### Thread 4: Ask the Right Question

**Chapters:** 6, 9, 16, 23

Sometimes the problem as stated is hard, but a rephrased version is easy. The art is in the rephrasing.

**Where you see it:**

- **Ch 6:** "Is this algorithm fast enough?" becomes "How many operations does it do as a function of n?"
- **Ch 9:** "Find the peak element" -- instead of checking every element, ask "which half MUST contain a peak?"
- **Ch 16:** "What is the minimum distance to deliver all packages?" becomes "Can I deliver all packages with distance <= D?" (binary search on answers).
- **Ch 23:** "What is the maximum profit?" becomes "What is the maximum profit using only the first i items?" (DP state definition).

**The lesson:** If the problem seems impossible, you might be answering the wrong question. Rephrase it.

---

### Thread 5: Brute Force Is a Strategy

**Chapters:** 10, 12-13, 31

Brute force is not a failure -- it is a starting point. Sometimes it IS the intended solution (when n is small). Always code brute force first for two reasons: (1) it might be fast enough, and (2) it gives you a correct reference to test your optimized solution against.

**Where you see it:**

- **Ch 10:** Recursion generates all possibilities. For small n, this IS the answer.
- **Ch 12:** Bitmask enumeration of all subsets: O(2^n). For n <= 20, this is 10^6 -- perfectly fine.
- **Ch 13:** Complete search (Bronze level) -- USACO Bronze problems are often solvable by trying everything.
- **Ch 31:** Bitmask DP is "smart brute force" -- enumerate all subsets but reuse computations.

**The lesson:** Always start with brute force. Then optimize. Never skip step one.

---

### Thread 6: Two Pointers Everywhere

**Chapters:** 15, 17, 21, 29

The two-pointer technique appears in many disguises beyond the classic "sorted array" version.

**Where you see it:**

- **Ch 15:** The classic: two pointers on a sorted array (Two Sum, Three Sum, container with most water).
- **Ch 17:** A heap with K elements is conceptually a "pointer" to the K-th largest element, sliding over the data.
- **Ch 21:** Floyd's cycle detection uses slow and fast pointers. Finding the middle of a linked list uses the same idea.
- **Ch 29:** Kruskal's algorithm processes edges in sorted order (one pointer) while Union-Find tracks connectivity (the second "pointer" into the component structure).

**The lesson:** Two pointers is not just a technique -- it is a paradigm. Whenever you have two things moving through data at different rates or from different ends, you are using two pointers.

---

## B.7 Quick Reference: Data Structure Selection

When the problem requires a specific operation pattern, this table tells you which data structure to reach for.

| I need to... | Use | Time per Op | Ch |
|---|---|---|---|
| Look up by key | Hash Map | O(1) avg | 11 |
| Check membership | Hash Set | O(1) avg | 11 |
| Get min/max repeatedly | Heap (Priority Queue) | O(log n) | 17 |
| Undo last action (LIFO) | Stack | O(1) | 22 |
| Process in order (FIFO) | Queue | O(1) | 22 |
| Range sum queries + point updates | Fenwick Tree | O(log n) | 30 |
| Range queries + range updates | Segment Tree + Lazy | O(log n) | 30 |
| Dynamic connectivity | Union-Find | O(alpha(n)) | 29 |
| Sorted order + fast search | BST / TreeMap / set | O(log n) | 26 |
| Prefix search on strings | Trie | O(L) | 32 |
| "Next greater element" | Monotonic Stack | O(n) total | 22 |
| Sliding window max/min | Deque (Monotonic) | O(n) total | 22 |

---

## B.8 The Five-Lens Framework (Quick Reference)

When you sit down with a new problem, run it through these five lenses in order.

**Lens 1: Constraints.**
Read the input bounds. Use Section B.4 to determine the required time complexity. This eliminates most approaches immediately.

**Lens 2: Brute Force.**
Write the simplest correct solution. Even if it is O(n^3) and the problem needs O(n log n), you now have a working reference.

**Lens 3: Pattern.**
Does this problem match a known pattern? Use Section B.2 and B.3 to identify it. "This looks like a shortest path problem." "This is just Knapsack in disguise."

**Lens 4: Optimization.**
Can you improve the brute force? Common optimizations:
- Sort the input (Thread 1).
- Precompute with a table or prefix sum (Thread 2).
- Reduce to a known problem (Thread 3).
- Rephrase the question (Thread 4).
- Use a smarter data structure (Section B.7).

**Lens 5: Proof.**
Why is your solution correct? For greedy: exchange argument. For DP: induction on the recurrence. For binary search: the monotonicity property. If you cannot sketch a reason, your solution might be wrong.

---

{% hint style="info" %}
**This cheatsheet covers Chapters 2-34 of the workbook.** For contest-day strategy (when to skip, when to debug, when to submit), see [Appendix A: Contest Strategy](contest-strategy.md). For USACO-specific logistics (registration, grading, input format), see [Appendix C: USACO Guide](usaco-guide.md).
{% endhint %}
