# Segment Trees & Range Queries

{% hint style="info" %}
**Welcome to Part V: The Platinum Summit!** This is the first Platinum chapter — you have mastered Bronze, Silver, and Gold. Now we tackle the data structures and techniques that separate Gold from Platinum. Segment trees are arguably the single most important data structure in competitive programming at this level. If you learn ONE thing well from Part V, make it this chapter.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand the **range query with updates** problem and why prefix sums are not enough
- Know what a **segment tree** is: a balanced binary tree where each node stores the aggregate of a contiguous range
- Build a segment tree from an array in **O(n)** time
- Answer range queries (sum, min, max, XOR, GCD) in **O(log n)** time
- Perform point updates in **O(log n)** time
- Implement **lazy propagation** to handle **range updates** in O(log n)
- Understand the difference between point updates and range updates
- Know what a **Fenwick tree** (Binary Indexed Tree / BIT) is and implement it
- Choose the right tool: prefix sums vs BIT vs segment tree vs sqrt decomposition
- Apply coordinate compression for problems with large value ranges
- Solve classic competitive programming problems: range sum/min/max queries, count inversions, distinct values in range, maximum subarray in range
- Recognize segment tree patterns in **USACO Platinum** problems

---

## The Story: "The Stock Analyst"

Maya had just started her internship at a high-frequency trading firm. Her desk had six monitors, all flashing with real-time stock prices. Thousands of numbers, updating every millisecond.

Her boss, Tanya, walked over with a coffee in hand. "Maya, I need you to build a system. We track 500,000 stocks. Analysts keep asking questions like: *What was the highest price between stocks 100 and 500?* or *What is the total value of stocks 200 through 800?* And prices change constantly — hundreds of updates per second."

Maya thought about her prefix sums from Chapter 14. "I could precompute prefix sums and answer range queries in O(1)!"

Tanya shook her head. "That works if prices never change. But every update means you have to rebuild the entire prefix array — that is O(n) per update. With 500,000 stocks and thousands of updates per second, you would need *billions* of operations per second. Our servers would melt."

Maya thought harder. "What if I split the stocks into blocks of about 700 each? Then queries scan at most two partial blocks plus some full blocks..."

"That is sqrt decomposition," Tanya said, impressed. "It gives O(sqrt(n)) per operation. Better, but still not fast enough for our latency requirements."

"Is there something faster?"

Tanya smiled. "There is a data structure that gives you O(log n) for BOTH queries and updates. It is called a **segment tree**. Learn it, and you will never look at range queries the same way again."

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: The Slow Way

Given an array `[3, 1, 4, 1, 5, 9, 2, 6]`, find the sum of elements from index 2 to index 5 (inclusive).

That is `4 + 1 + 5 + 9 = 19`.

Now update index 3 to `7`. The array becomes `[3, 1, 4, 7, 5, 9, 2, 6]`. What is the new sum of indices 2 to 5?

That is `4 + 7 + 5 + 9 = 25`.

If you have Q queries (mix of sums and updates), the naive approach scans up to n elements per query. That is O(n * Q). With n = 500,000 and Q = 500,000, that is 250 billion operations. Way too slow.

{% hint style="info" %}
**Key insight**: We need a data structure that handles BOTH queries and updates faster than O(n) each.
{% endhint %}

### Puzzle 2: Precompute Everything?

Could you precompute ALL possible range sums and store them in a table? For an array of size n, there are O(n^2) possible ranges. So the table would need O(n^2) space and O(n^2) time to build.

For n = 500,000, that is 250 billion entries. Your computer does not have 250 billion cells of memory. This approach is dead on arrival.

{% hint style="info" %}
**Takeaway**: O(n^2) precomputation is too expensive in both time and space.
{% endhint %}

### Puzzle 3: Split Into Blocks

What if you split the array into blocks of size roughly sqrt(n)? For n = 9, split into blocks of 3:

```
Block 0: [3, 1, 4]  sum=8
Block 1: [1, 5, 9]  sum=15
Block 2: [2, 6, 0]  sum=8
```

To query sum(1, 7): scan partial Block 0 (index 1-2: 1+4=5), add full Block 1 (15), scan partial Block 2 (index 6-7: 2+6=8). Total = 5 + 15 + 8 = 28. You touched at most ~3*sqrt(n) elements.

To update index 4 to 10: change the element and update Block 1's sum. That is O(1).

Both operations are O(sqrt(n)). Much better than O(n)! But can we do even better?

{% hint style="info" %}
**Sqrt decomposition** gives O(sqrt(n)) per operation. A segment tree gives O(log n) — exponentially faster. For n = 500,000: sqrt(n) is about 707, but log2(n) is about 19. That is a 37x speedup!
{% endhint %}

---

## 30.1 The Problem — Range Queries with Updates

