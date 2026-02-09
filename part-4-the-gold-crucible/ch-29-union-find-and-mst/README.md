# Union-Find & Minimum Spanning Trees

{% hint style="info" %}
**This is the FINAL Gold chapter — a milestone!** Union-Find (Disjoint Set Union) is one of the most versatile data structures in competitive programming, and Minimum Spanning Trees are a cornerstone of graph algorithms. Together they solve a huge family of connectivity problems. Master these, and you will have completed the entire Gold-level curriculum. USACO Gold contests are within your reach!
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand the connectivity problem: "are two nodes in the same group?"
- Implement Union-Find (Disjoint Set Union) from scratch with union and find operations
- Apply path compression to make find nearly O(1) amortized
- Apply union by rank (or size) to keep the tree balanced
- Understand that combined optimizations give amortized O(alpha(n)) per operation, where alpha is the inverse Ackermann function (effectively constant)
- Use Union-Find to count connected components in an undirected graph
- Use Union-Find to detect cycles in an undirected graph
- Solve the Accounts Merge problem using Union-Find with index mapping
- Define what a Minimum Spanning Tree (MST) is and why it matters
- Implement Kruskal's Algorithm (sort edges + Union-Find)
- Implement Prim's Algorithm (greedy expansion with a priority queue)
- Understand MST correctness through the cut property and exchange argument
- Recognize when a problem reduces to Union-Find or MST

---

## The Story: "The Network Builder"

Ravi had just been hired by FiberLink, a startup connecting cities across the country with fiber optic cables. His boss dropped a map on his desk — 50 cities, hundreds of possible cable routes, each with a different cost.

"We need ALL cities connected," said the boss. "But we are on a tight budget. Find the cheapest way to wire them all up."

Ravi stared at the map. Some routes were cheap (neighboring towns), some were expensive (cables across mountain ranges). He could not just connect each city to its nearest neighbor — that might leave clusters of cities disconnected from each other.

He needed a plan that guaranteed EVERY city could reach EVERY other city, using the least total cable.

But that was only half the job. As cables were installed day by day, the construction team kept asking: "Are city A and city B ALREADY connected? Or do we still need to build that route?"

Ravi needed two tools:
1. A way to quickly answer "are these two cities already connected?" even as new connections were added.
2. An algorithm to find the cheapest set of cables that connects everything.

The first tool is **Union-Find**. The second is the **Minimum Spanning Tree**. Together, they are the foundation of network design — and they are what you will learn in this chapter.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "The Cheapest Network"

You need to connect 5 cities. Building a cable between any two costs different amounts:

| Route | Cost |
|-------|------|
| A - B | 4 |
| A - C | 8 |
| B - C | 2 |
| B - D | 6 |
| C - D | 3 |
| C - E | 9 |
| D - E | 5 |

What is the cheapest way to connect ALL 5 cities? Remember: you need a path from every city to every other city, but you do not need a DIRECT cable between every pair.

{% hint style="info" %}
Try sorting the routes by cost and picking the cheapest ones that do not create a loop. The answer is 14 (routes B-C=2, C-D=3, A-B=4, D-E=5). You just discovered Kruskal's algorithm!
{% endhint %}

### Puzzle 2: "The Connection Tracker"

Cables are installed one at a time in this order:
1. Connect A-B
2. Connect C-D
3. Connect B-C

After each step, how many separate groups of cities exist? (Start with 5 separate cities: A, B, C, D, E.)

{% hint style="info" %}
Step 1: {A,B}, {C}, {D}, {E} -> 4 groups. Step 2: {A,B}, {C,D}, {E} -> 3 groups. Step 3: {A,B,C,D}, {E} -> 2 groups. The operation of merging groups and checking "same group?" is exactly what Union-Find does.
{% endhint %}

### Puzzle 3: "The Extra Cable"

A network has exactly n cities and n cables (edges). A tree connecting n cities needs exactly n-1 edges. So one cable is redundant — it creates a cycle. Which cable is it?

Given: Cities 1-3, cables: [1,2], [1,3], [2,3]. Which cable, when removed, still leaves all cities connected?

