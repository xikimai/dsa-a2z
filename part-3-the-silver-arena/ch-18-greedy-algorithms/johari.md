# Johari Window: Chapter 18 — Greedy Algorithms — The Smart Shortcut

Use this worksheet **before** and **after** studying the chapter. Be honest — there are no wrong answers! This is a tool for YOU to track your own growth.

---

## Before This Chapter

Think about what you already know (or think you know) about greedy algorithms, optimization, and proof techniques.

### Open (I know well)
> Things I'm confident I understand:
> - [ ] What "optimization" means (finding the best answer, not just any answer)
> - [ ] That sorting helps many problems (from Ch 8)
> - [ ] That complete search tries every possibility (from Ch 13)
> - [ ] That some problems have faster solutions than brute force
> - [ ] _________________________________

### Hidden (I think I know but I'm not sure)
> Things I've heard of but couldn't explain clearly:
> - [ ] What "greedy" means in algorithm design
> - [ ] When greedy gives the right answer vs. when it doesn't
> - [ ] What the "greedy choice property" is
> - [ ] How to prove a greedy algorithm is correct
> - [ ] _________________________________

### Blind Spot (I know I don't know)
> Things I know exist but haven't learned:
> - [ ] The exchange argument proof technique
> - [ ] Activity selection / interval scheduling algorithms
> - [ ] Why fractional knapsack is greedy but 0/1 knapsack needs DP
> - [ ] How to solve jump game, interval merging, and job sequencing
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
> - [ ] Greedy = make the locally optimal choice at each step, never look back
> - [ ] Greedy needs TWO properties: greedy choice property + optimal substructure
> - [ ] The exchange argument proves greedy works by swapping non-greedy choices without worsening the solution
> - [ ] Activity selection: sort by END time (not start, not duration!)
> - [ ] Fractional knapsack: sort by value/weight ratio. 0/1 knapsack: greedy FAILS, need DP
> - [ ] Most greedy algorithms follow: SORT → SCAN → PICK locally best → never go back
> - [ ] The 2-minute counterexample test: if you can break it in 2 minutes, greedy is wrong
> - [ ] _________________________________

### Surprised Me! (was Unknown/Blind Spot, now Open)
> - [ ] That the SAME problem (knapsack) can be greedy or not depending on whether you allow fractions!
> - [ ] That sorting by the WRONG criterion (start time vs end time) makes greedy give wrong answers
> - [ ] That the exchange argument is actually a simple, mechanical proof technique once you learn the template
> - [ ] That Dijkstra's shortest path (Ch 27) and Kruskal's MST (Ch 29) are both greedy algorithms!
> - [ ] _________________________________

### Still Working On (honest self-assessment)
> - [ ] Choosing the right sorting criterion for a new greedy problem
> - [ ] Writing a clean exchange argument proof without hints
> - [ ] Recognizing the difference between "greedy works" and "greedy feels like it works"
> - [ ] Knowing when to give up on greedy and switch to DP
> - [ ] _________________________________

### Questions I Now Have (new curiosity!)
> - [ ] What is dynamic programming, and how does it handle the problems where greedy fails? (Hint: Ch 23!)
> - [ ] Are there problems where greedy gives a "good enough" answer even if not optimal? (approximation algorithms)
> - [ ] Can the exchange argument prove other things besides greedy correctness?
> - [ ] How do Dijkstra and Kruskal use the greedy choice property? (Hint: Ch 27, 29!)
> - [ ] _________________________________

---

**Tip:** Revisit this page after completing Ch 23 (DP I) — you'll finally see what happens when greedy fails and you need to consider ALL choices!
