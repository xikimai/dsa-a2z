# Advanced Trees & Graph Algorithms

{% hint style="info" %}
**Platinum-level content!** This chapter covers advanced tree techniques (binary lifting, Euler tour, HLD, centroid decomposition) and graph algorithms (bridges, articulation points, SCCs). These are core tools for USACO Platinum and competitive programming at the highest levels. If you have made it this far, you are among the top competitive programmers in your age group.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand the Lowest Common Ancestor (LCA) problem and why it appears everywhere in tree problems
- Implement Binary Lifting to precompute 2^k ancestors and answer LCA queries in O(log n)
- Understand the Euler Tour Technique and how it flattens a tree into an array
- Use the Euler Tour to convert subtree queries into range queries on an array
- Learn the concept of Heavy-Light Decomposition (HLD) for path queries on trees
- Learn the concept of Centroid Decomposition for divide-and-conquer on trees
- Find bridges in an undirected graph using Tarjan's algorithm
- Find articulation points in an undirected graph using Tarjan's algorithm
- Find Strongly Connected Components (SCCs) in a directed graph using Kosaraju's two-pass algorithm
- Condense a directed graph into a DAG of SCCs
- Compute distances between arbitrary nodes in a tree using LCA + distance from root
- Recognize which technique to apply to a given tree or graph problem

---

## The Story: "The Ancestry Database"

Dr. Priya managed the world's largest online genealogy database — FamilyTree.com — with over 50 million people traced across 400 generations. Every day, millions of users would ask the same question: "Who is the closest common ancestor of person A and person B?"

The naive approach was obvious: start from person A, walk up the tree to the root, recording every ancestor. Then start from person B, walk up until you hit someone on A's path. But with trees up to 400 levels deep and 10 million queries per day, this was painfully slow. Each query could take up to 400 steps, and at 10 million queries, that was 4 billion operations daily. The servers were melting.

"There has to be a faster way," Priya muttered, staring at the family tree. She noticed something: if she could jump up the tree in powers of 2 — first 1 step, then 2, then 4, then 8 — she could reach any ancestor in at most log2(400) = 9 jumps instead of 400. She just needed to precompute a table of "who is the 2^k-th ancestor of each person?"

That night, she implemented Binary Lifting. Query time dropped from 400 steps to 9 steps. The servers stopped melting. And she realized: this same trick of precomputing power-of-2 jumps could solve dozens of other tree problems too.

But Priya's work was not done. The next week, the security team found something alarming in their network graph: critical connections — single links whose failure would split the entire network in two. Finding these "bridges" required a different kind of algorithm entirely...

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles.

### Puzzle 1: "The Ancestor Jump"

In a family tree with depth 20, the naive LCA algorithm walks up from both nodes step by step, comparing ancestors at each level. In the worst case, how many steps does this take per query?

Now imagine you could "jump" up the tree in powers of 2: jump 1 level, jump 2 levels, jump 4 levels, jump 8 levels. How many jumps would you need to reach any ancestor in a tree of depth 20?

{% hint style="info" %}
Naive: up to 20 steps per node, so up to 40 steps per query. With power-of-2 jumps: at most ceil(log2(20)) = 5 jumps. For a tree of depth 100,000, that is 100,000 vs 17 jumps — a massive difference! This is the core idea behind Binary Lifting.
{% endhint %}

### Puzzle 2: "Strongly Connected Cities"

Consider a directed road network between cities. City A can reach city B, but maybe city B cannot reach city A (one-way roads). We say two cities are "strongly connected" if you can travel from either to the other.

Given these one-way roads: 0->1, 1->2, 2->0, 1->3, 3->4. How many groups of mutually reachable cities are there?

{% hint style="info" %}
Cities {0, 1, 2} can all reach each other (through the cycle 0->1->2->0). City 3 can only be reached from 1 but cannot get back. City 4 can only be reached from 3. So there are 3 groups: {0,1,2}, {3}, {4}. These groups are called Strongly Connected Components (SCCs).
{% endhint %}

### Puzzle 3: "The Critical Bridge"

A network has 5 computers (0-4) connected by cables: 0-1, 1-2, 2-0, 1-3, 3-4. If a single cable fails, which cables would disconnect part of the network?