{% hint style="info" %}
Any one of the three cables can be removed. But the problem typically asks for the LAST cable in the list that creates a cycle. Process cables in order using Union-Find: [1,2] merges 1 and 2, [1,3] merges the group with 3, [2,3] tries to merge 2 and 3 but they are ALREADY connected — this is the redundant cable!
{% endhint %}

---

## 29.1 The Connectivity Problem

Imagine you have n cities and edges are added one by one. After each edge, you want to answer: "Are city A and city B connected?"

### Naive Approach: BFS/DFS Every Time

You could run BFS or DFS from A and see if you reach B. But if you have Q queries, that is O(Q * (V + E)) — far too slow when Q is large.

### What We Need

A data structure that supports two operations efficiently:
- **Union(a, b)**: merge the groups containing a and b
- **Find(a)**: return the "representative" (root) of the group containing a

If Find(a) == Find(b), then a and b are in the same group (connected).

This is the **Union-Find** (also called **Disjoint Set Union** or **DSU**) data structure.

---

## 29.2 Union-Find — Basic Implementation

The idea is simple: represent each group as a tree. Every node points to its parent. The root of the tree is the "representative" of the group.

{% tabs %}
{% tab title="Python" %}
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # each node is its own parent

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y  # attach x's tree under y's root
```
{% endtab %}
{% tab title="Java" %}
```java
class UnionFind {
    int[] parent;

    UnionFind(int n) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        while (parent[x] != x) x = parent[x];
        return x;
    }

    void union(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX != rootY) parent[rootX] = rootY;
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
class UnionFind {
public:
    vector<int> parent;

    UnionFind(int n) : parent(n) {
        iota(parent.begin(), parent.end(), 0); // parent[i] = i
    }

    int find(int x) {
        while (parent[x] != x) x = parent[x];
        return x;
    }

    void unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx != ry) parent[rx] = ry;
    }
};
```
{% endtab %}
{% endtabs %}

**Problem**: In the worst case, the tree becomes a long chain (like a linked list). Then `find()` takes O(n) per call. We need optimizations.

---

## 29.3 Optimizations: Path Compression + Union by Rank

### Path Compression

During `find(x)`, make every node on the path point directly to the root. This flattens the tree so future queries are faster.

### Union by Rank

When merging two trees, attach the shorter tree under the root of the taller tree. This keeps trees balanced.

{% tabs %}
{% tab title="Python" %}
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # already connected
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True  # merged two different components
```
{% endtab %}
{% tab title="Java" %}
```java
class UnionFind {
    int[] parent, rank;

    UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]); // path compression
        return parent[x];
    }

    boolean union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
        return true;
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
class UnionFind {
public:
    vector<int> parent, rnk;

    UnionFind(int n) : parent(n), rnk(n, 0) {
        iota(parent.begin(), parent.end(), 0);
    }

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]); // path compression
        return parent[x];
    }

    bool unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return false;
        if (rnk[rx] < rnk[ry]) parent[rx] = ry;
        else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rnk[rx]++; }
        return true;
    }
};
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Amortized Complexity**: With BOTH path compression and union by rank, each `find` and `union` operation runs in amortized **O(alpha(n))** time, where alpha is the **inverse Ackermann function**. For all practical purposes, alpha(n) <= 5 for any n that fits in the universe. So it is effectively **O(1)** per operation!
{% endhint %}

### Language Spotlight: Union-Find Initialization

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Parent array | `list(range(n))` | `for` loop with `parent[i] = i` | `iota(parent.begin(), parent.end(), 0)` |
| Rank array | `[0] * n` | `new int[n]` (default 0) | `vector<int>(n, 0)` |
| Return value from union | `bool` (True if merged) | `boolean` | `bool` |

---

## 29.4 Applications of Union-Find

Union-Find is incredibly versatile. Here are the key applications:

### 1. Connected Components

Count how many connected components exist in an undirected graph: start with n components, subtract 1 for each successful `union()`.

### 2. Cycle Detection

In an undirected graph, process edges one by one. If `find(u) == find(v)` before merging, the edge (u, v) creates a cycle.

### 3. Redundant Connection

Given a graph that is a tree plus ONE extra edge, find the extra edge. Process edges in order; the first edge where both endpoints are already connected is the answer.

### 4. Accounts Merge

Given accounts like `["John", "email1", "email2"]`, merge accounts that share any email. Use Union-Find on email indices, then group all emails by their root.

### 5. Making Largest Island

Label connected components with Union-Find, then try flipping each 0 to 1 and see what components it would merge.

---

## 29.5 Minimum Spanning Trees — What and Why

A **spanning tree** of a connected graph is a subset of edges that:
1. Connects all vertices (it is a spanning subgraph)
2. Has no cycles (it is a tree)
3. Has exactly n-1 edges (for n vertices)

A **Minimum Spanning Tree (MST)** is a spanning tree with the smallest possible total edge weight.

**Real-world uses**:
- Building the cheapest road/cable/pipe network
- Approximation algorithms for NP-hard problems (like Traveling Salesman)
- Clustering (remove the heaviest MST edges to get clusters)
- Network design (connect computers with minimum wiring)

{% hint style="warning" %}
MST only makes sense for **undirected, connected, weighted** graphs. If the graph is disconnected, you get a **minimum spanning forest** (one tree per component).
{% endhint %}

---

## 29.6 Kruskal's Algorithm

**Idea**: Sort all edges by weight. Process edges from lightest to heaviest. Add an edge if it connects two different components (use Union-Find to check). Skip it if it would create a cycle.

{% tabs %}
{% tab title="Python" %}
```python
def kruskal(n, edges):
    """edges = [[u, v, weight], ...]  Return total MST weight."""
    edges.sort(key=lambda e: e[2])  # sort by weight
    uf = UnionFind(n)
    total = 0
    count = 0
    for u, v, w in edges:
        if uf.union(u, v):  # returns True if merged
            total += w
            count += 1
            if count == n - 1:
                break  # MST complete
    return total
