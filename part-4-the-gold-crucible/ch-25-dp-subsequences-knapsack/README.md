# Dynamic Programming III — Subsequences & Knapsack

{% hint style="info" %}
**This chapter is the crown jewel of DP.** If Ch 23 taught you to walk and Ch 24 taught you to run on grids, this chapter teaches you to FLY. The Knapsack problem, Longest Common Subsequence, Edit Distance, and Longest Increasing Subsequence are among the most frequently tested topics in USACO Gold, coding interviews, and competitive programming. Master these patterns, and you will recognize them everywhere.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Solve the 0/1 Knapsack problem: maximize value within a weight capacity
- Understand why iterating BACKWARDS makes items single-use (0/1) while FORWARDS allows reuse (unbounded)
- Solve Subset Sum: can a subset reach a target value?
- Solve both Coin Change variants: minimum coins and count combinations
- Compute the Longest Common Subsequence (LCS) of two strings
- Compute Edit Distance (Levenshtein distance) between two strings
- Find the Longest Increasing Subsequence (LIS) using both O(n^2) DP and O(n log n) binary search
- Solve DP on strings: distinct subsequences, wildcard matching, shortest common supersequence
- Reduce advanced problems to known patterns: Target Sum to Subset Sum, Min Palindrome Insertions to LCS
- Reconstruct actual solutions from DP tables (not just optimal values)
- Apply the Knapsack family to real competitive programming problems
- Recognize which Knapsack variant a new problem maps to

---

## The Story: "The Backpacker"

Maya was packing for the trip of a lifetime — a month-long hike through the mountains. Her backpack could hold exactly 7 kilograms. On the table lay four items:

| Item | Weight | Value (to Maya) |
|------|--------|-----------------|
| First aid kit | 1 kg | 1 |
| Warm jacket | 3 kg | 4 |
| Sleeping bag | 4 kg | 5 |
| Cooking set | 5 kg | 7 |

She could not take everything — the total weight was 13 kg, nearly double her capacity. So she had to choose. She tried the greedy approach: "Take the most valuable item first!" That gave her the cooking set (5 kg, value 7) and the first aid kit (1 kg, value 1). Total weight: 6 kg, total value: 8. Not bad.

But then she noticed something. If she took the jacket (3 kg, value 4) and the sleeping bag (4 kg, value 5) instead, the total weight was exactly 7 kg and the total value was 9 — BETTER than the greedy choice!

"Greedy doesn't work here," she realized. "I need to consider ALL combinations."

But with 4 items, there are 2^4 = 16 possible subsets. With 30 items, there would be over a BILLION. She needed a smarter approach.

That evening, Maya pulled out her notebook. "What if I build up the answer piece by piece? For each item, I ask: should I include it or skip it? And for each possible weight limit, I record the best value I can achieve."

She had just invented the Knapsack algorithm. And you are about to learn it.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "The Mini Knapsack"

You have a backpack with capacity 5 kg. Three items are available:

| Item | Weight | Value |
|------|--------|-------|
| A | 2 | 3 |
| B | 3 | 4 |
| C | 4 | 5 |

Which items do you take to maximize value? List all valid combinations and their total values. Is greedy (take the highest value-per-weight ratio first) optimal here?

{% hint style="info" %}
There are 8 possible subsets (including empty). The best is A+B (weight 5, value 7). Notice that greedy by ratio (A has ratio 1.5, B has 1.33, C has 1.25) would also pick A first, then B — greedy works here! But can you construct a case where greedy fails? Hint: make the ratios misleading.
{% endhint %}

### Puzzle 2: "Common Letters"

Find the longest sequence of letters that appears in BOTH strings (in order, but not necessarily consecutive):

- String 1: **ABCBDAB**
- String 2: **BDCAB**

Try to find it by hand. The answer is 4 — can you find a subsequence of length 4?

{% hint style="info" %}
One answer is **BCAB** (length 4). Another is **BDAB**. This is the Longest Common Subsequence (LCS) problem. To solve it systematically, we build a 2D table.
{% endhint %}

### Puzzle 3: "Making Change"

You have coins of denominations 1, 5, and 11 cents. What is the minimum number of coins to make exactly 15 cents?

