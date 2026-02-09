# Advanced DP — Bitmask, Interval, Trees

{% hint style="info" %}
**Welcome to the Platinum Summit!** This chapter takes everything you learned about dynamic programming in Chapters 23-25 and cranks it up to competition level. Bitmask DP, interval DP, and tree DP are the three advanced DP patterns you will see in USACO Platinum and top-tier contests. They are not harder conceptually — they just encode **states** in creative ways.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand bitmask DP: encoding subsets of items as integers using bit manipulation (connecting back to Ch 12)
- Solve the Traveling Salesman Problem (TSP) in O(2^n * n^2) instead of O(n!)
- Recognize the "n <= 20" signal that screams bitmask DP
- Understand interval DP: solving problems by merging or splitting contiguous ranges
- Solve Matrix Chain Multiplication and Burst Balloons using interval DP
- Know the critical loop order for interval DP: iterate by interval LENGTH, not endpoints
- Understand DP on trees: computing answers bottom-up from leaves to root
- Solve the maximum independent set problem on trees
- Get a first look at digit DP for counting numbers with digit-based constraints
- Survey DP optimizations (Knuth, Divide & Conquer, Convex Hull Trick) at a conceptual level
- Build a decision framework for recognizing which advanced DP pattern to apply
- Connect these techniques to USACO Platinum contest patterns

---

## The Story: "The Puzzle Master"

Zara loved puzzles — the kind you find at thrift stores with 500 pieces and no box lid. She had a system: sort the edges, group by color, build outward. But one day she found a puzzle unlike any she had seen before.

It was a strange board game with 16 tiles. Each tile was either placed on the board (1) or still in the box (0). The rules said: "Find the cheapest way to place ALL tiles, one at a time, where the cost of placing a tile depends on which tiles are already on the board."

Zara realized something: with 16 tiles, there were 2^16 = 65,536 possible states of the board — each tile either on or off. She could represent each state as a binary number! The state `1011` means tiles 0, 1, and 3 are placed, but tile 2 is still in the box.

"If I can figure out the best move from every possible state," she thought, "I can work backward from the goal (all tiles placed) to the start (empty board)."

That night she also tackled a chain-cutting puzzle — figuring out the cheapest order to cut a gold chain into pieces — and a tree-shaped mobile where she had to pick which ornaments to hang so no two adjacent hooks were both loaded.

Three puzzles. Three different structures. But all three shared the same secret: define the right **state**, find the right **transitions**, and let dynamic programming do the rest.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "The Shortest Road Trip"

You are planning a road trip to visit 4 cities (numbered 0-3). The driving times between cities are:

| From\To | 0 | 1 | 2 | 3 |
|---------|---|---|---|---|
| 0 | 0 | 10 | 15 | 20 |
| 1 | 10 | 0 | 35 | 25 |
| 2 | 15 | 35 | 0 | 30 |
| 3 | 20 | 25 | 30 | 0 |

You start at city 0, visit every city exactly once, and return to city 0. What is the shortest total driving time?

Try listing all possible routes. How many are there? (Hint: from city 0, you have 3 choices for the next city, then 2, then 1.)

{% hint style="info" %}
There are 3! = 6 possible routes from city 0:
- 0 -> 1 -> 2 -> 3 -> 0: 10 + 35 + 30 + 20 = 95
- 0 -> 1 -> 3 -> 2 -> 0: 10 + 25 + 30 + 15 = 80 **<-- best!**
- 0 -> 2 -> 1 -> 3 -> 0: 15 + 35 + 25 + 20 = 95
- 0 -> 2 -> 3 -> 1 -> 0: 15 + 30 + 25 + 10 = 80 **<-- tied!**
- 0 -> 3 -> 1 -> 2 -> 0: 20 + 25 + 35 + 15 = 95
- 0 -> 3 -> 2 -> 1 -> 0: 20 + 30 + 35 + 10 = 95

The minimum is **80**. For 4 cities that is manageable, but for 20 cities there would be 19! = 121 quadrillion routes. We need a smarter approach!
{% endhint %}

### Puzzle 2: "The Matrix Multiplication Order"

You need to multiply three matrices:
- A is 10 x 30
- B is 30 x 5
- C is 5 x 60