```
{% endtab %}
{% tab title="Java" %}
```java
static int kruskal(int n, int[][] edges) {
    Arrays.sort(edges, (a, b) -> a[2] - b[2]);
    UnionFind uf = new UnionFind(n);
    int total = 0, count = 0;
    for (int[] e : edges) {
        if (uf.union(e[0], e[1])) {
            total += e[2];
            if (++count == n - 1) break;
        }
    }
    return total;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int kruskal(int n, vector<vector<int>>& edges) {
    sort(edges.begin(), edges.end(),
         [](auto& a, auto& b) { return a[2] < b[2]; });
    UnionFind uf(n);
    int total = 0, count = 0;
    for (auto& e : edges) {
        if (uf.unite(e[0], e[1])) {
            total += e[2];
            if (++count == n - 1) break;
        }
    }
    return total;
}
```
{% endtab %}
{% endtabs %}

**Time Complexity**: O(E log E) for sorting + O(E * alpha(V)) for Union-Find = **O(E log E)**.

---

## 29.7 Prim's Algorithm

**Idea**: Start from any vertex. Grow the MST one edge at a time: always pick the cheapest edge that connects a visited vertex to an unvisited vertex. Use a priority queue (min-heap) to efficiently find the next cheapest edge.

{% tabs %}
{% tab title="Python" %}
```python
import heapq

def prim(n, edges):
    """edges = [[u, v, weight], ...]  Return total MST weight."""
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = [False] * n
    heap = [(0, 0)]  # (weight, vertex) — start from vertex 0
    total = 0
    count = 0

    while heap and count < n:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        count += 1
        for nw, nv in adj[u]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv))

    return total
