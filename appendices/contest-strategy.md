# Contest Strategy & Time Management

You have spent months (maybe over a year!) learning algorithms, solving practice problems, and building your skills chapter by chapter. Now it is time to put it all together in a real contest. This appendix is your game-day playbook.

Contests are a different beast from practice. In practice, you can take as long as you want, look things up, and try a dozen approaches. In a contest, you have a clock ticking down, your palms might be sweaty, and that problem you thought would be easy suddenly has a tricky edge case you did not see coming.

The good news? Contest skills are learnable. They are not about being "naturally fast" or "naturally calm." They are specific, trainable habits. And this appendix will teach you every single one.

---

## A.1 Before the Contest

The contest does not start when the timer begins. It starts the night before.

### The Night Before

**Do NOT cram new algorithms.** If you do not know segment trees by the night before a Gold contest, you are not going to learn them in one evening. Instead:

- **Review your templates and snippets.** Read through your code library. Remind yourself what you have ready to use. (See the "Templates" section below.)
- **Solve one or two easy problems.** This is like a basketball player shooting free throws before a game. It warms up your brain and builds confidence.
- **Pick out what you will wear and eat.** Seriously. Deciding what to have for breakfast during the contest is a waste of mental energy. Decide now.
- **Set TWO alarms.** Missing a contest because your alarm did not go off is one of the worst feelings in competitive programming.

{% hint style="warning" %}
**Sleep matters more than last-minute studying.** A well-rested brain solves problems faster than a tired brain that memorized one more algorithm. Aim for 8 hours of sleep. Your future self will thank you.
{% endhint %}

### Check Your Setup

An hour before the contest, run through this checklist:

| Item | Check |
|------|-------|
| **Computer** | Charged or plugged in? |
| **Internet** | Stable connection? Backup plan (phone hotspot)? |
| **IDE / Editor** | Open and working? Can you compile and run code? |
| **USACO login** | Can you log in to usaco.org? (Do not wait until the contest starts to discover your password is wrong.) |
| **Browser** | Contest page bookmarked or easy to find? |
| **Templates** | Copied into your working directory, ready to paste? |
| **Water & snack** | Within arm's reach? |
| **Bathroom** | Go now, not 45 minutes into the contest. |
| **Phone** | Silent and out of sight. Distractions are the enemy. |

### Your Template Library

Throughout this book, you have built up algorithms and data structures. The top competitive programmers keep pre-written, pre-tested templates ready to paste into their code. This is not cheating — it is smart preparation.

{% hint style="info" %}
**Benq's template philosophy**: Benq (Benjamin Qi, multiple USACO Finalist and IOI medalist) has a template with 50+ helper functions ready to go, tested and refined over years of contests. His reasoning: contest time should go to THINKING about the problem, not to retyping a Union-Find class you have written a hundred times. (See Ch 4 for more on this debate, and Ch 29 for Union-Find templates.)
{% endhint %}

Here is a starter template library organized by division:

**Bronze templates:**
- Fast I/O setup (all three languages)
- Common helper functions (min, max, gcd)

**Silver templates:**
- Binary search (on arrays and on answers — Ch 16)
- BFS/DFS graph traversal (Ch 19-20)
- Prefix sums (1D and 2D — Ch 14)

**Gold templates:**
- Union-Find with path compression and union by rank (Ch 29)
- Segment tree with lazy propagation (Ch 30)
- Dijkstra's algorithm (Ch 27)
- Topological sort (Ch 28)

**Platinum templates:**
- Segment tree with lazy propagation (Ch 30)
- Convex hull (Ch 34)
- String hashing and KMP (Ch 32)
- LCA with binary lifting (Ch 33)

{% hint style="warning" %}
**Important rule**: Only include templates for algorithms you UNDERSTAND. Pasting a segment tree template you do not understand is worse than writing a brute-force solution you do understand. When something goes wrong (and it will), you need to be able to debug your code. You cannot debug code you do not understand.
{% endhint %}

---

## A.2 The First 15 Minutes: Reading All Problems

The contest has started. The clock is ticking. Your instinct says: "Jump into Problem 1 immediately!"

**Fight that instinct.** The first 15 minutes are the most important of the entire contest, and you should spend them reading, not coding.

### Why Read All Problems First?

Here is a scenario that happens to beginners all the time:

> You see Problem 1, think "I can do this!", and start coding. You spend 90 minutes on it, get stuck on edge cases, and finally solve it. Then you look at Problem 3 — and realize it is a straightforward BFS that you could have solved in 20 minutes. But now you only have 50 minutes left and you are mentally exhausted.

