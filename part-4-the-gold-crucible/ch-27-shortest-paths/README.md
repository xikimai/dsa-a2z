# Shortest Paths — Finding the Best Route

{% hint style="info" %}
**This chapter unlocks one of the most powerful graph algorithms in all of computer science.** Dijkstra's algorithm powers Google Maps, internet routing, and game AI pathfinding. Bellman-Ford handles tricky negative weights. Floyd-Warshall solves all-pairs shortest paths in a clean triple loop. And 0-1 BFS gives you blazing speed when weights are binary. Master these four algorithms and you will be ready for every shortest path problem USACO Gold can throw at you.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand why shortest path problems appear everywhere: GPS navigation, network routing, game AI, robotics
- Implement Dijkstra's algorithm using a min-heap (priority queue) from Ch 17
- Prove why Dijkstra's greedy strategy is correct (and why it fails on negative weights)
- Implement Bellman-Ford to handle graphs with negative edge weights
- Detect negative cycles using Bellman-Ford's (V-1)+1 relaxation trick
- Implement Floyd-Warshall for all-pairs shortest paths in O(V^3) time
- Use 0-1 BFS with a deque for graphs where edge weights are only 0 or 1
- Solve shortest path problems on grids using BFS (unweighted) and Dijkstra (weighted)
- Choose the right algorithm based on the problem constraints (comparison table)
- Reconstruct the actual shortest path, not just the distance
- Apply shortest path algorithms to at least 13 problems across three difficulty tiers
- Recognize shortest path variants disguised as other problem types

---

## The Story: "The GPS Navigator"

Aiden had always been fascinated by maps. When he was little, he would trace routes with his finger on his family's road atlas. Now, at fourteen, he was building something bigger: his own navigation app.

"How hard can it be?" he thought. "I just need to find the shortest route between two points."

He started with a simple approach: try ALL possible paths from start to destination, measure each one, and pick the shortest. For a tiny map with five intersections, this worked fine. But when he loaded the map of his city — 10,000 intersections and 25,000 roads — his program ground to a halt.

"There are too many paths," Aiden muttered. "The number grows exponentially."

His computer science teacher, Ms. Rivera, smiled when he told her the problem. "You have just discovered one of the most important problems in computer science. In 1956, a Dutch computer scientist named Edsger Dijkstra was sitting in a cafe in Amsterdam, thinking about a similar problem. In about twenty minutes, he invented an algorithm that changed the world."

"Twenty minutes?" Aiden was skeptical.

"Twenty minutes. And that algorithm now powers every GPS device, every internet router, and every game character that finds its way through a maze. It is called Dijkstra's algorithm, and today, you are going to learn it."

Aiden leaned forward. "Let's go."

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "The Road Map"

You are building a GPS app. Here is a small road network with distances (in minutes):

```
    A --4-- B
    |       |
    1       5
    |       |
    C --2-- B  (via C→B shortcut)
    |       |
    8       1
    |       |
    D ------E
```

More precisely:
- A→B: 4 minutes, A→C: 1 minute
- C→B: 2 minutes, C→D: 8 minutes
- B→E: 5 minutes, B→D (via shortcut): not available
- D→E: 1 minute

What is the shortest route from A to E? Did you find a route through C that is shorter than going directly A→B→E?

{% hint style="info" %}
A→B→E = 4+5 = 9 minutes. But A→C→B→E = 1+2+5 = 8 minutes! And A→C→D→E = 1+8+1 = 10 minutes. The shortest is A→C→B→E at 8 minutes. Notice: the shortest path does NOT always use the shortest individual edges.
{% endhint %}

### Puzzle 2: "The Negative Shortcut"

Now imagine some roads give you a TIME BONUS (negative weight). Edge A→B costs 4, B→C costs -2 (you gain 2 minutes!), A→C costs 3. What is the cheapest path from A to C?

- Direct: A→C = 3
- Via B: A→B→C = 4 + (-2) = 2

{% hint style="warning" %}
The path through B is cheaper because of the negative edge! Dijkstra's algorithm would NOT find this — it would greedily pick A→C = 3 and stop. This is why we need Bellman-Ford for negative weights.
{% endhint %}