- Greedy: use the largest coin first. 11 + 1 + 1 + 1 + 1 = 15 (5 coins)
- Better: 5 + 5 + 5 = 15 (3 coins!)

Greedy fails here. Why? Because the locally optimal choice (grab the 11-cent coin) leads to a worse total.

{% hint style="info" %}
Coin Change requires DP because each coin choice affects what remains, and the greedy choice is not always optimal. `dp[amount] = min coins to make that amount`.
{% endhint %}

---

## 25.1 The Knapsack Family

The Knapsack problem is one of the most important in computer science. It has several variants, and MANY problems reduce to one of them.

| Variant | Items Reusable? | DP Direction | Key Question |
|---------|----------------|--------------|--------------|
| **0/1 Knapsack** | No (use each at most once) | Backwards | Max value within weight limit |
| **Unbounded Knapsack** | Yes (unlimited copies) | Forwards | Max value with reuse |
| **Subset Sum** | No | Backwards | Can we reach exactly this sum? |
| **Coin Change (min)** | Yes | Forwards | Min coins to reach amount |
| **Coin Change (count)** | Yes | Coins-first loop | How many ways to reach amount? |
| **Target Sum** | No | Backwards | How many +/- assignments reach target? |
| **Rod Cutting** | Yes | Forwards | Max revenue from cuts |

The beautiful thing: they all share the same core idea. Once you understand 0/1 Knapsack, the rest are variations on a theme.

---

## 25.2 0/1 Knapsack

**Problem**: Given `n` items with weights and values, and a knapsack capacity `W`, find the maximum total value of items that fit.

### The Recurrence

For each item `i`, we have two choices:
- **Skip it**: the best value stays `dp[i-1][w]`
- **Take it** (if it fits): we gain `values[i]` but lose `weights[i]` capacity, so `dp[i-1][w - weights[i]] + values[i]`

**dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i]] + values[i])**

### Space Optimization: The Magic of Backwards

We can compress the 2D table to a 1D array. The trick: **iterate capacity from right to left** (backwards). This ensures that when we compute `dp[w]`, the value `dp[w - weights[i]]` still reflects the PREVIOUS item's row (not the current one). If we went left to right, we might use item `i` twice!

{% tabs %}
{% tab title="Python" %}
```python
def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):  # BACKWARDS!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
```
{% endtab %}
{% tab title="Java" %}
```java
static int knapsack01(int[] weights, int[] values, int capacity) {
    int[] dp = new int[capacity + 1];
    for (int i = 0; i < weights.length; i++)
        for (int w = capacity; w >= weights[i]; w--)  // BACKWARDS!
            dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
    return dp[capacity];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int knapsack01(vector<int>& weights, vector<int>& values, int capacity) {
    vector<int> dp(capacity + 1, 0);
    for (int i = 0; i < (int)weights.size(); i++)
        for (int w = capacity; w >= weights[i]; w--)  // BACKWARDS!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);
    return dp[capacity];
}
```
{% endtab %}
{% endtabs %}

> **Language Spotlight: 0/1 Knapsack**
> | | Python | Java | C++ |
> |---|--------|------|-----|
> | Backwards loop | `range(cap, w-1, -1)` | `for(w=cap; w>=w[i]; w--)` | `for(w=cap; w>=w[i]; w--)` |
> | Array init | `[0] * (cap + 1)` | `new int[cap + 1]` | `vector<int>(cap+1, 0)` |

**Time**: O(n * capacity). **Space**: O(capacity).

---

## 25.3 Unbounded Knapsack & Rod Cutting

### Unbounded Knapsack

Same as 0/1, but each item can be used **unlimited times**. The only change: iterate capacity **forwards** (left to right). This lets `dp[w - weights[i]]` use the current item's updated value — allowing reuse.