Let us be precise about what we need. We have an array `A` of `n` elements. We want to support two operations:

1. **Query(l, r)**: Compute some aggregate (sum, min, max, XOR, GCD, etc.) over `A[l..r]`
2. **Update(i, val)**: Set `A[i] = val` (or add `val` to `A[i]`)

Here is a comparison of approaches:

| Approach | Build | Query | Point Update | Range Update |
|----------|-------|-------|--------------|--------------|
| Naive (scan) | O(1) | O(n) | O(1) | O(n) |
| Prefix Sums | O(n) | O(1) | O(n) rebuild | O(n) rebuild |
| Sqrt Decomposition | O(n) | O(sqrt(n)) | O(1) | O(sqrt(n)) |
| **Segment Tree** | **O(n)** | **O(log n)** | **O(log n)** | **O(log n) with lazy** |
| **Fenwick Tree (BIT)** | **O(n)** | **O(log n)** | **O(log n)** | Special cases only |

Prefix sums are perfect when there are NO updates (Ch 14). But the moment you need to mix queries and updates, you need something better. That something is the **segment tree**.

---

## 30.2 Segment Tree — The Big Idea

A segment tree is a **binary tree** built on top of an array. Here is the key insight:

> **Each node in the segment tree stores the aggregate of a contiguous range of the original array.**

For an array of size 8, the segment tree looks like this:

```
                    [0..7] sum=32
                   /              \
            [0..3] sum=10        [4..7] sum=22
           /         \           /         \
      [0..1] sum=4  [2..3] sum=6  [4..5] sum=14  [6..7] sum=8
      /    \        /    \        /    \          /    \
   [0] 1  [1] 3  [2] 5  [3] 1  [4] 5  [5] 9   [6] 2  [7] 6
```

- The **leaves** store individual elements.
- Each **internal node** stores the aggregate (here, sum) of its children.
- The tree has **O(n) nodes** and height **O(log n)**.

### Why Does This Help?

To answer `sum(2, 5)`:
1. Start at the root [0..7]. The query range [2,5] partially overlaps, so go to both children.
2. Left child [0..3]: [2,5] partially overlaps [0,3]. Go to its children.
   - [0..1]: [2,5] does not overlap [0,1] at all. Return 0.
   - [2..3]: [2,5] fully contains [2,3]. Return 6.
3. Right child [4..7]: [2,5] partially overlaps [4,7]. Go to its children.
   - [4..5]: [2,5] fully contains [4,5]. Return 14.
   - [6..7]: [2,5] does not overlap [6,7]. Return 0.
4. Total: 0 + 6 + 14 + 0 = 20.

At each level of the tree, we visit at most **2 nodes** (one on the left boundary, one on the right boundary). Since the tree has O(log n) levels, the total work is **O(log n)**.

### Array Representation

Just like a heap (Ch 17), we store the segment tree in a flat array. For a node at index `i`:
- Left child: `2*i`
- Right child: `2*i + 1`
- Parent: `i // 2`

We use **1-based indexing** for the tree (root at index 1). The array needs size **4*n** to be safe.

{% hint style="warning" %}
**Why 4*n and not 2*n?** A segment tree for n elements has at most 2*n - 1 nodes when n is a power of 2. But when n is NOT a power of 2, the tree can have up to 4*n nodes due to the way recursive splitting works. Always allocate 4*n to be safe.
{% endhint %}

---

## 30.3 Building, Querying, and Updating

### Build — O(n)

We build the tree bottom-up. Start at the leaves, then compute each parent as the aggregate of its children.

{% tabs %}
{% tab title="Python" %}
```python
def build(tree, arr, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(tree, arr, 2 * node, start, mid)
        build(tree, arr, 2 * node + 1, mid + 1, end)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

n = len(arr)
tree = [0] * (4 * n)
build(tree, arr, 1, 0, n - 1)
```
{% endtab %}
{% tab title="Java" %}
```java
void build(int[] tree, int[] arr, int node, int start, int end) {
    if (start == end) {
        tree[node] = arr[start];
    } else {
        int mid = (start + end) / 2;
        build(tree, arr, 2 * node, start, mid);
        build(tree, arr, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}

int[] tree = new int[4 * n];
build(tree, arr, 1, 0, n - 1);
```
{% endtab %}
{% tab title="C++" %}
```cpp
void build(vector<int>& tree, vector<int>& arr, int node, int start, int end) {
    if (start == end) {
        tree[node] = arr[start];
    } else {
        int mid = (start + end) / 2;
        build(tree, arr, 2 * node, start, mid);
        build(tree, arr, 2 * node + 1, mid + 1, end);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}

vector<int> tree(4 * n);
build(tree, arr, 1, 0, n - 1);
```
{% endtab %}
{% endtabs %}