Matrix multiplication is associative, so (A x B) x C = A x (B x C). But the number of scalar multiplications depends on the order:

- **(A x B) x C**: First A x B costs 10 * 30 * 5 = 1,500, giving a 10x5 result. Then result x C costs 10 * 5 * 60 = 3,000. **Total: 4,500.**
- **A x (B x C)**: First B x C costs 30 * 5 * 60 = 9,000, giving a 30x60 result. Then A x result costs 10 * 30 * 60 = 18,000. **Total: 27,000.**

That is a 6x difference! The order matters hugely. For 4+ matrices, how do you find the cheapest order?

{% hint style="info" %}
With n matrices, you need to decide where to "split" the chain at each level. This is a classic interval DP problem — the state is "what is the cheapest way to multiply matrices i through j?"
{% endhint %}

### Puzzle 3: "The Tree Heist"

A thief is robbing houses arranged in a tree (not a line — more like a family tree). Each house has some cash. But there is a catch: if you rob a house, you CANNOT rob any house directly connected to it (its parent or children). How much can you steal?

```
        1 (node 0)
       / \
      2   3 (nodes 1, 2)
     /
    4 (node 3)
```

Values: node 0 = 1, node 1 = 2, node 2 = 3, node 3 = 4.

{% hint style="info" %}
If you rob node 0 (value 1), you cannot rob nodes 1 or 2. You CAN rob node 3 (value 4). Total: 1 + 4 = 5.
If you skip node 0, you can rob nodes 1, 2, and 3 — but wait, robbing node 1 means you cannot rob node 3. So either: rob 1 + 2 = 2 + 3 = 5, or rob 2 + 3 = 3 + 4 = 7.
Best: skip node 0, skip node 1, rob nodes 2 and 3 = 3 + 4 = **7**.

This is DP on a tree: for each node, decide "rob it or skip it" based on what its children decided.
{% endhint %}

---

## 31.1 Bitmask DP — Encoding Subsets

### The Key Insight

Remember bit manipulation from Chapter 12? We used individual bits to represent true/false flags. Bitmask DP takes this further: we use an **integer** to represent a **subset** of items.

If you have n items (numbered 0 to n-1), a bitmask is an integer where:
- Bit i is 1 if item i is in the subset
- Bit i is 0 if item i is not in the subset

For example, with 4 items, the bitmask `1011` (decimal 11) represents the subset {0, 1, 3}.

```
Bitmask:  1 0 1 1
Bit:      3 2 1 0
Meaning:  in  out  in  in
Subset: {0, 1, 3}
```

### Common Bitmask Operations

{% tabs %}
{% tab title="Python" %}
```python
# Check if bit i is set (is item i in the subset?)
if mask & (1 << i):
    print(f"Item {i} is in the subset")

# Set bit i (add item i to the subset)
new_mask = mask | (1 << i)

# Clear bit i (remove item i from the subset)
new_mask = mask & ~(1 << i)

# Toggle bit i
new_mask = mask ^ (1 << i)

# Check if all n bits are set (full set)
full = (1 << n) - 1
if mask == full:
    print("All items included!")

# Count items in subset
count = bin(mask).count('1')

# Iterate over all subsets of n items
for mask in range(1 << n):
    # process subset represented by mask
    pass
```
{% endtab %}
{% tab title="Java" %}
```java
// Check if bit i is set
if ((mask & (1 << i)) != 0) { /* item i is in subset */ }

// Set bit i
int newMask = mask | (1 << i);

// Clear bit i
int newMask = mask & ~(1 << i);

// Full set
int full = (1 << n) - 1;

// Count items in subset
int count = Integer.bitCount(mask);

// Iterate over all subsets
for (int mask = 0; mask < (1 << n); mask++) { /* process */ }
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Check if bit i is set
if (mask & (1 << i)) { /* item i is in subset */ }

// Set bit i
int newMask = mask | (1 << i);

// Clear bit i
int newMask = mask & ~(1 << i);

// Full set
int full = (1 << n) - 1;

// Count items in subset
int count = __builtin_popcount(mask);

// Iterate over all subsets
for (int mask = 0; mask < (1 << n); mask++) { /* process */ }
```
{% endtab %}
{% endtabs %}

### The Traveling Salesman Problem (TSP)

