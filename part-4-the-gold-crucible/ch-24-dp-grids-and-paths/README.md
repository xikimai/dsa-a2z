# Dynamic Programming II — Grids and Paths

{% hint style="info" %}
**Welcome back to the Gold Crucible!** In Chapter 23, you learned to think in one dimension — arrays, stairs, houses, stock prices. Now we add a second dimension. Grid DP is everywhere: from robot navigation to image processing to game theory. Once you master filling a 2D table row by row, you will see grids in problems you never expected.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Extend the DP Recipe from 1D arrays to 2D grids
- Count unique paths in a grid using the recurrence dp[i][j] = dp[i-1][j] + dp[i][j-1]
- Handle obstacles and blocked cells in grid DP
- Solve the Minimum Path Sum problem using all four DP stages (recursion, memo, tabulation, space-optimized)
- Solve the Triangle problem using bottom-up DP
- Understand falling path problems (start from any column, fall with diagonal movement)
- Model two-agent problems using 3D DP (Cherry Pickup)
- Apply the Maximal Square recurrence: dp[i][j] = min(left, above, diagonal) + 1
- Count all square submatrices using the same recurrence
- Use reverse DP for the Dungeon Game (working backwards from destination)
- Build the Maximal Rectangle solution using histograms
- Space-optimize 2D DP from O(m*n) to O(n) using a single row
- Recognize when a grid problem is DP vs. backtracking

---

## The Story: "The Treasure Map"

After mastering the mountain toll roads (Chapter 23), the merchant Dara received a mysterious treasure map. It was a grid — rows and columns of numbers, each representing the gold coins hidden in that cell.

"Start at the top-left corner," the map read. "Move only right or down. When you reach the bottom-right corner, the sum of all the cells you visited is your treasure."

Dara stared at the grid. There were SO many possible paths. She could go all the way right and then all the way down. Or all the way down and then all the way right. Or zig-zag through the middle.

"This is just like the mountain roads," she realized. "But instead of a single line of crossroads, it is a GRID. Each cell is a crossroads with two choices: go right or go down."

She pulled out her notebook and started writing. For each cell, she noted the cheapest way to get there — using only the cells above and to the left. Row by row, column by column, she filled in the grid. When she reached the bottom-right corner, the answer was waiting for her.

"Two dimensions, same idea," she smiled. "Break it into subproblems. Remember the answers. Build up to the solution."

Today, you learn to think like Dara — in two dimensions.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "Count the Paths"

How many unique paths are there from the top-left to the bottom-right of a 3x3 grid, if you can only move right or down?

```
S . .
. . .
. . E
```

Try drawing all the paths. Each path makes exactly 2 right moves and 2 down moves (in some order). How many ways can you arrange 2 R's and 2 D's?

{% hint style="info" %}
There are 6 paths: RRDD, RDRD, RDDR, DRRD, DRDR, DDRR. This is the combinatorial formula C(4,2) = 6. But DP gives us a way to compute this WITHOUT knowing combinatorics — just fill in a grid!
{% endhint %}

### Puzzle 2: "Cheapest Path"

Find the minimum-cost path from S to E (moving only right or down):

```
1  3  1
1  5  1
4  2  1
```

Try a few paths:
- Right, Right, Down, Down: 1+3+1+1+1 = 7
- Down, Down, Right, Right: 1+1+4+2+1 = 9
- Right, Down, Down, Right: 1+3+5+2+1 = 12
- Down, Right, Right, Down: 1+1+5+1+1 = 9

The cheapest is 7 (path: 1->3->1->1->1). Can you find this systematically?

{% hint style="info" %}
At each cell, the cheapest way to arrive is from the cheaper of the cell above or the cell to the left. This is the Minimum Path Sum recurrence: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).
{% endhint %}

### Puzzle 3: "The Triangle"

Find the minimum path sum from top to bottom. At each step, move to an adjacent number in the next row:

```
    2
   3 4
  6 5 7
 4 1 8 3
```

From 2, you can go to 3 or 4. From 3, you can go to 6 or 5. And so on.

{% hint style="info" %}
The minimum path is 2->3->5->1 = 11. The trick is to work BOTTOM-UP: start from the last row and propagate upward. This avoids exploring all 2^n paths.
{% endhint %}