If you had read all three problems first, you would have started with Problem 3, solved it quickly, and then had plenty of time for Problem 1.

**USACO problems are NOT ordered by difficulty.** Problem 1 is not always easiest. Problem 3 is not always hardest. The ordering is essentially random. You must read all of them to find your best starting point.

### How to Skim a Problem (5 Minutes Each)

For each problem, do a quick scan:

1. **Read the problem title and first paragraph.** What is this problem about?
2. **Jump to the constraints.** This is the most important part. If n <= 20, you know brute force will work. If n <= 200,000, you need an efficient algorithm. (See Ch 6 and Ch 13 for the constraint table.)
3. **Look at the examples.** Do not solve them yet — just glance at the input and output to understand the format and get a feel for the problem.
4. **Gut check.** Does this problem remind you of anything you have seen before? Can you identify the algorithm family? (Graph problem? DP? Greedy? Complete search?)
5. **Assign a traffic light color.**

### The Traffic Light System

After skimming all problems, label each one:

| Color | Meaning | Action |
|-------|---------|--------|
| **Green** | "I know how to solve this. I have seen this pattern before." | Solve first |
| **Yellow** | "I have ideas, but I need to think more. Not sure about edge cases." | Solve second |
| **Red** | "I have no idea how to approach this. The algorithm is unfamiliar." | Solve last (aim for partial credit) |

{% hint style="info" %}
**Pro tip**: If you have two green problems, start with the one that has simpler implementation. A problem you can solve correctly in 30 minutes is better than a problem you can solve in 60 minutes — because it frees up time for harder problems.
{% endhint %}

### What If Everything Looks Red?

This happens. It does not mean you are going to score zero. It means you need to:

1. Re-read each problem more carefully. Sometimes a problem looks scary on first read but becomes clearer the second time.
2. Think about brute force. Even if you cannot find the optimal solution, can you write an O(n^3) or O(2^n) solution that solves the small test cases? That is partial credit.
3. Pick the problem where your brute force covers the most test cases and start there.

---

## A.3 Time Allocation by Division

One of the biggest mistakes in contests is spending too much time on one problem. Here is a practical time budget for each USACO division.

### Bronze (4 hours, 3 problems)

Bronze problems are designed for complete search and simulation. If you know your Bronze material (Ch 7-13), you should be able to solve all three.

| Phase | Time per problem | Notes |
|-------|-----------------|-------|
| Read & understand | 10 min | Read twice, work through examples by hand |
| Plan approach | 10 min | Identify: brute force? Simulation? Ad hoc? |
| Code | 30 min | Clean, simple code. No need for fancy algorithms. |
| Test & debug | 20 min | Test all examples + edge cases |
| Buffer | 10 min | Per-problem safety margin |
| **Total per problem** | **80 min** | |
| **Total for 3 problems** | **240 min (4 hrs)** | Leaves ~0 min buffer |

{% hint style="info" %}
**Bronze reality check**: If you are spending more than 30 minutes thinking about the algorithm for a Bronze problem, you are probably overthinking it. Bronze problems almost always have a brute-force solution that works within the constraints. Re-read the constraints and check if a simpler approach is possible.
{% endhint %}

### Silver (4 hours, 3 problems)

Silver problems require specific algorithmic techniques (binary search, two pointers, BFS/DFS, prefix sums). The difficulty jump from Bronze is real.

| Phase | Time per problem | Notes |
|-------|-----------------|-------|
| Read & understand | 10 min | Identify the algorithm category |
| Plan approach | 15 min | Sketch the solution on paper |
| Code | 25 min | Use your templates |
| Test & debug | 20 min | Edge cases are critical at Silver |
| **Total per problem** | **70 min** | |
| **Total for 3 problems** | **210 min** | **30 min buffer** |

Use the 30-minute buffer for:
- Going back to a problem you were stuck on
- Writing a brute-force solution for partial credit on a hard problem
- Double-checking your solutions with edge cases

### Gold (4 hours, 3 problems)

Gold problems often involve DP, trees, shortest paths, or advanced graph algorithms. Getting 2 out of 3 fully correct is a strong performance.

| Phase | Time per problem | Notes |
|-------|-----------------|-------|
| Read & understand | 10 min | Constraints will guide you to the right approach |
| Plan approach | 20 min | Think carefully — wrong approach = wasted time |
| Code | 25 min | Templates save time here |
| Test & debug | 15 min | Trust your logic, test systematically |
| **Total per problem** | **70 min** | |
| **Total for 3 problems** | **210 min** | **30 min buffer** |