The TSP asks: given n cities and distances between them, find the shortest route that visits every city exactly once and returns to the start.

**Brute force**: Try all n! permutations. For n=20, that is about 2.4 * 10^18 — way too slow.

**Bitmask DP insight**: We do not need to remember the ORDER we visited cities, only WHICH cities we have visited and WHERE we are now.

State: `dp[mask][i]` = minimum cost to have visited exactly the cities in `mask`, ending at city `i`.

Base case: `dp[1 << start][start] = 0` (visited only the start city, at cost 0).

Transition: To reach state `(mask, i)`, we came from some city `j` where:
- `j` is in `mask` (we have visited it)
- `i` was NOT in `mask` before (we just visited it)
- `dp[mask][i] = min(dp[mask ^ (1 << i)][j] + dist[j][i])` for all valid `j`

Final answer: `min(dp[full][i] + dist[i][start])` for all `i`.

{% tabs %}
{% tab title="Python" %}
```python
def tsp(n, dist):
    INF = float('inf')
    full = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at city 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue  # already visited
                new_mask = mask | (1 << v)
                cost = dp[mask][u] + dist[u][v]
                if cost < dp[new_mask][v]:
                    dp[new_mask][v] = cost

    # Return to start
    ans = INF
    for u in range(n):
        ans = min(ans, dp[full][u] + dist[u][0])
    return ans
```
{% endtab %}
{% tab title="Java" %}
```java
static int tsp(int n, int[][] dist) {
    int full = (1 << n) - 1;
    int[][] dp = new int[1 << n][n];
    for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE / 2);
    dp[1][0] = 0;

    for (int mask = 1; mask <= full; mask++)
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] >= Integer.MAX_VALUE / 2) continue;
            if ((mask & (1 << u)) == 0) continue;
            for (int v = 0; v < n; v++) {
                if ((mask & (1 << v)) != 0) continue;
                int nm = mask | (1 << v);
                dp[nm][v] = Math.min(dp[nm][v], dp[mask][u] + dist[u][v]);
            }
        }

    int ans = Integer.MAX_VALUE / 2;
    for (int u = 0; u < n; u++)
        ans = Math.min(ans, dp[full][u] + dist[u][0]);
    return ans;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int tsp(int n, vector<vector<int>>& dist) {
    int full = (1 << n) - 1;
    vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX / 2));
    dp[1][0] = 0;

    for (int mask = 1; mask <= full; mask++)
        for (int u = 0; u < n; u++) {
            if (dp[mask][u] >= INT_MAX / 2) continue;
            if (!(mask & (1 << u))) continue;
            for (int v = 0; v < n; v++) {
                if (mask & (1 << v)) continue;
                int nm = mask | (1 << v);
                dp[nm][v] = min(dp[nm][v], dp[mask][u] + dist[u][v]);
            }
        }

    int ans = INT_MAX / 2;
    for (int u = 0; u < n; u++)
        ans = min(ans, dp[full][u] + dist[u][0]);
    return ans;
}
```
{% endtab %}
{% endtabs %}

**Complexity**: O(2^n * n^2) time, O(2^n * n) space. For n=20, that is about 20 * 10^6 * 20 = 400 million — tight but feasible. For n=25, it is way too much (33 billion). The magic boundary is **n <= 20**.

{% hint style="warning" %}
**The n <= 20 Rule**: When a problem says n <= 20 and involves subsets, selections, or assignments, think bitmask DP immediately. 2^20 = 1,048,576 which is about 10^6, and with an extra factor of n or n^2, you stay under 10^9.
{% endhint %}

---

## 31.2 Interval DP — Merging Ranges

### The Key Insight

Interval DP solves problems where:
- You have a sequence of items
- You need to combine adjacent items (merge, split, or evaluate)
- The cost of combining depends on the items themselves
- You want to minimize (or maximize) the total cost

The state is `dp[i][j]` = optimal answer for the subproblem involving items `i` through `j`.

### Matrix Chain Multiplication (MCM)

Given n matrices with dimensions dims[0] x dims[1], dims[1] x dims[2], ..., dims[n-1] x dims[n], find the parenthesization that minimizes the total number of scalar multiplications.

State: `dp[i][j]` = minimum cost to multiply matrices i through j.