---

## 24.1 From 1D to 2D: The Grid World

In Chapter 23, our DP state had one dimension: `dp[i]` represented "the answer for the first i items." Now we have two dimensions: `dp[i][j]` represents "the answer for the subproblem at cell (i, j)."

The DP Recipe is the same:

| Step | 1D (Ch 23) | 2D (Ch 24) |
|------|------------|------------|
| **State** | `dp[i]` — answer at index i | `dp[i][j]` — answer at cell (i,j) |
| **Recurrence** | `dp[i]` depends on `dp[i-1]`, `dp[i-2]`, etc. | `dp[i][j]` depends on `dp[i-1][j]`, `dp[i][j-1]`, etc. |
| **Base case** | `dp[0]`, `dp[1]` | First row, first column |
| **Fill order** | Left to right | Row by row, left to right |
| **Space optimization** | O(n) -> O(1) (two variables) | O(m*n) -> O(n) (one row) |

The key insight for space optimization: if `dp[i][j]` only depends on the current row and the previous row, you only need to store ONE row at a time. As you process each new row, you overwrite the old values.

---

## 24.2 Unique Paths

**Problem**: Given an m x n grid, count the number of unique paths from (0,0) to (m-1,n-1), moving only right or down.

### The Recurrence

To reach cell (i,j), your last move was either:
- From (i-1, j) — you moved DOWN, or
- From (i, j-1) — you moved RIGHT

So: **dp[i][j] = dp[i-1][j] + dp[i][j-1]**

Base cases: The first row is all 1s (only one way: keep going right). The first column is all 1s (only one way: keep going down).

{% tabs %}
{% tab title="Python" %}
```python
def unique_paths(m, n):
    dp = [1] * n  # first row is all 1s
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # dp[j] already has "from above", add "from left"
    return dp[n - 1]
```
{% endtab %}
{% tab title="Java" %}
```java
static int uniquePaths(int m, int n) {
    int[] dp = new int[n];
    Arrays.fill(dp, 1);
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1];
    return dp[n - 1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int uniquePaths(int m, int n) {
    vector<int> dp(n, 1);
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] += dp[j - 1];
    return dp[n - 1];
}
```
{% endtab %}
{% endtabs %}

> **Language Spotlight: Unique Paths**
> | | Python | Java | C++ |
> |---|--------|------|-----|
> | Array init all 1s | `[1] * n` | `Arrays.fill(dp, 1)` | `vector<int>(n, 1)` |
> | In-place add | `dp[j] += dp[j-1]` | `dp[j] += dp[j-1]` | `dp[j] += dp[j-1]` |

**Time**: O(m * n). **Space**: O(n) — one row.

{% hint style="info" %}
**Fun fact**: The answer to Unique Paths is also C(m+n-2, m-1) — a binomial coefficient. The DP approach works even if you have never heard of combinatorics!
{% endhint %}

---

## 24.3 Obstacles and Blocked Cells

**Problem**: Same as Unique Paths, but some cells are blocked (grid[i][j] = 1 means obstacle).

The only change: if a cell is blocked, dp[i][j] = 0. No paths go through it.