### Puzzle 3: "All Pairs"

Given 4 cities with these direct flights (costs in dollars):
- 0→1: $3, 0→3: $7
- 1→0: $8, 1→2: $2
- 2→0: $5, 2→3: $1
- 3→0: $2

Fill in the cheapest cost to fly between EVERY pair of cities. Some pairs might be cheaper via a stopover.

{% hint style="info" %}
This is the all-pairs shortest path problem. For example, 1→3 is not a direct flight, but 1→2→3 costs 2+1 = $3. Floyd-Warshall solves this elegantly.
{% endhint %}

---

## 27.1 Why Shortest Paths Matter

Shortest path algorithms are everywhere:

| Application | Graph | Nodes | Edges | Weight |
|-------------|-------|-------|-------|--------|
| GPS navigation | Road network | Intersections | Roads | Distance/Time |
| Internet routing | Network | Routers | Links | Latency |
| Game AI pathfinding | Grid/Map | Tiles | Adjacent tiles | Movement cost |
| Social networks | Friendship graph | People | Relationships | Degrees of separation |
| Airline routing | Flight network | Airports | Flights | Cost/Time |
| Robot motion planning | Configuration space | States | Transitions | Energy cost |

There are two main flavors:

1. **Single-Source Shortest Path (SSSP)**: Find the shortest path from ONE source to ALL other nodes.
   - Dijkstra (non-negative weights): O((V + E) log V) with a min-heap
   - Bellman-Ford (any weights): O(V * E)
   - BFS (unweighted): O(V + E)

2. **All-Pairs Shortest Path (APSP)**: Find the shortest path between EVERY pair of nodes.
   - Floyd-Warshall: O(V^3)
   - Run Dijkstra from each node: O(V * (V + E) log V)

---

## 27.2 Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a graph with **non-negative** edge weights. It is a **greedy** algorithm that always processes the closest unvisited node next.

### The Idea

1. Set `dist[src] = 0` and `dist[v] = infinity` for all other nodes
2. Use a min-heap (priority queue). Push `(0, src)`
3. Pop the node with the smallest distance. If already finalized, skip it
4. For each neighbor, try to **relax**: if `dist[u] + weight(u,v) < dist[v]`, update and push
5. Repeat until the heap is empty

### Why It Works (Proof Sketch)

**Claim**: When Dijkstra pops a node `u` from the heap, `dist[u]` is the true shortest distance.

**Proof by contradiction**: Suppose node `u` is popped but `dist[u]` is NOT optimal. Then there exists a shorter path P from src to u. This path must pass through some node `x` that has not been popped yet. But since all edge weights are non-negative, `dist[x] >= dist[u]` (otherwise `x` would have been popped before `u`). So the path through `x` cannot be shorter — contradiction!

{% hint style="danger" %}
**Dijkstra fails on negative weights!** If an edge has negative weight, a node that looks "close" might actually have a shorter path through a distant node with a negative edge. The greedy assumption breaks.
{% endhint %}

### Implementation

{% tabs %}
{% tab title="Python" %}
```python
import heapq

def dijkstra(n, edges, src):
    """Dijkstra's SSSP. edges = [[u, v, w], ...] (directed)."""
    INF = 10**9
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]  # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale entry
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

int[] dijkstra(int n, int[][] edges, int src) {
    int INF = (int) 1e9;
    List<int[]>[] adj = new ArrayList[n];
    for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
    for (int[] e : edges) adj[e[0]].add(new int[]{e[1], e[2]});

    int[] dist = new int[n];
    Arrays.fill(dist, INF);
    dist[src] = 0;
    // min-heap: {distance, node}
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, src});

    while (!pq.isEmpty()) {
        int[] top = pq.poll();
        int d = top[0], u = top[1];
        if (d > dist[u]) continue;
        for (int[] edge : adj[u]) {
            int v = edge[0], w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.offer(new int[]{dist[v], v});
            }
        }
    }
    return dist;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <queue>
#include <climits>
using namespace std;

vector<int> dijkstra(int n, vector<vector<int>>& edges, int src) {
    const int INF = 1e9;
    vector<vector<pair<int,int>>> adj(n);
    for (auto& e : edges)
        adj[e[0]].push_back({e[1], e[2]});

    vector<int> dist(n, INF);
    dist[src] = 0;
    // min-heap: {distance, node}
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}
```
{% endtab %}
{% endtabs %}