Transition: Try every split point k between i and j:
```
dp[i][j] = min(dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1])
```

{% tabs %}
{% tab title="Python" %}
```python
def mcm(dims):
    n = len(dims) - 1  # number of matrices
    if n <= 1:
        return 0
    dp = [[0] * n for _ in range(n)]

    # Fill by increasing interval length
    for length in range(2, n + 1):          # length of chain
        for i in range(n - length + 1):     # start index
            j = i + length - 1              # end index
            dp[i][j] = float('inf')
            for k in range(i, j):           # split point
                cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]
```
{% endtab %}
{% tab title="Java" %}
```java
static int mcm(int[] dims) {
    int n = dims.length - 1;
    if (n <= 1) return 0;
    int[][] dp = new int[n][n];

    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = Integer.MAX_VALUE;
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1];
                dp[i][j] = Math.min(dp[i][j], cost);
            }
        }

    return dp[0][n - 1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int mcm(vector<int>& dims) {
    int n = dims.size() - 1;
    if (n <= 1) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++) {
                int cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1];
                dp[i][j] = min(dp[i][j], cost);
            }
        }

    return dp[0][n - 1];
}
```
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
**Critical Loop Order!** In interval DP, the outer loop must iterate by **length** (2, 3, 4, ..., n), NOT by endpoint. If you loop `for i ... for j ... for k`, shorter intervals have not been computed yet when you need them! Always think: "I need shorter intervals to build longer ones."
{% endhint %}

### Burst Balloons

Given an array `nums` of balloon values, burst all balloons to maximize coins. When you burst balloon `i`, you earn `nums[i-1] * nums[i] * nums[i+1]` coins (boundaries are treated as 1).

The trick: instead of thinking about which balloon to burst FIRST, think about which one to burst LAST in each interval. If balloon `k` is the last one burst in interval `[i, j]`, then at that point `nums[i-1]` and `nums[j+1]` are its neighbors.

```
dp[i][j] = max over k in [i..j] of:
    dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1]
```

**Complexity**: O(n^3) time, O(n^2) space.

---

## 31.3 DP on Trees — Thinking Bottom-Up

### The Key Insight

Trees have a natural recursive structure: every subtree is an independent subproblem. DP on trees processes nodes from **leaves to root** (bottom-up), computing each node's answer from its children's answers.

### Maximum Independent Set on a Tree

Given a tree where each node has a value, pick nodes to maximize the total value such that no two picked nodes are adjacent (connected by an edge).

State for each node `u`:
- `dp[u][0]` = max value in subtree of u when u is NOT picked
- `dp[u][1]` = max value in subtree of u when u IS picked

Transitions:
- If u is picked: children must NOT be picked.
  `dp[u][1] = value[u] + sum(dp[child][0] for each child)`
- If u is NOT picked: each child can be picked or not (take the best).
  `dp[u][0] = sum(max(dp[child][0], dp[child][1]) for each child)`