{% hint style="info" %}
Cables 0-1, 1-2, 2-0 form a cycle — removing any one still leaves a path between those three computers. But cable 1-3 is the ONLY path between {0,1,2} and {3,4}. And cable 3-4 is the ONLY path to computer 4. So cables [1,3] and [3,4] are bridges — their removal disconnects the network. Finding these efficiently is the job of Tarjan's Bridge-Finding Algorithm.
{% endhint %}

---

## 33.1 Binary Lifting — Fast LCA

### The Problem

Given a rooted tree and multiple queries "what is the LCA of nodes u and v?", answer each query efficiently.

**LCA (Lowest Common Ancestor)**: The deepest node that is an ancestor of both u and v.

### Naive Approach: Walk Up

1. Bring u and v to the same depth by walking the deeper one up.
2. Walk both up one step at a time until they meet.

**Time**: O(n) per query in the worst case (skewed tree).

### Binary Lifting Idea

Precompute a table `up[v][k]` = the 2^k-th ancestor of node v.

- `up[v][0]` = parent of v
- `up[v][k]` = `up[up[v][k-1]][k-1]` (the 2^(k-1)-th ancestor of the 2^(k-1)-th ancestor)

This table has size O(n log n) and can be built in O(n log n) time.

### LCA Algorithm

1. Bring u and v to the same depth using binary jumps.
2. If they are the same node, return it.
3. Jump both u and v up by decreasing powers of 2, but only when the jump does NOT make them equal (we want to stop just below the LCA).
4. Return the parent of where they end up.

**Time**: O(log n) per query after O(n log n) preprocessing.