**Language Spotlight: Priority Queue Syntax**

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Min-heap | `heapq` (default min) | `PriorityQueue<>` (default min) | `priority_queue<..., greater<>>` |
| Push | `heapq.heappush(h, (d,v))` | `pq.offer(new int[]{d,v})` | `pq.push({d,v})` |
| Pop | `heapq.heappop(h)` | `pq.poll()` | `pq.top(); pq.pop();` |
| Stale check | `if d > dist[u]: continue` | Same pattern | Same pattern |

**Time Complexity**: O((V + E) log V) with a binary heap.

---

## 27.3 Bellman-Ford Algorithm

When edges can have **negative weights**, Dijkstra's greedy approach fails. Bellman-Ford handles this by relaxing ALL edges V-1 times.

### The Idea

1. Set `dist[src] = 0` and `dist[v] = infinity` for all other nodes
2. Repeat V-1 times: for every edge (u, v, w), try to relax `dist[v] = min(dist[v], dist[u] + w)`
3. After V-1 rounds, all shortest paths are found (a shortest path has at most V-1 edges)
4. **Negative cycle detection**: Do one more round. If any distance improves, there is a negative cycle!

### Why V-1 Rounds?

A shortest path in a graph with V nodes can have at most V-1 edges (if it visits every node once). After round k, we have the correct shortest distances for all paths using at most k edges. So after V-1 rounds, we have ALL shortest distances.

{% tabs %}
{% tab title="Python" %}
```python
def bellman_ford(n, edges, src):
    """Bellman-Ford SSSP. Returns dist list. Handles negative weights."""
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative cycle detection (optional)
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return None  # negative cycle exists

    return dist
```
{% endtab %}
{% tab title="Java" %}
```java
int[] bellmanFord(int n, int[][] edges, int src) {
    int INF = (int) 1e9;
    int[] dist = new int[n];
    Arrays.fill(dist, INF);
    dist[src] = 0;

    for (int i = 0; i < n - 1; i++)
        for (int[] e : edges)
            if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
                dist[e[1]] = dist[e[0]] + e[2];

    // Negative cycle detection
    for (int[] e : edges)
        if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
            return null;

    return dist;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> bellmanFord(int n, vector<vector<int>>& edges, int src) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;

    for (int i = 0; i < n - 1; i++)
        for (auto& e : edges)
            if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
                dist[e[1]] = dist[e[0]] + e[2];

    // Negative cycle detection
    for (auto& e : edges)
        if (dist[e[0]] != INF && dist[e[0]] + e[2] < dist[e[1]])
            return {};  // negative cycle

    return dist;
}
```
{% endtab %}
{% endtabs %}

**Time Complexity**: O(V * E). Slower than Dijkstra but handles negative weights.

---

## 27.4 Floyd-Warshall (All-Pairs Shortest Paths)

What if you need the shortest path between EVERY pair of nodes? Floyd-Warshall does this in a clean triple loop.

### The Idea

