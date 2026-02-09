# Trees — Branches of Logic

{% hint style="info" %}
**Trees are everywhere in computer science.** File systems, HTML documents, database indices, game AI decision trees, compiler parse trees -- they all use tree structures. This chapter covers binary trees and Binary Search Trees (BSTs), the two most important tree types. You will learn traversals, classic tree problems, and BST operations that appear constantly in USACO Gold, coding interviews, and competitive programming. If you master trees, you will have a powerful mental model for thinking about hierarchical and recursive problems.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand binary tree terminology: root, leaf, height, depth, parent, child, subtree
- Implement three classic traversals: inorder, preorder, postorder (both recursive and iterative)
- Implement level-order traversal using BFS with a queue
- Compute height, diameter, and check if a tree is balanced
- Find the maximum path sum in a binary tree
- Compute different views of a tree: right side view, boundary traversal
- Find the Lowest Common Ancestor (LCA) of two nodes using three different approaches
- Understand Binary Search Trees: search, insert, delete, validate, kth element
- Construct a binary tree from its preorder and inorder traversals
- Serialize and deserialize a binary tree to/from a string
- Flatten a binary tree into a linked list following preorder order
- Solve the Binary Tree Cameras problem using greedy DFS
- Recognize when to use DFS vs BFS on tree problems
- Apply the Five-Lens Framework to tree problems

---

## The Story: "The Family Tree"

Maya was visiting her grandmother for the summer when she found an old, hand-drawn chart tucked inside a dusty photo album. It was her family tree -- names connected by lines, spreading out from her great-great-grandparents at the top.

"That is our family," her grandmother said, pointing to the top. "Your great-great-grandmother Elara is the **root**. She started it all."

Maya traced the lines downward. Elara had two children: Marcus and Lila. Marcus had three children, but Lila had only one. Some branches went deep -- five generations -- while others stopped after just two.

"Why do some branches end so quickly?" Maya asked.

"Some people never married, some moved far away and we lost touch," her grandmother said. "Those are the **leaves** -- the end of a branch."

Maya had a question: "If I wanted to find the youngest person who is an ancestor of BOTH me and cousin Theo, how would I do it?"

Her grandmother smiled. "You would trace upward from both of you until your paths meet. That meeting point is what we call the **lowest common ancestor**."

That evening, Maya sat down with her notebook and started drawing the tree more carefully. She realized that searching a family tree was a lot like searching a data structure. Every person was a **node**. Every parent-child connection was an **edge**. And the questions she wanted to answer -- "How many generations deep is the tree?" "Who can I see from the right side?" "What is the longest path between any two people?" -- were all algorithms waiting to be discovered.

She had found the branches of logic.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand. Grab a pencil and paper!

### Puzzle 1: "Trace the Path"

Here is a binary tree drawn out:

```
        1
       / \
      2   3
     / \
    4   5
```

Without looking anything up, try to list the nodes in these three orders:
1. Visit the left subtree completely, then the current node, then the right subtree (for every node)
2. Visit the current node first, then left subtree, then right subtree
3. Visit left subtree, then right subtree, then the current node last

{% hint style="info" %}
These are inorder, preorder, and postorder traversals. For tree (1): inorder = [4,2,5,1,3], preorder = [1,2,4,5,3], postorder = [4,5,2,3,1]. Notice that inorder puts the root "in the middle" of its children, preorder puts it "before," and postorder puts it "after."
{% endhint %}

### Puzzle 2: "The Common Ancestor"

Given this family tree (binary tree):

```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```

Who is the lowest common ancestor (youngest common ancestor) of:
- Nodes 5 and 1?
- Nodes 5 and 4?
- Nodes 7 and 8?

{% hint style="info" %}
LCA(5,1) = 3 (the root, because 5 is on the left and 1 is on the right). LCA(5,4) = 5 (because 4 is a descendant of 5, so 5 itself is the LCA). LCA(7,8) = 3 (they are in different subtrees of the root). The key insight: if p and q are in different subtrees, the LCA is the current node.
{% endhint %}

