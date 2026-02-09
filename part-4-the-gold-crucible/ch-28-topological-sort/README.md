# Topological Sort — Ordering Dependencies

{% hint style="info" %}
**This chapter unlocks the power of ordering.** Every build system, every course planner, every dependency resolver uses topological sort. If you can model a problem as a Directed Acyclic Graph (DAG), topological sort probably gives you the answer. Kahn's algorithm (BFS) and DFS-based topological sort are two sides of the same coin — learn both, and you will see dependencies everywhere.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand what a topological ordering is and why it only works on DAGs
- Implement Kahn's Algorithm (BFS-based topological sort) using in-degree tracking and a queue
- Implement DFS-based topological sort using post-order reversal
- Detect cycles in directed graphs using three-color DFS (white/gray/black)
- Understand the connection between topological sort and cycle detection
- Solve Course Schedule I (can you finish all courses?) and Course Schedule II (in what order?)
- Handle the prerequisite direction convention: `[a, b]` means "to take a, you need b first"
- Apply topological sort to real-world problems: build systems, task scheduling, alien dictionaries
- Compute the longest path in a DAG using topological sort + relaxation
- Find Minimum Height Trees using iterative leaf removal (Kahn's-like)
- Identify eventual safe states in a directed graph using reverse topological thinking
- Recognize that multiple valid topological orderings can exist for the same DAG

---

## The Story: "The Course Planner"

Zara stared at her high school course catalog, overwhelmed. She wanted to take Artificial Intelligence, but the catalog said: "Prerequisites: Data Structures and Algorithms." And Data Structures required "Introduction to Programming." And Algorithms required both "Discrete Math" and "Intro to Programming."

She drew a diagram on her whiteboard, with arrows from each prerequisite to the course it unlocked:

```
Intro to Programming --> Data Structures --> AI
Intro to Programming --> Algorithms ------> AI
Discrete Math --------> Algorithms
```

"I need to find an ORDER to take these courses," she thought. "I can only take a course after finishing ALL its prerequisites."

She started with courses that had NO prerequisites: Intro to Programming and Discrete Math. Then she could take Data Structures (Intro done) and Algorithms (both Intro and Discrete done). Finally, AI.

One valid order: `Intro, Discrete, Data Structures, Algorithms, AI`
Another valid order: `Discrete, Intro, Algorithms, Data Structures, AI`

Both work! But then her friend showed her a different catalog where Course A required Course B, and Course B required Course A. "That is impossible," Zara realized. "There is a circular dependency — you cannot take either course first!"

Zara had just discovered topological sorting — and the critical role of cycle detection.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the algorithms, try these puzzles by hand.

### Puzzle 1: "Task Dependencies"

You have 6 tasks (numbered 0-5) with these dependencies (arrows mean "must come before"):

```
5 --> 2 --> 3 --> 1
5 --> 0
4 --> 0
4 --> 1
```

Find a valid order to complete ALL tasks. Is there more than one valid order?

{% hint style="info" %}
One valid order: `[4, 5, 0, 2, 3, 1]`. Another: `[5, 4, 2, 0, 3, 1]`. Tasks with no dependencies (4 and 5) can go first in any order. Task 1 must come after both 3 and 4. Try to find all constraints and verify your ordering satisfies each one.
{% endhint %}

### Puzzle 2: "Circular Deadlock"

Three friends make a rule:
- Alice will not start her homework until Bob finishes his.
- Bob will not start until Carol finishes hers.
- Carol will not start until Alice finishes hers.

Can they ever start? What mathematical structure does this create?

{% hint style="info" %}
No! This is a **cycle**: Alice --> Bob --> Carol --> Alice. In graph terms, there is no topological ordering of a graph with a cycle. The graph must be a **DAG** (Directed Acyclic Graph) for topological sort to work.
{% endhint %}

### Puzzle 3: "Alien Language"

An alien civilization uses the letters `{w, e, r, t, f}`. You find a sorted alien dictionary:

```
wrt
wrf
er
ett
rftt
```

What is the order of letters in their alphabet?

{% hint style="info" %}
Compare consecutive words: `wrt` vs `wrf` tells you `t < f`. `wrf` vs `er` tells you `w < e`. `er` vs `ett` tells you `r < t`. `ett` vs `rftt` tells you `e < r`. So the order is `w < e < r < t < f`, or `"wertf"`. This is topological sort on character precedence!
{% endhint %}

---

## 28.1 What Is Topological Ordering?

A **topological ordering** (or topological sort) of a directed graph is a linear ordering of its vertices such that for every directed edge `u --> v`, vertex `u` comes before vertex `v` in the ordering.

Key facts:
- A topological ordering **only exists** for **DAGs** (Directed Acyclic Graphs) — graphs with no cycles.
- A DAG can have **multiple** valid topological orderings.
- If a graph has a cycle, NO topological ordering exists.
- A topological sort converts a **partial order** (some pairs are comparable) into a **total order** (all pairs are ordered).

Think of it this way: if edges represent "must come before" relationships, a topological ordering is any valid sequence where every "must come before" constraint is satisfied.

### When Do You Need Topological Sort?

- **Course scheduling**: Take prerequisites before advanced courses
- **Build systems**: Compile dependencies before the main project (like `make`)
- **Task scheduling**: Complete prerequisite tasks before dependent ones
- **Package managers**: Install dependency packages before the packages that need them
- **Spreadsheet evaluation**: Compute cells in dependency order

---

## 28.2 Kahn's Algorithm (BFS-Based)

Kahn's algorithm is elegant: repeatedly remove nodes with no incoming edges (in-degree 0).

### The Algorithm

1. Compute the **in-degree** of every node (count of incoming edges).
2. Add all nodes with in-degree 0 to a **queue**.
3. While the queue is not empty:
   - Dequeue a node `u`, add it to the result.
   - For each neighbor `v` of `u`, decrement `v`'s in-degree by 1.
   - If `v`'s in-degree becomes 0, enqueue `v`.
4. If the result contains ALL nodes, return it. Otherwise, there is a **cycle**.

### Why It Works

Nodes with in-degree 0 have no unsatisfied dependencies — they are safe to process. Removing them may create new zero-indegree nodes (their dependents, once all prerequisites are done). If we cannot process all nodes, some nodes are trapped in a cycle.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque, defaultdict

def kahns_topo_sort(n, edges):
    """Kahn's Algorithm: BFS-based topological sort.

    Args:
        n: number of nodes (0 to n-1)
        edges: list of [u, v] meaning u must come before v

    Returns:
        list of nodes in topological order, or [] if cycle exists
    """
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result if len(result) == n else []
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

public List<Integer> kahnsTopoSort(int n, int[][] edges) {
    List<List<Integer>> adj = new ArrayList<>();
    int[] inDegree = new int[n];
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    for (int[] e : edges) {
        adj.get(e[0]).add(e[1]);
        inDegree[e[1]]++;
    }

    Queue<Integer> queue = new ArrayDeque<>();
    for (int i = 0; i < n; i++)
        if (inDegree[i] == 0) queue.add(i);

    List<Integer> result = new ArrayList<>();
    while (!queue.isEmpty()) {
        int u = queue.poll();
        result.add(u);
        for (int v : adj.get(u)) {
            inDegree[v]--;
            if (inDegree[v] == 0) queue.add(v);
        }
    }
    return result.size() == n ? result : new ArrayList<>();
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <queue>
using namespace std;

vector<int> kahnsTopoSort(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    vector<int> inDegree(n, 0);
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        inDegree[e[1]]++;
    }

    queue<int> q;
    for (int i = 0; i < n; i++)
        if (inDegree[i] == 0) q.push(i);

    vector<int> result;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        result.push_back(u);
        for (int v : adj[u]) {
            inDegree[v]--;
            if (inDegree[v] == 0) q.push(v);
        }
    }
    return result.size() == n ? result : vector<int>{};
}
```
{% endtab %}
{% endtabs %}

**Time Complexity**: O(V + E) — visit every vertex and edge once.
**Space Complexity**: O(V + E) — adjacency list + in-degree array + queue.

---

## 28.3 DFS-Based Topological Sort

The DFS approach uses a key insight: in a DFS of a DAG, when you finish processing a node (all its descendants are done), that node can safely go at the END of the topological order. Reversing the finish-order gives a valid topological sort.

### The Algorithm

1. Mark all nodes as **unvisited** (WHITE).
2. For each unvisited node, run DFS.
3. In DFS: mark node as **in-progress** (GRAY), recurse on neighbors, then mark as **done** (BLACK) and push to a stack.
4. If you visit a GRAY node during DFS, you found a **cycle**.
5. The stack (reversed finish order) is the topological order.

{% tabs %}
{% tab title="Python" %}
```python
def dfs_topo_sort(n, edges):
    """DFS-based topological sort with cycle detection.

    Uses three colors: 0=white (unvisited), 1=gray (in progress), 2=black (done).
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    color = [0] * n  # 0=white, 1=gray, 2=black
    stack = []
    has_cycle = False

    def dfs(u):
        nonlocal has_cycle
        if has_cycle:
            return
        color[u] = 1  # gray: in progress
        for v in adj[u]:
            if color[v] == 1:  # back edge = cycle!
                has_cycle = True
                return
            if color[v] == 0:
                dfs(v)
        color[u] = 2  # black: done
        stack.append(u)

    for i in range(n):
        if color[i] == 0:
            dfs(i)

    if has_cycle:
        return []
    return stack[::-1]  # reverse finish order
```
{% endtab %}
{% tab title="Java" %}
```java
public List<Integer> dfsTopoSort(int n, int[][] edges) {
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    for (int[] e : edges) adj.get(e[0]).add(e[1]);

    int[] color = new int[n]; // 0=white, 1=gray, 2=black
    Deque<Integer> stack = new ArrayDeque<>();
    boolean[] hasCycle = {false};

    for (int i = 0; i < n; i++)
        if (color[i] == 0) dfs(i, adj, color, stack, hasCycle);

    if (hasCycle[0]) return new ArrayList<>();
    List<Integer> result = new ArrayList<>();
    while (!stack.isEmpty()) result.add(stack.pop());
    return result;
}

private void dfs(int u, List<List<Integer>> adj, int[] color,
                 Deque<Integer> stack, boolean[] hasCycle) {
    if (hasCycle[0]) return;
    color[u] = 1;
    for (int v : adj.get(u)) {
        if (color[v] == 1) { hasCycle[0] = true; return; }
        if (color[v] == 0) dfs(v, adj, color, stack, hasCycle);
    }
    color[u] = 2;
    stack.push(u);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> dfsTopoSort(int n, vector<vector<int>>& edges) {
    vector<vector<int>> adj(n);
    for (auto& e : edges) adj[e[0]].push_back(e[1]);

    vector<int> color(n, 0); // 0=white, 1=gray, 2=black
    vector<int> stk;
    bool hasCycle = false;

    function<void(int)> dfs = [&](int u) {
        if (hasCycle) return;
        color[u] = 1;
        for (int v : adj[u]) {
            if (color[v] == 1) { hasCycle = true; return; }
            if (color[v] == 0) dfs(v);
        }
        color[u] = 2;
        stk.push_back(u);
    };

    for (int i = 0; i < n; i++)
        if (color[i] == 0) dfs(i);

    if (hasCycle) return {};
    reverse(stk.begin(), stk.end());
    return stk;
}
```
{% endtab %}
{% endtabs %}

### Language Spotlight: BFS vs. DFS Topological Sort

| Feature | Kahn's (BFS) | DFS-based |
|---------|-------------|-----------|
| Core idea | Remove zero-indegree nodes | Reverse post-order |
| Cycle detection | Count processed nodes | Gray node revisited |
| Lexicographic order | Use min-heap instead of queue | Harder to guarantee |
| Parallelism insight | Nodes in same "wave" can run in parallel | Not obvious |
| Implementation | Iterative | Recursive (or explicit stack) |

---

## 28.4 Cycle Detection in Directed Graphs

The three-color DFS is the standard technique for cycle detection in directed graphs.

### Three Colors

- **WHITE (0)**: Not yet visited.
- **GRAY (1)**: Currently being processed (on the recursion stack). If you encounter a GRAY node, you have found a **back edge** — a cycle!
- **BLACK (2)**: Fully processed (all descendants explored). Encountering a BLACK node is fine — it just means you have already finished this branch.

{% hint style="warning" %}
**Why not just use a visited boolean?** In an undirected graph, a simple visited check works for cycle detection. But in a directed graph, visiting a node that is already DONE (BLACK) is NOT a cycle. Only visiting a node that is IN PROGRESS (GRAY) indicates a cycle. The three-color scheme distinguishes these cases.
{% endhint %}

### The Critical Difference

```
A --> B --> C --> D       (no cycle: when DFS from A reaches D,
                           then backtracks to C, B, A — all turn BLACK)

A --> B --> C --> A        (cycle: when DFS reaches C and tries A,
                           A is GRAY = still in progress = CYCLE!)
```

---

## 28.5 Applications

### Course Scheduling

The classic application. Given `numCourses` and `prerequisites` where `[a, b]` means "to take course `a`, you need course `b` first":
- **Course Schedule I**: Can you finish all courses? (Is the prerequisite graph a DAG?)
- **Course Schedule II**: Return a valid order. (Topological sort of the prerequisite graph.)

{% hint style="warning" %}
**Direction trap!** The prerequisite format `[a, b]` means `b --> a` (take b before a). Many people accidentally create the edge backwards. Always draw a small example to verify.
{% endhint %}

### Build Systems

`make`, `gradle`, `npm` — all use topological sort to determine build order. If package A depends on B and C, then B and C must be built before A.

### Alien Dictionary

Given a sorted list of words in an alien language, determine the character ordering. Compare consecutive words to extract character precedence edges, then topologically sort the characters.

### Longest Path in a DAG

Unlike general graphs (where longest path is NP-hard!), in a DAG you can find the longest path efficiently:
1. Topologically sort the nodes.
2. Process nodes in topological order, relaxing edges: `dist[v] = max(dist[v], dist[u] + weight(u,v))`.

This is the basis for **Critical Path Method** (CPM) in project management.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque, defaultdict

def longest_path_dag(n, edges):
    """Find longest path in a DAG using topological sort + relaxation.
    edges = [(u, v, weight), ...]
    Returns list of longest distances from node 0.
    """
    adj = defaultdict(list)
    in_degree = [0] * n
    for u, v, w in edges:
        adj[u].append((v, w))
        in_degree[v] += 1

    # Kahn's topo sort
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Relaxation in topological order
    dist = [0] * n
    for u in topo_order:
        for v, w in adj[u]:
            dist[v] = max(dist[v], dist[u] + w)

    return dist
```
{% endtab %}
{% tab title="Java" %}
```java
public int[] longestPathDAG(int n, int[][] edges) {
    // edges[i] = {u, v, weight}
    List<int[]>[] adj = new List[n];
    int[] inDeg = new int[n];
    for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
    for (int[] e : edges) {
        adj[e[0]].add(new int[]{e[1], e[2]});
        inDeg[e[1]]++;
    }
    Queue<Integer> queue = new ArrayDeque<>();
    for (int i = 0; i < n; i++)
        if (inDeg[i] == 0) queue.add(i);
    List<Integer> topo = new ArrayList<>();
    while (!queue.isEmpty()) {
        int u = queue.poll();
        topo.add(u);
        for (int[] nxt : adj[u])
            if (--inDeg[nxt[0]] == 0) queue.add(nxt[0]);
    }
    int[] dist = new int[n];
    for (int u : topo)
        for (int[] nxt : adj[u])
            dist[nxt[0]] = Math.max(dist[nxt[0]], dist[u] + nxt[1]);
    return dist;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> longestPathDAG(int n, vector<tuple<int,int,int>>& edges) {
    vector<vector<pair<int,int>>> adj(n);
    vector<int> inDeg(n, 0);
    for (auto& [u, v, w] : edges) {
        adj[u].push_back({v, w});
        inDeg[v]++;
    }
    queue<int> q;
    for (int i = 0; i < n; i++)
        if (inDeg[i] == 0) q.push(i);
    vector<int> topo;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        topo.push_back(u);
        for (auto [v, w] : adj[u])
            if (--inDeg[v] == 0) q.push(v);
    }
    vector<int> dist(n, 0);
    for (int u : topo)
        for (auto [v, w] : adj[u])
            dist[v] = max(dist[v], dist[u] + w);
    return dist;
}
```
{% endtab %}
{% endtabs %}

---

## 28.6 Parallel Courses and Level-Based Processing

Kahn's algorithm naturally reveals **parallelism**. All nodes in the queue at the same time are independent — they can be processed simultaneously. This gives us the concept of "levels" or "semesters."

The **minimum number of semesters** to complete all courses equals the number of "waves" in Kahn's BFS (process all zero-indegree nodes level by level). This is equivalent to the **longest path** in the DAG plus one.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque, defaultdict

def min_semesters(n, relations):
    """Minimum semesters to take all n courses.
    relations = [[prev, next], ...] (1-indexed)
    Returns -1 if impossible (cycle).
    """
    adj = defaultdict(list)
    in_degree = [0] * (n + 1)
    for prev, nxt in relations:
        adj[prev].append(nxt)
        in_degree[nxt] += 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    semesters = 0
    count = 0
    while queue:
        semesters += 1
        for _ in range(len(queue)):
            u = queue.popleft()
            count += 1
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    return semesters if count == n else -1
```
{% endtab %}
{% tab title="Java" %}
```java
public int minSemesters(int n, int[][] relations) {
    List<List<Integer>> adj = new ArrayList<>();
    int[] inDeg = new int[n + 1];
    for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
    for (int[] r : relations) {
        adj.get(r[0]).add(r[1]);
        inDeg[r[1]]++;
    }
    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 1; i <= n; i++)
        if (inDeg[i] == 0) q.add(i);
    int semesters = 0, count = 0;
    while (!q.isEmpty()) {
        semesters++;
        int size = q.size();
        for (int i = 0; i < size; i++) {
            int u = q.poll();
            count++;
            for (int v : adj.get(u))
                if (--inDeg[v] == 0) q.add(v);
        }
    }
    return count == n ? semesters : -1;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int minSemesters(int n, vector<vector<int>>& relations) {
    vector<vector<int>> adj(n + 1);
    vector<int> inDeg(n + 1, 0);
    for (auto& r : relations) {
        adj[r[0]].push_back(r[1]);
        inDeg[r[1]]++;
    }
    queue<int> q;
    for (int i = 1; i <= n; i++)
        if (inDeg[i] == 0) q.push(i);
    int semesters = 0, count = 0;
    while (!q.empty()) {
        semesters++;
        int sz = q.size();
        for (int i = 0; i < sz; i++) {
            int u = q.front(); q.pop();
            count++;
            for (int v : adj[u])
                if (--inDeg[v] == 0) q.push(v);
        }
    }
    return count == n ? semesters : -1;
}
```
{% endtab %}
{% endtabs %}

---

## Five-Lens Framework: Course Schedule

Let us apply the Five-Lens Framework to the Course Schedule problem: given `numCourses` and `prerequisites`, determine if all courses can be finished.

### Lens 1: Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i] = [a, b]` means b must come before a
- Can have disconnected components (courses with no prerequisites)

### Lens 2: Brute Force

Try all `numCourses!` permutations. For each permutation, check if every prerequisite constraint is satisfied (a appears after b). If any permutation works, return `True`.

**Time**: O(n! * m) where m is the number of prerequisites. For n=10, this is 3.6 million checks. For n=20, impossible.

### Lens 3: Pattern Recognition

This is a graph problem. Each prerequisite `[a, b]` is an edge `b --> a`. The question is: "Does this directed graph have a cycle?" If no cycle, it is a DAG and a valid course ordering exists.

### Lens 4: Optimization

Use Kahn's algorithm (BFS topo sort). If we can process all nodes, no cycle exists. Or use DFS with three-color cycle detection.

**Time**: O(V + E) — optimal!

### Lens 5: Proof of Correctness

**Claim**: If the prerequisite graph is a DAG, all courses can be finished. If it has a cycle, they cannot.

**Proof**: (Forward) If the graph is a DAG, Kahn's algorithm processes all nodes — each removed node had in-degree 0, meaning all prerequisites were already processed. (Backward) If there is a cycle of length k, none of those k courses can ever have in-degree 0 (each depends on at least one other in the cycle), so Kahn's algorithm will stall with k unprocessed nodes.

---

## Think Like a Pro

{% hint style="info" %}
**Benq** (Benjamin Qi) — USACO Platinum, IOI Gold: "My approach to any DAG problem: immediately think topological sort. If you can model the problem as a DAG, topo sort probably gives you the answer. In USACO Gold, at least one problem per contest involves either topological sort directly or some DP on a DAG that requires topological ordering."

*What you can learn*: When you see the word "dependency," "prerequisite," "ordering," or "before/after" in a problem statement, your first thought should be: "Can I model this as a DAG and topologically sort it?"
{% endhint %}

{% hint style="info" %}
**Errichto** (Kamil Debowski) — ICPC World Finalist: "Kahn's BFS is my default for topological sort because it naturally gives you the level structure. When the problem asks for minimum time/rounds/semesters, Kahn's BFS levels give you the answer directly. DFS topo sort is fine too, but I use it mainly when I need cycle detection with the three-color technique."

*What you can learn*: Choose the right variant for the problem. Kahn's is better for level-based questions; DFS is better when you need cycle details or post-order processing.
{% endhint %}

---

## AOPS Showcase: "Course Schedule" — Three Progressive Solutions

**Problem**: Given `numCourses` and `prerequisites`, can you finish all courses?

### Approach 1: Brute Force — O(n! * m)

Try every permutation of courses. For each permutation, verify all prerequisites are satisfied.

```python
from itertools import permutations

def can_finish_brute(numCourses, prerequisites):
    for perm in permutations(range(numCourses)):
        pos = {course: i for i, course in enumerate(perm)}
        if all(pos[b] < pos[a] for a, b in prerequisites):
            return True
    return False
```

This is conceptually simple but absurdly slow. For 10 courses, we check 3,628,800 permutations.

### Approach 2: Kahn's BFS — O(V + E)

Build the prerequisite graph. Use in-degree tracking. If all nodes are processed, return True.

```python
from collections import deque, defaultdict

def can_finish_kahns(numCourses, prerequisites):
    adj = defaultdict(list)
    in_degree = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        in_degree[a] += 1

    queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
    count = 0
    while queue:
        u = queue.popleft()
        count += 1
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return count == numCourses
```

### Approach 3: DFS with Three-Color Cycle Detection — O(V + E)

Same time complexity as Kahn's, but uses the recursive DFS approach. A cycle means we cannot finish.

```python
def can_finish_dfs(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        adj[b].append(a)

    color = [0] * numCourses  # 0=white, 1=gray, 2=black

    def has_cycle(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return True
            if color[v] == 0 and has_cycle(v):
                return True
        color[u] = 2
        return False

    for i in range(numCourses):
        if color[i] == 0 and has_cycle(i):
            return False
    return True
```

### Comparison Table

| Approach | Time | Space | Key Insight |
|----------|------|-------|-------------|
| Brute Force | O(n! * m) | O(n) | Try all orderings |
| Kahn's BFS | O(V + E) | O(V + E) | In-degree peeling |
| DFS 3-Color | O(V + E) | O(V + E) | Back edge = cycle |

---

## Legend's Corner

{% hint style="info" %}
**Arthur B. Kahn** published his algorithm in 1962 in the paper "Topological Sorting of Large Networks." But the idea is much older than computer science — any recipe is a topological sort of cooking steps! You cannot frost a cake before baking it, and you cannot bake it before mixing the batter. Ancient builders used the same idea: lay the foundation before the walls, walls before the roof.

In competitive programming, topological sort problems appear in nearly every USACO Gold contest. The pattern is so common that experienced contestants can spot it within seconds: any problem involving "ordering" or "dependencies" is likely a topological sort problem in disguise.

**What you can learn**: The best algorithms are often formalizations of ideas people have used intuitively for centuries. When you learn an algorithm, try to connect it to a real-world process you already understand.
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Gotcha 1: Forgetting cycle detection**

Topological sort only works on DAGs. If the input graph has a cycle and you do not check for it, Kahn's algorithm will silently return a partial ordering (missing the nodes in the cycle), and DFS might loop forever. ALWAYS check that all nodes were processed.
{% endhint %}

{% hint style="danger" %}
**Gotcha 2: Prerequisite direction confusion**

In Course Schedule problems, `[a, b]` means "to take course a, you need b first" — so the edge is `b --> a`. Many people accidentally create `a --> b`, which reverses the entire graph and gives wrong answers.
{% endhint %}

{% hint style="danger" %}
**Gotcha 3: Not handling disconnected components**

A graph can have multiple connected components. Kahn's algorithm handles this naturally (all zero-indegree nodes start in the queue). But DFS-based approaches must iterate over ALL nodes, not just start from node 0.
{% endhint %}

{% hint style="danger" %}
**Gotcha 4: Confusing visited with in-progress**

In directed cycle detection, a node that is already fully processed (BLACK) is NOT evidence of a cycle. Only encountering a node that is currently IN PROGRESS (GRAY / on the recursion stack) indicates a cycle. Using a simple boolean `visited` array instead of three colors will produce false positives.
{% endhint %}

{% hint style="danger" %}
**Gotcha 5: Modifying in-degree array during iteration**

In Kahn's algorithm, you decrement in-degrees as you process nodes. Do NOT use the original in-degree array for any other purpose after the algorithm runs — it has been modified. If you need the original in-degrees, make a copy.
{% endhint %}

{% hint style="danger" %}
**Gotcha 6: 0-indexed vs. 1-indexed nodes**

Some problems use 0-indexed nodes, others use 1-indexed. Mixing them up causes off-by-one errors and missed nodes. Always check the problem statement carefully and adjust your array sizes accordingly.
{% endhint %}

{% hint style="danger" %}
**Gotcha 7: Alien Dictionary edge cases**

In the Alien Dictionary problem, be careful of: (1) words where a longer word comes before its prefix (e.g., "abc" before "ab") — this is INVALID. (2) Characters that appear in words but have no ordering constraints — they still need to be in the output.
{% endhint %}

{% hint style="danger" %}
**Gotcha 8: Multiple valid topological orderings**

When testing topological sort, remember that multiple valid orderings exist. Do NOT test for a specific output sequence. Instead, validate that every edge `u --> v` has `u` appearing before `v` in the result. Use a validation function!
{% endhint %}

---

## Practice Problems

| # | Name | Difficulty | Key Concept |
|---|------|-----------|-------------|
| W1 | Topological Sort (Kahn's) | ★ | Basic Kahn's algorithm |
| W2 | Course Schedule I | ★ | Cycle detection via topo sort |
| W3 | Course Schedule II | ★ | Return valid ordering or [] |
| W4 | Detect Cycle in Directed Graph | ★ | Three-color DFS |
| P1 | Alien Dictionary | ★★ | Extract edges from word comparisons |
| P2 | Parallel Courses | ★★ | Level-based Kahn's (min semesters) |
| P3 | Find All Recipes | ★★ | Topo sort with string nodes |
| P4 | All Ancestors of a Node | ★★ | Reverse graph + DFS/BFS per node |
| C1 | Minimum Height Trees | ★★★ | Iterative leaf removal (Kahn's-like on undirected tree) |
| C2 | Find Eventual Safe States | ★★★ | Reverse graph + topo sort |
| C3 | Largest Color Value in Directed Graph | ★★★ | Topo sort + DP on DAG |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque, defaultdict

# ── Kahn's Algorithm pattern ──
adj = defaultdict(list)
in_degree = [0] * n
for u, v in edges:
    adj[u].append(v)
    in_degree[v] += 1

queue = deque(i for i in range(n) if in_degree[i] == 0)
result = []
while queue:
    u = queue.popleft()
    result.append(u)
    for v in adj[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            queue.append(v)

# ── DFS topo sort pattern ──
color = [0] * n  # 0=white, 1=gray, 2=black
stack = []
def dfs(u):
    color[u] = 1
    for v in adj[u]:
        if color[v] == 1: return True  # cycle
        if color[v] == 0 and dfs(v): return True
    color[u] = 2
    stack.append(u)
    return False
# result = stack[::-1]
```
{% endtab %}
{% tab title="Java" %}
```java
import java.util.*;

// ── Kahn's Algorithm pattern ──
List<List<Integer>> adj = new ArrayList<>();
int[] inDegree = new int[n];
for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
// ... build graph ...
Queue<Integer> queue = new ArrayDeque<>();
for (int i = 0; i < n; i++)
    if (inDegree[i] == 0) queue.add(i);
List<Integer> result = new ArrayList<>();
while (!queue.isEmpty()) {
    int u = queue.poll();
    result.add(u);
    for (int v : adj.get(u))
        if (--inDegree[v] == 0) queue.add(v);
}

// ── DFS 3-color cycle detection ──
int[] color = new int[n]; // 0=white, 1=gray, 2=black
boolean hasCycle(int u) {
    color[u] = 1;
    for (int v : adj.get(u)) {
        if (color[v] == 1) return true;
        if (color[v] == 0 && hasCycle(v)) return true;
    }
    color[u] = 2;
    return false;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
#include <vector>
#include <queue>
using namespace std;

// ── Kahn's Algorithm pattern ──
vector<vector<int>> adj(n);
vector<int> inDegree(n, 0);
// ... build graph ...
queue<int> q;
for (int i = 0; i < n; i++)
    if (inDegree[i] == 0) q.push(i);
vector<int> result;
while (!q.empty()) {
    int u = q.front(); q.pop();
    result.push_back(u);
    for (int v : adj[u])
        if (--inDegree[v] == 0) q.push(v);
}

// ── DFS 3-color cycle detection ──
vector<int> color(n, 0);
function<bool(int)> dfs = [&](int u) -> bool {
    color[u] = 1;
    for (int v : adj[u]) {
        if (color[v] == 1) return true;
        if (color[v] == 0 && dfs(v)) return true;
    }
    color[u] = 2;
    return false;
};
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 19** (Graphs I) introduced adjacency lists, BFS, and DFS — the building blocks for topological sort
- **Ch 20** (Graphs II) covered connected components and graph traversals — topological sort extends DFS with post-order processing
- **Ch 27** (Shortest Paths) used BFS for unweighted shortest paths — Kahn's algorithm is structurally similar to BFS

### Looking Forward
- **Ch 29** (Union-Find & MST) will introduce another way to handle graph connectivity — Union-Find is for undirected graphs while topo sort is for directed graphs
- **Ch 31** (Advanced DP) will use topological ordering as a prerequisite for DP on DAGs — you process states in topological order to ensure dependencies are resolved

### Cross-Chapter Threads
- **"Reduce to known"**: Alien Dictionary reduces to topological sort. Course Schedule reduces to cycle detection. Minimum Height Trees reduces to iterative leaf removal. The skill of recognizing these reductions separates Gold from Platinum.
- **"Right question"**: Course Schedule I asks "is there a cycle?" while Course Schedule II asks "what is the ordering?" Same graph, different questions. Choosing the right formulation matters.
- **"Brute force is a strategy"**: The brute force for Course Schedule (try all permutations) is O(n!). Kahn's is O(V+E). But writing the brute force FIRST helps you understand what "valid ordering" means.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"What if we need the LEXICOGRAPHICALLY smallest topological order?"** Hint: replace the queue in Kahn's algorithm with a min-heap (priority queue). Instead of processing any zero-indegree node, always process the smallest one. This gives the lexicographically smallest valid ordering in O((V + E) log V) time.

2. **"Can we topologically sort in parallel?"** Yes! In Kahn's algorithm, all nodes in the queue at any given time are independent — they have no dependencies on each other. This is the basis for parallel build systems. The minimum number of "rounds" (semesters, build steps) equals the longest path in the DAG plus one.

3. **"What real-world systems use topological sort?"** Build tools (`make`, `gradle`, `bazel`), package managers (`npm`, `pip`, `apt`), spreadsheet engines (compute cell dependencies), CI/CD pipelines (job dependencies), and even JavaScript module bundlers (`webpack`). Every time you run `npm install`, topological sort is happening behind the scenes.

---

## What's Next

You have now mastered topological sort — one of the most practically useful graph algorithms. You know two approaches (Kahn's BFS and DFS), you can detect cycles, and you can apply these techniques to course scheduling, build systems, alien dictionaries, and more.

But graphs have more secrets. What happens when you need to determine if two nodes are in the same connected component, and the edges keep arriving one by one? What if you need to find the cheapest set of edges that connects all nodes?

In **Ch 29 (Union-Find & Minimum Spanning Trees)**, you will learn the Union-Find data structure for dynamic connectivity queries and Kruskal's/Prim's algorithms for finding minimum spanning trees. These complete your Gold-level graph toolkit and prepare you for the most advanced graph problems in USACO.

The journey continues!