`dist[i][j]` = shortest distance from i to j. For each intermediate node k (from 0 to V-1):
- `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

The key insight: after processing intermediate node k, `dist[i][j]` holds the shortest path from i to j using only nodes 0, 1, ..., k as intermediates.

{% tabs %}
{% tab title="Python" %}
```python
def floyd_warshall(n, edges):
    """All-pairs shortest paths. edges = [u, v, w] (directed)."""
    INF = 10**9
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # handle parallel edges

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```
{% endtab %}
{% tab title="Java" %}
```java
int[][] floydWarshall(int n, int[][] edges) {
    int INF = (int) 1e9;
    int[][] dist = new int[n][n];
    for (int[] row : dist) Arrays.fill(row, INF);
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    for (int[] e : edges) dist[e[0]][e[1]] = Math.min(dist[e[0]][e[1]], e[2]);

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    return dist;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<vector<int>> floydWarshall(int n, vector<vector<int>>& edges) {
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) dist[i][i] = 0;
    for (auto& e : edges) dist[e[0]][e[1]] = min(dist[e[0]][e[1]], e[2]);

    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];

    return dist;
}
```
{% endtab %}
{% endtabs %}

**Time Complexity**: O(V^3). Best when V is small (V <= 400 or so).

---

## 27.5 0-1 BFS

When all edge weights are either **0 or 1**, you can use a deque instead of a priority queue. Push weight-0 edges to the **front** and weight-1 edges to the **back**. This gives O(V + E) time — as fast as regular BFS!

### Why It Works

The deque maintains a sorted order: nodes at the front have smaller distances. Adding a 0-weight edge keeps the same distance (push front), while a 1-weight edge increases distance by 1 (push back). This mimics a priority queue without the O(log V) overhead.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque

def bfs_01(n, adj, src):
    """0-1 BFS. adj[u] = [(v, w)] where w is 0 or 1."""
    INF = 10**9
    dist = [INF] * n
    dist[src] = 0
    dq = deque([src])

    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)  # front
                else:
                    dq.append(v)      # back

    return dist
```
{% endtab %}
{% tab title="Java" %}
```java
int[] bfs01(int n, List<int[]>[] adj, int src) {
    int INF = (int) 1e9;
    int[] dist = new int[n];
    Arrays.fill(dist, INF);
    dist[src] = 0;
    Deque<Integer> dq = new ArrayDeque<>();
    dq.addFirst(src);

    while (!dq.isEmpty()) {
        int u = dq.pollFirst();
        for (int[] edge : adj[u]) {
            int v = edge[0], w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) dq.addFirst(v);
                else dq.addLast(v);
            }
        }
    }
    return dist;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> bfs01(int n, vector<vector<pair<int,int>>>& adj, int src) {
    const int INF = 1e9;
    vector<int> dist(n, INF);
    dist[src] = 0;
    deque<int> dq;
    dq.push_front(src);

    while (!dq.empty()) {
        int u = dq.front(); dq.pop_front();
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }
    return dist;
}
```
{% endtab %}
{% endtabs %}

**Time Complexity**: O(V + E) — same as BFS!

---

## 27.6 Shortest Paths on Grids

Many shortest path problems use a 2D grid instead of an explicit graph. Each cell is a node, and edges connect adjacent cells.

- **Unweighted grid** (all moves cost 1): Use BFS
- **Weighted grid** (different costs per cell): Use Dijkstra
- **Binary weights** (0 or 1 per cell): Use 0-1 BFS

### Grid Dijkstra Pattern

{% tabs %}
{% tab title="Python" %}
```python
import heapq

def grid_dijkstra(grid):
    """Shortest path from (0,0) to (m-1,n-1) on weighted grid."""
    m, n = len(grid), len(grid[0])
    INF = 10**9
    dist = [[INF] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    heap = [(grid[0][0], 0, 0)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    while heap:
        d, r, c = heapq.heappop(heap)
        if d > dist[r][c]:
            continue
        if r == m-1 and c == n-1:
            return d
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n:
                nd = d + grid[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(heap, (nd, nr, nc))

    return dist[m-1][n-1]
```
{% endtab %}
{% tab title="Java" %}
```java
int gridDijkstra(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    int INF = (int) 1e9;
    int[][] dist = new int[m][n];
    for (int[] row : dist) Arrays.fill(row, INF);
    dist[0][0] = grid[0][0];
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{grid[0][0], 0, 0});
    int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

    while (!pq.isEmpty()) {
        int[] top = pq.poll();
        int d = top[0], r = top[1], c = top[2];
        if (d > dist[r][c]) continue;
        if (r == m-1 && c == n-1) return d;
        for (int[] dir : dirs) {
            int nr = r+dir[0], nc = c+dir[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int nd = d + grid[nr][nc];
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    pq.offer(new int[]{nd, nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int gridDijkstra(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    const int INF = 1e9;
    vector<vector<int>> dist(m, vector<int>(n, INF));
    dist[0][0] = grid[0][0];
    priority_queue<tuple<int,int,int>,
                   vector<tuple<int,int,int>>,
                   greater<>> pq;
    pq.push({grid[0][0], 0, 0});
    int dirs[][2] = {{0,1},{0,-1},{1,0},{-1,0}};

    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d > dist[r][c]) continue;
        if (r == m-1 && c == n-1) return d;
        for (auto& dir : dirs) {
            int nr = r+dir[0], nc = c+dir[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                int nd = d + grid[nr][nc];
                if (nd < dist[nr][nc]) {
                    dist[nr][nc] = nd;
                    pq.push({nd, nr, nc});
                }
            }
        }
    }
    return dist[m-1][n-1];
}
```
{% endtab %}
{% endtabs %}