{% tabs %}
{% tab title="Python" %}
```python
def knapsack_unbounded(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # FORWARDS!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
```
{% endtab %}
{% tab title="Java" %}
```java
static int knapsackUnbounded(int[] weights, int[] values, int capacity) {
    int[] dp = new int[capacity + 1];
    for (int i = 0; i < weights.length; i++)
        for (int w = weights[i]; w <= capacity; w++)  // FORWARDS!
            dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
    return dp[capacity];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int knapsackUnbounded(vector<int>& weights, vector<int>& values, int capacity) {
    vector<int> dp(capacity + 1, 0);
    for (int i = 0; i < (int)weights.size(); i++)
        for (int w = weights[i]; w <= capacity; w++)  // FORWARDS!
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i]);
    return dp[capacity];
}
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**The critical insight**: The ONLY difference between 0/1 and unbounded knapsack is the direction of the inner loop. Backwards = use once. Forwards = reuse. This is one of the most important DP facts to memorize.
{% endhint %}

### Rod Cutting

**Problem**: Given a rod of length `n` and prices for each piece length, find the maximum revenue.

This IS unbounded knapsack! The "items" are piece lengths 1 through n, the "weights" are the lengths, and the "values" are the prices.

```python
def rod_cutting(prices):
    n = len(prices)
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for k in range(1, length + 1):
            dp[length] = max(dp[length], dp[length - k] + prices[k - 1])
    return dp[n]
```

---

## 25.4 Subset Sum & Partition

### Subset Sum

**Problem**: Given integers and a target, can any subset sum to exactly the target?

This is 0/1 Knapsack with boolean values: `dp[s] = True if sum s is achievable`.

```python
def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):  # backwards (0/1)
            if dp[s - num]:
                dp[s] = True
    return dp[target]