### Query — O(log n)

Three cases at each node:
1. **No overlap**: Query range does not intersect node range. Return identity (0 for sum, INF for min, -INF for max).
2. **Total overlap**: Query range fully contains node range. Return node's stored value.
3. **Partial overlap**: Recurse into both children and combine.

{% tabs %}
{% tab title="Python" %}
```python
def query(tree, node, start, end, l, r):
    if r < start or end < l:       # no overlap
        return 0
    if l <= start and end <= r:     # total overlap
        return tree[node]
    mid = (start + end) // 2        # partial overlap
    left_sum = query(tree, 2 * node, start, mid, l, r)
    right_sum = query(tree, 2 * node + 1, mid + 1, end, l, r)
    return left_sum + right_sum
```
{% endtab %}
{% tab title="Java" %}
```java
int query(int[] tree, int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;           // no overlap
    if (l <= start && end <= r) return tree[node]; // total overlap
    int mid = (start + end) / 2;                   // partial
    return query(tree, 2 * node, start, mid, l, r)
         + query(tree, 2 * node + 1, mid + 1, end, l, r);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int query(vector<int>& tree, int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;           // no overlap
    if (l <= start && end <= r) return tree[node]; // total overlap
    int mid = (start + end) / 2;                   // partial
    return query(tree, 2 * node, start, mid, l, r)
         + query(tree, 2 * node + 1, mid + 1, end, l, r);
}
```
{% endtab %}
{% endtabs %}

### Point Update — O(log n)

Update a single element and propagate changes up to the root.

{% tabs %}
{% tab title="Python" %}
```python
def update(tree, node, start, end, idx, val):
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(tree, 2 * node, start, mid, idx, val)
        else:
            update(tree, 2 * node + 1, mid + 1, end, idx, val)
        tree[node] = tree[2 * node] + tree[2 * node + 1]
```
{% endtab %}
{% tab title="Java" %}
```java
void update(int[] tree, int node, int start, int end, int idx, int val) {
    if (start == end) {
        tree[node] = val;
    } else {
        int mid = (start + end) / 2;
        if (idx <= mid) update(tree, 2 * node, start, mid, idx, val);
        else update(tree, 2 * node + 1, mid + 1, end, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
void update(vector<int>& tree, int node, int start, int end, int idx, int val) {
    if (start == end) {
        tree[node] = val;
    } else {
        int mid = (start + end) / 2;
        if (idx <= mid) update(tree, 2 * node, start, mid, idx, val);
        else update(tree, 2 * node + 1, mid + 1, end, idx, val);
        tree[node] = tree[2 * node] + tree[2 * node + 1];
    }
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Pattern**: Build is O(n) because each of the O(n) nodes is visited once. Query and update are O(log n) because they follow a single path from root to leaf (with at most one branch at each level).
{% endhint %}

---

## 30.4 Lazy Propagation — Range Updates in O(log n)

So far we can handle **point updates** (change one element). But what if we need to **update an entire range**? For example: "Add 5 to all elements from index 2 to index 7."

Without lazy propagation, a range update would require O(n) point updates. With lazy propagation, we can do it in **O(log n)**.

### The Idea: Procrastination That Works

When we update a range, we do NOT immediately update every leaf. Instead, we **mark the node** with a "lazy" value that says: "When you visit my children, do not forget to apply this update."

This is like a teacher putting a sticky note on a folder: "Add 5 to all grades inside." The teacher does not open the folder and change every grade right away — they only do it when someone actually needs to look at a specific grade.

### Implementation

Each node gets an extra `lazy` array. When we need to access a node's children, we first **push down** the lazy value.

{% tabs %}
{% tab title="Python" %}
```python
def push_down(tree, lazy, node):
    if lazy[node] != 0:
        for child in [2 * node, 2 * node + 1]:
            tree[child] += lazy[node]  # for sum: multiply by range size
            lazy[child] += lazy[node]
        lazy[node] = 0

def range_update(tree, lazy, node, start, end, l, r, val):
    if r < start or end < l:
        return
    if l <= start and end <= r:
        tree[node] += val * (end - start + 1)
        lazy[node] += val
        return
    push_down(tree, lazy, node)
    mid = (start + end) // 2
    range_update(tree, lazy, 2 * node, start, mid, l, r, val)
    range_update(tree, lazy, 2 * node + 1, mid + 1, end, l, r, val)
    tree[node] = tree[2 * node] + tree[2 * node + 1]

def range_query(tree, lazy, node, start, end, l, r):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    push_down(tree, lazy, node)
    mid = (start + end) // 2
    return (range_query(tree, lazy, 2 * node, start, mid, l, r)
          + range_query(tree, lazy, 2 * node + 1, mid + 1, end, l, r))