{% tabs %}
{% tab title="Python" %}
```python
import math

def build_binary_lifting(n, edges, root=0):
    """Build adjacency list, compute depths and binary lifting table."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    LOG = max(1, math.ceil(math.log2(n)) + 1) if n > 1 else 1
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    # BFS to set depths and parents
    from collections import deque
    visited = [False] * n
    queue = deque([root])
    visited[root] = True
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                depth[neighbor] = depth[node] + 1
                up[neighbor][0] = node
                queue.append(neighbor)

    # Fill binary lifting table
    for k in range(1, LOG):
        for v in range(n):
            if up[v][k - 1] != -1:
                up[v][k] = up[up[v][k - 1]][k - 1]

    return up, depth, LOG

def lca(u, v, up, depth, LOG):
    """Find LCA of u and v using binary lifting."""
    # Step 1: bring to same depth
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if (diff >> k) & 1:
            u = up[u][k]

    if u == v:
        return u

    # Step 2: jump both up
    for k in range(LOG - 1, -1, -1):
        if up[u][k] != up[v][k]:
            u = up[u][k]
            v = up[v][k]

    return up[u][0]
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

public class BinaryLifting {
    int[][] up;
    int[] depth;
    int LOG;

    public BinaryLifting(int n, int[][] edges, int root) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        LOG = Math.max(1, (int)(Math.ceil(Math.log(n) / Math.log(2))) + 1);
        up = new int[n][LOG];
        depth = new int[n];
        for (int[] row : up) Arrays.fill(row, -1);

        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(root);
        visited[root] = true;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int nb : adj.get(node)) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    depth[nb] = depth[node] + 1;
                    up[nb][0] = node;
                    queue.add(nb);
                }
            }
        }

        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (up[v][k - 1] != -1)
                    up[v][k] = up[up[v][k - 1]][k - 1];
    }

    public int lca(int u, int v) {
        if (depth[u] < depth[v]) { int t = u; u = v; v = t; }
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if (((diff >> k) & 1) == 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

class BinaryLifting {
public:
    vector<vector<int>> up;
    vector<int> depth;
    int LOG;

    BinaryLifting(int n, vector<vector<int>>& edges, int root = 0) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        LOG = max(1, (int)ceil(log2(n)) + 1);
        up.assign(n, vector<int>(LOG, -1));
        depth.assign(n, 0);

        vector<bool> visited(n, false);
        queue<int> q;
        q.push(root);
        visited[root] = true;
        while (!q.empty()) {
            int node = q.front(); q.pop();
            for (int nb : adj[node]) {
                if (!visited[nb]) {
                    visited[nb] = true;
                    depth[nb] = depth[node] + 1;
                    up[nb][0] = node;
                    q.push(nb);
                }
            }
        }

        for (int k = 1; k < LOG; k++)
            for (int v = 0; v < n; v++)
                if (up[v][k - 1] != -1)
                    up[v][k] = up[up[v][k - 1]][k - 1];
    }

    int lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        int diff = depth[u] - depth[v];
        for (int k = 0; k < LOG; k++)
            if ((diff >> k) & 1) u = up[u][k];
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k]; }
        return up[u][0];
    }
};
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Language Spotlight**: All three languages use the same algorithm. Python uses lists of lists, Java uses 2D arrays, and C++ uses `vector<vector<int>>`. The BFS-based initialization avoids recursion depth issues on large trees.
{% endhint %}

---

## 33.2 Euler Tour Technique

### The Idea

An Euler Tour "flattens" a tree into an array by recording the DFS entry time (tin) and exit time (tout) of each node. After flattening:

- **Subtree of node v** corresponds to the contiguous range `[tin[v], tout[v]]` in the array.
- This means any subtree query (sum, min, max) becomes a range query on an array — and we already know how to do range queries efficiently (prefix sums, segment trees from Ch 30, BITs).

### How It Works

Run a DFS from the root. Assign a "timestamp" to each node when you first visit it (tin) and when you leave it (tout). The Euler tour array records nodes in order of their tin values.

{% tabs %}
{% tab title="Python" %}
```python
def euler_tour(n, edges, root=0):
    """Return the Euler tour order and tin/tout arrays."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    tin = [0] * n
    tout = [0] * n
    order = []
    timer = [0]  # use list for mutability in closure

    def dfs(node, parent):
        tin[node] = timer[0]
        order.append(node)
        timer[0] += 1
        for nb in adj[node]:
            if nb != parent:
                dfs(nb, node)
        tout[node] = timer[0] - 1

    dfs(root, -1)
    return order, tin, tout
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

public class EulerTour {
    int[] tin, tout;
    List<Integer> order;
    int timer = 0;
    List<List<Integer>> adj;

    public void build(int n, int[][] edges, int root) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        tin = new int[n];
        tout = new int[n];
        order = new ArrayList<>();
        dfs(root, -1);
    }

    void dfs(int node, int parent) {
        tin[node] = timer;
        order.add(node);
        timer++;
        for (int nb : adj.get(node))
            if (nb != parent) dfs(nb, node);
        tout[node] = timer - 1;
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
using namespace std;

class EulerTour {
public:
    vector<int> tin, tout, order;
    int timer = 0;
    vector<vector<int>> adj;

    void build(int n, vector<vector<int>>& edges, int root = 0) {
        adj.assign(n, {});
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        tin.resize(n);
        tout.resize(n);
        dfs(root, -1);
    }

    void dfs(int node, int parent) {
        tin[node] = timer;
        order.push_back(node);
        timer++;
        for (int nb : adj[node])
            if (nb != parent) dfs(nb, node);
        tout[node] = timer - 1;
    }
};
```
{% endtab %}
{% endtabs %}

### Subtree Queries with Euler Tour

Once you have the Euler tour, the subtree of node v is exactly the nodes at positions `tin[v]` through `tout[v]` in the order array. To find the sum of values in v's subtree, just sum the values at those positions — a perfect use case for prefix sums!

---

## 33.3 Heavy-Light Decomposition (Concept)

{% hint style="warning" %}
**Concept only** — full implementation is beyond typical USACO Platinum, but understanding the idea is valuable.
{% endhint %}

### The Problem

We want to answer **path queries** on a tree: "What is the sum (or max, min, etc.) of values on the path from u to v?" Euler Tour handles subtree queries, but path queries need something more.

### The Idea

1. Decompose the tree into **chains** (paths) such that any root-to-leaf path crosses at most O(log n) chains.
2. Each chain is stored in a segment tree (or BIT).
3. A path query from u to v crosses O(log n) chains, and each chain query takes O(log n) time with a segment tree.
4. Total: O(log^2 n) per query.

### How to Decompose

For each node, the **heavy child** is the child with the largest subtree. The **heavy edge** connects a node to its heavy child. Heavy edges form chains. Every root-to-leaf path has at most O(log n) light edges (non-heavy), so it crosses at most O(log n) chains.

{% hint style="info" %}
**When you need HLD**: Path queries with updates (like "add x to every node on the path from u to v, then query the sum from a to b"). If you only need subtree queries, Euler Tour is sufficient.
{% endhint %}

---

## 33.4 Centroid Decomposition (Concept)

{% hint style="warning" %}
**Concept only** — this is an advanced divide-and-conquer technique on trees.
{% endhint %}

### The Idea

The **centroid** of a tree is a node whose removal splits the tree into components of size at most n/2. Every tree has a centroid (and at most two).

**Centroid Decomposition** recursively finds the centroid, removes it, and recurses on each subtree. This creates a "centroid tree" of depth O(log n).

### Applications

- Count pairs of nodes at distance exactly k
- Find the closest marked node to a query node
- Problems where you need to consider all paths passing through a node

{% hint style="info" %}
**Key insight**: In the centroid decomposition tree, any path in the original tree passes through the LCA of its endpoints in the centroid tree. The depth is O(log n), so algorithms that process "all paths through a node" run in O(n log n) total.
{% endhint %}

---

## 33.5 Bridges and Articulation Points

### Bridges

A **bridge** is an edge whose removal disconnects the graph. Finding all bridges is critical for network reliability analysis.

### Tarjan's Bridge-Finding Algorithm

Use DFS and track two values for each node:
- `disc[v]` = discovery time (when v was first visited)
- `low[v]` = the lowest discovery time reachable from the subtree of v (using back edges)

An edge (u, v) where u is the parent of v in the DFS tree is a bridge if and only if `low[v] > disc[u]` — meaning the subtree rooted at v has NO back edge to u or any of u's ancestors.

{% tabs %}
{% tab title="Python" %}
```python
def find_bridges(n, edges):
    """Find all bridges in an undirected graph."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * n
    low = [0] * n
    bridges = []
    timer = [0]

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in adj[u]:
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append([min(u, v), max(u, v)])
            elif v != parent:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    bridges.sort()
    return bridges
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