{% tabs %}
{% tab title="Python" %}
```python
def max_independent_set(n, values, edges):
    if n == 0:
        return 0
    if n == 1:
        return values[0]

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dp = [[0, 0] for _ in range(n)]

    # Iterative post-order (avoids recursion limit)
    visited = [False] * n
    parent = [-1] * n
    order = []
    stack = [0]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                stack.append(v)

    # Process in reverse order (leaves first)
    for u in reversed(order):
        dp[u][1] = values[u]
        for v in adj[u]:
            if v == parent[u]:
                continue
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

    return max(dp[0][0], dp[0][1])
```
{% endtab %}
{% tab title="Java" %}
```java
static int maxIndependentSet(int n, int[] values, int[][] edges) {
    if (n == 0) return 0;
    if (n == 1) return values[0];
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

    int[][] dp = new int[n][2];
    boolean[] visited = new boolean[n];
    int[] par = new int[n];
    Arrays.fill(par, -1);
    List<Integer> order = new ArrayList<>();
    Deque<Integer> stack = new ArrayDeque<>();
    stack.push(0);
    while (!stack.isEmpty()) {
        int u = stack.pop();
        if (visited[u]) continue;
        visited[u] = true;
        order.add(u);
        for (int v : adj.get(u))
            if (!visited[v]) { par[v] = u; stack.push(v); }
    }
    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order.get(idx);
        dp[u][1] = values[u];
        for (int v : adj.get(u)) {
            if (v == par[u]) continue;
            dp[u][0] += Math.max(dp[v][0], dp[v][1]);
            dp[u][1] += dp[v][0];
        }
    }
    return Math.max(dp[0][0], dp[0][1]);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int maxIndependentSet(int n, vector<int>& values, vector<vector<int>>& edges) {
    if (n == 0) return 0;
    if (n == 1) return values[0];
    vector<vector<int>> adj(n);
    for (auto& e : edges) { adj[e[0]].push_back(e[1]); adj[e[1]].push_back(e[0]); }

    vector<array<int,2>> dp(n, {0, 0});
    vector<bool> visited(n, false);
    vector<int> par(n, -1), order;
    stack<int> stk;
    stk.push(0);
    while (!stk.empty()) {
        int u = stk.top(); stk.pop();
        if (visited[u]) continue;
        visited[u] = true;
        order.push_back(u);
        for (int v : adj[u])
            if (!visited[v]) { par[v] = u; stk.push(v); }
    }
    for (int idx = order.size() - 1; idx >= 0; idx--) {
        int u = order[idx];
        dp[u][1] = values[u];
        for (int v : adj[u]) {
            if (v == par[u]) continue;
            dp[u][0] += max(dp[v][0], dp[v][1]);
            dp[u][1] += dp[v][0];
        }
    }
    return max(dp[0][0], dp[0][1]);
}
```
{% endtab %}
{% endtabs %}

### Tree Diameter via DP

The diameter of a tree is the longest path between any two nodes. We can find it with a single DFS:

For each node, track the two longest paths going DOWN into its subtree. The diameter through that node is the sum of those two paths. The overall diameter is the maximum across all nodes.

---

## 31.4 Digit DP — Counting with Constraints

### The Key Insight

Digit DP counts numbers in a range `[1, N]` that satisfy some property about their digits (e.g., all digits are unique, digit sum equals k, no consecutive same digits).

The idea: build the number digit by digit from left to right, tracking:
1. **Position**: which digit we are placing
2. **Tight**: are we still bounded by N? (if all digits so far match N, the next digit is capped)
3. **State**: whatever property we are tracking (e.g., which digits have been used)

For "count numbers with all unique digits up to N":
- State includes a **bitmask** of used digits (combining digit DP with bitmask DP!)
- At each position, try each digit 0-9
- If tight, the digit cannot exceed the corresponding digit of N
- Skip digits already in the bitmask

{% hint style="info" %}
Digit DP is a niche but powerful technique. USACO Platinum occasionally features digit DP problems, and it appears frequently in Codeforces Div 1 contests. The key is recognizing that "count numbers in [L, R] with property X" almost always means digit DP.
{% endhint %}

---

## 31.5 DP Optimizations Preview

As you advance, you will encounter DP problems where the naive O(n^3) or O(n^2) solution is too slow. Here is a preview of optimization techniques you will master later:

| Technique | Reduces | When to Use | Example |
|-----------|---------|-------------|---------|
| **Knuth's Optimization** | O(n^3) -> O(n^2) | Interval DP where optimal split point is monotone | Optimal BST |
| **Divide & Conquer DP** | O(n * k * n) -> O(n * k * log n) | DP with monotone "opt" array | Splitting into k groups |
| **Convex Hull Trick** | O(n^2) -> O(n log n) or O(n) | DP transition is a linear function of state | Minimize cost with linear functions |
| **Li Chao Tree** | O(n^2) -> O(n log n) | Like CHT but more general | Range of linear functions |
| **Aliens Trick (Lambda)** | Removes one dimension | Penalty for using extra items | k-edge shortest path |

For now, just know these exist. Recognizing that a problem CAN be optimized is the first step. The actual techniques will come in advanced study.

---

## 31.6 Recognizing Advanced DP Patterns

When you see a new problem, use this decision framework:

