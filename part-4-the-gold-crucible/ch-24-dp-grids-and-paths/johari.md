# Johari Window: Chapter 24 — Dynamic Programming II — Grids and Paths

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about 2D DP, grid paths, and space optimization.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] The DP Recipe: state, recurrence, base case, fill order, optimize space (from Ch 23)
> - [ ] Top-down vs. bottom-up DP (from Ch 23)
> - [ ] How to space-optimize 1D DP from an array to two variables
> - [ ] That dp[i][j] can represent subproblems indexed by two dimensions
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] How to fill a 2D DP table row by row
> - [ ] What "space optimization" means for a 2D DP table
> - [ ] How to count paths in a grid using DP
> - [ ] What a "triangle DP" problem looks like
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] How DP works when two agents move simultaneously (3D DP)
> - [ ] How to find the largest square or rectangle of all 1s
> - [ ] What "reverse DP" means (working backwards from the destination)
> - [ ] How to reduce a 2D DP table to a 1D array
> - [ ] _________________________________

### Unknown (I haven't even thought about)
> Things I don't know that I don't know — leave blank now, fill in after!
> - [ ] _________________________________
> - [ ] _________________________________
> - [ ] _________________________________

---

## After This Chapter

Come back here after finishing the chapter. Compare with your "Before" answers!

### Open — Expanded (Now I truly understand)
> - [ ] 2D DP: dp[i][j] fills a grid row by row, depending on dp[i-1][j] and dp[i][j-1]
> - [ ] Space optimization: since each row only depends on the previous row, use a 1D array
> - [ ] Unique Paths = dp[i][j] = dp[i-1][j] + dp[i][j-1], first row/col all 1s
> - [ ] Obstacles: set dp[i][j] = 0 for blocked cells
> - [ ] Min Path Sum: dp[i][j] = grid[i][j] + min(from_above, from_left)
> - [ ] Triangle: work bottom-up, dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
> - [ ] 3D DP: two agents modeled as dp[step][agent1_pos][agent2_pos]
> - [ ] Maximal Square: dp[i][j] = min(left, above, diagonal) + 1
> - [ ] Dungeon Game: reverse DP — dp[i][j] = min health needed FROM this cell TO end
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That maximal square and count squares use the SAME recurrence — just aggregate differently!
> - [ ] That the Dungeon Game requires thinking BACKWARDS, not forwards
> - [ ] That Cherry Pickup (round trip) can be modeled as two simultaneous forward walks
> - [ ] That reducing 2D DP to 1D only requires one extra variable (prev_diag) for square problems
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Deciding when to use 2D DP vs. 3D DP
> - [ ] Space-optimizing 2D DP without making errors (the prev_diag trick)
> - [ ] Recognizing when to use reverse DP (destination to source)
> - [ ] Writing the maximal rectangle histogram stack solution from scratch
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] How does DP work on strings (like longest common subsequence)?
> - [ ] What about the 0-1 knapsack — how is it different from grid DP?
> - [ ] Can DP handle problems on trees or graphs, not just grids?
> - [ ] How would I solve Cherry Pickup I if the grid were very large (n=500)?
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 25 (Subsequences and Knapsack) and Ch 26 (Strings DP) — the patterns from this chapter extend beautifully to new problem families!