```

### Partition Equal Subset Sum

**Problem**: Can the array be split into two subsets with equal sum?

**Reduction**: If the total sum is odd, impossible. Otherwise, this is Subset Sum with target = total / 2.

### Target Sum

**Problem**: Assign + or - to each element to reach a target. Count the ways.

**Reduction**: Let P = sum of positives, N = sum of negatives. Then P + N = total and P - N = target. So P = (total + target) / 2. Count subsets summing to P — this is a **Subset Sum Count** problem.

---

## 25.5 Coin Change

### Minimum Coins

**Problem**: Given coin denominations and an amount, find the minimum coins needed.

This is unbounded knapsack (coins can be reused) with **min** instead of max.

{% tabs %}
{% tab title="Python" %}
```python
def coin_change_min(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```
{% endtab %}
{% tab title="Java" %}
```java
static int coinChangeMin(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;
    for (int a = 1; a <= amount; a++)
        for (int coin : coins)
            if (coin <= a) dp[a] = Math.min(dp[a], dp[a - coin] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int coinChangeMin(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int a = 1; a <= amount; a++)
        for (int coin : coins)
            if (coin <= a) dp[a] = min(dp[a], dp[a - coin] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}
```
{% endtab %}
{% endtabs %}

### Count Combinations

**Problem**: Count the number of distinct combinations that sum to the amount.

The key insight: iterate **coins in the outer loop** and amounts in the inner loop. This ensures we count combinations (not permutations). If you swap the loops, you count permutations instead.

```python
def coin_change_count(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:        # coins OUTER
        for a in range(coin, amount + 1):  # forwards (unbounded)
            dp[a] += dp[a - coin]
    return dp[amount]
```

{% hint style="warning" %}
**Combinations vs. Permutations**: Coins outer = combinations (1+2 and 2+1 counted once). Amounts outer = permutations (1+2 and 2+1 counted separately). For Coin Change II, we want combinations.
{% endhint %}

---

## 25.6 Longest Common Subsequence (LCS)

**Problem**: Given two strings, find the length of their longest common subsequence.

### The Recurrence

Compare characters one at a time:
- If `text1[i-1] == text2[j-1]`: this character is part of the LCS. `dp[i][j] = dp[i-1][j-1] + 1`
- Otherwise: skip one character from either string. `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

{% tabs %}
{% tab title="Python" %}
```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    prev = [0] * (n + 1)
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[n]
```
{% endtab %}
{% tab title="Java" %}
```java
static int lcs(String a, String b) {
    int m = a.length(), n = b.length();
    int[] prev = new int[n + 1];
    for (int i = 1; i <= m; i++) {
        int[] curr = new int[n + 1];
        for (int j = 1; j <= n; j++) {
            if (a.charAt(i-1) == b.charAt(j-1)) curr[j] = prev[j-1] + 1;
            else curr[j] = Math.max(prev[j], curr[j-1]);
        }
        prev = curr;
    }
    return prev[n];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int lcs(const string& a, const string& b) {
    int m = a.size(), n = b.size();
    vector<int> prev(n + 1, 0);
    for (int i = 1; i <= m; i++) {
        vector<int> curr(n + 1, 0);
        for (int j = 1; j <= n; j++) {
            if (a[i-1] == b[j-1]) curr[j] = prev[j-1] + 1;
            else curr[j] = max(prev[j], curr[j-1]);
        }
        prev = curr;
    }
    return prev[n];
}
```
{% endtab %}
{% endtabs %}

**Time**: O(m * n). **Space**: O(n) with two-row optimization.

### Reconstructing the LCS

To get the actual LCS string (not just its length), keep the full 2D table and backtrack from `dp[m][n]`:

```python
# After building the 2D dp table:
i, j = m, n
result = []
while i > 0 and j > 0:
    if text1[i-1] == text2[j-1]:
        result.append(text1[i-1])
        i -= 1; j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1
return ''.join(reversed(result))
```

---

## 25.7 Edit Distance

**Problem**: Find the minimum number of operations (insert, delete, replace) to convert `word1` into `word2`.

### The Recurrence

- If characters match: `dp[i][j] = dp[i-1][j-1]` (no operation needed)
- Otherwise: `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
  - `dp[i-1][j]` = delete from word1
  - `dp[i][j-1]` = insert into word1
  - `dp[i-1][j-1]` = replace

Base cases: `dp[i][0] = i` (delete all of word1), `dp[0][j] = j` (insert all of word2).

{% tabs %}
{% tab title="Python" %}
```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
        prev = curr
    return prev[n]
```
{% endtab %}
{% tab title="Java" %}
```java
static int editDistance(String a, String b) {
    int m = a.length(), n = b.length();
    int[] prev = new int[n + 1];
    for (int j = 0; j <= n; j++) prev[j] = j;
    for (int i = 1; i <= m; i++) {
        int[] curr = new int[n + 1];
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (a.charAt(i-1) == b.charAt(j-1)) curr[j] = prev[j-1];
            else curr[j] = 1 + Math.min(prev[j], Math.min(curr[j-1], prev[j-1]));
        }
        prev = curr;
    }
    return prev[n];
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int editDistance(const string& a, const string& b) {
    int m = a.size(), n = b.size();
    vector<int> prev(n + 1);
    iota(prev.begin(), prev.end(), 0);  // fill with 0,1,2,...,n
    for (int i = 1; i <= m; i++) {
        vector<int> curr(n + 1);
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (a[i-1] == b[j-1]) curr[j] = prev[j-1];
            else curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});
        }
        prev = curr;
    }
    return prev[n];
}
```
{% endtab %}
{% endtabs %}

> **Language Spotlight: Edit Distance**
> | | Python | Java | C++ |
> |---|--------|------|-----|
> | Min of 3 | `min(a, b, c)` | `Math.min(a, Math.min(b, c))` | `min({a, b, c})` |
> | Range init | `list(range(n+1))` | `for(j=0;j<=n;j++) prev[j]=j` | `iota(begin, end, 0)` |

**Time**: O(m * n). **Space**: O(n).

{% hint style="info" %}
**LCS and Edit Distance are related.** For strings of length m and n with LCS length L:
- Edit distance >= m + n - 2L
- If only insert and delete are allowed (no replace), edit distance = m + n - 2L exactly.
{% endhint %}

---

## 25.8 Longest Increasing Subsequence (LIS)

**Problem**: Find the length of the longest strictly increasing subsequence in an array.

### Approach 1: O(n^2) DP

`dp[i]` = length of the LIS ending at index `i`. For each `i`, check all `j < i` where `nums[j] < nums[i]`.

{% tabs %}
{% tab title="Python" %}
```python
def lis_n2(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```
{% endtab %}
{% tab title="Java" %}
```java
static int lisN2(int[] nums) {
    int n = nums.length;
    int[] dp = new int[n];
    Arrays.fill(dp, 1);
    int best = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++)
            if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
        best = Math.max(best, dp[i]);
    }
    return best;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int lisN2(vector<int>& nums) {
    int n = nums.size();
    vector<int> dp(n, 1);
    int best = 1;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++)
            if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
        best = max(best, dp[i]);
    }
    return best;
}
```
{% endtab %}
{% endtabs %}

### Approach 2: O(n log n) with Binary Search (Patience Sorting)

Maintain an array `tails` where `tails[k]` is the smallest possible tail element of an increasing subsequence of length `k+1`. For each element, binary search for its position in `tails`.

{% tabs %}
{% tab title="Python" %}
```python
from bisect import bisect_left