{% tabs %}
{% tab title="Python" %}
```python
def unique_paths_obstacles(grid):
    m, n = len(grid), len(grid[0])
    if grid[0][0] == 1:
        return 0
    dp = [0] * n
    dp[0] = 1
    for j in range(1, n):
        dp[j] = dp[j - 1] if grid[0][j] == 0 else 0
    for i in range(1, m):
        dp[0] = dp[0] if grid[i][0] == 0 else 0
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[j] = 0
            else:
                dp[j] += dp[j - 1]
    return dp[n - 1]
```
{% endtab %}
{% tab title="Java" %}
```java
static int uniquePathsObstacles(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    if (grid[0][0] == 1) return 0;
    int[] dp = new int[n];
    dp[0] = 1;
    for (int j = 1; j < n; j++) dp[j] = grid[0][j] == 0 ? dp[j-1] : 0;
    for (int i = 1; i < m; i++) {
        dp[0] = grid[i][0] == 0 ? dp[0] : 0;
        for (int j = 1; j < n; j++)
            dp[j] = grid[i][j] == 1 ? 0 : dp[j] + dp[j-1];
    }
    return dp[n - 1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int uniquePathsObstacles(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    if (grid[0][0] == 1) return 0;
    vector<int> dp(n, 0);
    dp[0] = 1;
    for (int j = 1; j < n; j++) dp[j] = grid[0][j] == 0 ? dp[j-1] : 0;
    for (int i = 1; i < m; i++) {
        dp[0] = grid[i][0] == 0 ? dp[0] : 0;
        for (int j = 1; j < n; j++)
            dp[j] = grid[i][j] == 1 ? 0 : dp[j] + dp[j-1];
    }
    return dp[n - 1];
}
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Watch out**: An obstacle in the first row blocks ALL cells to its right in that row. An obstacle in the first column blocks ALL cells below it. The 1D space optimization handles this naturally — once dp[0] becomes 0, it stays 0.
{% endhint %}

---

## 24.4 Minimum Path Sum — AOPS Showcase

This is the perfect problem to demonstrate the four-stage DP progression on a 2D grid.

**Problem**: Given an m x n grid of non-negative integers, find the path from top-left to bottom-right with the minimum sum (moving only right or down).

### Approach 1: Pure Recursion — O(2^(m+n)) time

{% tabs %}
{% tab title="Python" %}
```python
def min_path_recursive(grid, i, j):
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return float('inf')
    return grid[i][j] + min(
        min_path_recursive(grid, i - 1, j),
        min_path_recursive(grid, i, j - 1)
    )
```
{% endtab %}
{% tab title="Java" %}
```java
static int minPathRecursive(int[][] grid, int i, int j) {
    if (i == 0 && j == 0) return grid[0][0];
    if (i < 0 || j < 0) return Integer.MAX_VALUE;
    return grid[i][j] + Math.min(
        minPathRecursive(grid, i - 1, j),
        minPathRecursive(grid, i, j - 1));
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int minPathRecursive(vector<vector<int>>& grid, int i, int j) {
    if (i == 0 && j == 0) return grid[0][0];
    if (i < 0 || j < 0) return INT_MAX;
    return grid[i][j] + min(
        minPathRecursive(grid, i - 1, j),
        minPathRecursive(grid, i, j - 1));
}
```
{% endtab %}
{% endtabs %}

**Time**: O(2^(m+n)) — exponential. Each cell branches into two calls.

### Approach 2: Memoization — O(m*n) time

{% tabs %}
{% tab title="Python" %}
```python
def min_path_memo(grid):
    m, n = len(grid), len(grid[0])
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        memo[(i, j)] = grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))
        return memo[(i, j)]
    return dp(m - 1, n - 1)
