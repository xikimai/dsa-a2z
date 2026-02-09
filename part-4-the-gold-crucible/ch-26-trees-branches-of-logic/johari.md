# Johari Window: Chapter 26 — Trees — Branches of Logic

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about trees, traversals, and BSTs.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] Recursion — functions that call themselves, base cases, recursive cases (from Ch 10)
> - [ ] BFS — level-order exploration using a queue (from Ch 19)
> - [ ] DFS — depth-first exploration using recursion or a stack (from Ch 19)
> - [ ] What a tree looks like — root, leaves, parent, child
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What a "binary tree" is and how it differs from a general tree
> - [ ] What "inorder," "preorder," and "postorder" traversals mean
> - [ ] What a Binary Search Tree (BST) is and why it matters
> - [ ] How to find the "lowest common ancestor" of two nodes
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but have not learned:
> - [ ] How to serialize and deserialize a tree to/from a string
> - [ ] What "diameter" or "maximum path sum" of a tree means
> - [ ] How to construct a tree from its traversal sequences
> - [ ] What "boundary traversal" or "tree cameras" problems are
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
> - [ ] Binary tree: every node has at most 2 children (left and right)
> - [ ] Inorder (L-Root-R) gives sorted order for BSTs; Preorder (Root-L-R) for serialization; Postorder (L-R-Root) for deletion
> - [ ] Level-order uses a BFS queue — process one level at a time
> - [ ] Height/depth are computed recursively: 1 + max(left_height, right_height)
> - [ ] BST validation requires passing a valid range (lo, hi) to every node — not just checking parent
> - [ ] LCA can be found with a single DFS: if both sides return non-null, current node is the ancestor
> - [ ] Maximum path sum uses a "max gain" helper that returns the best single-branch sum to the parent
> - [ ] Trees can be constructed from preorder + inorder using the "first element is root" insight
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That diameter of a tree is just left_height + right_height at each node — so simple!
> - [ ] That BST validation is wrong if you only check the immediate parent — you need the FULL range
> - [ ] That the LCA algorithm only needs one pass through the tree, not two
> - [ ] That binary tree cameras uses a greedy DFS from leaves up — three states per node
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Iterative tree traversals (using an explicit stack instead of recursion)
> - [ ] Constructing trees from traversal sequences without getting confused by indices
> - [ ] The boundary traversal — getting the three parts (left boundary, leaves, right boundary) right
> - [ ] Deciding between DFS and BFS for different tree problems
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] Can we answer LCA queries in O(1) after preprocessing? (Sparse tables, Euler tour)
> - [ ] What are balanced BSTs (AVL, Red-Black) and when do we need them?
> - [ ] How does DP on trees work — is it different from DP on arrays?
> - [ ] Can trees have more than 2 children? How does that change the algorithms?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 27 (Shortest Paths) and Ch 33 (Advanced Trees) — many tree patterns extend to graphs and advanced data structures!