def lis_nlogn(nums):
    tails = []
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```
{% endtab %}
{% tab title="Java" %}
```java
static int lisNLogN(int[] nums) {
    List<Integer> tails = new ArrayList<>();
    for (int num : nums) {
        int pos = Collections.binarySearch(tails, num);
        if (pos < 0) pos = -(pos + 1);
        if (pos == tails.size()) tails.add(num);
        else tails.set(pos, num);
    }
    return tails.size();
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int lisNLogN(vector<int>& nums) {
    vector<int> tails;
    for (int num : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), num);
        if (it == tails.end()) tails.push_back(num);
        else *it = num;
    }
    return tails.size();
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Why "patience sorting"?** The algorithm was discovered by analyzing the card game Patience (also known as Klondike Solitaire). You deal cards into piles: each card goes on the leftmost pile whose top card is >= the dealt card, or starts a new pile. The number of piles at the end equals the LIS length!
{% endhint %}

---

## 25.9 DP on Strings

### Distinct Subsequences

**Problem**: Count the number of distinct subsequences of `s` that equal `t`.

`dp[j]` = number of ways to form `t[:j]` from `s[:i]`. If `s[i-1] == t[j-1]`, we can either use this character (`dp[j-1]`) or skip it (`dp[j]`). So `dp[j] += dp[j-1]`. Iterate `j` backwards to avoid overwriting.

### Wildcard Matching

**Problem**: Match string `s` against pattern `p` with `?` (any single char) and `*` (any sequence including empty).

`dp[i][j]` = True if `s[:i]` matches `p[:j]`. For `*`: match empty (`dp[i][j-1]`) or extend by one char (`dp[i-1][j]`).

### Shortest Common Supersequence

**Problem**: Find the shortest string having both `str1` and `str2` as subsequences.

**Approach**: Compute the LCS, then backtrack to build the SCS. Characters in the LCS appear once; all others are included from their respective strings.

---

## 25.10 LIS Variations

### Longest String Chain

**Problem**: Find the longest chain of words where each word is a predecessor of the next (add one letter to get the next word).

This is a variant of LIS where "increasing" means "predecessor relationship." Sort by length, then for each word, try removing each character and look up the predecessor in a hash map.

### Minimum Insertions for Palindrome

**Problem**: Find the minimum insertions to make a string a palindrome.

**Key insight**: `min_insertions = len(s) - LPS(s)`, where LPS is the Longest Palindromic Subsequence. And `LPS(s) = LCS(s, reverse(s))`. So we reduce this to LCS!

---

## Five-Lens Framework: 0/1 Knapsack

### Lens 1: Constraints

- `n <= 1000` items, `capacity <= 1000`, values up to 1000
- O(n * capacity) = O(10^6) — well within time limits
- Memory: O(capacity) with 1D optimization

### Lens 2: Brute Force

Try all 2^n subsets, check weight, track max value. Time: O(2^n). For n=30, that is over a billion — way too slow.

### Lens 3: Pattern

For each item: take or skip. The optimal answer for items 1..i at capacity w depends on the optimal answer for items 1..i-1. Overlapping subproblems + optimal substructure = DP.

### Lens 4: Optimization

- 2D table: O(n * W) time and space
- 1D array with backwards iteration: O(n * W) time, O(W) space
- Cannot do better in the general case (NP-hard for exponential W)

### Lens 5: Proof

By induction on the number of items. At each step, "take" or "skip" are exhaustive and mutually exclusive choices. The recurrence picks the max of both, so the result is optimal.

---

## Think Like a Pro

{% hint style="info" %}
**Errichto** (Kamil Debowski): "When I see a DP problem with items and a budget, I immediately think Knapsack. The first question is: can items be reused? If yes, iterate forwards. If no, iterate backwards. That one decision determines the entire algorithm."