### Puzzle 3: "Is This a BST?"

A Binary Search Tree has this rule: for every node, ALL values in its left subtree are smaller, and ALL values in its right subtree are larger.

Which of these trees are valid BSTs?

```
Tree A:       Tree B:       Tree C:
    2             5             5
   / \           / \           / \
  1   3         1   4         1   6
                   / \           /
                  3   6         4
```

{% hint style="info" %}
Tree A: Valid BST (1 < 2 < 3). Tree B: INVALID -- 4 is in the right subtree of 5, but 4 < 5. Also, 3 is in the right subtree of 5 but 3 < 5. Tree C: Valid BST -- every node satisfies the constraint when you check the FULL range, not just the parent. The common mistake is only checking the immediate parent.
{% endhint %}

---

## 26.1 Binary Trees: Representation and Terminology

A **binary tree** is a tree where each node has at most two children, called **left** and **right**.

### Key Terminology

| Term | Definition |
|------|-----------|
| **Root** | The topmost node (has no parent) |
| **Leaf** | A node with no children |
| **Parent** | The node directly above |
| **Child** | A node directly below (left child, right child) |
| **Subtree** | A node and all its descendants |
| **Height** | The number of nodes on the longest root-to-leaf path |
| **Depth** | The number of edges from the root to a node |
| **Level** | All nodes at the same depth |

### Tree Node Representation

{% tabs %}
{% tab title="Python" %}
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
{% endtab %}
{% tab title="Java" %}
```java
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};
```
{% endtab %}
{% endtabs %}

### Building a Tree from a Level-Order List

Throughout this chapter, we use a `build_tree` function that takes a list like `[1, 2, 3, None, None, 4, 5]` and constructs the corresponding tree using BFS:

{% tabs %}
{% tab title="Python" %}
```python
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
```
{% endtab %}
{% tab title="Java" %}
```java
static TreeNode buildTree(Integer[] values) {
    if (values == null || values.length == 0 || values[0] == null) return null;
    TreeNode root = new TreeNode(values[0]);
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    int i = 1;
    while (!queue.isEmpty() && i < values.length) {
        TreeNode node = queue.poll();
        if (i < values.length && values[i] != null) {
            node.left = new TreeNode(values[i]);
            queue.add(node.left);
        }
        i++;
        if (i < values.length && values[i] != null) {
            node.right = new TreeNode(values[i]);
            queue.add(node.right);
        }
        i++;
    }
    return root;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Using INT_MIN as null sentinel
TreeNode* buildTree(vector<int> values, int null_val = INT_MIN) {
    if (values.empty() || values[0] == null_val) return nullptr;
    TreeNode* root = new TreeNode(values[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)values.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)values.size() && values[i] != null_val) {
            node->left = new TreeNode(values[i]);
            q.push(node->left);
        }
        i++;
        if (i < (int)values.size() && values[i] != null_val) {
            node->right = new TreeNode(values[i]);
            q.push(node->right);
        }
        i++;
    }
    return root;
}
```
{% endtab %}
{% endtabs %}

---

## 26.2 Traversals

Traversals are the foundation of all tree algorithms. There are four essential ones.

### Recursive Traversals: Inorder, Preorder, Postorder

{% tabs %}
{% tab title="Python" %}
```python
def inorder(root):       # Left -> Root -> Right
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):      # Root -> Left -> Right
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):     # Left -> Right -> Root
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```
{% endtab %}
{% tab title="Java" %}
```java
void inorder(TreeNode node, List<Integer> res) {
    if (node == null) return;
    inorder(node.left, res);
    res.add(node.val);
    inorder(node.right, res);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
void inorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    inorder(node->left, res);
    res.push_back(node->val);
    inorder(node->right, res);
}
```
{% endtab %}
{% endtabs %}

**Key insight:** Inorder traversal of a BST gives elements in sorted order. This is extremely useful!

### Level-Order Traversal (BFS)

Process nodes level by level, left to right. Use a queue.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque

def level_order(root):
    if not root: return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result
```
{% endtab %}
{% tab title="Java" %}
```java
List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> result = new ArrayList<>();
    if (root == null) return result;
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    while (!q.isEmpty()) {
        int size = q.size();
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = q.poll();
            level.add(node.val);
            if (node.left != null)  q.add(node.left);
            if (node.right != null) q.add(node.right);
        }
        result.add(level);
    }
    return result;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left)  q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(level);
    }
    return result;
}
```
{% endtab %}
{% endtabs %}

### When to Use Which Traversal?

| Traversal | Use Case |
|-----------|----------|
| **Inorder** | BST operations (sorted order), expression trees |
| **Preorder** | Serialization, tree copying, prefix expressions |
| **Postorder** | Deletion, expression evaluation, "bottom-up" computations |
| **Level-order** | Right/left view, minimum depth, connecting siblings |

---

## 26.3 Height, Diameter, Balanced Check, Maximum Path Sum

### Height (Maximum Depth)

```
height(node) = 0                        if node is null
             = 1 + max(height(left), height(right))   otherwise
```

This is the simplest and most important tree recursive pattern. Almost every tree problem builds on this idea.

### Diameter of Binary Tree

The **diameter** is the longest path between any two nodes (measured in edges). It may not pass through the root.

**Key insight:** At each node, the longest path through that node = left_height + right_height. Track the maximum across all nodes.

{% tabs %}
{% tab title="Python" %}
```python
def diameter(root):
    best = [0]
    def height(node):
        if not node: return 0
        lh = height(node.left)
        rh = height(node.right)
        best[0] = max(best[0], lh + rh)  # path through this node
        return 1 + max(lh, rh)
    height(root)
    return best[0]