public class Bridges {
    static int timer = 0;
    static int[] disc, low;
    static List<List<Integer>> adj;
    static List<int[]> bridges;

    public static List<int[]> findBridges(int n, int[][] edges) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        disc = new int[n];
        low = new int[n];
        Arrays.fill(disc, -1);
        bridges = new ArrayList<>();
        timer = 0;
        for (int i = 0; i < n; i++)
            if (disc[i] == -1) dfs(i, -1);
        return bridges;
    }

    static void dfs(int u, int parent) {
        disc[u] = low[u] = timer++;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > disc[u])
                    bridges.add(new int[]{Math.min(u,v), Math.max(u,v)});
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <algorithm>
using namespace std;

int timer_val = 0;
vector<int> disc_arr, low_arr;
vector<vector<int>> adj_g;
vector<vector<int>> bridges_result;

void dfs_bridge(int u, int parent) {
    disc_arr[u] = low_arr[u] = timer_val++;
    for (int v : adj_g[u]) {
        if (disc_arr[v] == -1) {
            dfs_bridge(v, u);
            low_arr[u] = min(low_arr[u], low_arr[v]);
            if (low_arr[v] > disc_arr[u])
                bridges_result.push_back({min(u,v), max(u,v)});
        } else if (v != parent) {
            low_arr[u] = min(low_arr[u], disc_arr[v]);
        }
    }
}