*What you can learn*: Train yourself to identify the Knapsack variant in the first 30 seconds. The 0/1 vs. unbounded distinction is the most important classification.
{% endhint %}

{% hint style="info" %}
**Neal Wu**: "LCS and Edit Distance are the bread and butter of string DP. Once you master the 2D table for LCS, at least 5 other problems (SCS, palindromic subsequences, etc.) become trivial reductions."

*What you can learn*: Master LCS deeply — not just the algorithm, but how to reconstruct the answer and how other problems reduce to it.
{% endhint %}

---

## AOPS Showcase: "LIS" — Four Progressive Solutions

The Longest Increasing Subsequence is the perfect problem to demonstrate progressive optimization.

### Approach 1: Brute Force — O(2^n)

Try all subsequences, check if each is increasing, track the longest.

### Approach 2: O(n^2) DP

`dp[i] = max(dp[j] + 1)` for all j < i where `nums[j] < nums[i]`. Simple and clean.

### Approach 3: O(n log n) with Binary Search

Maintain a `tails` array. For each number, use binary search to find where it belongs. The length of `tails` is the LIS length.

### Approach 4: O(n log n) with Patience Sorting Visualization

Same algorithm as Approach 3, but visualized as dealing cards into sorted piles. Each pile's top is the `tails` array.

### Comparison Table

| Approach | Time | Space | Idea |
|----------|------|-------|------|
| Brute Force | O(2^n) | O(n) | Try all subsequences |
| DP | O(n^2) | O(n) | dp[i] = LIS ending at i |
| Binary Search | O(n log n) | O(n) | Maintain smallest tails |
| Patience Sort | O(n log n) | O(n) | Same as binary search, card game visualization |

---

## Legend's Corner

{% hint style="info" %}
**Petr Mitrichev** — Two-time IOI gold, 6-time ICPC World Finals: "The Knapsack problem is one of the first DP problems I learned, and I still see it in disguise in Codeforces Div 1 problems. The trick is not knowing the algorithm — it is recognizing that a new problem IS a Knapsack problem. My advice: after learning each DP pattern, find 10 problems that reduce to it. Build a mental index of reductions."

**What you can learn**: The algorithm is the easy part. The hard part is RECOGNIZING the pattern in a problem that doesn't say "Knapsack" anywhere. Build your pattern library through deliberate practice.
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Gotcha 1: Backwards vs. Forwards confusion**

In 0/1 Knapsack, iterate backwards. In Unbounded Knapsack, iterate forwards. Mixing them up gives wrong answers with no error message — the code runs fine but the results are wrong. This is the #1 Knapsack bug.
{% endhint %}

{% hint style="danger" %}
**Gotcha 2: Combinations vs. Permutations in Coin Change**