```
Is n <= 20 and the problem involves subsets/assignments?
  --> Bitmask DP: dp[mask][...]

Does the problem involve merging/splitting a sequence?
  --> Interval DP: dp[i][j], iterate by length

Is the problem on a tree (pick/skip nodes, aggregate subtrees)?
  --> Tree DP: dp[node][state], process leaves to root

Does it say "count numbers in [L,R] with digit property"?
  --> Digit DP: dp[pos][tight][state]

None of the above?
  --> Check if it is a standard 1D/2D DP from Chapters 23-25
```

---

## Five-Lens Framework: Bitmask DP (TSP)

{% hint style="info" %}
### Lens 1: Constraints
n <= 20 cities. Distance matrix given. Need minimum-cost Hamiltonian cycle.

### Lens 2: Brute Force
Try all n! permutations of cities. For n=20, that is 2.4 * 10^18 operations. Way too slow.

### Lens 3: Pattern
Many permutations share the same "prefix" in terms of WHICH cities are visited. The state is (current city, set of visited cities). Two paths that visit the same cities and end at the same city are interchangeable — keep only the cheaper one.

### Lens 4: Optimization
dp[mask][i] = min cost to visit exactly the cities in mask, ending at city i. There are 2^n * n states, each with O(n) transitions. Total: O(2^n * n^2).

For n=20: 2^20 * 20^2 = 1,048,576 * 400 = ~4 * 10^8. Tight but feasible in C++.

### Lens 5: Proof
Each (mask, city) state is computed exactly once. The recurrence correctly considers all possible previous cities. The final answer correctly considers the return trip. By induction on the number of set bits in mask, dp[mask][i] is optimal.
{% endhint %}

---

## Think Like a Pro

{% hint style="warning" %}
**Errichto** (Kamil Debowski, Codeforces Legendary Grandmaster):

"When I see n <= 20 in the constraints, my eyes light up — that is the bitmask DP signal. I immediately think: what is the state? Usually it is dp[mask][something]. For interval DP, I look for keywords like 'merge', 'split', 'parenthesize', or 'partition contiguous'. For tree DP, any problem that says 'choose nodes in a tree' or 'maximum independent set' is a dead giveaway.

The hardest part of advanced DP is not the implementation — it is defining the state. Spend 80% of your time on the state definition and 20% on coding. If the state is right, the transitions write themselves."
{% endhint %}

---

## AOPS Showcase: Matrix Chain Multiplication — Four Ways

We solve MCM four different ways, each building on the previous one.

### Solution 1: Brute Force Recursion

Try every possible split point at every level.

{% tabs %}
{% tab title="Python" %}
```python
def mcm_brute(dims, i, j):
    if i == j:
        return 0
    best = float('inf')
    for k in range(i, j):
        cost = mcm_brute(dims, i, k) + mcm_brute(dims, k+1, j) + dims[i] * dims[k+1] * dims[j+1]
        best = min(best, cost)
    return best

# Usage: mcm_brute(dims, 0, len(dims) - 2)
```
{% endtab %}
{% tab title="Java" %}
```java
static int mcmBrute(int[] dims, int i, int j) {
    if (i == j) return 0;
    int best = Integer.MAX_VALUE;
    for (int k = i; k < j; k++) {
        int cost = mcmBrute(dims, i, k) + mcmBrute(dims, k+1, j) + dims[i] * dims[k+1] * dims[j+1];
        best = Math.min(best, cost);
    }
    return best;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int mcmBrute(vector<int>& dims, int i, int j) {
    if (i == j) return 0;
    int best = INT_MAX;
    for (int k = i; k < j; k++) {
        int cost = mcmBrute(dims, i, k) + mcmBrute(dims, k+1, j) + dims[i] * dims[k+1] * dims[j+1];
        best = min(best, cost);
    }
    return best;
}
```
{% endtab %}
{% endtabs %}

**Time**: O(2^n) — exponential! Same subproblems solved repeatedly.

### Solution 2: Memoized Recursion (Top-Down)