vector<vector<int>> find_bridges(int n, vector<vector<int>>& edges) {
    adj_g.assign(n, {});
    for (auto& e : edges) {
        adj_g[e[0]].push_back(e[1]);
        adj_g[e[1]].push_back(e[0]);
    }
    disc_arr.assign(n, -1);
    low_arr.assign(n, 0);
    bridges_result.clear();
    timer_val = 0;
    for (int i = 0; i < n; i++)
        if (disc_arr[i] == -1) dfs_bridge(i, -1);
    sort(bridges_result.begin(), bridges_result.end());
    return bridges_result;
}
```
{% endtab %}
{% endtabs %}

### Articulation Points

An **articulation point** is a vertex whose removal disconnects the graph. The algorithm is similar to bridge finding:

- The root of the DFS tree is an articulation point if it has 2+ children.
- A non-root node u is an articulation point if it has a child v where `low[v] >= disc[u]` — meaning v's subtree cannot reach above u.

{% tabs %}
{% tab title="Python" %}
```python
def find_articulation_points(n, edges):
    """Find all articulation points in an undirected graph."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    disc = [-1] * n
    low = [0] * n
    ap = set()
    timer = [0]

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        children = 0
        for v in adj[u]:
            if disc[v] == -1:
                children += 1
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if parent == -1 and children > 1:
                    ap.add(u)
                if parent != -1 and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return sorted(ap)
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

public class ArticulationPoints {
    static int timer = 0;
    static int[] disc, low;
    static List<List<Integer>> adj;
    static Set<Integer> ap;

    public static List<Integer> findAP(int n, int[][] edges) {
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        disc = new int[n]; low = new int[n];
        Arrays.fill(disc, -1);
        ap = new TreeSet<>();
        timer = 0;
        for (int i = 0; i < n; i++)
            if (disc[i] == -1) dfs(i, -1);
        return new ArrayList<>(ap);
    }

    static void dfs(int u, int parent) {
        disc[u] = low[u] = timer++;
        int children = 0;
        for (int v : adj.get(u)) {
            if (disc[v] == -1) {
                children++;
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);
                if (parent == -1 && children > 1) ap.add(u);
                if (parent != -1 && low[v] >= disc[u]) ap.add(u);
            } else if (v != parent) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int ap_timer = 0;
vector<int> ap_disc, ap_low;
vector<vector<int>> ap_adj;
set<int> ap_set;

void dfs_ap(int u, int parent) {
    ap_disc[u] = ap_low[u] = ap_timer++;
    int children = 0;
    for (int v : ap_adj[u]) {
        if (ap_disc[v] == -1) {
            children++;
            dfs_ap(v, u);
            ap_low[u] = min(ap_low[u], ap_low[v]);
            if (parent == -1 && children > 1) ap_set.insert(u);
            if (parent != -1 && ap_low[v] >= ap_disc[u]) ap_set.insert(u);
        } else if (v != parent) {
            ap_low[u] = min(ap_low[u], ap_disc[v]);
        }
    }
}

vector<int> find_ap(int n, vector<vector<int>>& edges) {
    ap_adj.assign(n, {});
    for (auto& e : edges) {
        ap_adj[e[0]].push_back(e[1]);
        ap_adj[e[1]].push_back(e[0]);
    }
    ap_disc.assign(n, -1);
    ap_low.assign(n, 0);
    ap_set.clear();
    ap_timer = 0;
    for (int i = 0; i < n; i++)
        if (ap_disc[i] == -1) dfs_ap(i, -1);
    return vector<int>(ap_set.begin(), ap_set.end());
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Bridge vs Articulation Point**: An edge (u,v) is a bridge when `low[v] > disc[u]` (strict inequality). A node u is an articulation point when `low[v] >= disc[u]` (non-strict). The difference matters! A bridge means the subtree has NO back edge to u or above. An articulation point means the subtree has no back edge ABOVE u (it might have one to u itself, but that does not help if u is removed).
{% endhint %}

---

## 33.6 Strongly Connected Components (Kosaraju's Algorithm)

### The Problem

In a **directed** graph, a Strongly Connected Component (SCC) is a maximal set of vertices such that every vertex is reachable from every other vertex in the set.

### Kosaraju's Two-Pass Algorithm

1. **First pass**: Run DFS on the original graph. Push each node onto a stack when its DFS finishes (post-order).
2. **Transpose**: Reverse all edges in the graph.
3. **Second pass**: Pop nodes from the stack and run DFS on the transposed graph. Each DFS from the second pass finds one SCC.

**Why it works**: The stack order ensures we process SCCs in reverse topological order. In the transposed graph, a DFS from a node in the "first" SCC (topologically) will only reach nodes in that same SCC.

{% tabs %}
{% tab title="Python" %}
```python
def kosaraju(n, edges):
    """Find SCCs using Kosaraju's algorithm. Returns list of component labels."""
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        radj[v].append(u)

    # First pass: get finish order
    visited = [False] * n
    order = []
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # Second pass: assign components
    comp = [-1] * n
    count = 0
    def dfs2(u, label):
        comp[u] = label
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v, label)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, count)
            count += 1

    return count, comp
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