---

## 27.7 Comparison Table: When to Use Which Algorithm

| Algorithm | Weights | Scope | Time | Space | Use When... |
|-----------|---------|-------|------|-------|-------------|
| **BFS** | Unweighted (all 1) | SSSP | O(V+E) | O(V) | All edges have equal cost |
| **0-1 BFS** | 0 or 1 only | SSSP | O(V+E) | O(V) | Binary edge weights |
| **Dijkstra** | Non-negative | SSSP | O((V+E) log V) | O(V) | Most common — GPS, grids |
| **Bellman-Ford** | Any (incl. negative) | SSSP | O(V*E) | O(V) | Negative weights, negative cycle detection |
| **Floyd-Warshall** | Any | All-pairs | O(V^3) | O(V^2) | Small graph, need all-pairs distances |

{% hint style="warning" %}
**Decision flowchart**: Unweighted? → BFS. Weights are 0/1? → 0-1 BFS. Non-negative weights? → Dijkstra. Negative weights? → Bellman-Ford. Need all-pairs? → Floyd-Warshall.
{% endhint %}

---

## Five-Lens Framework: Dijkstra's Algorithm

Let us apply the Five-Lens Framework (from Ch 6) to Dijkstra's Single-Source Shortest Path.

### Lens 1: Constraints
- V, E up to 10^5 typically. O(V^2) algorithms are too slow for large graphs.
- Edge weights are **non-negative** (Dijkstra requirement).
- With a min-heap, O((V+E) log V) fits within time limits.

### Lens 2: Brute Force
- Try all possible paths from source to every node — exponential in the worst case.
- Even with BFS-like exploration, without a priority queue you might process nodes in the wrong order.

### Lens 3: Pattern
- **Greedy**: Always process the node with the smallest known distance.
- **Relaxation**: If going through u to v is shorter, update v's distance.
- This is the same "relax and improve" pattern used in Bellman-Ford, but Dijkstra does it efficiently using a heap.

### Lens 4: Optimization
- Binary heap gives O(log V) per operation → O((V+E) log V) total.
- Fibonacci heap gives O(V log V + E) — theoretically better but rarely used in practice.
- For dense graphs, an O(V^2) version without a heap can be faster.

### Lens 5: Proof
- **Exchange argument**: If Dijkstra's answer for node u is wrong, there must be a shorter path. But that path goes through some unprocessed node x, and since weights are non-negative, dist[x] >= dist[u]. Contradiction.

---

## Think Like a Pro

{% hint style="info" %}
**How tourist approaches shortest path problems:**

"When I see a shortest path problem, the FIRST thing I check is: are edge weights non-negative? If yes, Dijkstra is almost always the answer. If there are negative weights, I check if I need negative cycle detection — if yes, Bellman-Ford. If the problem asks for all-pairs, and V is small (<= 400), Floyd-Warshall. For grid problems with binary weights (free/blocked cells), 0-1 BFS is perfect."

"The trickiest part is recognizing DISGUISED shortest path problems. 'Minimum effort path' is Dijkstra where edge weight = abs difference. 'Swim in rising water' is Dijkstra where edge weight = max elevation. 'Minimum obstacle removal' is 0-1 BFS. Train yourself to see the graph underneath the problem."
{% endhint %}

---

## AOPS Showcase: Network Delay Time

**Problem**: Given a network of `n` nodes and weighted directed edges `times = [[u, v, w], ...]`, find the minimum time for a signal sent from node `k` to reach ALL nodes. Return -1 if not all nodes are reachable.

### Approach 1: BFS (Fails on Weighted Graphs!)