To count combinations (order doesn't matter), put coins in the outer loop. To count permutations (order matters), put amounts in the outer loop. The wrong loop order gives a valid but DIFFERENT answer.
{% endhint %}

{% hint style="danger" %}
**Gotcha 3: Off-by-one in LCS/Edit Distance base cases**

`dp[0][j]` and `dp[i][0]` represent empty strings. For Edit Distance, `dp[i][0] = i` (delete all chars from word1). Forgetting these base cases produces wrong answers.
{% endhint %}

{% hint style="danger" %}
**Gotcha 4: Subset Sum with target 0**

An empty subset always sums to 0. So `dp[0] = True` is a critical base case. Without it, the entire DP fails.
{% endhint %}

{% hint style="danger" %}
**Gotcha 5: Target Sum parity check**

In Target Sum, if `(total + target)` is odd, the answer is 0. Also check that `total + target >= 0` and that `(total + target) / 2` is non-negative. Missing these checks causes array index errors.
{% endhint %}

{% hint style="danger" %}
**Gotcha 6: LIS strictly increasing**

LIS requires STRICTLY increasing (not non-decreasing). For the O(n log n) version, use `bisect_left` (Python) or `lower_bound` (C++) for strictly increasing. Use `bisect_right` / `upper_bound` for non-decreasing.
{% endhint %}

{% hint style="danger" %}
**Gotcha 7: Reconstructing SCS requires full 2D table**

The space-optimized 2-row LCS is great for computing the LENGTH, but you cannot backtrack through it to reconstruct the actual string. For Shortest Common Supersequence, keep the full O(m*n) table.
{% endhint %}

{% hint style="danger" %}
**Gotcha 8: Wildcard matching with leading stars**

For the base case `dp[0][j]` (empty string vs. pattern), `*` matches empty. So `dp[0][j] = True` as long as ALL characters in `p[:j]` are `*`. Once you hit a non-star, all subsequent `dp[0][j]` are False.
{% endhint %}

{% hint style="danger" %}
**Gotcha 9: Integer overflow in counting problems**

Distinct Subsequences and Coin Change Count can produce very large numbers. In C++, use `long long`. In Java, watch for integer overflow — the answer can exceed 2^31.
{% endhint %}

---

## Practice Problems

| # | Name | Difficulty | Key Concept |
|---|------|-----------|-------------|
| W1 | 0/1 Knapsack | ★ | Core knapsack: dp[w] backwards |
| W2 | Subset Sum | ★ | Boolean knapsack |
| W3 | Coin Change (Min Coins) | ★ | Unbounded + min |
| W4 | Coin Change II (Count Ways) | ★ | Coins-outer loop for combinations |
| W5 | Longest Common Subsequence | ★ | 2D string DP, match vs. skip |
| P1 | Partition Equal Subset Sum | ★★ | Reduce to Subset Sum with target=sum/2 |
| P2 | Unbounded Knapsack | ★★ | Forwards iteration for reuse |
| P3 | Edit Distance | ★★ | 3 operations: insert, delete, replace |
| P4 | Longest Increasing Subsequence | ★★ | O(n^2) DP or O(n log n) binary search |
| P5 | Distinct Subsequences | ★★ | Count subsequences matching a pattern |
| P6 | Wildcard Matching | ★★ | DP with ?, * pattern operators |
| C1 | Shortest Common Supersequence | ★★★ | LCS + backtrack reconstruction |
| C2 | Rod Cutting | ★★★ | Unbounded knapsack on piece lengths |
| C3 | Target Sum | ★★★ | Reduce +/- assignment to Subset Sum Count |
| C4 | Longest String Chain | ★★★ | LIS variant with predecessor relation |
| C5 | Min Insertions for Palindrome | ★★★ | Reduce to LCS(s, reverse(s)) |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
# ── 0/1 Knapsack pattern ──
dp = [0] * (capacity + 1)
for i in range(n):
    for w in range(capacity, weight[i] - 1, -1):  # BACKWARDS
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])

# ── Unbounded Knapsack pattern ──
for i in range(n):
    for w in range(weight[i], capacity + 1):  # FORWARDS
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i])

# ── LCS pattern ──
prev = [0] * (n + 1)
for i in range(1, m + 1):
    curr = [0] * (n + 1)
    for j in range(1, n + 1):
        if a[i-1] == b[j-1]: curr[j] = prev[j-1] + 1
        else: curr[j] = max(prev[j], curr[j-1])
    prev = curr

# ── LIS with bisect ──
from bisect import bisect_left
tails = []
for num in nums:
    pos = bisect_left(tails, num)
    if pos == len(tails): tails.append(num)
    else: tails[pos] = num
```
{% endtab %}
{% tab title="Java" %}
```java
// ── 0/1 Knapsack pattern ──
int[] dp = new int[capacity + 1];
for (int i = 0; i < n; i++)
    for (int w = capacity; w >= weight[i]; w--)  // BACKWARDS
        dp[w] = Math.max(dp[w], dp[w - weight[i]] + value[i]);

// ── Unbounded Knapsack pattern ──
for (int i = 0; i < n; i++)
    for (int w = weight[i]; w <= capacity; w++)  // FORWARDS
        dp[w] = Math.max(dp[w], dp[w - weight[i]] + value[i]);

// ── LCS pattern ──
int[] prev = new int[n + 1];
for (int i = 1; i <= m; i++) {
    int[] curr = new int[n + 1];
    for (int j = 1; j <= n; j++) {
        if (a.charAt(i-1) == b.charAt(j-1)) curr[j] = prev[j-1] + 1;
        else curr[j] = Math.max(prev[j], curr[j-1]);
    }
    prev = curr;
}