{% tabs %}
{% tab title="Python" %}
```python
def mcm_memo(dims):
    n = len(dims) - 1
    memo = {}
    def dp(i, j):
        if i == j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        best = float('inf')
        for k in range(i, j):
            cost = dp(i, k) + dp(k+1, j) + dims[i] * dims[k+1] * dims[j+1]
            best = min(best, cost)
        memo[(i, j)] = best
        return best
    return dp(0, n - 1)
```
{% endtab %}
{% tab title="Java" %}
```java
static int mcmMemo(int[] dims) {
    int n = dims.length - 1;
    int[][] memo = new int[n][n];
    for (int[] row : memo) Arrays.fill(row, -1);
    return dpMemo(dims, memo, 0, n - 1);
}
static int dpMemo(int[] dims, int[][] memo, int i, int j) {
    if (i == j) return 0;
    if (memo[i][j] != -1) return memo[i][j];
    int best = Integer.MAX_VALUE;
    for (int k = i; k < j; k++) {
        int cost = dpMemo(dims, memo, i, k) + dpMemo(dims, memo, k+1, j) + dims[i]*dims[k+1]*dims[j+1];
        best = Math.min(best, cost);
    }
    return memo[i][j] = best;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int dpMemo(vector<int>& dims, vector<vector<int>>& memo, int i, int j) {
    if (i == j) return 0;
    if (memo[i][j] != -1) return memo[i][j];
    int best = INT_MAX;
    for (int k = i; k < j; k++) {
        int cost = dpMemo(dims, memo, i, k) + dpMemo(dims, memo, k+1, j) + dims[i]*dims[k+1]*dims[j+1];
        best = min(best, cost);
    }
    return memo[i][j] = best;
}
```
{% endtab %}
{% endtabs %}

**Time**: O(n^3) — each of O(n^2) subproblems solved once, with O(n) split points each.

### Solution 3: Bottom-Up Tabulation

This is the "classic" interval DP approach: fill the table by increasing interval length.

{% tabs %}
{% tab title="Python" %}
```python
def mcm_tabulation(dims):
    n = len(dims) - 1
    if n <= 1:
        return 0
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dims[i] * dims[k+1] * dims[j+1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]
```
{% endtab %}
{% tab title="Java" %}
```java
static int mcmTab(int[] dims) {
    int n = dims.length - 1;
    if (n <= 1) return 0;
    int[][] dp = new int[n][n];
    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = Integer.MAX_VALUE;
            for (int k = i; k < j; k++)
                dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]);
        }
    return dp[0][n - 1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int mcmTab(vector<int>& dims) {
    int n = dims.size() - 1;
    if (n <= 1) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 2; len <= n; len++)
        for (int i = 0; i <= n - len; i++) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + dims[i]*dims[k+1]*dims[j+1]);
        }
    return dp[0][n - 1];
}
```
{% endtab %}
{% endtabs %}

**Time**: O(n^3). Same complexity as memoized, but sometimes faster in practice due to cache-friendly memory access.

### Solution 4: Knuth's Optimization (Concept)

When the optimal split point `opt[i][j]` satisfies `opt[i][j-1] <= opt[i][j] <= opt[i+1][j]` (monotonicity), we can narrow the search range for each split. This reduces the total work from O(n^3) to O(n^2).

MCM satisfies this property! But implementing Knuth's optimization requires careful bookkeeping of the optimal split points. For now, know that it exists and can speed up interval DP when the monotonicity condition holds.

---

## Legend's Corner

{% hint style="info" %}
**Tourist** (Gennady Korotkevich, highest-rated competitive programmer in history):

"Advanced DP is where competitive programming gets truly creative. The key is defining the right state — it must capture exactly the information you need to make future decisions, and nothing more. For bitmask DP, I always ask: what do I need to remember about which items have been processed? If the answer fits in 20 bits, we are golden.

For interval DP, the insight that changed everything for me was thinking about what happens LAST, not first. In burst balloons, which balloon do you burst last? In MCM, where is the outermost split? Thinking backward often makes the recurrence cleaner."
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
1. **Bitmask DP is only for n <= ~20.** 2^20 is about a million, 2^25 is 33 million, 2^30 is a billion. If n > 22, bitmask DP is almost certainly too slow. Look for a different approach.

2. **Interval DP loop order matters!** Always iterate by LENGTH first:
   ```
   for length in 2..n:      # outer loop
     for i in 0..n-length:   # start
       j = i + length - 1    # end
   ```
   If you loop `for i for j`, shorter intervals are not ready when you need them.

3. **Tree DP: do not forget leaf base cases.** Leaves have no children, so `dp[leaf][1] = value[leaf]` and `dp[leaf][0] = 0`. If you miss this, everything propagates incorrectly.