If we ignore weights and do plain BFS, we find the path with the fewest EDGES, not the shortest DISTANCE. This is WRONG for weighted graphs.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque

def network_delay_bfs(times, n, k):
    """WRONG for weighted graphs! BFS ignores edge weights."""
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append(v)  # ignoring weight!
    visited = [False] * (n + 1)
    visited[k] = True
    q = deque([k])
    hops = 0
    reached = 1
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    reached += 1
                    q.append(v)
        hops += 1
    # This counts HOPS, not actual delay time!
    return hops if reached == n else -1
```
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
BFS finds the path with fewest edges, NOT shortest total weight. For the input `times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2`, BFS says 2 hops. But the actual delay is 2 time units (2→3→4). Here it happens to match, but for other inputs it will not!
{% endhint %}

### Approach 2: Dijkstra (Correct!)

Since all weights are non-negative, Dijkstra finds the true shortest distance from k to every node.

{% tabs %}
{% tab title="Python" %}
```python
import heapq

def network_delay_dijkstra(times, n, k):
    """Correct! Dijkstra handles weighted edges."""
    INF = 10**9
    adj = [[] for _ in range(n + 1)]
    for u, v, w in times:
        adj[u].append((v, w))
    dist = [INF] * (n + 1)
    dist[k] = 0
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    ans = max(dist[1:])  # nodes 1..n
    return ans if ans < INF else -1
```
{% endtab %}
{% tab title="Java" %}
```java
int networkDelayDijkstra(int[][] times, int n, int k) {
    int INF = (int) 1e9;
    List<int[]>[] adj = new ArrayList[n + 1];
    for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();
    for (int[] t : times) adj[t[0]].add(new int[]{t[1], t[2]});

    int[] dist = new int[n + 1];
    Arrays.fill(dist, INF);
    dist[k] = 0;
    PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
    pq.offer(new int[]{0, k});

    while (!pq.isEmpty()) {
        int[] top = pq.poll();
        int d = top[0], u = top[1];
        if (d > dist[u]) continue;
        for (int[] edge : adj[u]) {
            int v = edge[0], w = edge[1];
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.offer(new int[]{dist[v], v});
            }
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
    return ans >= INF ? -1 : ans;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int networkDelayDijkstra(vector<vector<int>>& times, int n, int k) {
    const int INF = 1e9;
    vector<vector<pair<int,int>>> adj(n + 1);
    for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});

    vector<int> dist(n + 1, INF);
    dist[k] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, k});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    int ans = *max_element(dist.begin() + 1, dist.end());
    return ans >= INF ? -1 : ans;
}
```
{% endtab %}
{% endtabs %}

### Approach 3: Bellman-Ford (Also Correct, Handles Negative Weights Too)

Bellman-Ford relaxes all edges V-1 times. Slower but works even with negative weights.

{% tabs %}
{% tab title="Python" %}
```python
def network_delay_bellman(times, n, k):
    """Bellman-Ford — slower but handles negative weights."""
    INF = 10**9
    dist = [INF] * (n + 1)
    dist[k] = 0
    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    ans = max(dist[1:])
    return ans if ans < INF else -1