```
{% endtab %}
{% tab title="Java" %}
```java
static int prim(int n, int[][] edges) {
    List<int[]>[] adj = new List[n];
    for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
    for (int[] e : edges) {
        adj[e[0]].add(new int[]{e[2], e[1]});
        adj[e[1]].add(new int[]{e[2], e[0]});
    }
    boolean[] vis = new boolean[n];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, 0});
    int total = 0, count = 0;
    while (!pq.isEmpty() && count < n) {
        int[] top = pq.poll();
        if (vis[top[1]]) continue;
        vis[top[1]] = true;
        total += top[0];
        count++;
        for (int[] nb : adj[top[1]])
            if (!vis[nb[1]]) pq.offer(nb);
    }
    return total;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int prim(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back({e[2], e[1]});
        adj[e[1]].push_back({e[2], e[0]});
    }
    vector<bool> vis(n, false);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    int total = 0, count = 0;
    while (!pq.empty() && count < n) {
        auto [w, u] = pq.top(); pq.pop();
        if (vis[u]) continue;
        vis[u] = true;
        total += w;
        count++;
        for (auto [nw, nv] : adj[u])
            if (!vis[nv]) pq.push({nw, nv});
    }
    return total;
}
```
{% endtab %}
{% endtabs %}

**Time Complexity**: O(E log V) with a binary heap.

### Kruskal vs. Prim — When to Use Which?

| | Kruskal's | Prim's |
|---|-----------|--------|
| Approach | Edge-centric (sort edges) | Vertex-centric (grow tree) |
| Best for | Sparse graphs (E close to V) | Dense graphs (E close to V^2) |
| Data structure | Union-Find | Priority queue |
| Time | O(E log E) | O(E log V) |
| Edge list input? | Natural fit | Must build adjacency list |

---

## 29.8 MST Correctness — The Cut Property

Why do Kruskal's and Prim's algorithms actually produce an MST? The answer lies in the **cut property**.

### The Cut Property

A **cut** divides the vertices into two non-empty sets S and V-S. A **crossing edge** is an edge with one endpoint in S and the other in V-S.

**Cut Property**: For any cut, the minimum-weight crossing edge is in SOME MST.

**Proof** (by exchange argument):
1. Suppose the minimum crossing edge e is NOT in an MST T.
2. Add e to T. This creates a cycle (since T is a tree and adding any edge creates exactly one cycle).
3. The cycle must cross the cut at least twice (it starts in S, goes to V-S via e, and must return to S).
4. So there is another crossing edge e' in the cycle that is also in T.
5. Since e is the minimum crossing edge, weight(e) <= weight(e').
6. Remove e' from the cycle and keep e. The result T' = T - {e'} + {e} is still a spanning tree.
7. weight(T') <= weight(T), so T' is also an MST.
8. Therefore e IS in some MST.

Both algorithms exploit this property:
- **Kruskal's**: Each edge considered is the lightest crossing edge for the cut separating its two components.
- **Prim's**: Each edge added is the lightest crossing edge for the cut separating visited from unvisited vertices.

{% hint style="info" %}
**Exchange argument** is a proof technique you will see again and again in competitive programming. The idea is: assume the optimal solution does NOT include our choice, then show you can SWAP something to include it without making things worse. This thread connects to the greedy proofs in Ch 18!
{% endhint %}

---

## Five-Lens Framework: MST

Let us apply the five lenses to the Minimum Spanning Tree problem.

| Lens | Application |
|------|-------------|
| **Constraints** | n vertices, E edges, weights can be negative (MST still works!). Need exactly n-1 edges. |
| **Brute Force** | Try all possible subsets of n-1 edges: C(E, n-1) possibilities. Exponential! |
| **Pattern** | Greedy: always pick the cheapest safe edge. This is a "greedy on sorted input" pattern (like activity selection in Ch 18). |
| **Optimization** | Kruskal's uses Union-Find to check connectivity in near O(1). Prim's uses a heap to find the next cheapest edge in O(log V). |
| **Proof** | The cut property guarantees that the greedy choice is always safe. Exchange argument shows no better option exists. |

---

## Think Like a Pro

{% hint style="info" %}
**Petr Mitrichev** on connectivity problems: "If the question is 'are X and Y connected?' or 'how many connected components?', Union-Find is almost always the answer. It is one of the most useful data structures in competitive programming — simple to implement, almost impossible to get wrong once you have a template, and blazingly fast. I use it in nearly every contest."
{% endhint %}

---

## AOPS Showcase: "Minimum Spanning Tree"

The same problem — find the MST of a weighted graph — solved two ways, then proven correct.

### Approach 1: Kruskal's (Sort Edges + Union-Find)

**Strategy**: Sort all edges by weight. Greedily add edges that do not create cycles.

{% tabs %}
{% tab title="Python" %}
```python
def kruskal_mst(n, edges):
    """Return total MST weight using Kruskal's algorithm."""
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    edges.sort(key=lambda e: e[2])
    total = 0
    for u, v, w in edges:
        if union(u, v):
            total += w
    return total