public class Kosaraju {
    public static int[] kosaraju(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>(), radj = new ArrayList<>();
        for (int i = 0; i < n; i++) { adj.add(new ArrayList<>()); radj.add(new ArrayList<>()); }
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); radj.get(e[1]).add(e[0]); }

        boolean[] visited = new boolean[n];
        List<Integer> order = new ArrayList<>();
        for (int i = 0; i < n; i++)
            if (!visited[i]) dfs1(i, adj, visited, order);

        int[] comp = new int[n];
        Arrays.fill(comp, -1);
        int count = 0;
        for (int i = order.size() - 1; i >= 0; i--)
            if (comp[order.get(i)] == -1)
                dfs2(order.get(i), count++, radj, comp);
        return new int[]{count}; // return count
    }

    static void dfs1(int u, List<List<Integer>> adj, boolean[] vis, List<Integer> order) {
        vis[u] = true;
        for (int v : adj.get(u)) if (!vis[v]) dfs1(v, adj, vis, order);
        order.add(u);
    }

    static void dfs2(int u, int label, List<List<Integer>> radj, int[] comp) {
        comp[u] = label;
        for (int v : radj.get(u)) if (comp[v] == -1) dfs2(v, label, radj, comp);
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Kosaraju {
public:
    int n;
    vector<vector<int>> adj, radj;
    vector<int> order, comp;
    vector<bool> visited;

    Kosaraju(int n, vector<vector<int>>& edges) : n(n), adj(n), radj(n), comp(n, -1), visited(n, false) {
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            radj[e[1]].push_back(e[0]);
        }
    }

    void dfs1(int u) {
        visited[u] = true;
        for (int v : adj[u]) if (!visited[v]) dfs1(v);
        order.push_back(u);
    }

    void dfs2(int u, int label) {
        comp[u] = label;
        for (int v : radj[u]) if (comp[v] == -1) dfs2(v, label);
    }

    int solve() {
        for (int i = 0; i < n; i++) if (!visited[i]) dfs1(i);
        int count = 0;
        for (int i = n - 1; i >= 0; i--)
            if (comp[order[i]] == -1) dfs2(order[i], count++);
        return count;
    }
};
```
{% endtab %}
{% endtabs %}

---

## 33.7 Putting It All Together — Advanced Graph Patterns

### When to Use What

| Technique | Problem Type | Time Complexity |
|-----------|-------------|-----------------|
| Binary Lifting | LCA queries, ancestor queries | O(n log n) prep, O(log n) query |
| Euler Tour | Subtree queries (sum, min, max) | O(n) prep, O(1) per subtree range |
| HLD | Path queries with updates | O(n) prep, O(log^2 n) query |
| Centroid Decomposition | Distance-related tree queries | O(n log n) total |
| Bridges (Tarjan) | Find critical edges | O(V + E) |
| Articulation Points | Find critical vertices | O(V + E) |
| Kosaraju's SCC | Find strongly connected components | O(V + E) |

### Common Combinations

1. **LCA + Distance**: Compute `dist[v]` = distance from root to v. Then `dist(u,v) = dist[u] + dist[v] - 2 * dist[LCA(u,v)]`.
2. **Euler Tour + Prefix Sums**: Flatten tree, compute prefix sums for O(1) subtree sum queries.
3. **SCC + DAG**: Condense SCCs into single nodes to get a DAG, then apply topological sort/DP.
4. **Bridges + 2-Edge-Connected Components**: Remove bridges to find components where every pair is connected by at least 2 edge-disjoint paths.

---

## Five-Lens Framework: LCA with Binary Lifting

{% hint style="info" %}
**Constraints**: n up to 10^5 nodes, Q up to 10^5 queries. Must answer all queries efficiently.

**Brute Force**: Walk up from both nodes to find common ancestor. O(n) per query, O(nQ) total. For n = Q = 10^5, that is 10^10 operations — way too slow.

**Pattern**: Binary representation! Any integer up to n can be represented as a sum of powers of 2. So any "jump up the tree" can be decomposed into O(log n) power-of-2 jumps.

**Optimization**: Precompute a table `up[v][k]` = 2^k-th ancestor of v. Table size O(n log n). Each LCA query uses O(log n) jumps. Total: O(n log n + Q log n).

**Proof**: Correctness relies on the binary representation property: every positive integer has a unique binary representation, so any jump distance can be achieved by combining power-of-2 jumps. The preprocessing recurrence `up[v][k] = up[up[v][k-1]][k-1]` is correct because jumping 2^k = jumping 2^(k-1) twice.
{% endhint %}

---

## Think Like a Pro

{% hint style="info" %}
**Tourist (Gennady Korotkevich)**: "Binary lifting is one of those techniques that appears simple but has deep applications. Once you can jump to any ancestor in O(log n), you can binary search on paths, find the first ancestor satisfying a property, and combine with segment trees for path queries. I use it in probably 20% of tree problems at the competitive programming level."
{% endhint %}

---

## AOPS Showcase: "LCA Queries"

**Problem**: Given a rooted tree with n nodes and Q queries, each asking for the LCA of two nodes, answer all queries.

### Solution 1: Naive Walk-Up — O(n) per query

For each query (u, v):
1. Bring the deeper node up to the same depth as the shallower one.
2. Walk both up one step at a time until they meet.

```python
def lca_naive(u, v, parent, depth):
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u
```

**Time**: O(n) per query. For a skewed tree (linked list), we might walk all the way up.

### Solution 2: Binary Lifting — O(log n) per query

Precompute the table and use the algorithm from Section 33.1.

**Time**: O(n log n) preprocessing, O(log n) per query. This is the standard approach for most competitive programming problems.

### Solution 3: Euler Tour + Sparse Table — O(1) per query (concept)

1. Run an Euler tour that records each node every time it is visited (entry AND return).
2. LCA(u, v) = the node with minimum depth in the Euler tour between the first occurrences of u and v.
3. This is a Range Minimum Query (RMQ) on an array — solvable in O(1) with a Sparse Table.

**Time**: O(n log n) preprocessing, O(1) per query. Best asymptotically, but more complex to implement. Binary lifting is usually preferred in contests for its simplicity.

---

## Legend's Corner

{% hint style="info" %}
**Benq (Benjamin Qi)**: "In USACO Platinum, I would say about 30% of tree problems use binary lifting or Euler tour. The key insight is that Euler tour converts tree problems into array problems — and we already have powerful tools for arrays like segment trees and BITs. That conversion is incredibly powerful. For graph problems, knowing bridges and SCCs opens up a whole class of problems about network reliability and graph condensation. These are not just contest tricks — they are fundamental tools that make hard problems tractable."
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Watch out for these common mistakes!**

1. **Binary lifting depth mismatch**: Before finding LCA, you MUST bring both nodes to the same depth first. Forgetting this step leads to wrong answers on every query where the nodes start at different depths.

2. **Tarjan's bridge: parent check**: When updating `low[u]`, do NOT update from the parent edge. The back edge to the parent is the edge you came from — it does not count as a "back edge" for bridge detection. Using `v != parent` is the correct check.

3. **Kosaraju's transpose**: You must reverse ALL edges, not just some. A common bug is building the transpose graph incorrectly (e.g., adding edges in both directions instead of reversing).

4. **Euler tour off-by-one**: The subtree of v spans `[tin[v], tout[v]]` inclusive. Getting the boundary wrong by 1 silently corrupts all subtree queries.

5. **SCC on undirected graphs**: Strongly Connected Components are a concept for DIRECTED graphs only. Every connected component in an undirected graph is trivially strongly connected. If you are asked for SCCs, the graph must be directed!

6. **Binary lifting table size**: You need `ceil(log2(n)) + 1` columns, not n columns. Using n columns wastes massive amounts of memory. For n = 10^5, you need about 17 columns, not 100,000.

7. **Recursion depth**: For large trees (n > 10^4), recursive DFS may hit Python's recursion limit. Use `sys.setrecursionlimit(n + 100)` or convert to iterative DFS with an explicit stack.
{% endhint %}

---

## Practice Problems

| # | Problem | Difficulty | Key Technique |
|---|---------|-----------|---------------|
| W1 | LCA with Binary Lifting | Warmup | Binary lifting |
| W2 | Euler Tour of Tree | Warmup | DFS order |
| W3 | Find Bridges in Graph | Warmup | Tarjan's algorithm |
| P1 | Articulation Points | Practice | Tarjan's variant |
| P2 | Strongly Connected Components | Practice | Kosaraju's algorithm |
| P3 | Subtree Sum (Euler Tour) | Practice | Euler tour + prefix sums |
| P4 | LCA Queries with Values | Practice | Binary lifting |
| P5 | Count SCCs of Size > 1 | Practice | Kosaraju's + counting |
| C1 | Critical Connections in Network | Challenge | Bridges (LC 1192) |
| C2 | Reorder Routes to City Zero | Challenge | Directed tree DFS (LC 1466) |
| C3 | Tree Distance Queries | Challenge | Binary lifting + LCA + dist |
| C4 | SCC Condensation DAG | Challenge | Kosaraju's + DAG construction |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
- `sys.setrecursionlimit(200000)` — essential for deep recursive DFS on large trees
- `from collections import deque` — BFS for building tree levels (avoids recursion depth issues)
- Use iterative DFS with explicit stack for production code on large inputs
- `math.log2(n)` for computing LOG in binary lifting
{% endtab %}
{% tab title="Java" %}
- `Arrays.fill(disc, -1)` — fast initialization of discovery array
- `List<List<Integer>>` for adjacency lists, but `int[][]` for the binary lifting table (arrays are faster)
- Use `ArrayDeque` instead of `LinkedList` for BFS queues (faster)
- Watch for stack overflow on recursive DFS: increase JVM stack size with `-Xss` flag or use iterative DFS
{% endtab %}
{% tab title="C++" %}
- `vector<vector<int>>` for adjacency lists and binary lifting table
- `iota(parent.begin(), parent.end(), 0)` to initialize parent array
- `function<void(int,int)> dfs = [&](int u, int p) { ... };` for lambda DFS (convenient but slightly slower than regular functions)
- `__builtin_clz(n)` to compute `floor(log2(n))` in O(1) for bit tricks
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

{% hint style="info" %}
**Looking Back**:
- Chapter 19-20 (Graphs): BFS and DFS are the foundation. Tarjan's algorithm is a sophisticated use of DFS with additional bookkeeping.
- Chapter 26 (Trees): Tree traversals and subtree concepts. Euler tour is a generalization of these traversals.
- Chapter 28 (Topological Sort): SCC condensation produces a DAG, which you can then topologically sort — combining two powerful techniques.

**Looking Forward**:
- Chapter 34 (Geometry & Sweep): The final chapter! Sweep line algorithms share the same spirit of "preprocess, then answer queries efficiently."
- USACO Platinum: Binary lifting, Euler tour, and SCC are all common in Platinum contests. HLD and centroid decomposition appear in the hardest problems.
{% endhint %}

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **Virtual Trees**: When you have Q queries on a tree, sometimes only a few nodes matter per query. A "virtual tree" (auxiliary tree) contains only the relevant nodes and their LCAs, dramatically reducing the tree size. How would you construct a virtual tree efficiently?

2. **Link-Cut Trees**: What if the tree changes dynamically — edges are added and removed? Link-Cut Trees (Sleator-Tarjan) support LCA, path queries, and edge modifications all in O(log n) amortized. They use splay trees internally. Can you think of problems where the tree structure itself changes over time?

3. **Block-Cut Trees**: A block-cut tree represents the biconnected components and articulation points of an undirected graph as a tree. Every graph has a unique block-cut tree. How might this tree structure help solve problems about paths that must avoid certain vertices?

---

## What's Next

**Chapter 34: Computational Geometry & Sweep Line** — the final chapter of The Platinum Summit! You will learn about convex hulls, sweep line algorithms, and geometric techniques that complete your competitive programming toolkit. With the tree and graph mastery from this chapter, you will have a complete foundation for tackling the hardest problems in USACO Platinum and beyond.