```
{% endtab %}
{% tab title="Java" %}
```java
static int minPathMemo(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    int[][] memo = new int[m][n];
    for (int[] row : memo) Arrays.fill(row, -1);
    return dpMemo(grid, m - 1, n - 1, memo);
}
static int dpMemo(int[][] g, int i, int j, int[][] memo) {
    if (i == 0 && j == 0) return g[0][0];
    if (i < 0 || j < 0) return Integer.MAX_VALUE;
    if (memo[i][j] != -1) return memo[i][j];
    return memo[i][j] = g[i][j] + Math.min(
        dpMemo(g, i-1, j, memo), dpMemo(g, i, j-1, memo));
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int dpMemo(vector<vector<int>>& g, int i, int j, vector<vector<int>>& memo) {
    if (i == 0 && j == 0) return g[0][0];
    if (i < 0 || j < 0) return INT_MAX;
    if (memo[i][j] != -1) return memo[i][j];
    return memo[i][j] = g[i][j] + min(
        dpMemo(g, i-1, j, memo), dpMemo(g, i, j-1, memo));
}
```
{% endtab %}
{% endtabs %}

**Time**: O(m*n). **Space**: O(m*n) for memo + O(m+n) recursion stack.

### Approach 3: Tabulation — O(m*n) time, O(m*n) space

{% tabs %}
{% tab title="Python" %}
```python
def min_path_tabulation(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]
```
{% endtab %}
{% tab title="Java" %}
```java
static int minPathTabulation(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    int[][] dp = new int[m][n];
    dp[0][0] = grid[0][0];
    for (int j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
    for (int i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[i][j] = grid[i][j] + Math.min(dp[i-1][j], dp[i][j-1]);
    return dp[m-1][n-1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int minPathTabulation(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<vector<int>> dp(m, vector<int>(n));
    dp[0][0] = grid[0][0];
    for (int j = 1; j < n; j++) dp[0][j] = dp[0][j-1] + grid[0][j];
    for (int i = 1; i < m; i++) dp[i][0] = dp[i-1][0] + grid[i][0];
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
    return dp[m-1][n-1];
}
```
{% endtab %}
{% endtabs %}

**Time**: O(m*n). **Space**: O(m*n).

### Approach 4: Space-Optimized — O(m*n) time, O(n) space

{% tabs %}
{% tab title="Python" %}
```python
def min_path_optimized(grid):
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = grid[0][0]
    for j in range(1, n):
        dp[j] = dp[j-1] + grid[0][j]
    for i in range(1, m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
    return dp[n-1]
```
{% endtab %}
{% tab title="Java" %}
```java
static int minPathOptimized(int[][] grid) {
    int m = grid.length, n = grid[0].length;
    int[] dp = new int[n];
    dp[0] = grid[0][0];
    for (int j = 1; j < n; j++) dp[j] = dp[j-1] + grid[0][j];
    for (int i = 1; i < m; i++) {
        dp[0] += grid[i][0];
        for (int j = 1; j < n; j++)
            dp[j] = Math.min(dp[j], dp[j-1]) + grid[i][j];
    }
    return dp[n-1];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int minPathOptimized(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> dp(n);
    dp[0] = grid[0][0];
    for (int j = 1; j < n; j++) dp[j] = dp[j-1] + grid[0][j];
    for (int i = 1; i < m; i++) {
        dp[0] += grid[i][0];
        for (int j = 1; j < n; j++)
            dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
    }
    return dp[n-1];
}
```
{% endtab %}
{% endtabs %}

**Time**: O(m*n). **Space**: O(n) — just one row!

### Why Does the 1D Trick Work?

When we process row `i` left to right:
- `dp[j]` (before update) holds the value from row `i-1` — that is "from above"
- `dp[j-1]` (after update in the same row) holds the value from row `i` — that is "from the left"

So `min(dp[j], dp[j-1])` gives us exactly `min(dp[i-1][j], dp[i][j-1])`. The old values get overwritten just in time!

### Comparison Table

| Approach | Time | Space | Idea |
|----------|------|-------|------|
| Pure Recursion | O(2^(m+n)) | O(m+n) | Every cell branches; massive redundancy |
| Memoization | O(m*n) | O(m*n) | Cache results; each cell solved once |
| Tabulation | O(m*n) | O(m*n) | Fill 2D table row by row |
| Space-Optimized | O(m*n) | O(n) | Only keep one row at a time |

{% hint style="info" %}
**This four-stage progression works for EVERY 2D grid DP problem.** Practice it until the space optimization feels automatic. The pattern is always: "Does dp[i][j] only depend on row i and row i-1? If yes, use one row."
{% endhint %}

---

## 24.5 The Triangle Problem

**Problem**: Given a triangle of numbers, find the minimum path sum from the top to the bottom. From position `j` in row `i`, you can move to position `j` or `j+1` in row `i+1`.

The trick here is to work **bottom-up**. Start from the last row (it IS the base case), then for each row above, pick the better child:

**dp[j] = triangle[i][j] + min(dp[j], dp[j+1])**

{% tabs %}
{% tab title="Python" %}
```python
def triangle_min_total(triangle):
    dp = triangle[-1][:]  # copy last row
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]
```
{% endtab %}
{% tab title="Java" %}
```java
static int triangleMinTotal(int[][] tri) {
    int n = tri.length;
    int[] dp = tri[n - 1].clone();
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            dp[j] = tri[i][j] + Math.min(dp[j], dp[j + 1]);
    return dp[0];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int triangleMinTotal(vector<vector<int>>& tri) {
    int n = tri.size();
    vector<int> dp = tri[n - 1];
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            dp[j] = tri[i][j] + min(dp[j], dp[j + 1]);
    return dp[0];
}
```
{% endtab %}
{% endtabs %}

**Time**: O(n^2) where n = number of rows. **Space**: O(n).

{% hint style="info" %}
**Why bottom-up?** If we worked top-down, we would need to track the minimum across ALL positions in the last row. But bottom-up naturally funnels all paths into dp[0] at the top.
{% endhint %}

---

## 24.6 Falling Paths and Variations

**Problem**: Given an n x n matrix, find the minimum "falling path" sum. Start at any column in row 0. At each step, move directly below, or diagonally below-left, or diagonally below-right.

This is like the triangle, but on a square grid with 3 choices per cell instead of 2. The difference from Min Path Sum: you can start at ANY column in row 0, and you have diagonal movement.

**Recurrence**: dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

**Answer**: min(dp[n-1][0], dp[n-1][1], ..., dp[n-1][n-1])

{% hint style="warning" %}
**Boundary care**: When j=0, there is no dp[i-1][j-1]. When j=n-1, there is no dp[i-1][j+1]. Check bounds before accessing!
{% endhint %}

---

## 24.7 3D DP: Cherry Pickup (Two Agents)

Some grid problems involve TWO agents moving simultaneously. This requires a 3D DP state.

### Cherry Pickup II (Two Robots)

**Problem**: Two robots start at (0, 0) and (0, n-1). Both move DOWN one row per step, and can shift left, stay, or shift right. They collect cherries. If both are on the same cell, collect once. Maximize total cherries.

**State**: dp[i][c1][c2] = max cherries from row i to the last row, with robot 1 at column c1 and robot 2 at column c2.

**Space**: Since each row only depends on the next row, we optimize from O(m*n^2) to O(n^2).

### Cherry Pickup I (Round Trip)

**Problem**: Go from (0,0) to (n-1,n-1) and back. Collect cherries (each at most once).

**Key insight**: Instead of "forward then backward," model as TWO people walking simultaneously from (0,0) to (n-1,n-1). After t steps, person 1 is at (r1, t-r1) and person 2 is at (r2, t-r2).

**State**: dp[t][r1][r2]. Optimize to dp[r1][r2] per step.

{% hint style="info" %}
**Cross-chapter thread: "Reduce to known."** The "round trip" Cherry Pickup problem REDUCES to "two simultaneous forward walks." This is a classic transformation — whenever you see a "there and back" problem, ask: can I model it as two agents going the same direction?
{% endhint %}

---

## 24.8 DP on Squares

### Maximal Square

**Problem**: Given a binary matrix, find the largest square of all 1s. Return its area.

**Recurrence**: dp[i][j] = side length of the largest square with bottom-right corner at (i,j).

If matrix[i][j] == 1:
```
dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
```

Why min of three? A square of side k at (i,j) requires: a square of side k-1 above, a square of side k-1 to the left, and a square of side k-1 at the diagonal. The smallest of these limits the current square.

**Answer**: max_side^2.

### Count Square Submatrices

**Problem**: Count ALL square submatrices with all ones.

**Same recurrence!** But instead of tracking the maximum, SUM all dp values. A cell with dp[i][j] = k contributes k squares (1x1, 2x2, ..., kxk).

{% hint style="info" %}
**Two problems, one recurrence.** The Maximal Square and Count Squares problems use the exact same DP — they just aggregate differently (max vs. sum). Recognizing shared structure between problems is a key competitive programming skill.
{% endhint %}

---

## 24.9 The Dungeon Game (Reverse DP)

**Problem**: A knight must travel from (0,0) to (m-1,n-1). Each cell adds or subtracts from health. Health must stay >= 1 at all times. What is the minimum starting health?

**Why forward DP fails**: If you compute "minimum health to REACH cell (i,j)," you can not determine the minimum starting health — because a cell with a huge positive value in the middle might "save" you, but you need to survive the cells BEFORE it.

**Solution**: Reverse DP. Work backwards from (m-1,n-1) to (0,0).

**dp[i][j] = minimum health needed AT cell (i,j) to survive from here to the end.**

**Recurrence**: dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

The `max(1, ...)` ensures health never drops below 1.

{% hint style="warning" %}
**Reverse DP** is needed when the "cost" depends on the FUTURE, not the past. The Dungeon Game is the classic example: you need to know what lies ahead to decide how much health you need now.
{% endhint %}

---

## Five-Lens Framework: Minimum Path Sum

### Lens 1: Constraints
- Grid up to 200 x 200. That is 40,000 cells.
- Values 0-200. Sum can be up to 200*400 = 80,000. Fits in int.

### Lens 2: Brute Force
- Try all paths from (0,0) to (m-1,n-1). Each path has m+n-2 steps.
- Number of paths = C(m+n-2, m-1). For 200x200, this is astronomically large. Way too slow.

### Lens 3: Pattern
- At each cell, the optimal path depends only on the optimal paths to the cell above and to the left.
- Overlapping subproblems + optimal substructure = DP.

### Lens 4: Optimization
- Full 2D DP table: O(m*n) time, O(m*n) space.
- Space-optimized: O(m*n) time, O(n) space. Since dp[i][j] only depends on the current and previous row.

### Lens 5: Proof
- By induction on cells in fill order (row by row, left to right).
- Base: dp[0][0] = grid[0][0] is trivially optimal.
- Step: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) considers ALL possible last moves (right or down) and picks the best. Since subproblems are optimal (by inductive hypothesis), the overall solution is optimal. QED.

---

## Think Like a Pro

{% hint style="info" %}
**Errichto**: "For grid DP, I always draw the 2D table on paper and fill in a few cells by hand. If I can fill it correctly by hand, I can code it. If I am confused, I need to rethink my state definition."

*What you can learn*: Never jump straight to code for 2D DP. Draw the grid, write the recurrence, fill in 3-4 cells manually. The code writes itself after that.
{% endhint %}

{% hint style="info" %}
**Tourist** (Gennady Korotkevich): "When I see a problem with two agents on a grid, I immediately think: can I model this as a single DP with a combined state (pos1, pos2, step)? The step parameter often lets me reduce the dimension since pos = step - row."

*What you can learn*: Two agents on the same grid is almost always 3D DP. The trick is using the step count to eliminate one dimension (column = step - row).
{% endhint %}

---

## Legend's Corner

{% hint style="info" %}
**Petr Mitrichev** — multiple-time world champion, Google engineer: "Grid DP was one of the first DP families I mastered. The beautiful thing about grid problems is that they are VISUAL. You can literally draw the DP table and watch the values propagate. That visual intuition is priceless — it transfers to string DP, tree DP, and every other DP family. If you truly understand why the 1D space optimization works on a grid, you understand the core idea behind ALL DP space optimization."

**What you can learn**: Invest time in truly understanding the space optimization trick. Do not just memorize the code — draw the grid, watch which cells depend on which, and see WHY one row is enough. That understanding is portable to every DP problem you will ever encounter.
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Gotcha 1: Forgetting the first row and first column**

In grid DP, the first row and first column are base cases. If you skip initializing them and jump straight to the general recurrence, you will read uninitialized values. Always handle row 0 and column 0 separately.
{% endhint %}

{% hint style="danger" %}
**Gotcha 2: Obstacles in the first row/column**

An obstacle at (0, 3) means ALL cells (0, 4), (0, 5), ... have 0 paths (you cannot skip over it). Do not just set the obstacle cell to 0 — propagate the effect.
{% endhint %}

{% hint style="danger" %}
**Gotcha 3: Space optimization with diagonals**

For Maximal Square, dp[i][j] depends on dp[i-1][j-1] (the diagonal). In the 1D array, dp[j-1] has ALREADY been overwritten to the current row's value. You need a `prev_diag` variable to save the old dp[j] before overwriting it.
{% endhint %}

{% hint style="danger" %}
**Gotcha 4: 3D DP memory explosion**

Cherry Pickup I with n=50 needs dp[100][50][50] = 250,000 entries. That fits in memory. But if you accidentally allocate dp[50][50][50] for each of 100 steps without reusing space, you use 25x more memory than needed. Always space-optimize.
{% endhint %}

{% hint style="danger" %}
**Gotcha 5: Reverse DP direction**

The Dungeon Game requires filling from bottom-right to top-left. If you accidentally fill top-left to bottom-right (the natural direction), your recurrence depends on values that have not been computed yet. Always trace the data dependencies.
{% endhint %}

{% hint style="danger" %}
**Gotcha 6: max(1, ...) in the Dungeon Game**

Health must be >= 1 at ALL times. If you compute dp[i][j] = min_next - dungeon[i][j] and forget the max(1, ...), you might get dp values of 0 or negative, which means "the knight is dead." Always clamp to at least 1.
{% endhint %}

{% hint style="danger" %}
**Gotcha 7: Cherry Pickup — same cell, count once**

When two agents are on the same cell, the cherry is collected only ONCE. If you add grid[r1][c1] + grid[r2][c2] without checking r1 == r2, you double-count. Always check: `cherries = grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0)`.
{% endhint %}

{% hint style="danger" %}
**Gotcha 8: Backtracking vs DP**

Unique Paths III (visit every cell exactly once) is NOT a standard DP problem — it requires backtracking. The constraint "visit every cell" means you cannot decompose the problem into independent subproblems the usual way. When you see "visit all" or "Hamiltonian path," think backtracking, not grid DP.
{% endhint %}

---

## Practice Problems

| # | Name | Difficulty | Key Concept | Hint |
|---|------|-----------|-------------|------|
| W1 | Unique Paths | ★ | dp[j] += dp[j-1], 1D array | First row/col are all 1s |
| W2 | Unique Paths with Obstacles | ★ | Set dp = 0 for blocked cells | Obstacle in row 0 blocks rightward |
| W3 | Minimum Path Sum | ★ | dp[j] = min(dp[j], dp[j-1]) + grid[i][j] | Space-optimize to 1 row |
| W4 | Triangle Minimum Total | ★ | Bottom-up: dp[j] = tri[i][j] + min(dp[j], dp[j+1]) | Start from last row |
| P1 | Unique Paths III | ★★ | Backtracking, not DP | Count empty cells, DFS with visited marking |
| P2 | Minimum Falling Path Sum | ★★ | 3 choices per cell (down/diag-left/diag-right) | Watch boundary conditions |
| P3 | Maximal Square | ★★ | dp[i][j] = min(left, above, diag) + 1 | Track prev_diag for space opt |
| P4 | Cherry Pickup II | ★★ | 3D DP: dp[c1][c2] per row, 9 moves | Robots start at columns 0 and n-1 |
| P5 | Count Square Submatrices | ★★ | Same as Maximal Square, sum instead of max | dp value = number of squares ending here |
| C1 | Dungeon Game | ★★★ | Reverse DP from (m-1,n-1) to (0,0) | max(1, min_next - dungeon[i][j]) |
| C2 | Maximal Rectangle | ★★★ | Histogram heights + stack per row | Build heights row by row |
| C3 | Ninja Training | ★★★ | dp[day][activity], can not repeat | max(prev[k] for k != j) + points[i][j] |
| C4 | Cherry Pickup I | ★★★ | 3D DP: two walkers, same direction | Round trip = two simultaneous forward walks |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
# ── 2D DP table creation ──
dp = [[0] * n for _ in range(m)]

# ── Space-optimized 1D row ──
dp = [0] * n
for i in range(m):
    for j in range(n):
        dp[j] = f(dp[j], dp[j-1])  # dp[j] = "from above", dp[j-1] = "from left"

# ── prev_diag trick for square DP ──
prev_diag = 0
for j in range(n):
    temp = dp[j]        # save current (will be prev_diag for next j)
    dp[j] = new_value   # overwrite
    prev_diag = temp     # use saved value next iteration

# ── Bottom-up triangle ──
dp = triangle[-1][:]     # copy last row
for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

# ── Negative infinity for unreachable states ──
NEG_INF = float('-inf')
```
{% endtab %}
{% tab title="Java" %}
```java
// ── 2D DP table creation ──
int[][] dp = new int[m][n];

// ── Space-optimized 1D row ──
int[] dp = new int[n];
for (int i = 0; i < m; i++)
    for (int j = 0; j < n; j++)
        dp[j] = f(dp[j], dp[j-1]);

// ── prev_diag trick ──
int prevDiag = 0;
for (int j = 0; j < n; j++) {
    int temp = dp[j];
    dp[j] = newValue;
    prevDiag = temp;
}

// ── Clone an array row ──
int[] dp = lastRow.clone();

// ── Fill with sentinel ──
Arrays.fill(dp, Integer.MAX_VALUE);
```
{% endtab %}
{% tab title="C++" %}
```cpp
// ── 2D DP table creation ──
vector<vector<int>> dp(m, vector<int>(n, 0));

// ── Space-optimized 1D row ──
vector<int> dp(n);
for (int i = 0; i < m; i++)
    for (int j = 0; j < n; j++)
        dp[j] = f(dp[j], dp[j-1]);

// ── prev_diag trick ──
int prevDiag = 0;
for (int j = 0; j < n; j++) {
    int temp = dp[j];
    dp[j] = newValue;
    prevDiag = temp;
}

// ── min of three values ──
dp[j] = min({dp[j], dp[j-1], prevDiag}) + 1;

// ── Copy last row ──
vector<int> dp = triangle.back();
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 23** (DP I — The Foundation) gave you the DP Recipe, the four-stage progression, and 1D patterns like climbing stairs and house robber. This chapter extends EVERYTHING to 2D — same recipe, bigger table.
- **Ch 10** (Recursion) gave you the DFS/backtracking skills needed for Unique Paths III.
- **Ch 6** (How Fast Is Your Code?) taught you to analyze nested loops — now you see that two nested loops over an m x n grid give O(m*n).

### Looking Forward
- **Ch 25** (DP III — Subsequences and Knapsack): DP on pairs of sequences (LCS, edit distance) and the 0-1 Knapsack. Same 2D table, different meaning.
- **Ch 26** (DP IV — Strings): DP on strings, palindromes, and regex matching. The 2D table techniques from this chapter transfer directly.
- **Ch 31** (Advanced DP): Bitmask DP, interval DP, DP on trees — advanced patterns that build on everything here.

### Cross-Chapter Threads
- **"Trade space for time"**: The 2D-to-1D space optimization is a masterclass in this thread. We spend O(m*n) time to avoid 2^(m+n) brute-force paths, and then trade O(m*n) space down to O(n) by reusing one row.
- **"Reduce to known"**: Cherry Pickup I reduces a "round trip" problem to "two forward walks." Maximal Rectangle reduces a 2D problem to "1D histogram per row." Reduction is the most powerful problem-solving tool.
- **"Brute force is a strategy"**: Every problem in this chapter starts with a brute-force recursive solution. We optimize from there. Never skip step 1.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"We optimized 2D grid DP to O(n) space. But what about problems where dp[i][j] depends on dp[i-1][j-1] (the diagonal)? How do we handle that extra dependency?"** Hint: you already saw the answer in Maximal Square — one extra variable, `prev_diag`. But what if the dependency reaches further back?

2. **"Grid DP works when you move right/down. What if you can move in ALL FOUR directions (up, down, left, right)? Can DP still work?"** Hint: standard DP cannot handle cycles. You would need shortest-path algorithms like BFS or Dijkstra. But there IS a DP variant for DAGs (directed acyclic graphs). Can you figure out when a grid IS a DAG?

3. **"We used 3D DP for two agents. What if there are THREE agents? Four?"** Hint: the state space explodes — dp[pos1][pos2][pos3] is O(n^3) per step. For k agents, it is O(n^k). At some point, you need bitmask DP or other tricks. Coming in Ch 31.

---

## What's Next

You have just conquered the second dimension. You know how to fill a 2D DP table, optimize it to 1D, handle obstacles, triangles, falling paths, two-agent problems, squares, rectangles, and even reverse DP.

But so far, all our 2D DP problems have been on grids — the "state" is a position (i, j). What happens when the two dimensions represent positions in two DIFFERENT sequences? That is the world of subsequences and knapsack.

In Ch 25 (**Dynamic Programming III — Subsequences and Knapsack**), you will learn the Longest Common Subsequence (LCS), 0-1 Knapsack, coin change, and subset sum. The 2D table works the same way — but now dp[i][j] means "considering the first i items of sequence A and the first j items of sequence B." The DP Recipe scales beautifully.

Get ready to combine sequences!