4. **Digit DP: handle leading zeros carefully.** The number 007 is really 7. If your digit DP allows leading zeros, you might double-count or count invalid numbers. Track a "started" flag.

5. **Memory in bitmask DP can explode.** `dp[1 << 20][20]` has 20 million entries. If each is a 4-byte int, that is 80 MB — close to many contest memory limits (256 MB). Use `int` instead of `long` when possible.

6. **Integer overflow in interval DP.** When dimensions or values are large, the product `dims[i] * dims[k+1] * dims[j+1]` can overflow 32-bit integers. Use `long` / `long long` in Java/C++ when needed.

7. **Bitmask DP initialization.** Make sure your "infinity" value does not cause overflow when you add to it. Use `INT_MAX / 2` instead of `INT_MAX` in C++/Java.
{% endhint %}

---

## Practice Problems

| # | Problem | Difficulty | Key Technique |
|---|---------|------------|---------------|
| W1 | Traveling Salesman (TSP) | Warmup | Bitmask DP |
| W2 | Matrix Chain Multiplication | Warmup | Interval DP |
| W3 | House Robber on Tree | Warmup | Tree DP |
| P1 | Shortest Hamiltonian Path | Practice | Bitmask DP (no return) |
| P2 | Burst Balloons | Practice | Interval DP |
| P3 | Minimum Score Triangulation | Practice | Interval DP |
| P4 | Tree Diameter via DP | Practice | Tree DP |
| P5 | Count Numbers with Unique Digits | Practice | Digit DP |
| C1 | Minimum Cost to Merge Stones | Challenge | Interval DP + constraints |
| C2 | Number of Ways to Wear Hats | Challenge | Bitmask DP on people |
| C3 | Binary Tree Cameras | Challenge | Tree DP (3 states) |
| C4 | Palindrome Partitioning II | Challenge | DP + palindrome preprocessing |

---

## Language Idioms

| Concept | Python | Java | C++ |
|---------|--------|------|-----|
| Bitmask full set | `(1 << n) - 1` | `(1 << n) - 1` | `(1 << n) - 1` |
| Popcount | `bin(x).count('1')` | `Integer.bitCount(x)` | `__builtin_popcount(x)` |
| 2D array init | `[[0]*m for _ in range(n)]` | `new int[n][m]` | `vector<vector<int>>(n, vector<int>(m, 0))` |
| Infinity | `float('inf')` | `Integer.MAX_VALUE / 2` | `INT_MAX / 2` |
| Recursion limit | `sys.setrecursionlimit()` | No limit (stack) | No limit (stack) |
| Memoization | `@functools.cache` | `HashMap` or `int[][]` | `map` or `vector<vector<int>>` |

---

## Breadcrumbs

**Looking back:**
- Chapter 12 (Bit Manipulation): The bit operations we use for bitmask DP
- Chapters 23-25 (DP I-III): The foundation — states, transitions, tabulation, memoization
- Chapter 26 (Trees): Tree structure, traversal order, parent-child relationships

**Looking forward:**
- Chapter 33 (Advanced Trees): Heavy-Light Decomposition and Euler Tour — more advanced tree DP
- Chapter 34 (Geometry & Sweep): Some geometry problems use interval DP for polygon triangulation

**Cross-chapter threads:**
- *Brute-force-to-DP*: TSP brute force (Ch 13) -> TSP bitmask DP (this chapter)
- *Space-for-time*: Bitmask DP trades O(2^n * n) memory for exponential time savings
- *Reduce-to-known*: Many problems reduce to MCM, TSP, or max independent set on trees

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

- What if the TSP graph has special structure (e.g., cities on a line, or distances satisfy triangle inequality)? Can we do better than O(2^n * n^2)?
- Is there a polynomial-time algorithm for TSP? (This is one of the most famous open questions in computer science — the P vs NP problem!)
- Can interval DP be extended to 2D (rectangles instead of intervals)? What problems would that solve?

---

## What's Next

In **Chapter 32: String Algorithms**, we move from numbers and trees to text. You will learn the KMP algorithm for pattern matching, Z-function, string hashing (Rabin-Karp), and the basics of suffix arrays. These string algorithms are essential for USACO Platinum problems involving text processing and pattern detection.