// ── LIS with binary search ──
List<Integer> tails = new ArrayList<>();
for (int num : nums) {
    int pos = Collections.binarySearch(tails, num);
    if (pos < 0) pos = -(pos + 1);
    if (pos == tails.size()) tails.add(num);
    else tails.set(pos, num);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
// ── 0/1 Knapsack pattern ──
vector<int> dp(capacity + 1, 0);
for (int i = 0; i < n; i++)
    for (int w = capacity; w >= weight[i]; w--)  // BACKWARDS
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i]);

// ── Unbounded Knapsack pattern ──
for (int i = 0; i < n; i++)
    for (int w = weight[i]; w <= capacity; w++)  // FORWARDS
        dp[w] = max(dp[w], dp[w - weight[i]] + value[i]);

// ── LCS pattern ──
vector<int> prev(n + 1, 0);
for (int i = 1; i <= m; i++) {
    vector<int> curr(n + 1, 0);
    for (int j = 1; j <= n; j++) {
        if (a[i-1] == b[j-1]) curr[j] = prev[j-1] + 1;
        else curr[j] = max(prev[j], curr[j-1]);
    }
    prev = curr;
}

// ── LIS with lower_bound ──
vector<int> tails;
for (int num : nums) {
    auto it = lower_bound(tails.begin(), tails.end(), num);
    if (it == tails.end()) tails.push_back(num);
    else *it = num;
}
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 23** (DP I — The Foundation) gave you the DP Recipe, top-down vs. bottom-up, and space optimization — all of which we use heavily here
- **Ch 24** (DP II — Grids and Paths) introduced 2D DP tables — LCS and Edit Distance are 2D DP on strings instead of grids

### Looking Forward
- **Ch 26** (Trees) will introduce tree structures — DP on trees combines the recursion from Ch 10 with the DP from this chapter
- **Ch 31** (Advanced DP) will cover Bitmask DP, Interval DP, and DP on Trees — extensions of the patterns you learned here

### Cross-Chapter Threads
- **"Trade space for time"**: The Knapsack DP table uses O(capacity) space to avoid O(2^n) brute force — the ultimate trade. This thread started in Ch 6 (concept), grew through Ch 11 (hash maps), Ch 23 (memoization), and reaches its peak here.
- **"Reduce to known"**: Target Sum reduces to Subset Sum Count. Min Palindrome Insertions reduces to LCS. Rod Cutting reduces to Unbounded Knapsack. The skill of recognizing reductions is what separates Gold from Platinum.
- **"Brute force is a strategy"**: Every Knapsack problem starts with "try all subsets" — O(2^n). DP makes it polynomial. But writing the brute force FIRST helps you discover the recurrence.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"We solved 0/1 Knapsack in O(n * W) time. But what if W is enormous (like 10^18)? The DP table would be too big. Is there a way to handle large capacities?"** Hint: if the number of items is small (n <= 40), you can split items into two halves and use "meet in the middle" — enumerate all 2^20 subsets for each half and combine. This is beyond standard DP but appears in competitive programming.

2. **"LCS runs in O(m * n) time. For two strings of length 10^5, that is 10^10 operations — too slow. Can we do better?"** For general strings, O(mn) is essentially optimal. But for special cases (like when the alphabet is small or the LCS is short), there are faster algorithms using bitmask tricks.

3. **"We used DP to find the LENGTH of the LIS in O(n log n). But what if we need to PRINT the actual subsequence? Can we still do it in O(n log n)?"** Yes! Maintain a parent pointer for each element and backtrack. The `tails` array alone is NOT the LIS — it just tells you the length.

---

## What's Next

You have now mastered the three pillars of Dynamic Programming: linear DP (Ch 23), grid DP (Ch 24), and subsequence/knapsack DP (this chapter). These cover the vast majority of DP problems in USACO Gold and coding interviews.

But DP can go even further. What happens when you need to solve problems on trees? How do you find the diameter of a tree, or the maximum independent set? What about problems where the state is a bitmask of which elements you have visited?

In **Ch 26 (Trees — The Branching World)**, you will learn about tree traversals, tree DP, and how recursive structures lead to elegant recursive solutions. And later in **Ch 31 (Advanced DP)**, you will tackle Bitmask DP, Interval DP, and Digit DP — the advanced techniques that unlock USACO Platinum.

The journey continues!