```
{% endtab %}
{% tab title="Java" %}
```java
void pushDown(long[] tree, long[] lazy, int node, int start, int end) {
    if (lazy[node] != 0) {
        int mid = (start + end) / 2;
        tree[2 * node] += lazy[node] * (mid - start + 1);
        tree[2 * node + 1] += lazy[node] * (end - mid);
        lazy[2 * node] += lazy[node];
        lazy[2 * node + 1] += lazy[node];
        lazy[node] = 0;
    }
}

void rangeUpdate(long[] tree, long[] lazy, int node, int start, int end,
                 int l, int r, long val) {
    if (r < start || end < l) return;
    if (l <= start && end <= r) {
        tree[node] += val * (end - start + 1);
        lazy[node] += val;
        return;
    }
    pushDown(tree, lazy, node, start, end);
    int mid = (start + end) / 2;
    rangeUpdate(tree, lazy, 2 * node, start, mid, l, r, val);
    rangeUpdate(tree, lazy, 2 * node + 1, mid + 1, end, l, r, val);
    tree[node] = tree[2 * node] + tree[2 * node + 1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
void pushDown(vector<long long>& tree, vector<long long>& lazy,
              int node, int start, int end) {
    if (lazy[node] != 0) {
        int mid = (start + end) / 2;
        tree[2 * node] += lazy[node] * (mid - start + 1);
        tree[2 * node + 1] += lazy[node] * (end - mid);
        lazy[2 * node] += lazy[node];
        lazy[2 * node + 1] += lazy[node];
        lazy[node] = 0;
    }
}

void rangeUpdate(vector<long long>& tree, vector<long long>& lazy,
                 int node, int start, int end, int l, int r, long long val) {
    if (r < start || end < l) return;
    if (l <= start && end <= r) {
        tree[node] += val * (end - start + 1);
        lazy[node] += val;
        return;
    }
    pushDown(tree, lazy, node, start, end);
    int mid = (start + end) / 2;
    rangeUpdate(tree, lazy, 2 * node, start, mid, l, r, val);
    rangeUpdate(tree, lazy, 2 * node + 1, mid + 1, end, l, r, val);
    tree[node] = tree[2 * node] + tree[2 * node + 1];
}
```
{% endtab %}
{% endtabs %}

{% hint style="danger" %}
**Critical Rule**: You MUST push down lazy values before accessing children. Forgetting this is the #1 bug in lazy segment tree implementations. If you query a child without pushing down, you will get stale (wrong) data.
{% endhint %}

---

## 30.5 Fenwick Tree (Binary Indexed Tree)

A Fenwick tree (also called a Binary Indexed Tree or BIT) is a simpler alternative to a segment tree for certain problems. It was invented by Peter Fenwick in 1994.

### When to Use Fenwick Tree

Fenwick trees work for **invertible operations** — operations where you can "undo" one value to get another. For example:
- **Sum**: `sum(l, r) = prefix(r) - prefix(l-1)` — subtraction undoes addition
- **XOR**: `xor(l, r) = prefix(r) ^ prefix(l-1)` — XOR undoes itself

Fenwick trees do NOT work for:
- **Min/Max**: You cannot recover `min(l, r)` from `min(0, r)` and `min(0, l-1)` — knowing the minimum of a larger range does not tell you the minimum of a subrange.

### The Clever Bit Trick

The Fenwick tree uses 1-based indexing. Each index `i` is responsible for a range of elements determined by the **lowest set bit** of `i`.

The lowest set bit of `i` is `i & (-i)`. For example:
- `i = 6` (binary `110`): lowest set bit is `2` (binary `10`), so index 6 stores the sum of 2 elements (indices 5-6).
- `i = 8` (binary `1000`): lowest set bit is `8`, so index 8 stores the sum of 8 elements (indices 1-8).

### Implementation

{% tabs %}
{% tab title="Python" %}
```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        """Add delta to index i (1-indexed)."""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # move to next responsible index

    def prefix_sum(self, i):
        """Sum of elements from index 1 to i."""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # move to parent
        return total

    def range_sum(self, l, r):
        """Sum of elements from index l to r (1-indexed)."""
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
```
{% endtab %}
{% tab title="Java" %}
```java
class FenwickTree {
    int[] tree;
    int n;

    FenwickTree(int n) {
        this.n = n;
        tree = new int[n + 1]; // 1-indexed
    }

    void update(int i, int delta) {
        for (; i <= n; i += i & (-i))
            tree[i] += delta;
    }

    int prefixSum(int i) {
        int sum = 0;
        for (; i > 0; i -= i & (-i))
            sum += tree[i];
        return sum;
    }

    int rangeSum(int l, int r) {
        return prefixSum(r) - prefixSum(l - 1);
    }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
struct FenwickTree {
    vector<int> tree;
    int n;

    FenwickTree(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, int delta) {
        for (; i <= n; i += i & (-i))
            tree[i] += delta;
    }

    int prefixSum(int i) {
        int sum = 0;
        for (; i > 0; i -= i & (-i))
            sum += tree[i];
        return sum;
    }

    int rangeSum(int l, int r) {
        return prefixSum(r) - prefixSum(l - 1);
    }
};
```
{% endtab %}
{% endtabs %}

### Fenwick Tree vs Segment Tree

| Feature | Fenwick Tree (BIT) | Segment Tree |
|---------|-------------------|--------------|
| Code length | ~15 lines | ~50 lines |
| Operations | Invertible only (sum, XOR) | ANY associative (min, max, GCD, sum) |
| Point update | O(log n) | O(log n) |
| Range query | O(log n) | O(log n) |
| Range update | With tricks | With lazy propagation |
| Constant factor | Smaller | Larger |
| Memory | n + 1 | 4 * n |

{% hint style="info" %}
**Rule of thumb**: If the problem only needs prefix sums with point updates, use a Fenwick tree — it is shorter, faster, and easier to debug. For everything else (min/max, range updates, complex merges), use a segment tree.
{% endhint %}

---

## 30.6 When to Use What — Decision Table

When you see a range query problem, use this decision tree:

1. **No updates at all?** -> Prefix sums (Ch 14). O(1) per query after O(n) build.
2. **Point updates + prefix/range sum or XOR?** -> Fenwick tree (BIT). Shortest code, fastest constant.
3. **Point updates + min/max/GCD?** -> Segment tree (no lazy needed).
4. **Range updates + range queries?** -> Segment tree with lazy propagation.
5. **Need something quick and dirty in a contest?** -> Sqrt decomposition. Easy to code, O(sqrt(n)) per op.

| Problem Type | Best Tool | Time per Op |
|-------------|-----------|-------------|
| Static range sum | Prefix sums | O(1) query |
| Point update + range sum | BIT | O(log n) |
| Point update + range min | Segment tree | O(log n) |
| Range add + range sum | Lazy segment tree | O(log n) |
| Range set + range sum | Lazy segment tree | O(log n) |
| Count inversions | BIT | O(n log n) |
| Distinct in range | Offline + BIT | O((n + Q) log n) |
| Max subarray in range | Segment tree (4 values/node) | O(log n) |

---

## 30.7 USACO Platinum Applications

Segment trees appear in USACO Platinum problems frequently. Here are typical patterns:

### Pattern 1: Range Update + Range Query
Many Platinum problems reduce to: "perform range updates and answer range queries." This is the direct application of lazy segment tree.

### Pattern 2: Coordinate Compression + BIT
When values are large (up to 10^9) but the number of distinct values is small (up to 10^5), compress values to a smaller range and use a BIT. This is common in "count inversions" and "count of elements in range" problems.

### Pattern 3: Sweep Line + Segment Tree
Sweep across events (sorted by one coordinate) and use a segment tree to maintain information about the other coordinate. Common in geometry and scheduling problems.

### Pattern 4: Offline Processing
Some problems become easier if you sort queries by right endpoint. Process elements left to right, maintaining a BIT/segment tree, and answer queries when you reach their right endpoint. The "distinct values in range" problem uses this technique.

### Pattern 5: DP Optimization
Some DP transitions can be written as `dp[i] = min(dp[j] + cost(j, i))` for j in some range. A segment tree can answer "min of dp[j] for j in [l, r]" in O(log n), turning an O(n^2) DP into O(n log n). You will see this in Chapter 31.

---

## Five-Lens Framework: "Range Sum with Updates"

Let us apply the Five-Lens Framework to the core problem of this chapter.

### Lens 1: Constraints
- Array size n up to 10^5 or 10^6
- Number of queries Q up to 10^5 or 10^6
- Mix of update and query operations
- Need total time O((n + Q) log n) or better

### Lens 2: Brute Force
For each query, scan the range. O(n) per query, O(nQ) total. With n = Q = 10^5, that is 10^10 operations — about 100 seconds. Too slow (most judges allow 1-2 seconds).

### Lens 3: Pattern
The array can be divided recursively into halves. Each half can be divided into halves again. This creates a balanced binary tree of ranges. If we store the sum of each range, we can combine them.

### Lens 4: Optimization
- Build the segment tree: O(n)
- Each query: follow at most O(log n) nodes
- Each update: update at most O(log n) nodes on the path from leaf to root
- Total: O(n + Q log n)

### Lens 5: Proof
**Why is each query O(log n)?** At each level of the tree, we visit at most 2 "boundary" nodes (one on the left edge of the query range, one on the right edge). All nodes in between are either fully contained (return immediately) or not overlapping (return immediately). The tree has O(log n) levels, so we visit at most O(2 log n) = O(log n) nodes total.

---

## Think Like a Pro

{% hint style="info" %}
**Benjamin Qi (Benq)** — USACO Platinum, IOI Gold medalist:

"When I see range queries with point updates, I immediately reach for BIT because it is shorter to code. When I need range updates or non-invertible operations (like min/max), I switch to segment tree with lazy propagation. The decision takes 10 seconds but saves 10 minutes of debugging. In a contest, the fastest correct solution wins — and BIT is almost always faster to implement correctly than segment tree."
{% endhint %}

---

## AOPS Showcase: "Range Sum with Updates" — Four Solutions

Let us solve the same problem four different ways, each one faster than the last. The problem: given an array, handle point updates (set A[i] = val) and range sum queries (sum of A[l..r]).

### Solution 1: Brute Force — O(n) per query

{% tabs %}
{% tab title="Python" %}
```python
def solve_brute(arr, queries):
    results = []
    for q in queries:
        if q[0] == 1:  # sum query
            results.append(sum(arr[q[1]:q[2]+1]))
        else:           # update
            arr[q[1]] = q[2]
    return results
```
{% endtab %}
{% tab title="Java" %}
```java
static List<Integer> solveBrute(int[] arr, int[][] queries) {
    List<Integer> results = new ArrayList<>();
    for (int[] q : queries) {
        if (q[0] == 1) {
            int s = 0;
            for (int i = q[1]; i <= q[2]; i++) s += arr[i];
            results.add(s);
        } else {
            arr[q[1]] = q[2];
        }
    }
    return results;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<int> solveBrute(vector<int>& arr, vector<vector<int>>& queries) {
    vector<int> results;
    for (auto& q : queries) {
        if (q[0] == 1) {
            int s = 0;
            for (int i = q[1]; i <= q[2]; i++) s += arr[i];
            results.push_back(s);
        } else {
            arr[q[1]] = q[2];
        }
    }
    return results;
}
```
{% endtab %}
{% endtabs %}

**Time**: O(n) per query, O(nQ) total. Works for small inputs but too slow for n, Q > 10^4.

### Solution 2: Sqrt Decomposition — O(sqrt(n)) per operation

{% tabs %}
{% tab title="Python" %}
```python
import math

def solve_sqrt(arr, queries):
    n = len(arr)
    block = int(math.sqrt(n)) + 1
    blocks = [0] * (n // block + 1)
    for i, v in enumerate(arr):
        blocks[i // block] += v

    results = []
    for q in queries:
        if q[0] == 1:  # sum query
            l, r = q[1], q[2]
            s = 0
            while l <= r:
                if l % block == 0 and l + block - 1 <= r:
                    s += blocks[l // block]
                    l += block
                else:
                    s += arr[l]
                    l += 1
            results.append(s)
        else:           # update
            i, val = q[1], q[2]
            blocks[i // block] += val - arr[i]
            arr[i] = val
    return results
```
{% endtab %}
{% tab title="Java" %}
```java
// Sqrt decomposition: O(sqrt(n)) per operation
// (Full implementation similar to Python — block-based approach)
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Sqrt decomposition: O(sqrt(n)) per operation
// (Full implementation similar to Python — block-based approach)
```
{% endtab %}
{% endtabs %}

**Time**: O(sqrt(n)) per operation. Good enough for n, Q up to 10^5, but not for 10^6.

### Solution 3: Segment Tree — O(log n) per operation

{% tabs %}
{% tab title="Python" %}
```python
def solve_segtree(arr, queries):
    n = len(arr)
    tree = [0] * (4 * n)

    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        return (query(2 * node, start, mid, l, r) +
                query(2 * node + 1, mid + 1, end, l, r))

    build(1, 0, n - 1)
    results = []
    for q in queries:
        if q[0] == 1:
            results.append(query(1, 0, n - 1, q[1], q[2]))
        else:
            update(1, 0, n - 1, q[1], q[2])
    return results
```
{% endtab %}
{% tab title="Java" %}
```java
// Segment tree: O(log n) per operation
// (Same recursive build/query/update as Python)
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Segment tree: O(log n) per operation
// (Same recursive build/query/update as Python)
```
{% endtab %}
{% endtabs %}

**Time**: O(n + Q log n). Handles n, Q up to 10^6 easily.

### Solution 4: Fenwick Tree — O(log n), simpler code

{% tabs %}
{% tab title="Python" %}
```python
def solve_bit(arr, queries):
    n = len(arr)
    bit = [0] * (n + 1)

    def update(i, delta):
        i += 1  # convert to 1-indexed
        while i <= n:
            bit[i] += delta
            i += i & (-i)

    def prefix(i):
        i += 1  # convert to 1-indexed
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    # Build: add each element
    for i, v in enumerate(arr):
        update(i, v)

    results = []
    for q in queries:
        if q[0] == 1:  # sum(l, r)
            l, r = q[1], q[2]
            s = prefix(r) - (prefix(l - 1) if l > 0 else 0)
            results.append(s)
        else:  # set arr[idx] = val
            idx, val = q[1], q[2]
            update(idx, val - arr[idx])
            arr[idx] = val
    return results
```
{% endtab %}
{% tab title="Java" %}
```java
// Fenwick tree: O(log n), shorter code for sum queries
// (Same bit-manipulation approach as Python)
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Fenwick tree: O(log n), shorter code for sum queries
// (Same bit-manipulation approach as Python)
```
{% endtab %}
{% endtabs %}

**Time**: O(n log n + Q log n). Same asymptotic as segment tree but with a smaller constant factor and half the code.

### Language Spotlight: Segment Tree Implementation

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Array declaration | `[0] * (4 * n)` | `new int[4 * n]` | `vector<int>(4 * n)` |
| Integer size | Unlimited | `int` (32-bit), `long` (64-bit) | `int`, `long long` |
| Recursion limit | Default 1000 (increase with `sys.setrecursionlimit`) | No practical limit | No practical limit |
| Bit trick for BIT | `i & (-i)` | `i & (-i)` | `i & (-i)` |
| Speed for n=10^6 | May TLE in USACO | OK | Fastest |

{% hint style="warning" %}
**Python recursion limit**: Segment trees for n = 10^6 can recurse ~20 levels deep, which is fine. But Python's default recursion limit is 1000. For safety, add `sys.setrecursionlimit(300000)` at the top of your solution. Or use an iterative segment tree.
{% endhint %}

---

## Legend's Corner

{% hint style="info" %}
**Petr Mitrichev** — Two-time IOI Gold, Google Code Jam champion, one of the greatest competitive programmers ever:

"I have used segment trees in probably half of all competitive programming problems I have solved. They are like a Swiss Army knife — once you learn them, you see applications everywhere. The key insight is that segment trees do not just work for sum — they work for ANY associative operation. Min, max, GCD, XOR, matrix multiplication, you name it. Once I understood that, my problem-solving toolkit expanded enormously."
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**1. Off-by-one in segment tree indexing.** The most common bug. Decide on 0-indexed or 1-indexed and be consistent. The tree array is 1-indexed (root at index 1), but the original array can be 0-indexed. Always be clear about whether ranges are inclusive or exclusive.
{% endhint %}

{% hint style="danger" %}
**2. Forgetting to push down lazy values.** This is the #1 bug with lazy propagation. Before you access a node's children (for either query or update), you MUST push down the lazy value first. If you forget, you will read stale data and get wrong answers that are incredibly hard to debug.
{% endhint %}

{% hint style="warning" %}
**3. Using segment tree when BIT would suffice.** If you only need point updates and prefix sums, a BIT is shorter, faster, and less error-prone. Do not over-engineer. Use the simplest tool that solves the problem.
{% endhint %}

{% hint style="danger" %}
**4. Tree array too small.** Always allocate `4 * n` for the segment tree array, not `2 * n`. When n is not a power of 2, a tree of size `2 * n` can have out-of-bounds access. The `4 * n` bound guarantees safety.
{% endhint %}

{% hint style="warning" %}
**5. Integer overflow in sum queries.** If array elements are up to 10^9 and you are summing up to 10^5 of them, the result can be up to 10^{14} — which overflows a 32-bit integer. Use `long` in Java, `long long` in C++, or Python's arbitrary precision.
{% endhint %}

{% hint style="warning" %}
**6. Confusing point update with range update.** Point update changes ONE element; range update changes ALL elements in a range. They have completely different implementations. A range update without lazy propagation is O(n) — no better than brute force. Always use lazy propagation for range updates.
{% endhint %}

---

## Practice Problems

### Warmup (Straightforward application)

| # | Name | Difficulty | Topic | Hint |
|---|------|-----------|-------|------|
| W1 | Range Sum Query | Easy | Segment tree basics | Build, query sum, point update |
| W2 | Range Min Query | Easy | Segment tree with min | Change `+` to `min`, identity is `INF` |
| W3 | Prefix Sum with BIT | Easy | Fenwick tree | 1-indexed, `i & (-i)` trick |
| W4 | Count Inversions | Medium | BIT + coordinate compression | Process right-to-left, count elements already inserted that are smaller |

### Practice (Apply the concept)

| # | Name | Difficulty | Topic | Hint |
|---|------|-----------|-------|------|
| P1 | Range Sum with Range Update | Medium | Lazy propagation (add) | Each node stores sum; lazy stores pending add |
| P2 | Range Max with Point Update | Medium | Segment tree max | Change `+` to `max`, identity is `-INF` |
| P3 | Count Elements in Range | Medium | Merge sort tree / Offline | Sort elements in each node's range, binary search |
| P4 | Kth Order Statistics | Hard | Segment tree on values | Frequency tree: walk left/right based on counts |
| P5 | XOR on Range | Medium | Segment tree XOR | XOR is associative, identity is 0 |

### Challenge (Contest-level)

| # | Name | Difficulty | Topic | Hint |
|---|------|-----------|-------|------|
| C1 | Range Update Range Query (Set) | Hard | Lazy propagation (set) | Lazy stores "set all to val"; push replaces children |
| C2 | Distinct Values in Range | Hard | Offline + BIT | Sort queries by r; for each val, track last occurrence |
| C3 | Max Subarray Sum in Range | Hard | Segment tree (4 values) | Each node: total, prefix_max, suffix_max, best |
| C4 | Interval Scheduling | Medium | Greedy + sorting | Sort by end time, greedily pick non-overlapping |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
**Python Segment Tree Tips:**
- Use `sys.setrecursionlimit(300000)` for deep recursion
- Python's unlimited integers mean no overflow worries for sums
- For maximum speed, consider iterative segment tree (bottom-up)
- `float('inf')` for min-query identity, `float('-inf')` for max-query identity
- BIT is often fast enough in Python even for tight time limits
{% endtab %}
{% tab title="Java" %}
**Java Segment Tree Tips:**
- Use `long[]` instead of `int[]` when sums can exceed 2^31
- `Integer.MAX_VALUE` for min-query identity, `Integer.MIN_VALUE` for max-query identity
- Java's recursion stack is large enough for segment trees (no limit issues)
- Arrays are faster than ArrayLists for the tree — always use `int[]` or `long[]`
- `Arrays.fill(lazy, 0)` to reset lazy array
{% endtab %}
{% tab title="C++" %}
**C++ Segment Tree Tips:**
- Use `long long` when sums can overflow `int`
- `INT_MAX` for min-query identity, `INT_MIN` for max-query identity (include `<climits>`)
- `vector<int>(4 * n, 0)` is the standard tree declaration
- `function<int(int)>` lambdas work but are slower than regular functions — in contests, use global arrays and plain functions
- For maximum speed, use iterative segment tree with bottom-up updates
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 14 (Prefix Sums)**: Prefix sums answer range queries in O(1) but break when updates happen. Segment trees fix this.
- **Ch 17 (Heaps)**: Heaps store data in an array-backed binary tree — segment trees use the same array layout (node i, children 2i and 2i+1).
- **Ch 26 (Trees)**: A segment tree IS a binary tree. The tree concepts you learned (height, leaves, traversal) apply directly.
- **Ch 12 (Bit Manipulation)**: Fenwick trees use `i & (-i)` — the lowest set bit trick you learned in Ch 12.

### Looking Forward
- **Ch 31 (Advanced DP)**: Segment trees can optimize DP transitions from O(n^2) to O(n log n) by answering "min/max of dp[j] for j in range" queries.
- **Ch 33 (Advanced Trees)**: Euler tour + segment tree = subtree queries in O(log n). Heavy-light decomposition + segment tree = path queries in O(log^2 n).

### Cross-Chapter Threads
- **Space-for-time**: We use O(n) extra space (the tree array) to answer queries in O(log n) instead of O(n). This is the same space-for-time tradeoff we have seen throughout the book.
- **Divide and conquer**: The segment tree recursively divides the array in half — the same divide-and-conquer pattern from merge sort (Ch 8).

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

- **"What if the array is 2D?"** You can build a 2D segment tree — a segment tree where each node contains another segment tree. This handles 2D range queries in O(log^2 n) per operation. Used in some advanced geometry and grid problems.

- **"Can you make a persistent segment tree that remembers all versions?"** Yes! Instead of modifying nodes in place, you create new nodes for each update and share unchanged subtrees. This uses O(n log n) total memory and answers "what was the kth element at version t?" in O(log n). This is used in offline query problems and functional programming.

- **"What problems can segment trees solve that Fenwick trees cannot?"** Range min/max queries, maximum subarray in range, and any non-invertible operation. Also, segment tree with lazy propagation handles range updates, which Fenwick trees cannot do directly (only with advanced tricks).

---

## What's Next

You have just learned the most important data structure for USACO Platinum: the segment tree. Combined with what you know about DP, graphs, and trees, you are now equipped for a huge portion of competitive programming problems.

In **Chapter 31: Advanced DP — Bitmask, Interval, Trees**, we will push dynamic programming to its limits. What if the "state" of your DP is not just a number, but a bitmask representing which elements have been used? What if the transition between states can be optimized using segment trees? Bitmask DP, interval DP, and tree DP await — and they are the techniques that distinguish Gold from Platinum.