```
{% endtab %}
{% tab title="Java" %}
```java
int diameter;
int height(TreeNode node) {
    if (node == null) return 0;
    int lh = height(node.left), rh = height(node.right);
    diameter = Math.max(diameter, lh + rh);
    return 1 + Math.max(lh, rh);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int best;
int height(TreeNode* node) {
    if (!node) return 0;
    int lh = height(node->left), rh = height(node->right);
    best = max(best, lh + rh);
    return 1 + max(lh, rh);
}
```
{% endtab %}
{% endtabs %}

### Balanced Binary Tree

A tree is **balanced** if for every node, the heights of its left and right subtrees differ by at most 1.

**Efficient approach:** Return -1 (unbalanced signal) instead of computing height separately. This avoids O(n^2).

### Maximum Path Sum

For each node, the maximum path sum through it = node.val + max(left_gain, 0) + max(right_gain, 0). The "gain" is the best single-branch sum. We clamp to 0 because a negative branch should be skipped.

---

## 26.4 Views: Right Side, Boundary Traversal

### Right Side View

Use level-order traversal. The last node of each level is visible from the right.

### Boundary Traversal

Anti-clockwise boundary: root + left boundary (top-down, excluding leaves) + all leaves (left to right) + right boundary (bottom-up, excluding leaves).

This problem tests your ability to decompose a complex task into clean sub-problems.

---

## 26.5 Lowest Common Ancestor (LCA)

The LCA of two nodes p and q is the deepest node that is an ancestor of both.

### The Elegant Recursive Solution

{% tabs %}
{% tab title="Python" %}
```python
def lca(root, p, q):
    if not root: return None
    if root.val == p or root.val == q: return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right: return root    # p and q in different subtrees
    return left if left else right    # both in same subtree
```
{% endtab %}
{% tab title="Java" %}
```java
TreeNode lca(TreeNode root, int p, int q) {
    if (root == null) return null;
    if (root.val == p || root.val == q) return root;
    TreeNode left = lca(root.left, p, q);
    TreeNode right = lca(root.right, p, q);
    if (left != null && right != null) return root;
    return left != null ? left : right;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
TreeNode* lca(TreeNode* root, int p, int q) {
    if (!root) return nullptr;
    if (root->val == p || root->val == q) return root;
    TreeNode* left = lca(root->left, p, q);
    TreeNode* right = lca(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}
```
{% endtab %}
{% endtabs %}

**Why this works:** If p is in the left subtree and q is in the right subtree, the current node is the LCA. If both are in the same subtree, the first one found "wins" and propagates up.

---

## 26.6 Binary Search Trees (BST)

A BST is a binary tree where for every node: all left descendants < node < all right descendants.

### BST Search: O(h)

Go left if target < current, right if target > current.

### BST Insert: O(h)

Find the right spot (same as search), add a new leaf.

### BST Delete: O(h)

Three cases:
1. **Leaf**: Just remove it.
2. **One child**: Replace with the child.
3. **Two children**: Replace with the inorder successor (smallest in right subtree), then delete the successor.

### BST Validation

{% hint style="danger" %}
**Common mistake:** Checking only the immediate parent. The tree `[5, 1, 6, null, null, 3, 7]` has 3 < 6 (valid as left child), but 3 < 5 (invalid -- 3 is in the RIGHT subtree of 5). You must pass the full valid range (lo, hi) down the tree.
{% endhint %}

### Kth Smallest Element

Inorder traversal of a BST gives sorted order. Count nodes during inorder and stop at k.

---

## 26.7 Construct Tree from Traversals

Given preorder and inorder arrays, you can reconstruct the unique binary tree:

1. The first element of preorder is the root.
2. Find this root in inorder -- everything to its left is the left subtree, everything to its right is the right subtree.
3. Use the left subtree size to split the preorder array.
4. Recurse.

**Optimization:** Use a hash map to look up positions in inorder in O(1).

{% tabs %}
{% tab title="Python" %}
```python
def build(preorder, inorder):
    if not preorder: return None
    in_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(ps, pe, is_, ie):
        if ps > pe: return None
        root = TreeNode(preorder[ps])
        mid = in_map[preorder[ps]]
        left_size = mid - is_
        root.left = helper(ps+1, ps+left_size, is_, mid-1)
        root.right = helper(ps+left_size+1, pe, mid+1, ie)
        return root

    return helper(0, len(preorder)-1, 0, len(inorder)-1)
```
{% endtab %}
{% tab title="Java" %}
```java
// Same approach: preorder[ps] is root, find in inorder, split
Map<Integer, Integer> inMap = new HashMap<>();
// ... build map, then recurse with index bounds
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Same approach using unordered_map<int,int> for O(1) lookup
```
{% endtab %}
{% endtabs %}

---

## 26.8 Serialize and Deserialize

**Serialization** converts a tree to a string. **Deserialization** reconstructs it.

**BFS approach:** Level-order traversal with "N" for null nodes.

```
Tree: [1, 2, 3, null, null, 4, 5]
Serialized: "1,2,3,N,N,4,5,N,N,N,N"
```

Deserialization reverses the process: parse tokens, use a queue to assign children.

---

## 26.9 Flatten Binary Tree, Binary Tree Cameras

### Flatten to Linked List

Flatten the tree in preorder: for each node, set left to null and right to the next preorder node. The simplest approach: collect preorder traversal, then rewire.

### Binary Tree Cameras

Place cameras on nodes. Each camera monitors its parent, itself, and children. Minimize cameras.

**Greedy DFS from leaves up.** Three states:
- 0 = NOT covered (needs camera from parent)
- 1 = HAS camera
- 2 = COVERED (by child's camera)

If any child is NOT covered, we MUST place a camera here. If any child HAS a camera, we are covered. Otherwise, we are NOT covered (hope parent helps).

---

## Five-Lens Framework: LCA

Let us apply all five lenses to the Lowest Common Ancestor problem.

### Lens 1: Constraints
- Tree has n nodes (1 <= n <= 10^5).
- Both p and q exist in the tree.
- All node values are unique.
- We need O(n) time or better.

### Lens 2: Brute Force
Store the path from root to p and from root to q. Compare paths to find the last common node. Time: O(n), Space: O(n) for paths.

### Lens 3: Pattern
This is a "post-order processing" pattern: we need information from both subtrees before making a decision at the current node. The pattern appears in diameter, balanced check, and maximum path sum too.

### Lens 4: Optimization
The single-pass recursive DFS avoids storing paths. It uses the insight that if we find p in one subtree and q in the other, the current node IS the LCA. Time: O(n), Space: O(h) stack.

### Lens 5: Proof
**Correctness:** If p and q are in different subtrees of node X, then X is the deepest such node (because any deeper node would have both in the same subtree). If one is an ancestor of the other, the ancestor is returned first and propagated up.

---

## Think Like a Pro

{% hint style="info" %}
**When tourist sees a tree problem, the first thing he asks is: "Rooted or unrooted?"** That single question determines the approach. A rooted tree has a designated root and clear parent-child relationships. An unrooted tree (common in competitive programming) can be rooted at any node. For this chapter, all trees are rooted -- but when you reach Ch 33 (Advanced Trees), you will see problems where choosing the right root changes the difficulty from hard to trivial.
{% endhint %}

**Errichto's tree debugging tip:** "When my tree solution gives wrong answers, I draw the tree for the failing test case. 90% of the time, the bug is in the null checks."

---

## AOPS Showcase: "LCA" — Three Progressive Solutions

### Solution 1: Store Paths and Compare (Brute Force)

Find the path from root to p and from root to q. Walk both paths from the beginning and return the last matching node.

{% tabs %}
{% tab title="Python" %}
```python
def lca_paths(root, p, q):
    def find_path(node, target, path):
        if not node: return False
        path.append(node)
        if node.val == target: return True
        if find_path(node.left, target, path) or find_path(node.right, target, path):
            return True
        path.pop()
        return False

    path_p, path_q = [], []
    find_path(root, p, path_p)
    find_path(root, q, path_q)

    lca = None
    for a, b in zip(path_p, path_q):
        if a.val == b.val:
            lca = a
        else:
            break
    return lca.val
```
{% endtab %}
{% tab title="Java" %}
```java
// Same approach: find paths, zip-compare
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Same approach: find paths, zip-compare
```
{% endtab %}
{% endtabs %}

**Time:** O(n), **Space:** O(n) for storing two paths.

### Solution 2: Parent Pointer Approach

Build a parent map using BFS. Then walk upward from p, marking visited ancestors. Walk upward from q until you hit a visited node.

{% tabs %}
{% tab title="Python" %}
```python
from collections import deque

def lca_parent(root, p, q):
    parent = {root.val: None}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            parent[node.left.val] = node
            queue.append(node.left)
        if node.right:
            parent[node.right.val] = node
            queue.append(node.right)

    # Walk up from p, mark ancestors
    ancestors = set()
    node_p = p
    while node_p is not None:
        ancestors.add(node_p)
        node_p = parent.get(node_p)

    # Walk up from q until we hit a p-ancestor
    node_q = q
    while node_q not in ancestors:
        node_q = parent[node_q]
    return node_q
```
{% endtab %}
{% tab title="Java" %}
```java
// Same approach: build parent map, walk up from both
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Same approach using unordered_map<int, TreeNode*> parent
```
{% endtab %}
{% endtabs %}

**Time:** O(n), **Space:** O(n) for parent map.

### Solution 3: Single-Pass Recursive DFS (Optimal)

The elegant solution we saw in Section 26.5. One DFS call, no extra data structures.

**Time:** O(n), **Space:** O(h) for recursion stack.

### Comparison

| Approach | Time | Space | Passes | Code Simplicity |
|----------|------|-------|--------|-----------------|
| Store Paths | O(n) | O(n) | 2 (find paths) + 1 (compare) | Medium |
| Parent Pointers | O(n) | O(n) | 1 (build map) + 2 (walk up) | Medium |
| Recursive DFS | O(n) | O(h) | 1 | Elegant |

The recursive DFS is the clear winner: minimal space, single pass, clean code. It demonstrates the power of thinking recursively about tree problems.

---

## Legend's Corner

{% hint style="info" %}
**Neal Wu** started competing in programming contests in 8th grade -- the same age as you. He went on to become one of the strongest competitive programmers in the United States, representing the US at the International Olympiad in Informatics (IOI).

Neal once shared his approach to tree problems: "Trees are just graphs with no cycles. The moment you realize that, DFS and BFS from graph theory work perfectly on trees. But trees have one extra superpower: every node has exactly one path to the root. That means any problem about 'paths in a tree' can be solved by thinking about ancestors."

That insight -- trees have unique paths -- is the key to LCA, diameter, and path sum problems. When you see a tree problem, ask yourself: "What path am I looking for?"
{% endhint %}

---

## Gotchas

1. **Forgetting null checks.** Every recursive tree function needs a base case for `null` / `None` / `nullptr`. This is the #1 source of tree bugs.

2. **Confusing height vs depth.** Height is measured from a node DOWN to its deepest leaf. Depth is measured from the root DOWN to a node. The height of the tree equals the depth of the deepest leaf.

3. **BST validation: checking only the parent.** The tree `[5,1,6,null,null,3,7]` looks valid if you only check parent-child pairs (3 < 6), but 3 is in the RIGHT subtree of 5, violating 3 < 5. Always pass the full range (lo, hi).

4. **Diameter does not always pass through the root.** Consider a tree where the longest path is entirely within one subtree. The diameter must be tracked as a global maximum, not just computed at the root.

5. **Maximum path sum: forgetting to clamp negative gains to 0.** If the left subtree contributes a negative sum, we should skip it entirely (take 0 instead). But the single-node case must still handle all-negative trees.

6. **Level-order: forgetting to process by level.** If you do not snapshot `len(queue)` at the start of each level, you will mix nodes from different levels.

7. **Serialization: inconsistent null representation.** Make sure your serialize and deserialize use the same sentinel for null nodes. "N" and "" are both fine, but they must match.

---

## Practice Problems

| # | Problem | Difficulty | Topic | Hint |
|---|---------|-----------|-------|------|
| W1 | Inorder Traversal | Easy | Traversal | Left, root, right -- recursion |
| W2 | Preorder Traversal | Easy | Traversal | Root, left, right -- recursion |
| W3 | Level Order Traversal | Easy | BFS | Use a queue, process one level at a time |
| W4 | Maximum Depth | Easy | Recursion | 1 + max(left, right) |
| W5 | Symmetric Tree | Easy | Recursion | Compare left.left with right.right |
| P1 | Diameter of Binary Tree | Medium | DFS | Track left+right height at each node |
| P2 | Balanced Binary Tree | Medium | DFS | Return -1 as "unbalanced" signal |
| P3 | Right Side View | Medium | BFS | Last node of each level |
| P4 | Validate BST | Medium | DFS | Pass (lo, hi) range, not just parent |
| P5 | Kth Smallest in BST | Medium | Inorder | Count during inorder traversal |
| P6 | LCA of Binary Tree | Medium | DFS | If both sides return non-null, you found it |
| P7 | Maximum Path Sum | Hard | DFS | Clamp negative gains to 0 |
| C1 | Construct from Preorder+Inorder | Hard | Recursion | First preorder element is root, split inorder |
| C2 | Serialize/Deserialize | Hard | BFS | Level-order with null markers |
| C3 | Boundary Traversal | Hard | Mixed | Three parts: left boundary, leaves, right boundary |
| C4 | Binary Tree Cameras | Hard | Greedy | Three states: not covered, has camera, covered |
| C5 | Flatten Binary Tree | Medium | Preorder | Collect preorder traversal as a list |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
# BFS queue: use collections.deque for O(1) popleft
from collections import deque
q = deque([root])
node = q.popleft()  # O(1) -- list.pop(0) is O(n)!

# Recursive traversal with list accumulation
def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Tracking global state with mutable container
best = [0]  # use list to allow mutation inside nested function
def dfs(node):
    best[0] = max(best[0], ...)
```
{% endtab %}
{% tab title="Java" %}
```java
// BFS queue: use LinkedList (implements Queue interface)
Queue<TreeNode> queue = new LinkedList<>();
queue.add(root);
TreeNode node = queue.poll();

// Recursive traversal with List parameter
void inorder(TreeNode node, List<Integer> result) {
    if (node == null) return;
    inorder(node.left, result);
    result.add(node.val);
    inorder(node.right, result);
}

// Global state: use static fields or int[] wrapper
static int diameter = 0;
```
{% endtab %}
{% tab title="C++" %}
```cpp
// BFS queue: use std::queue
queue<TreeNode*> q;
q.push(root);
TreeNode* node = q.front(); q.pop();

// Recursive traversal with reference parameter
void inorder(TreeNode* node, vector<int>& res) {
    if (!node) return;
    inorder(node->left, res);
    res.push_back(node->val);
    inorder(node->right, res);
}

// Lambda with capture for state
int best = 0;
function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
    // can read/write best via capture
};
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 10** (Recursion) gave you the mental model for recursive thinking -- tree problems are the ultimate application of recursion. Every tree algorithm is a recursive function with a null base case.
- **Ch 19-20** (Graphs) introduced DFS and BFS. Trees are just connected acyclic graphs, and the same traversal techniques apply. Level-order traversal IS BFS on a tree.

### Looking Forward
- **Ch 27** (Shortest Paths) will use tree-like structures in algorithms like Dijkstra's. The shortest-path tree of a graph is literally a tree.
- **Ch 33** (Advanced Trees) will cover balanced BSTs (AVL, Red-Black), tree DP, heavy-light decomposition, and Euler tour -- the Platinum-level extensions of everything in this chapter.

### Cross-Chapter Threads
- **"Recursion everywhere"**: Trees are the most natural recursive data structure. Every tree problem decomposes into "solve for left subtree, solve for right subtree, combine." This pattern appeared in Ch 10 and will continue through Ch 31 (DP on Trees).
- **"Reduce to known"**: Many tree problems reduce to traversal + some extra logic. Diameter = height computation + max tracking. Kth smallest = inorder traversal + counting. Recognizing the base pattern saves you from reinventing the wheel.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"We computed LCA in O(n) per query. But what if we have 10^5 queries on the same tree? Can we answer each in O(1)?"** Yes! Techniques like Binary Lifting (O(n log n) preprocessing, O(log n) per query) and Euler Tour + Sparse Table (O(n log n) preprocessing, O(1) per query) make this possible. These appear in competitive programming and USACO Platinum problems.

2. **"All our trees are 'static' -- they do not change. What if we need to insert, delete, AND answer queries like 'kth smallest' efficiently?"** Balanced BSTs (AVL trees, Red-Black trees) maintain O(log n) height after insertions and deletions. Augmented BSTs can answer order-statistic queries in O(log n). These are the workhorses behind `std::set` in C++ and `TreeMap` in Java.

3. **"Can we store a binary tree in just one array, without any pointers?"** Yes! For a complete binary tree, store it level by level. Node at index i has children at 2i+1 and 2i+2. This is exactly how heaps work (Ch 17). But for sparse trees, the array wastes space on null entries.

---

## What's Next

You have now mastered binary trees and BSTs -- the most fundamental tree structures in computer science. You can traverse them in every direction, compute their properties, validate them, construct them, serialize them, and solve hard problems on them.

But trees are just the beginning of graph algorithms. What happens when you have a graph with weighted edges and you want to find the shortest path? That is the domain of Dijkstra's algorithm, Bellman-Ford, and Floyd-Warshall.

In **Ch 27 (Shortest Paths -- Finding the Best Route)**, you will learn how to find the shortest path in a weighted graph. And you will discover that shortest-path algorithms actually BUILD a tree -- the shortest-path tree -- connecting the source to every reachable node. Trees and graphs are deeply connected, and the journey continues!