```
{% endtab %}
{% endtabs %}

**Comparison for this problem**:
- BFS: O(V+E) but WRONG (ignores weights)
- Dijkstra: O((V+E) log V) — correct and fast
- Bellman-Ford: O(V*E) — correct but slower

---

## Legend's Corner

{% hint style="info" %}
**Edsger Dijkstra** invented his famous algorithm in 1956 while sitting at a cafe in Amsterdam with his fiancee. He was thinking about how to demonstrate the power of a new computer called ARMAC, and decided to find the shortest route between two cities in the Netherlands. He designed the algorithm in about 20 minutes — without a computer, just pen and paper on a cafe napkin. He did not publish it until 1959 because he thought it was "too simple" to be worth writing up. The algorithm now runs on billions of devices worldwide, powering every GPS navigation system. Dijkstra later reflected: "The question of how to write good algorithms became one of the driving forces in my life."

For you: When a problem feels "too hard," remember that one of the greatest algorithms in history was designed in 20 minutes by someone who was just trying to impress his fiancee.
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
1. **Dijkstra with negative weights**: Dijkstra assumes once a node is popped, its distance is final. Negative edges can violate this. ALWAYS check if weights can be negative — if yes, use Bellman-Ford.

2. **Stale priority queue entries**: When you relax a node, you push a NEW entry but the OLD one remains in the heap. Always check `if d > dist[u]: continue` when popping. Without this, your algorithm may be O(V * E log V) instead of O((V+E) log V).

3. **Forgetting INF initialization**: If you initialize distances to 0 instead of infinity, every node looks reachable with distance 0. Always use a large sentinel (10^9 works; avoid INT_MAX since adding to it causes overflow).

4. **Integer overflow with INF**: If INF = INT_MAX and you compute INF + weight, you get integer overflow (negative number in C++, undefined behavior). Use `INF = 10^9` instead, which is large enough but safe to add to.

5. **0-indexed vs 1-indexed nodes**: Some problems use 1-indexed nodes (like Network Delay Time). Make sure your arrays are sized n+1 and you skip index 0. Mixing this up causes array-out-of-bounds or wrong answers.

6. **Bidirectional vs directed edges**: Read the problem carefully! "roads" are usually bidirectional (add both u→v and v→u). "flights" are usually directed. Adding edges in the wrong direction gives wrong answers.

7. **Negative cycle infinite loop**: In Bellman-Ford, if you do not limit to V-1 iterations, a negative cycle will cause distances to decrease forever. Always stop after exactly V-1 rounds for shortest paths.

8. **Floyd-Warshall loop order**: The intermediate node `k` MUST be the outermost loop. If you put `i` or `j` as the outer loop, the algorithm is WRONG. This is the single most common Floyd-Warshall bug.
{% endhint %}

---

## Practice Problems

| # | Problem | Difficulty | Algorithm | Key Insight |
|---|---------|------------|-----------|-------------|
| W1 | Dijkstra SSSP | Warmup | Dijkstra | Standard shortest path from source |
| W2 | Network Delay Time | Warmup | Dijkstra | Max of all shortest distances (1-indexed) |
| W3 | Bellman-Ford SSSP | Warmup | Bellman-Ford | Handles negative edge weights |
| W4 | Shortest Path in Binary Matrix | Warmup | BFS | 8-directional grid traversal |
| P1 | Cheapest Flights Within K Stops | Practice | Modified Bellman-Ford | Limit relaxation rounds to k+1 |
| P2 | Path with Minimum Effort | Practice | Dijkstra on grid | Edge weight = max abs diff on path |
| P3 | Find City with Smallest Neighbors | Practice | Floyd-Warshall | All-pairs + counting |
| P4 | Number of Ways to Arrive at Destination | Practice | Dijkstra + counting | Count shortest paths (mod 10^9+7) |
| P5 | Swim in Rising Water | Practice | Dijkstra / Binary Search+BFS | Minimize max elevation on path |
| C1 | Minimum Obstacle Removal | Challenge | 0-1 BFS | Obstacle = weight 1, empty = weight 0 |
| C2 | Shortest Path with Alternating Colors | Challenge | BFS with state | State = (node, last_color) |
| C3 | Minimum Cost for Valid Path | Challenge | 0-1 BFS | Follow arrow = 0, change = 1 |
| C4 | Path with Maximum Minimum Value | Challenge | Dijkstra (max-min) | Maximize the minimum value on path |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
# ── Min-heap with heapq ──
import heapq
heap = []
heapq.heappush(heap, (dist, node))
d, u = heapq.heappop(heap)

# ── Deque for 0-1 BFS ──
from collections import deque
dq = deque([src])
dq.appendleft(v)  # push front (weight 0)
dq.append(v)      # push back (weight 1)
u = dq.popleft()

# ── INF sentinel ──
INF = 10**9  # safe to add without overflow

# ── Build adjacency list from edge list ──
adj = [[] for _ in range(n)]
for u, v, w in edges:
    adj[u].append((v, w))
```
{% endtab %}
{% tab title="Java" %}
```java
// ── Min-heap ──
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
pq.offer(new int[]{dist, node});
int[] top = pq.poll();

// ── Deque for 0-1 BFS ──
Deque<Integer> dq = new ArrayDeque<>();
dq.addFirst(v);  // push front
dq.addLast(v);   // push back
int u = dq.pollFirst();

// ── INF sentinel ──
int INF = (int) 1e9;

// ── Build adjacency list ──
List<int[]>[] adj = new ArrayList[n];
for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
for (int[] e : edges) adj[e[0]].add(new int[]{e[1], e[2]});
```
{% endtab %}
{% tab title="C++" %}
```cpp
// ── Min-heap (NOTE: greater<> for min!) ──
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
pq.push({dist, node});
auto [d, u] = pq.top(); pq.pop();

// ── Deque for 0-1 BFS ──
deque<int> dq;
dq.push_front(v);  // weight 0
dq.push_back(v);   // weight 1
int u = dq.front(); dq.pop_front();

// ── INF sentinel (avoid INT_MAX overflow!) ──
const int INF = 1e9;

// ── Build adjacency list ──
vector<vector<pair<int,int>>> adj(n);
for (auto& e : edges) adj[e[0]].push_back({e[1], e[2]});
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 17** (Heaps & Priority Queues) gave you the min-heap — the engine that makes Dijkstra fast
- **Ch 19** (Graphs I) introduced adjacency lists and BFS — the foundation for all graph traversals
- **Ch 20** (Graphs II) covered BFS on grids — we extend this with weighted grids using Dijkstra
- **Ch 18** (Greedy Algorithms) taught you the greedy paradigm — Dijkstra is a greedy algorithm!

### Looking Forward
- **Ch 28** (Topological Sort) will show you how to find shortest paths on DAGs in O(V+E) — even faster than Dijkstra, because you process nodes in topological order
- **Ch 29** (Union-Find & MST) will use similar edge-based thinking — Kruskal's MST is like finding the "cheapest network" instead of the "shortest path"

### Cross-Chapter Threads
- **"Trade space for time"**: Dijkstra uses O(V) space for the distance array to avoid exponential brute-force path enumeration. Floyd-Warshall trades O(V^2) space for O(V^3) time to solve all-pairs.
- **"Reduce to known"**: Many grid problems REDUCE to shortest path problems. "Minimum effort" reduces to Dijkstra. "Obstacle removal" reduces to 0-1 BFS. Recognizing the reduction is the hard part.
- **"Brute force is a strategy"**: The brute-force approach (try all paths) is exponential. Dijkstra eliminates redundant work through the greedy property. But writing the brute force first helps you understand what "shortest path" means in each problem.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"Can we find shortest paths faster than Dijkstra? What about A*?"** A* uses a heuristic function h(v) that estimates the distance from v to the destination. It explores nodes in order of `dist[v] + h(v)` instead of just `dist[v]`. With a good heuristic, A* can be much faster in practice — it is what video games use for pathfinding. But it requires a problem-specific heuristic.

2. **"What if edge weights change dynamically?"** In real GPS systems, traffic changes constantly. Rerunning Dijkstra from scratch is expensive. There are "dynamic shortest path" algorithms that update distances incrementally when edges change. This is an active area of research!

3. **"Is there a shortest path algorithm that works in parallel?"** Delta-stepping is a parallelizable variant of Dijkstra's algorithm. It groups nodes into "buckets" by distance and processes each bucket in parallel. This is important for computing shortest paths on massive graphs like social networks or the entire internet.

---

## What's Next

You have now mastered the four major shortest path algorithms: Dijkstra for non-negative weights, Bellman-Ford for negative weights, Floyd-Warshall for all-pairs, and 0-1 BFS for binary weights. These algorithms appear constantly in USACO Gold and coding interviews.

But what about graphs with no cycles? If your graph is a DAG (Directed Acyclic Graph), you can find shortest paths even FASTER than Dijkstra — in O(V+E) time — by processing nodes in topological order.

In **Ch 28 (Topological Sort — Ordering Dependencies)**, you will learn how to find a valid ordering of nodes in a DAG, detect cycles, and solve problems like course scheduling, build systems, and shortest paths on DAGs. It is a natural extension of the graph algorithms you learned here.

The journey continues!