```
{% endtab %}
{% tab title="Java" %}
```java
static int kruskalMST(int n, int[][] edges) {
    int[] parent = new int[n], rank = new int[n];
    for (int i = 0; i < n; i++) parent[i] = i;

    // find with path compression
    java.util.function.IntUnaryOperator find = null;
    final int[] p = parent, r = rank;  // effectively final
    find = x -> { if (p[x] != x) p[x] = find.applyAsInt(p[x]); return p[x]; };
    // Note: Java lambdas can't self-reference easily; use a helper method instead

    Arrays.sort(edges, (a, b) -> a[2] - b[2]);
    int total = 0;
    for (int[] e : edges) {
        int rx = findRoot(parent, e[0]), ry = findRoot(parent, e[1]);
        if (rx != ry) {
            if (rank[rx] < rank[ry]) parent[rx] = ry;
            else if (rank[rx] > rank[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rank[rx]++; }
            total += e[2];
        }
    }
    return total;
}

static int findRoot(int[] parent, int x) {
    if (parent[x] != x) parent[x] = findRoot(parent, parent[x]);
    return parent[x];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int kruskalMST(int n, vector<vector<int>>& edges) {
    vector<int> parent(n), rnk(n, 0);
    iota(parent.begin(), parent.end(), 0);

    function<int(int)> find = [&](int x) -> int {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    };

    sort(edges.begin(), edges.end(),
         [](auto& a, auto& b) { return a[2] < b[2]; });

    int total = 0;
    for (auto& e : edges) {
        int rx = find(e[0]), ry = find(e[1]);
        if (rx != ry) {
            if (rnk[rx] < rnk[ry]) parent[rx] = ry;
            else if (rnk[rx] > rnk[ry]) parent[ry] = rx;
            else { parent[ry] = rx; rnk[rx]++; }
            total += e[2];
        }
    }
    return total;
}
```
{% endtab %}
{% endtabs %}

**Time**: O(E log E) — dominated by sorting.

### Approach 2: Prim's (Grow One Tree)

**Strategy**: Start from vertex 0. Always expand to the nearest unvisited vertex.

{% tabs %}
{% tab title="Python" %}
```python
import heapq

def prim_mst(n, edges):
    """Return total MST weight using Prim's algorithm."""
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = [False] * n
    heap = [(0, 0)]  # (weight, vertex)
    total = 0
    count = 0

    while heap and count < n:
        w, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        count += 1
        for nw, nv in adj[u]:
            if not visited[nv]:
                heapq.heappush(heap, (nw, nv))

    return total
```
{% endtab %}
{% tab title="Java" %}
```java
static int primMST(int n, int[][] edges) {
    List<int[]>[] adj = new List[n];
    for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
    for (int[] e : edges) {
        adj[e[0]].add(new int[]{e[2], e[1]});
        adj[e[1]].add(new int[]{e[2], e[0]});
    }
    boolean[] vis = new boolean[n];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, 0});
    int total = 0, count = 0;
    while (!pq.isEmpty() && count < n) {
        int[] top = pq.poll();
        if (vis[top[1]]) continue;
        vis[top[1]] = true;
        total += top[0];
        count++;
        for (int[] nb : adj[top[1]])
            if (!vis[nb[1]]) pq.offer(nb);
    }
    return total;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int primMST(int n, vector<vector<int>>& edges) {
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges) {
        adj[e[0]].push_back({e[2], e[1]});
        adj[e[1]].push_back({e[2], e[0]});
    }
    vector<bool> vis(n, false);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    int total = 0, count = 0;
    while (!pq.empty() && count < n) {
        auto [w, u] = pq.top(); pq.pop();
        if (vis[u]) continue;
        vis[u] = true;
        total += w;
        count++;
        for (auto [nw, nv] : adj[u])
            if (!vis[nv]) pq.push({nw, nv});
    }
    return total;
}
```
{% endtab %}
{% endtabs %}

**Time**: O(E log V) — each edge is pushed/popped from the heap at most once.

### Correctness: Exchange Argument

Both algorithms are correct because of the **cut property** (proved in Section 29.8). At every step, the algorithm picks the minimum-weight crossing edge for some cut, which is guaranteed to be in an MST.

The exchange argument lets us prove that if our chosen edge is not in the "current" MST, we can swap it in without increasing the total weight. Since both algorithms only add edges that are minimum crossing edges for some cut, the result must be an MST.

---

## Legend's Corner

{% hint style="info" %}
**Joseph Kruskal** published his MST algorithm in 1956 — the same year that **Edsger Dijkstra** independently published both his shortest-path algorithm AND a version of Prim's MST algorithm! (Voitech Jarnik had actually discovered Prim's algorithm even earlier, in 1930, but it went unnoticed.) Two legendary algorithms born in the same year, both still used every single day, 70 years later. In competitive programming, Kruskal's is often preferred because Union-Find is easy to implement and edges often come as a list. But Prim's shines when the graph is dense and you already have an adjacency list.
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Common mistakes to avoid:**

1. **Forgetting path compression**: Without it, `find()` can degrade to O(n) per call. Always add `parent[x] = find(parent[x])` in the recursive find, or use iterative path compression.

2. **Forgetting union by rank (or size)**: Without it, trees can become unbalanced. Both optimizations together give the amortized O(alpha(n)) guarantee.

3. **1-indexed vs 0-indexed nodes**: Some problems (like Redundant Connection) use 1-indexed nodes. If your Union-Find is 0-indexed, either allocate size n+1, or subtract 1 from each node. This is a VERY common source of bugs.

4. **Prim's without a visited check**: If you do not skip already-visited vertices when popping from the priority queue, you will add edges incorrectly and may not get an MST.

5. **Kruskal's without sorting**: The entire algorithm relies on processing edges from lightest to heaviest. Forget to sort and you get nonsense.

6. **Using Union-Find on directed graphs**: Union-Find is for UNDIRECTED connectivity. For directed graphs, use DFS-based algorithms (like Tarjan's for SCCs).

7. **Off-by-one in MST edge count**: An MST of n vertices has exactly n-1 edges. If you have fewer, the graph is disconnected. If your algorithm adds more, something is wrong.

8. **Accounts Merge index confusion**: When using Union-Find for strings (like emails), map each string to an integer index first. Do not try to use strings directly as Union-Find keys.
{% endhint %}

---

## Practice Problems

| # | Problem | Difficulty | Key Technique |
|---|---------|-----------|---------------|
| W1 | Connected Components (UF) | Warmup | Union-Find basics |
| W2 | Redundant Connection | Warmup | Cycle detection (1-indexed!) |
| W3 | Kruskal's MST | Warmup | Sort edges + Union-Find |
| W4 | Prim's MST | Warmup | Priority queue MST |
| P1 | Number of Provinces | Practice | Union-Find on adjacency matrix |
| P2 | Accounts Merge | Practice | Union-Find with string mapping |
| P3 | Most Stones Removed | Practice | Connected components (row/col grouping) |
| P4 | Min Cost to Connect All Points | Practice | MST with Manhattan distance |
| P5 | Satisfiability of Equality Equations | Practice | Union-Find for equality/inequality |
| C1 | Operations to Make Network Connected | Challenge | Redundant edge counting |
| C2 | Making a Large Island | Challenge | Component labeling + flip |
| C3 | Number of Islands II | Challenge | Online Union-Find |
| C4 | Smallest String With Swaps | Challenge | Union-Find + per-component sorting |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
# Union-Find with defaultdict (flexible node types)
parent = {}
rank = {}

def find(x):
    if x not in parent:
        parent[x] = x
        rank[x] = 0
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Kruskal's in one line (after UF setup):
total = sum(w for u, v, w in sorted(edges, key=lambda e: e[2]) if union(u, v))

# heapq for Prim's — remember it's a MIN-heap by default (perfect!)
import heapq
```
{% endtab %}
{% tab title="Java" %}
```java
// Union-Find as int[] arrays (fastest for competitive programming)
int[] parent = new int[n], rank = new int[n];
for (int i = 0; i < n; i++) parent[i] = i;

// Kruskal's edge sort:
Arrays.sort(edges, (a, b) -> a[2] - b[2]);

// Prim's with PriorityQueue:
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Union-Find with iota initialization
vector<int> parent(n), rnk(n, 0);
iota(parent.begin(), parent.end(), 0);

// Lambda find with path compression
function<int(int)> find = [&](int x) -> int {
    return parent[x] == x ? x : parent[x] = find(parent[x]);
};

// Prim's min-heap: use greater<> for min priority_queue
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 19-20** (Graphs I & II) introduced BFS, DFS, and graph representations — Union-Find is an alternative to BFS/DFS for connectivity queries, and MST builds on the weighted graph concepts from those chapters
- **Ch 17** (Heaps & Priority Queues) gave you the min-heap — Prim's algorithm relies on it
- **Ch 18** (Greedy Algorithms) introduced the greedy paradigm and exchange arguments — both Kruskal's and Prim's are greedy algorithms, and MST correctness uses exchange argument
- **Ch 27** (Shortest Paths) covered Dijkstra's algorithm — Prim's looks very similar to Dijkstra's (both use a priority queue to greedily expand), but they optimize different things (total edge weight vs. distance from source)

### Looking Forward
- **Ch 30** (Segment Trees) will introduce range queries — a different "query data structure" that complements Union-Find
- **Ch 31** (Advanced DP) will cover DP on trees — MST creates a tree structure that can be analyzed with tree DP
- **Part V** awaits — you have completed all Gold-level content!

### Cross-Chapter Threads
- **"Reduce to known"**: Many connectivity problems (accounts merge, stones removed, satisfiability) REDUCE to Union-Find. The skill of recognizing that "this is really a connectivity problem" is what makes Union-Find so powerful.
- **"Brute force is a strategy"**: Brute-force MST tries all C(E, n-1) subsets. Kruskal's greedy approach reduces this to O(E log E). But understanding the brute force helps you see WHY greedy works.
- **"Sort first"**: Kruskal's algorithm is a perfect example of the "sort-first" pattern — sorting the input reveals structure that makes the greedy choice obvious.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"Can we maintain an MST as edges are added or removed?"** This is the **dynamic MST** problem. Adding edges is manageable (add the edge, find the cycle, remove the heaviest edge in the cycle). Removing edges is much harder and requires advanced data structures like link-cut trees. This appears in some Platinum problems.

2. **"What if we want the SECOND minimum spanning tree?"** Find the MST, then for each non-MST edge, consider swapping it with the heaviest edge on the MST path between its endpoints. The best such swap gives the second MST. This can be done in O(E log V) with LCA (Lowest Common Ancestor) techniques.

3. **"How does Union-Find work in distributed systems?"** In distributed computing, different servers may need to track which nodes are connected across a network. Distributed Union-Find is an active research area — the challenge is maintaining path compression when data is spread across machines.

---

## What's Next

{% hint style="info" %}
**CONGRATULATIONS! You have completed Part IV: The Gold Crucible!**

Take a moment to appreciate how far you have come. You have mastered:
- **Dynamic Programming** (three full chapters: foundation, grids, subsequences/knapsack)
- **Trees** (traversals, BST, tree DP)
- **Shortest Paths** (Dijkstra, Bellman-Ford, Floyd-Warshall)
- **Topological Sort** (Kahn's algorithm, cycle detection in DAGs)
- **Union-Find & MST** (Kruskal's, Prim's, connectivity problems)

You are now ready to attempt **USACO Gold** contests! These seven chapters cover the core topics that appear on Gold. Practice with past USACO Gold problems, and you will see these patterns everywhere.

**Part V: The Platinum Summit** awaits. Segment trees, advanced DP (bitmask, interval, trees), string algorithms, advanced graph algorithms, and computational geometry — the final frontier of competitive programming. The summit is in sight!
{% endhint %}