{% hint style="warning" %}
**Gold strategy shift**: At Gold, partial credit becomes essential. If you cannot solve a problem optimally, write a brute-force solution that handles the small test cases (often worth 30-50% of the points). A brute-force solution that earns 4/10 test cases is better than a broken optimal solution that earns 0/10.
{% endhint %}

### Platinum (4 hours, 3 problems)

Platinum is the top division. The problems are genuinely hard. Even the best contestants often do not solve all three.

| Phase | Time per problem | Notes |
|-------|-----------------|-------|
| Read & understand | 15 min | These problems are complex — take your time reading |
| Plan approach | 30 min | Correctness of approach is everything |
| Code | 30 min | Implementation can be tricky |
| Test & debug | 20 min | Custom test cases are essential |
| **Total per problem** | **95 min** | |

**Platinum reality**: You have 240 minutes for 3 problems, but 3 x 95 = 285 minutes. That is more time than you have. This is by design — you are NOT expected to solve all three.

**Recommended Platinum strategy:**
1. Spend 15 minutes reading all three problems.
2. Identify your strongest 1-2 problems.
3. Spend 90-100 minutes on your best problem. Get it fully correct.
4. Spend 80-90 minutes on your second-best problem. Get it fully correct if possible, or aim for partial credit.
5. Use remaining time (30-50 min) for partial credit on the third problem (brute force).

---

## A.4 During the Contest: Solving Strategy

You have read all three problems, assigned traffic lights, and picked your starting problem. Now it is time to solve.

### Start With Your Green Problem

Your first goal is to get points on the board. Solve your easiest problem cleanly and correctly. This does several things:

- **Builds confidence.** Solving one problem calms your nerves and lets you think more clearly.
- **Secures points.** Even if everything else goes wrong, you have one problem solved.
- **Warms up your brain.** Your coding muscles are now loose and ready for harder problems.

### The 20-Minute Rule

This rule comes from Errichto (Kamil Debowski), one of the top competitive programmers in the world, and we first mentioned it back in Ch 1:

> **If you have been stuck on a problem for 20 minutes with no new ideas, move on to another problem.**

This does NOT mean give up forever. It means:

1. Write down where you are stuck and what you have tried.
2. Switch to a different problem.
3. Come back later with fresh eyes.

Why does this work? Your brain continues processing the hard problem in the background, even while you are working on something else. This is called "incubation" — and it is a real, studied cognitive phenomenon. Many programmers report having their "aha!" moment for Problem 2 while coding Problem 3.

{% hint style="info" %}
**The 20-minute rule in practice**: This does NOT mean you stop thinking about a problem after 20 minutes of working on it. It means 20 minutes of being STUCK — making no progress, having no new ideas, staring at the screen. If you are making steady progress (coding, debugging, testing), keep going even if it takes longer than 20 minutes.
{% endhint %}

### The Partial Credit Strategy

USACO uses test-case-based scoring. If a problem has 10 test cases, each one you pass earns you points — even if you do not pass all 10. This has a huge strategic implication:

**A brute-force solution that passes the small test cases is worth real points.**

Here is the typical test case structure for a USACO problem:

| Test cases | Input size | Points |
|-----------|-----------|--------|
| 1-3 | Small (n <= 100) | 30% |
| 4-7 | Medium (n <= 5,000) | 40% |
| 8-10 | Large (n <= 200,000) | 30% |

An O(n^2) brute-force solution will pass test cases 1-3 (and maybe 4-7), earning you 30-70% of the points. That is a LOT better than 0%.

**When to write a brute-force solution:**
- You do not see the optimal approach.
- You have at least 15-20 minutes left.
- The brute force is straightforward to implement.

**How to do it:**
1. Write the simplest, most obvious solution. Nested loops, recursion, whatever works.
2. Make sure it is CORRECT on the examples.
3. Submit it. Take the partial credit.
4. If you have time left, think about the optimal approach and submit an improved solution.

### When to Switch Problems

Switch problems when:
- You have been stuck for 20 minutes (the 20-minute rule).
- You realize your approach is fundamentally wrong and you need to rethink.
- You have a working brute-force submitted and need to move on.
- You feel your frustration level rising to the point where you cannot think clearly.

Do NOT switch problems when:
- You are making steady progress, even if it is slow.
- You are in the middle of debugging and have a clear plan for what to check next.
- You have invested 60+ minutes and are close to a working solution (the sunk cost is real here — finish it).

### Debugging Under Pressure

When your code gives wrong answers during a contest, you do not have the luxury of spending an hour with a debugger. Here is a fast debugging protocol:

1. **Re-read the problem statement.** Seriously. 30% of contest bugs come from misunderstanding the problem. Did you miss a constraint? Did you misread "less than or equal" as "less than"?

2. **Test with the given examples.** If your code fails on the examples, you have a logic bug. Trace through your code by hand with the first example.

3. **Test with small custom cases.** Create the simplest possible input that tests your logic:
   - n = 1 (single element)
   - n = 2 (smallest non-trivial case)
   - Sorted input, reverse-sorted input
   - All elements the same

4. **Add print statements.** Print intermediate values at key points. For example, if you are running BFS, print the queue at each step. If you are filling a DP table, print the table. Remove or comment out the prints before submitting.

5. **Check the usual suspects** (see the list below).

### Common Contest Pitfalls

These bugs cause more wrong answers than anything else. Check for them EVERY time:

| Pitfall | What goes wrong | How to prevent |
|---------|----------------|----------------|
| **Integer overflow** | Multiplying two large ints exceeds 2^31 | Use `long long` in C++, `long` in Java (see Ch 5) |
| **Off-by-one errors** | Array index out of bounds, wrong loop boundary | Double-check: should it be `< n` or `<= n`? |
| **Uninitialized variables** | Variable has garbage value in C++ | Initialize everything. Arrays too. |
| **Wrong data type** | Using `int` when you need `long long` | Check: can intermediate results exceed 2 x 10^9? |
| **Forgetting to reset** | Global arrays not cleared between test cases | Clear arrays at the start of each test case |
| **Edge case: empty input** | n = 0 or empty string crashes your code | Check for empty input before processing |
| **Edge case: n = 1** | Single element is often a special case | Test with n = 1 explicitly |
| **Sorting stability** | Ties broken differently than expected | Make your comparator handle ties explicitly |
| **1-indexed vs 0-indexed** | Off-by-one when converting between the two | Pick one convention and stick with it for the entire problem |

{% hint style="danger" %}
**The #1 contest killer: integer overflow.** In C++, `int` can hold up to about 2.1 billion (2^31 - 1). If a problem says n <= 100,000 and asks for a sum, the answer could be up to 10^10 — which does NOT fit in an `int`. Use `long long` by default for any problem involving sums, products, or large counts. This single habit will save you from dozens of wrong answers over your contest career.
{% endhint %}

---

## A.5 The Last 30 Minutes

The clock shows 30 minutes left. What you do now can be the difference between solving 2 problems and solving 3.

### If You Are Still Coding a Solution

You need to make a decision: **Can I finish and debug this in 30 minutes?**

- If yes: focus and finish it. Skip elaborate testing — just make sure it passes the examples and submit.
- If no: stop coding the optimal solution. Write a brute force instead. A brute-force solution you can finish is worth more than an optimal solution you cannot.

### If You Have Submitted Everything

Do NOT sit back and relax. Use this time productively:

**Step 1: Review your submitted solutions (10 minutes)**

Re-read each solution and look for:
- Integer overflow (are you using the right data types?)
- Off-by-one errors in loops and array indices
- Edge cases you might have missed (n = 0, n = 1, all elements equal)
- Copy-paste errors (did you change all the variable names?)

**Step 2: Create and test edge cases (10 minutes)**

For each problem, think of the nastiest test case you can:
- Maximum input size (does your solution run fast enough?)
- Minimum input size (n = 0, n = 1)
- Extreme values (all zeros, all maximums, negative numbers if allowed)
- The "boring" case (sorted input, all elements the same)

Run these test cases on your machine. If something breaks, you have time to fix it.

**Step 3: Partial credit check (10 minutes)**

For any problem where you submitted a brute-force solution, ask yourself:
- Can I make a small optimization to pass a few more test cases?
- Is there a simple improvement (like sorting the input first) that might help?
- Did I handle ALL the small test cases correctly?

### The Final Minute

{% hint style="danger" %}
**Make sure all your solutions are actually submitted.** This sounds obvious, but every contest season, someone writes a perfect solution, tests it locally, and then forgets to click "Submit." Check your submission page. Verify that every problem shows your latest submission. Do this with 5 minutes left, not 30 seconds.
{% endhint %}

---

## A.6 After the Contest

The contest is over. Whether you solved all three or struggled with every problem, what you do in the next few days matters more than the contest itself.

### Step 1: Take a Break (1-2 Hours)

Close your laptop. Get some fresh air. Eat something. Your brain just did 4 hours of intense work — give it a rest. Trying to analyze your performance immediately after a contest is not productive because your emotions are too raw.

### Step 2: Review ALL Problems (That Evening or Next Day)

Once you have recovered, go through every problem — including the ones you solved:

**For problems you solved correctly:**
- Was your approach the intended one? Read the editorial to find out.
- Is there a simpler or faster solution? Learning alternative approaches deepens your understanding.
- How long did it take you? Could you solve it faster next time?

**For problems you got wrong:**
- What went wrong? Wrong approach? Bug in implementation? Misread the problem?
- If it was a bug: what type of bug? (This goes into your mistake journal — see below.)
- If it was a wrong approach: what was the right approach? Could you have figured it out during the contest?

**For problems you did not attempt:**
- Read the editorial. Understand the solution.
- This is NOT "cheating." This IS learning.

{% hint style="info" %}
**Tourist's philosophy on editorials**: Gennady Korotkevich (tourist), the highest-rated competitive programmer in history, does not memorize algorithms. He understands WHY they work so he can reconstruct them from scratch. When you read an editorial, do not just memorize the solution. Ask yourself: "Why does this work? What is the key insight? How would I recognize a similar problem in the future?" (See Ch 1 for more on tourist's approach.)
{% endhint %}

### Step 3: Upsolve

"Upsolving" means going back and solving contest problems you could not solve during the contest, after reading the editorial. This is the single most effective way to improve.

Here is the upsolving protocol:

1. Read the editorial. Understand the approach (but do not copy the code).
2. Close the editorial.
3. Implement the solution yourself, from scratch, without looking at the editorial's code.
4. If you get stuck, re-read only the part of the editorial you need. Then close it again and continue coding.
5. Test your solution. Make sure it passes all test cases.
6. Think about it: "What pattern does this problem use? What was the key insight I was missing?"

{% hint style="warning" %}
**Common upsolving mistake**: Reading the editorial, nodding along, and thinking "Oh, I could have done that" without actually implementing it. You have not learned the technique until you can code it. Understanding and implementing are different skills. Do not skip the implementation step.
{% endhint %}

### Step 4: Keep a Mistake Journal

This is the single habit that separates competitors who plateau from competitors who keep improving.

After every contest, write down:

| Date | Problem | What went wrong | Category | Lesson |
|------|---------|----------------|----------|--------|
| Dec 2024 | Silver P2 | Used int instead of long long | Overflow | Always use long long for sums |
| Dec 2024 | Silver P3 | Did not consider case where graph is disconnected | Edge case | Check if graph is connected before running algo |
| Jan 2025 | Gold P1 | Spent 80 min on wrong DP formulation | Wrong approach | Spend more time planning before coding |

After a few contests, patterns will emerge. Maybe you keep making overflow errors. Maybe you always spend too long on your first problem. Maybe you never test edge cases. Once you see the pattern, you can fix it.

### Step 5: The 1% Improvement Mindset

You will not go from Bronze to Platinum in one contest. You will not even go from Bronze to Silver in one contest. Improvement in competitive programming is gradual, and that is okay.

After each contest, aim to be 1% better than last time:
- Read problems 1 minute faster
- Make one fewer silly bug
- Recognize one more pattern
- Stay calm for 5 more minutes before getting frustrated

These 1% improvements compound. After 50 contests, you are not 50% better — you are dramatically better, because each improvement builds on the last.

---

## A.7 Practice Contest Routine

You would not show up to a basketball game without having practiced, and you should not show up to a contest without having simulated the contest experience.

### How to Simulate a Real Contest

1. **Pick a past contest.** USACO archives every contest at [usaco.org](http://usaco.org). Start with contests from 1-2 years ago in your current division.

2. **Set a timer for 4 hours.** Not 3 hours 50 minutes. Not "I'll just finish this one problem." Four hours, hard stop.

3. **No outside resources.** No Googling, no looking at your notes (except your template library — you would have that in a real contest too). No asking friends for help.

4. **Submit to the USACO grading server.** The grading server accepts practice submissions. This lets you see exactly how many test cases you pass.

5. **When the timer goes off, STOP.** Even if you are one line away from finishing. The discipline of stopping is part of the practice.

6. **Upsolve everything you did not finish.** This is where the real learning happens.

### Practice Resources

| Resource | What it is | Best for |
|----------|-----------|----------|
| **USACO past contests** ([usaco.org](http://usaco.org)) | Official past problems with grading | Practicing for USACO specifically |
| **Codeforces** ([codeforces.com](http://codeforces.com)) | Huge problem archive, regular contests | General CP practice, virtual contests |
| **AtCoder** ([atcoder.jp](http://atcoder.jp)) | Clean problems, excellent editorials | Practicing clean problem-solving |
| **USACO Guide** ([usaco.guide](http://usaco.guide)) | Curated problems by topic and division | Targeted practice for weak areas |
| **CSES Problem Set** ([cses.fi](http://cses.fi)) | 300 classic problems | Building fundamental skills |

### Weekly Practice Schedule

Here is a realistic weekly schedule for a student who is also juggling school:

| Day | Activity | Time |
|-----|----------|------|
| Monday | Solve 2-3 practice problems (focused on weak areas) | 1-1.5 hrs |
| Tuesday | Rest or light review | 0-30 min |
| Wednesday | Solve 2-3 practice problems | 1-1.5 hrs |
| Thursday | Rest or light review | 0-30 min |
| Friday | Virtual contest (full 4 hours) OR solve 3-4 harder problems | 2-4 hrs |
| Saturday | Upsolve Friday's contest + review editorials | 1-2 hrs |
| Sunday | Rest | 0 min |

**Total: 5-10 hours per week.** This is enough to make steady progress. Consistency matters far more than volume.

{% hint style="info" %}
**Quality over quantity.** Solving 3 problems thoughtfully (with upsolving and editorial reading) is better than rushing through 10 problems and never reviewing your mistakes. Every problem you upsolve is worth more than three problems you solve easily.
{% endhint %}

### The Virtual Contest Strategy

Codeforces and AtCoder both offer "virtual contests" — you can take any past contest as if it were live, with a timer and a leaderboard showing where you would have placed.

**How to use virtual contests effectively:**

1. **Pick a contest rated slightly above your level.** If you are Codeforces 1200, try a Div 2 contest. If you are 1600, try a Div 1 contest.

2. **Do it in one sitting.** No pausing, no breaks longer than you would take in a real contest.

3. **After the virtual contest ends**, compare your performance to the real participants. Where did you rank? Which problems did the people around your rating solve that you did not?

4. **Upsolve the problems you missed.** Read editorials, implement solutions, understand the techniques.

---

## A.8 Mental Game

Here is something nobody tells you when you start competitive programming: the mental game is at least as important as the technical skills.

### Contest Anxiety Is Normal

Your heart is pounding. Your hands are shaky. You read the first problem and your mind goes blank. You think: "Everyone else is solving this already and I cannot even understand the problem."

This is completely normal. It happens to everyone — including the pros.

Petr Mitrichev, one of the greatest competitive programmers ever, has talked about feeling nervous before major contests. Tourist has mentioned the pressure of being the top-rated competitor and feeling like he "should" solve everything. If they get nervous, it is perfectly okay for you to get nervous too.

The difference between pros and beginners is not that pros do not get nervous. It is that pros have strategies for handling their nerves.

### Strategies for Managing Contest Anxiety

**Before the contest:**
- **Routine.** Do the same thing before every contest. Same setup, same snack, same warm-up problems. Routines calm your brain because they signal "I have been here before, I know what to do."
- **Remind yourself of your preparation.** You have worked through chapters of this book. You have solved hundreds of problems. You are prepared.
- **Set a realistic goal.** Not "I will solve all three problems." Instead: "I will read all problems carefully, start with my strongest, and give my best effort." Process goals reduce pressure.

**During the contest:**
- **Breathe.** When you feel panic rising, take three slow, deep breaths. In for 4 seconds, hold for 4, out for 4. This is not woo-woo nonsense — it activates your parasympathetic nervous system and physically calms you down.
- **Re-read the problem.** When your mind goes blank, your eyes are scanning words but your brain is not processing them. Slow down. Read one sentence at a time. Underline key information.
- **Draw examples.** Get a piece of paper (or open a text file) and work through examples by hand. Drawing activates different parts of your brain and often unlocks insights that just staring at the screen does not.
- **Talk to yourself.** (Quietly, if you are in a room with others.) Explain the problem to yourself as if you were explaining it to a friend. This is called "rubber duck debugging" and it works for problem-solving too.
- **Take a 2-minute break.** Stand up, stretch, look at something far away. Two minutes of rest can save you twenty minutes of unproductive staring.

**After a bad contest:**
- **Do not catastrophize.** One bad contest does not define you. Everyone has bad contests. It is one data point, not a trend.
- **Extract lessons, not judgments.** Instead of "I am bad at DP," think "I need to practice DP state transitions more." The first is an identity judgment. The second is an actionable plan.
- **Remember your trajectory.** Look at how far you have come since you started. Six months ago, you did not know what BFS was. Now you can implement it in three languages. That is real progress.

### Growth Mindset: You vs. Past You

The only competitor who matters is the version of you from last month. Are you better than that person? Then you are winning.

Do not compare yourself to the kid who solves all three problems in 90 minutes. You do not know their story. Maybe they have been doing this for five years. Maybe they have a parent who is a CS professor. Maybe they just happened to have seen those exact problem types before. Their journey is not your journey.

**Track YOUR progress:**
- How many problems could you solve in your first contest? And your fifth? And your tenth?
- What topics used to scare you that feel comfortable now?
- How has your debugging speed improved?

### Neal Wu's Story

Neal Wu started competitive programming in 8th grade — quite possibly around your age right now. He did not immediately win everything. He participated in many contests, solved many problems, read many editorials, and gradually improved.

By high school, he was one of the top competitive programmers in the United States. He made the US IOI team multiple times. His secret was not talent (though he is certainly talented) — it was consistent practice, upsolving, and a growth mindset.

He has said that the biggest mistake beginners make is not reading the entire problem before coding. That is why Section A.2 of this appendix emphasizes reading all problems first. Listen to Neal.

### What to Do When You Feel Stuck

Being stuck is not failure. It is a normal part of problem-solving. Here is what to do:

1. **Re-read the problem statement.** You probably missed something.
2. **Work through the examples by hand on paper.** Draw diagrams. Trace through the logic step by step.
3. **Think about simpler versions of the problem.** What if n = 1? What if n = 2? Can you solve those? Can you generalize?
4. **Think about the constraints.** What algorithm complexity do they suggest? (See Ch 6 and Ch 13 for the constraint-to-complexity table.)
5. **Consider the five lenses** (from Ch 1):
   - Constraints: What does the input size tell me about the expected complexity?
   - Brute Force: What is the simplest solution, even if it is slow?
   - Pattern: Have I seen something similar before? What technique did I use?
   - Optimization: Where is the brute force doing repeated work?
   - Proof: Can I convince myself this approach is correct before coding?
6. **If all else fails, write the brute force.** Get the partial credit and move on.

### Celebrating Small Wins

Competitive programming is a long road. If you only celebrate when you advance to the next division, you will spend most of your time feeling frustrated. Instead, celebrate:

- Solving a problem faster than you expected
- Debugging a tricky issue during a contest
- Understanding an editorial on the first read
- Implementing an algorithm from scratch without looking at notes
- Making fewer mistakes than last time
- Hitting a new personal best rating

These small wins add up. They keep you motivated when the big wins feel far away.

---

## A.9 The Problem-Solver's Checklist (Reference)

This checklist was introduced in Ch 1 and refined throughout the book. Here it is in its complete form. Print it out and keep it next to your computer during practice and contests.

### Before Coding

- [ ] **Read the problem twice.** Underline constraints and key requirements.
- [ ] **Work through the examples BY HAND on paper.** Do not skip this. Draw diagrams if the problem involves graphs, grids, or intervals.
- [ ] **Identify the problem type.** What category does this fall into?
  - Search / Optimization / Counting / Construction / Interactive
  - Graph / Tree / String / Array / Geometry
- [ ] **Check constraints and determine target complexity.**
  - n <= 20: O(2^n) or O(n!) -- brute force / backtracking
  - n <= 1,000: O(n^2) -- nested loops
  - n <= 100,000: O(n log n) -- sorting + binary search, or divide and conquer
  - n <= 1,000,000: O(n) -- single pass, hashing, two pointers
  - (See Ch 6 and Ch 13 for the full constraint table.)
- [ ] **Think brute force first.** Can you solve it with a simple approach that fits the constraints?
- [ ] **Look for patterns.** Does this remind you of a known technique?
  - Sorting? (Ch 8)
  - Binary search on the answer? (Ch 16)
  - Two pointers / sliding window? (Ch 15)
  - BFS / DFS? (Ch 19-20)
  - DP? (Ch 23-25)
  - Greedy? (Ch 18)
  - Segment tree? (Ch 30)
- [ ] **Plan your approach before touching the keyboard.** Outline it in comments or on paper.

### After Coding

- [ ] **Test with the given examples.** If they fail, you have a bug. Do not submit.
- [ ] **Test with edge cases:**
  - Empty input or n = 0 (if applicable)
  - Single element (n = 1)
  - Maximum input size (does it run within the time limit?)
  - All elements the same
  - Already sorted / reverse sorted
  - Negative numbers (if the problem allows them)
- [ ] **Test with a case you make up yourself.** Choose one that exercises a different code path than the given examples.
- [ ] **If wrong, debug systematically:**
  - Re-read the problem (did you misunderstand something?)
  - Add print statements at key points
  - Trace through your code by hand with the failing test case
  - Check the common pitfalls table from Section A.4

### After Solving (The Step Most Beginners Skip)

- [ ] **Can you solve it a different way?** Faster? With less code? Using a different algorithm?
- [ ] **Name the pattern.** "This was a binary search on the answer problem." "This was a DFS with backtracking problem." Naming patterns makes them easier to recognize in future problems.
- [ ] **What would make this harder?** Larger constraints? Additional requirements? What if the graph had weights? What if you needed the k-th best answer instead of the best? (This type of thinking prepares you for harder divisions.)

---

## A.10 Quick Reference Card

Cut this section out (or screenshot it) and keep it handy during contests.

### Pre-Contest Checklist

| Step | Done? |
|------|-------|
| Slept 8 hours | |
| Computer charged, internet working | |
| IDE open, can compile and run code | |
| USACO login tested | |
| Templates copied to working directory | |
| Water and snack ready | |
| Phone silenced | |

### First 15 Minutes Protocol

| Step | Time | Action |
|------|------|--------|
| 1 | 0:00 - 0:05 | Skim Problem 1 (constraints, examples, gut check) |
| 2 | 0:05 - 0:10 | Skim Problem 2 |
| 3 | 0:10 - 0:15 | Skim Problem 3, assign traffic lights, pick starting problem |

### Traffic Light Quick Reference

| Color | Criteria | Action |
|-------|----------|--------|
| Green | Know the approach, confident in implementation | Solve first |
| Yellow | Have ideas, need to think, unsure about details | Solve second |
| Red | No clear approach, unfamiliar technique required | Solve last, aim for partial credit |

### Time Budget Quick Reference

| Division | Per Problem | Buffer | Strategy |
|----------|-----------|--------|----------|
| Bronze | 80 min | 0 min | Solve all 3 — brute force is usually fine |
| Silver | 70 min | 30 min | Solve all 3 — need specific techniques |
| Gold | 70 min | 30 min | Focus on 2, partial credit on 3rd |
| Platinum | 90-100 min | 0 min | Focus on 1-2 fully, brute-force 3rd |

### During-Contest Decision Tree

```
Am I stuck?
  |
  +--> Been stuck < 20 min? --> Keep thinking, try a different angle
  |
  +--> Been stuck >= 20 min?
         |
         +--> Have another unsolved problem? --> Switch problems, come back later
         |
         +--> All other problems attempted? --> Write brute force for partial credit
```

### Debug Protocol (When Your Code Is Wrong)

```
1. Re-read the problem statement (30% of bugs are misunderstandings)
2. Test with given examples
3. Test with n=1 and n=2
4. Add print statements at key points
5. Check: integer overflow? off-by-one? uninitialized variable?
6. Trace through code by hand with failing input
```

### Constraint-to-Complexity Cheat Sheet

| Max n | Target complexity | Common techniques |
|-------|-------------------|-------------------|
| <= 10 | O(n!) | Permutations, full backtracking |
| <= 20 | O(2^n) | Subsets, bitmask DP |
| <= 500 | O(n^3) | Triple nested loops, Floyd-Warshall |
| <= 5,000 | O(n^2) | Double nested loops, simple DP |
| <= 100,000 | O(n log n) | Sorting, binary search, segment trees |
| <= 1,000,000 | O(n) | Two pointers, hashing, prefix sums |

### The Five Lenses (Quick Version)

1. **Constraints** -- What complexity can I afford?
2. **Brute Force** -- What is the simplest solution?
3. **Pattern** -- Have I seen something like this before?
4. **Optimization** -- Where is the repeated work?
5. **Proof** -- Why does this work?

### Post-Contest Protocol

```
1. Take a break (1-2 hours)
2. Review ALL problems (including ones you solved)
3. Read editorials
4. Upsolve (implement solutions you could not do during contest)
5. Update your mistake journal
6. Identify one thing to improve for next time
```

---

## Final Words

Contests are where everything comes together. All those chapters you have worked through — from your first "Hello, World!" in Ch 2 to segment trees in Ch 30 — they are all tools in your toolbox. Contests are where you learn to grab the right tool at the right time, under pressure.

You will have bad contests. You will have contests where you cannot solve a single problem. You will have contests where you make a silly mistake that costs you 200 points. Every competitive programmer who has ever lived has had those experiences.

But you will also have moments of brilliance. You will see a problem and immediately know the approach. You will write a solution in 15 minutes that you could not have written 6 months ago. You will solve a problem that stumps half the contestants in your division.

Those moments make it all worth it.

Keep practicing. Keep upsolving. Keep showing up. The only way to get better at contests is to do more contests.

Good luck. You have got this.
