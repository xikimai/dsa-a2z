# Appendix C: USACO Registration & Contest Guide

This appendix is your practical, step-by-step guide to the USA Computing Olympiad. By the end, you will know exactly what USACO is, how to register, what to expect on contest day, and how to build a training plan that takes you from Bronze to Platinum. No guesswork, no mystery.

---

## C.1 What Is USACO?

The **USA Computing Olympiad** (USACO) is one of the most prestigious programming competitions in the world for pre-college students. Here is what you need to know:

- **Free to enter.** No registration fee, no travel required. You compete from your own computer at home.
- **Open to everyone.** Despite the name, USACO is not limited to students in the United States. Students from any country can register and compete.
- **Online and flexible.** Contests happen over a multi-day window. You choose when to start within that window, and once you begin, you have 4 hours to solve 3 problems.
- **The path to IOI.** USACO is the official selection pipeline for the USA team at the International Olympiad in Informatics (IOI). The top ~15 USACO competitors are invited to a training camp each summer, and from that camp, 4 students are chosen to represent the USA at IOI.
- **Respected worldwide.** USACO results carry weight in college admissions (especially for CS programs), scholarship applications, and internship interviews. Even if you never reach the top tier, consistent improvement through the divisions demonstrates real problem-solving ability.

### A Brief History

USACO has been running since 1992, making it one of the oldest online programming contests. It was originally created by Don Piele and Rob Kolstad at the University of Wisconsin. Over the decades, it has grown from a small US competition to a global event with tens of thousands of participants from over 70 countries. The problems are written and tested by former IOI medalists and top competitive programmers.

{% hint style="info" %}
**Why USACO matters for you:** Even if IOI is not your goal, USACO gives you structured milestones. Instead of vaguely "learning algorithms," you have concrete divisions to aim for. Each promotion tells you that your skills have genuinely leveled up.
{% endhint %}

---

## C.2 How USACO Works

### The Contest Season

USACO runs four contests per season, spread across the school year:

| Contest | Typical Timing | Notes |
|---------|---------------|-------|
| **December** | Mid-December (Fri-Mon window) | Season opener. First chance to promote. |
| **January** | Mid-to-late January (Fri-Mon) | Second chance. Problems are independent of December. |
| **February** | Mid-to-late February (Fri-Mon) | Third chance. |
| **US Open** | Late March or early April (Fri-Mon) | The "championship" round. Slightly harder problems. |

Each contest is completely independent. You do not need to participate in all four. If you promote in December, you compete in your new division starting in January.

### The Format

- **3 problems** per contest
- **4 hours** to solve them (continuous -- no breaks in the timer)
- **From home** (or wherever you have a computer and internet)
- **Any time during the window**: the contest window is typically open Friday evening through Monday evening (US time). You pick when to start. Once you click "Begin Contest," your 4-hour clock starts and does not pause.
- **Submit online**: you upload your source code file. The judge compiles and runs it against test cases, and you see results immediately.
- **Unlimited resubmissions**: you can submit as many times as you want during your 4 hours. Only your last submission for each problem is scored.

{% hint style="warning" %}
**The timer is real.** Once you click "Begin Contest," your 4 hours start counting down. You cannot pause, restart, or get extra time. Make sure you are ready before you click that button.
{% endhint %}

### Supported Languages

USACO accepts solutions in three languages:

- **C++** (compiled with `g++ -O2 -std=c++17`)
- **Java** (compiled with `javac`, run with `java`)
- **Python** (run with `python3`, using PyPy for speed in recent seasons)

We will discuss which language to use for which division in Section C.7.

---

## C.3 The Division System

USACO has four divisions, and every new competitor starts at Bronze. You move up by performing well in a contest. Here is the full picture:

```
                    +------------------+
                    |    PLATINUM      |  Ch 30-34
                    |  Segment Trees   |  (This book's Part V)
                    |  Advanced DP     |
                    |  String Algos    |
                    |  Geometry        |
                    +--------+---------+
                             ^
                             | Promote
                    +--------+---------+
                    |      GOLD        |  Ch 23-29
                    |  DP (all types)  |  (This book's Part IV)
                    |  Shortest Paths  |
                    |  Trees           |
                    |  Union-Find, MST |
                    +--------+---------+
                             ^
                             | Promote
                    +--------+---------+
                    |     SILVER       |  Ch 14-22
                    |  Prefix Sums     |  (This book's Part III)
                    |  Binary Search   |
                    |  Greedy          |
                    |  BFS / DFS       |
                    |  Basic DP        |
                    +--------+---------+
                             ^
                             | Promote
                    +--------+---------+
                    |     BRONZE       |  Ch 7-13
                    |  Simulation      |  (This book's Part II)
                    |  Complete Search  |
                    |  Sorting         |
                    |  Ad Hoc          |
                    +--------+---------+
                             ^
                             |
                      Everyone starts here
```

### Bronze

**Where everyone begins.** Bronze problems test your ability to implement straightforward algorithms under small constraints. You do not need fancy data structures -- you need clean code and careful reading.

- **Key topics**: Simulation, complete search (brute force), sorting, basic math, ad hoc logic
- **Book chapters**: Ch 7 (Number Wizardry), Ch 8 (Sorting), Ch 9 (Searching), Ch 10 (Recursion), Ch 11 (Hashing), Ch 12 (Bit Manipulation), Ch 13 (Bronze Battle Plan)
- **Typical constraints**: n <= 1,000 or smaller (brute force is usually fast enough)
- **Promotion**: Solve 2-3 problems well in a single contest

{% hint style="info" %}
**The truth about Bronze:** Most students promote out of Bronze within 1-3 contests once they have practiced the core topics. The key is reading problems carefully and handling edge cases. Bronze is more about implementation than algorithm knowledge.
{% endhint %}

### Silver

**The first real algorithmic division.** Silver problems require you to know specific techniques and choose the right one. Brute force alone will not work -- constraints are too large.

- **Key topics**: Prefix sums, two pointers, binary search (on answers), greedy algorithms, BFS/DFS, basic graphs
- **Book chapters**: Ch 14 (Prefix Sums), Ch 15 (Two Pointers), Ch 16 (Binary Search Beyond), Ch 17 (Heaps), Ch 18 (Greedy), Ch 19-20 (Graphs), Ch 21 (Linked Lists), Ch 22 (Stacks & Queues)
- **Typical constraints**: n <= 100,000 (you need O(n log n) or O(n) solutions)
- **Promotion**: Consistently solve 2+ problems per contest

### Gold

**Where things get serious.** Gold requires deep understanding of algorithms, not just memorization. You need to see the structure of a problem and map it to the right technique.

- **Key topics**: Dynamic programming (all varieties), shortest paths (Dijkstra, Bellman-Ford), tree algorithms, Union-Find, minimum spanning trees
- **Book chapters**: Ch 23-25 (DP I-III), Ch 26 (Trees), Ch 27 (Shortest Paths), Ch 28 (Topological Sort), Ch 29 (Union-Find & MST)
- **Typical constraints**: n <= 200,000+ (efficiency and correctness both matter)
- **Promotion**: The hardest jump. Many strong competitors stay in Gold for months.

{% hint style="warning" %}
**The Gold-to-Platinum jump** is widely considered the hardest promotion in USACO. It requires not just knowing algorithms, but being able to combine multiple techniques creatively under pressure. Give yourself time -- this is a marathon, not a sprint.
{% endhint %}

### Platinum

**Expert level.** Platinum problems often require combining multiple advanced techniques or inventing new approaches on the spot.

- **Key topics**: Segment trees, advanced DP (bitmask, interval, on trees), string algorithms (KMP, hashing, suffix arrays), advanced graph algorithms, computational geometry
- **Book chapters**: Ch 30 (Segment Trees), Ch 31 (Advanced DP), Ch 32 (String Algorithms), Ch 33 (Advanced Trees & Graphs), Ch 34 (Geometry & Sweep Line)
- **Beyond Platinum**: Top scorers at the US Open are invited to the USACO Training Camp, from which the 4-person IOI team is selected.

---

## C.4 Registration (Step by Step)

Registering for USACO is free and takes about 5 minutes. Here is exactly what to do:

### Step 1: Go to the USACO website

Open your browser and navigate to **usaco.org**. You will see the main USACO page with news about the current or upcoming season.

### Step 2: Find the registration page

Click **"Register for New Account"** (usually linked from the top navigation or the contest announcement). This takes you to the registration form.

### Step 3: Fill in your information

You will need to provide:

| Field | What to enter |
|-------|--------------|
| **Username** | Choose something you will remember. This is your login name. |
| **Password** | Pick a strong password and write it down somewhere safe. |
| **Email** | Use an email you actually check. USACO sends contest announcements here. |
| **First name / Last name** | Your real name. |
| **School** | Your school name (or "Homeschool" if applicable). |
| **Country** | Your country of residence. |
| **Graduation year** | The year you expect to graduate high school. |

### Step 4: Verify your email

USACO will send a verification email. Click the link in that email to activate your account. Check your spam folder if you do not see it within a few minutes.

### Step 5: You are registered

That is it. No payment, no approval process, no waiting period. Your account works for the entire season and carries over year to year. You do not need to re-register for each contest -- just log in.

{% hint style="info" %}
**Keep your login credentials safe.** You will use the same account for every contest. If you forget your password, you can reset it via email, but do not leave this to the last minute before a contest.
{% endhint %}

### Step 6: Check your division

After registration, you start in **Bronze**. If you promoted in a previous season, your division carries over. You can check your current division by logging in and looking at your profile.

---

## C.5 Taking a Contest

Here is what actually happens when you compete:

### Before the contest window opens

- Make sure your USACO account works (log in and verify).
- Decide roughly when during the contest window you plan to compete.
- Set up your computer, IDE, and any templates you use (see Section C.8).
- Tell your family you need 4 uninterrupted hours.

### During the contest window

1. **Log in** to usaco.org during the contest window.
2. **Navigate to the contest page.** You will see a button like "Begin [Division] Contest."
3. **Read the instructions.** USACO shows you a page confirming your division and explaining the rules.
4. **Click "Begin Contest."** This starts your 4-hour timer. There is no going back.
5. **Read the problems.** You will see three problems. Each has a problem statement, input format, output format, sample input, and sample output.
6. **Solve and submit.** For each problem:
   - Write your solution in your preferred language.
   - Submit the source code file through the website.
   - The judge runs your code against test cases and reports the results.
   - You can see which test cases passed and which failed (but not the actual test data).
   - You can resubmit as many times as you want.
7. **When time runs out**, the contest ends automatically. Your last submission for each problem is your final score.

{% hint style="warning" %}
**You can only start once.** If you click "Begin Contest" and then close your browser, the timer keeps running. You cannot pause or restart. Plan accordingly.
{% endhint %}

### Choosing when to start

The contest window is typically open from Friday evening through Monday evening (US Eastern time). Some tips:

- **Pick a time when you are fresh and alert.** Saturday or Sunday morning works well for many students.
- **Make sure you have reliable internet** for the entire 4 hours.
- **Avoid starting late at night** -- you will make mistakes when you are tired.
- **Do not start right when the window opens** unless you are confident. There is no advantage to going first.
- **Do start early enough** that you are not rushing on the last day of the window.

---

## C.6 How Scoring Works

Understanding the scoring system helps you make smart decisions during a contest.

### Points per problem

- Each problem has **10 test cases**.
- Each test case is worth **100 points**.
- So each problem is worth up to **1,000 points**.
- With 3 problems, the maximum score is **3,000 points**.

### Partial credit is your friend

This is one of the best things about USACO scoring: **you get credit for every test case you pass.** If your solution is correct but too slow for the largest inputs, you might still pass 5-7 test cases and earn 500-700 points on that problem.

This means:

- A brute force solution that handles small inputs correctly is worth **300-500 points** per problem (the first few test cases have smaller inputs).
- Even an imperfect solution is worth submitting.
- Never leave a problem with 0 points if you can write any solution at all.

### How promotion works

After each contest, USACO announces a **promotion cutoff** -- a minimum score needed to advance to the next division. The cutoff varies from contest to contest based on problem difficulty and the number of participants.

Typical promotion thresholds:

| Promotion | Typical cutoff range |
|-----------|---------------------|
| Bronze to Silver | ~750-850 points (out of 3,000) |
| Silver to Gold | ~750-850 points |
| Gold to Platinum | ~750-850 points |

These thresholds mean you generally need to **fully solve at least 1 problem and get significant partial credit on another**, or get strong partial credit across all three.

{% hint style="info" %}
**Strategy tip:** If you are stuck on a problem, write the brute force solution and submit it for partial credit. Then move on to another problem. Come back and optimize later if you have time. This is almost always better than spending 2 hours on one problem trying to get the perfect solution.
{% endhint %}

### Perfect scores and in-contest promotion

If you score a **perfect 3,000** (all test cases on all problems), you are guaranteed promotion regardless of the cutoff. In fact, students who score perfectly sometimes get promoted mid-season and compete in the next division at the very next contest.

---

## C.7 Which Language to Choose?

You are learning three languages in this book, which is a genuine advantage. Here is honest advice about when to use each one in USACO:

### Language comparison for USACO

| Aspect | Python | Java | C++ |
|--------|--------|------|-----|
| **Bronze** | Works well | Works well | Works well |
| **Silver** | Risky (TLE on some problems) | Works well | Works well |
| **Gold** | Not recommended | Works (occasionally tight) | Recommended |
| **Platinum** | Not viable | Occasionally tight | Strongly recommended |
| **Coding speed** | Fastest to write | Medium | Slowest to write (but fastest to run) |
| **Runtime speed** | Slowest | Medium | Fastest |
| **Memory usage** | Highest | High | Lowest |

### The practical recommendation

- **Start with whatever you are most comfortable in.** For your first few Bronze contests, the language does not matter. Getting comfortable with the contest format is more important than language choice.
- **Transition to C++ by Silver.** Python's speed becomes a real problem in Silver, where n can be 100,000 or more. Java works fine for Silver but starts getting tight in Gold.
- **Use C++ for Gold and Platinum.** The time limits are designed with C++ in mind. Java gets a 2x time multiplier on USACO (your code gets twice the time limit), but even with that, some Gold and Platinum problems are tight.
- **This book prepares you for the switch.** Every chapter teaches all three languages, so by the time you reach Silver, C++ will feel familiar.

{% hint style="info" %}
**You do not have to switch all at once.** Some students use Python for quick prototyping (to test their algorithm on the sample cases) and then rewrite in C++ for the actual submission. This is a valid strategy if you are fast enough.
{% endhint %}

### TLE: Time Limit Exceeded

TLE is the most common reason Python solutions fail in Silver and above. A problem with a 2-second time limit in C++ might need 4 seconds in Java (with the multiplier) and would need 10+ seconds in Python -- far beyond any time limit. The algorithm might be correct, but the language is too slow to execute it in time.

---

## C.8 What to Prepare

Contest day should feel routine, not chaotic. Prepare everything in advance.

### Your computer setup

- **Reliable computer**: Make sure it will not run out of battery or overheat during 4 hours. Plug it in.
- **Stable internet**: If your home Wi-Fi is flaky, consider going to a library or using a wired connection. You need internet to submit solutions and (ideally) to check results.
- **Your IDE or editor**: Have your preferred development environment set up and tested. Make sure you can compile and run code in all your contest languages.
- **A browser tab with usaco.org** open and logged in before the contest.

### Templates and snippets

USACO allows you to use your own pre-written code. Many competitors have templates ready for:

- **Fast I/O**: Especially important in C++ and Java.
- **Common data structures**: If you have a segment tree or Union-Find template you trust, have it ready.
- **Standard includes**: In C++, a file with `#include <bits/stdc++.h>` and common macros.

{% hint style="info" %}
**Templates must be YOUR code.** You can prepare templates in advance, and you should. But do not copy someone else's template that you do not understand. If something goes wrong, you need to be able to debug it.
{% endhint %}

### Your physical environment

- **A quiet room** where nobody will interrupt you for 4 hours.
- **Water and snacks** within reach. You do not want to break your focus to get food.
- **Paper and a pen** for sketching diagrams, working through examples by hand, and planning your approach before coding.
- **A clock or timer** visible so you can track your remaining time (the USACO page also shows your timer).

### Mental preparation

- **Get a good night's sleep** the night before.
- **Do not cram** the morning of the contest. If you do not know an algorithm by contest day, you are not going to learn it in 30 minutes.
- **Warm up** by solving one easy practice problem 30-60 minutes before starting.

---

## C.9 Practice Resources

Consistent practice is what separates students who promote from those who stay stuck. Here are the best resources, in order of relevance:

### 1. Past USACO Problems (usaco.org)

The single best practice resource. USACO archives all past contest problems with test data and editorials (official solutions with explanations).

- Go to **usaco.org** and find the "Contest Results" or "Problems" section.
- Problems are organized by season, contest, and division.
- Start by solving past Bronze problems. When you can consistently solve 2-3 Bronze problems in 4 hours, you are ready for a real contest.

### 2. USACO Guide (usaco.guide)

A community-maintained website that organizes USACO topics into a study curriculum. It includes:

- Topic explanations with recommended problems
- Difficulty ratings for each problem
- Links to editorials
- A progress tracker

This is an excellent companion to this book. Many of the topics align directly with our chapters.

### 3. Codeforces (codeforces.com)

The largest competitive programming platform. Useful features for USACO preparation:

- **Virtual contests**: Replay any past contest as if it were live, with a timer.
- **Problem ratings**: Problems are rated by difficulty (800 = easy, 2000+ = very hard). Start around 800-1200 for Bronze-level practice.
- **Editorials**: Most contests have detailed solution explanations.
- **Active community**: Ask questions and discuss solutions in the comments.

### 4. AtCoder (atcoder.jp)

A Japanese competitive programming platform with excellent problems. Known for:

- **Clean, well-stated problems** with no ambiguity.
- **AtCoder Beginner Contests (ABC)**: Problems A-D are great for Bronze/Silver practice.
- **AtCoder Educational DP Contest**: 26 DP problems that map directly to Ch 23-25 of this book.

### 5. This book

This workbook is designed to map directly to USACO divisions:

| Book section | USACO division | Key chapters |
|-------------|---------------|-------------|
| Part I (Ch 2-6) | Pre-Bronze (fundamentals) | Language basics, complexity analysis |
| Part II (Ch 7-13) | Bronze | Complete search, simulation, sorting, recursion |
| Part III (Ch 14-22) | Silver | Prefix sums, binary search, greedy, graphs |
| Part IV (Ch 23-29) | Gold | DP, trees, shortest paths, Union-Find |
| Part V (Ch 30-34) | Platinum | Segment trees, advanced DP, strings, geometry |

Work through the chapters in order. By the time you finish a Part, you should be ready to attempt that division.

---

## C.10 Your Training Plan

Here is a realistic, week-by-week training plan that maps this book to the USACO season. This assumes you are starting from scratch and studying 5-8 hours per week.

### Phase 1: Foundation (Weeks 1-8)

**Goal**: Learn to code in all three languages and understand complexity.

| Weeks | Chapters | What you are learning |
|-------|----------|----------------------|
| 1-2 | Ch 0-1 | Dev environment setup, Git, problem-solving basics |
| 3-4 | Ch 2-3 | Variables, I/O, conditions, loops in Python/Java/C++ |
| 5-6 | Ch 4-5 | Functions, arrays, lists, maps |
| 7-8 | Ch 6 | Big-O notation, analyzing algorithm speed |

**Milestone**: You can write, compile, and run programs in all three languages. You understand why some solutions are faster than others.

### Phase 2: Bronze Ready (Weeks 9-20)

**Goal**: Master the topics tested in USACO Bronze.

| Weeks | Chapters | What you are learning |
|-------|----------|----------------------|
| 9-10 | Ch 7-8 | Number theory basics, sorting algorithms |
| 11-12 | Ch 9-10 | Searching, recursion |
| 13-14 | Ch 11-12 | Hash maps, bit manipulation |
| 15-17 | Ch 13 | Complete search, backtracking, simulation |
| 18-20 | Practice | Past USACO Bronze problems (aim for 15-20 problems) |

**Milestone**: You can solve 2 out of 3 past Bronze problems within 4 hours. **Try your first real USACO Bronze contest.**

```
Timeline visualization:

Week:  1----8----12----16----20----26----34----42----50----58----62
       |         |           |          |          |          |
       v         v           v          v          v          v
    Foundation  Bronze      Silver     Gold      Platinum   Advanced
    Ch 0-6      Ch 7-13    Ch 14-22   Ch 23-29  Ch 30-34   Practice
                  |           |          |          |
                  v           v          v          v
              First       Attempt    Attempt    Attempt
              Bronze!     Silver     Gold       Platinum
```

### Phase 3: Silver Ready (Weeks 21-34)

**Goal**: Learn the intermediate algorithms needed for USACO Silver.

| Weeks | Chapters | What you are learning |
|-------|----------|----------------------|
| 21-22 | Ch 14-15 | Prefix sums, two pointers, sliding window |
| 23-24 | Ch 16-17 | Binary search on answers, heaps |
| 25-26 | Ch 18 | Greedy algorithms |
| 27-30 | Ch 19-22 | Graphs (BFS, DFS), linked lists, stacks, queues |
| 31-34 | Practice | Past USACO Silver problems (aim for 15-20 problems) |

**Milestone**: You can solve 2 out of 3 past Silver problems within 4 hours. **Attempt USACO Silver.**

### Phase 4: Gold Ready (Weeks 35-50)

**Goal**: Master DP, trees, and advanced graph algorithms for USACO Gold.

| Weeks | Chapters | What you are learning |
|-------|----------|----------------------|
| 35-38 | Ch 23-25 | Dynamic programming (foundation, grids, subsequences) |
| 39-42 | Ch 26-27 | Trees, shortest paths (Dijkstra, Bellman-Ford) |
| 43-45 | Ch 28-29 | Topological sort, Union-Find, MST |
| 46-50 | Practice | Past USACO Gold problems (aim for 20+ problems) |

**Milestone**: You can solve 1-2 out of 3 past Gold problems within 4 hours. **Attempt USACO Gold.**

### Phase 5: Platinum Ready (Weeks 51-62)

**Goal**: Learn advanced techniques for USACO Platinum.

| Weeks | Chapters | What you are learning |
|-------|----------|----------------------|
| 51-53 | Ch 30 | Segment trees, range queries |
| 54-56 | Ch 31-32 | Advanced DP, string algorithms |
| 57-59 | Ch 33-34 | Advanced trees/graphs, computational geometry |
| 60-62 | Practice | Past USACO Platinum problems |

**Milestone**: You can solve at least 1 Platinum problem within 4 hours. **Attempt USACO Platinum.**

{% hint style="info" %}
**This is a 62-week plan -- about 14 months.** That is aggressive but realistic if you are consistent. Many students take 2-3 years to reach Platinum, and that is completely fine. The plan is a guide, not a deadline. If a topic takes longer, spend the extra time. Rushing past topics you do not understand will hurt you in later divisions.
{% endhint %}

---

## C.11 Common Questions

### "What if I do not solve any problems in my first contest?"

That is completely normal and nothing to worry about. Many successful USACO competitors scored 0 or close to 0 in their first contest. The first contest is about learning the format -- how the judge works, how to read USACO-style problems, how to manage your time under pressure. Treat it as a learning experience, not a test.

### "Can I use templates and pre-written code snippets?"

Yes. You can use any code you wrote yourself. Many competitors have templates for fast I/O, common data structures, and standard algorithms. You should NOT copy code from someone else during the contest, but using your own pre-prepared templates is expected and encouraged.

### "What if my internet disconnects during the contest?"

First, do not panic. Your timer keeps running, but the USACO team understands that technical issues happen. If you lose internet briefly, just reconnect and continue. If you have a major outage, email the USACO administrators (their contact info is on the website). They have been known to grant extensions for documented technical issues, though this is not guaranteed.

Save your solution files locally. Even if you lose internet, you will not lose your code.

### "Can I compete if I am not in the United States?"

Absolutely. USACO is open to any pre-college student worldwide. Your country does not affect your eligibility or your division placement. The only restriction is that to be selected for the US IOI team, you must be a US citizen or permanent resident -- but competing in USACO contests and promoting through divisions is open to everyone.

### "How many times can I try for promotion?"

You get up to four chances per season (December, January, February, and the US Open). If you do not promote this season, your division carries over to next season, and you get four more chances. There is no limit on the number of seasons you can compete.

### "What happens if I promote mid-season?"

You immediately compete in your new division at the next contest. For example, if you promote from Bronze to Silver in December, you take the Silver contest in January. This is great because it means you get practice in the new division right away.

### "Can I compete in a lower division after promoting?"

No. Once you promote, you compete in the higher division for all future contests. This is permanent -- there is no way to go back to a lower division.

### "Is USACO harder than Codeforces / AtCoder / LeetCode?"

Each platform has a different style. USACO problems tend to be longer, with more detailed stories and real-world scenarios (cows, farms, etc.). They often require you to combine multiple techniques in a single problem. Codeforces problems are shorter and more numerous, testing speed. LeetCode is more focused on interview-style problems. All of them are useful for practice, but USACO problems are the best preparation for USACO contests.

### "Do I need to know advanced math?"

Not much. Bronze and Silver require very basic math (modular arithmetic, GCD, simple counting). Gold introduces a bit more (graphs are mathematical objects), and Platinum occasionally uses number theory or geometry. But USACO is fundamentally about algorithms and programming, not math competitions. If you have worked through this book, you have all the math you need.

### "I am scared to compete. What if I embarrass myself?"

Nobody will know your score unless you tell them. USACO results are not published with your real name -- only your username appears on scoreboards, and participation is private. There is literally no downside to trying. The worst case is that you learn something about what you need to study next.

---

## C.12 Your First Contest: A Step-by-Step Walkthrough

Your first contest will feel scary, and that is okay. Here is exactly what to expect, minute by minute. Reading this in advance will make the real thing feel familiar instead of foreign.

### Before you start (T-minus 30 minutes)

- [x] Computer is plugged in and charged.
- [x] IDE or text editor is open with a fresh file.
- [x] Browser is open with usaco.org loaded and you are logged in.
- [x] Water, snacks, and paper/pen are within reach.
- [x] Phone is silenced and put away.
- [x] Family knows not to disturb you for the next 4.5 hours.
- [x] You have solved one easy warm-up problem to get your brain going.

### Starting the contest (T = 0:00)

Click "Begin Contest." The page will show you three problems labeled Problem 1, Problem 2, and Problem 3. Your 4-hour timer appears on screen. Take a deep breath.

### Reading phase (T = 0:00 to 0:15)

**Read all three problems before writing any code.** For each problem:

1. Read the problem statement carefully. USACO problems often have a story (usually involving cows -- that is a USACO tradition). Separate the story from the actual requirements.
2. Look at the **input format** and **output format**.
3. Study the **sample input and output**. Work through the sample by hand to make sure you understand what the problem is asking.
4. Check the **constraints** (the value of n). This tells you what time complexity you need.
5. Make a mental note: "This problem looks easy / medium / hard to me."

After reading all three, decide which to attempt first. Start with the one that feels most approachable.

### Problem 1 -- Your best shot (T = 0:15 to 1:30)

- **Plan before you code** (5-10 minutes). On paper, outline your approach. What data structures will you use? What is the algorithm? What edge cases might there be?
- **Code the solution** (20-40 minutes). Write clean, readable code. Use meaningful variable names -- you might need to debug this later.
- **Test on the sample input** (5 minutes). Run your code locally on the sample input from the problem. Does your output match the sample output exactly? If not, debug.
- **Submit** (2 minutes). Upload your source file. Wait for the results.
- **Evaluate the results.** If you got 10/10, great -- move on. If you got 7/10 or 8/10, think about what the failing test cases might be (large inputs? edge cases?). If you got 3/10 or fewer, your approach might be wrong -- but leave it for now and come back later.

{% hint style="info" %}
**Do not spend too long on any single problem in your first contest.** Getting partial credit on two problems is better than getting a perfect score on one and zero on the others. Budget roughly 75-90 minutes per problem.
{% endhint %}

### Problem 2 -- The next challenge (T = 1:30 to 2:45)

Repeat the same process: plan, code, test, submit. If this problem feels too hard after 15 minutes of thinking, skip to Problem 3 and come back.

### Problem 3 -- Whatever is left (T = 2:45 to 3:45)

By now you have submitted two problems (even if with partial scores). Attack the third problem. If you cannot solve it optimally, write the brute force solution and submit it for partial credit. Even 200-300 points from a brute force can make the difference in promotion.

### Review phase (T = 3:45 to 4:00)

Use the last 15 minutes to:

- **Revisit problems where you lost points.** Can you fix a bug and resubmit?
- **Check for silly mistakes**: off-by-one errors, wrong variable names, forgetting to read all the input.
- **Submit any improved solutions.** Remember, only your last submission counts, so there is no penalty for resubmitting.

### After the contest

- **Do not panic about your score.** Whatever happened, it is done.
- **Read the editorials** when USACO publishes them (usually within a few days). Understanding the intended solutions is one of the best ways to learn.
- **Upsolve**: Try to solve any problems you did not get during the contest, using the editorial as a guide if needed. This is where the real learning happens.
- **Reflect**: What went well? What would you do differently? Did you manage your time well?

---

## C.13 After the Contest: The Upsolving Habit

The most important thing you can do after a contest is **upsolve** -- go back and solve the problems you could not solve during the contest.

### Why upsolving matters

During the contest, you are under time pressure and stress. After the contest, you can think clearly, read the editorial, and learn from your mistakes. Most of your improvement will come from upsolving, not from the contest itself.

### How to upsolve effectively

1. **Try the problem again** without looking at the editorial (give yourself another 30-60 minutes).
2. **If still stuck, read the editorial.** Understand the approach -- do not just read the code.
3. **Code the solution yourself** from scratch, using the editorial's approach but your own code.
4. **Submit it** on the USACO practice server to verify it passes all test cases.
5. **Write a short note** about what you learned: "This problem required [technique]. I missed it because [reason]. Next time I will [lesson]."

{% hint style="info" %}
**Errichto's 20-minute rule** (mentioned in this book's chapters): If you are stuck on a problem for 20 minutes with no new ideas, read the editorial. Understanding solutions IS learning. Staring at a screen for hours without progress is not.
{% endhint %}

---

## C.14 Season Planning and Long-Term Strategy

### Aligning your study with the USACO calendar

The USACO season runs December through March/April. Here is how to plan around it:

| Time of year | What to focus on |
|-------------|-----------------|
| **Summer/Fall** (Jun-Nov) | Study new topics, work through book chapters, solve practice problems |
| **Early December** | Review topics for your target division, solve recent past problems |
| **December contest** | Your first attempt of the season -- treat it as practice |
| **January** | Upsolve December problems, address weak spots |
| **January contest** | Second attempt -- apply what you learned |
| **February** | More targeted practice on weak areas |
| **February contest** | Third attempt |
| **March** | Prepare for the US Open (slightly harder problems) |
| **US Open** | Final attempt of the season -- give it your best shot |
| **April-May** | Upsolve all four contests, plan for next season |

### Setting realistic goals

Do not set your goal as "promote to Platinum this season." Instead, set process goals:

- "I will study 6 hours per week, every week."
- "I will solve 3 practice problems per week."
- "I will upsolve every contest problem within one week of the contest."
- "I will finish Part III of the book before the February contest."

Process goals keep you motivated because they are within your control. Promotion depends partly on the difficulty of the specific contest you take -- process goals depend only on your effort.

### The long game

Here is a realistic trajectory for a student starting in 8th or 9th grade:

| Year | Realistic goal | What you are learning |
|------|---------------|----------------------|
| **Year 1** | Promote to Silver (maybe Gold) | Fundamentals + Bronze + Silver topics |
| **Year 2** | Promote to Gold (maybe Platinum) | Silver + Gold topics, lots of practice |
| **Year 3** | Compete in Platinum | Gold + Platinum topics, advanced practice |

Some students move faster, some slower. Neal Wu -- one of the most famous competitive programmers -- started competing in 8th grade, just like you might be doing right now. He did not become an IOI gold medalist overnight. It took years of consistent practice.

{% hint style="info" %}
**The most important thing is consistency.** Studying 1 hour every day is far more effective than studying 7 hours on Sunday. Your brain needs time to absorb and consolidate what you learn. Spread your practice out.
{% endhint %}

---

## C.15 Quick Reference Card

Keep this handy during contest season:

### Key URLs

| Resource | URL |
|----------|-----|
| USACO official site | usaco.org |
| USACO contest login | usaco.org (same site -- log in and find current contest) |
| Past problems & editorials | usaco.org (archived by season) |
| USACO Guide (community) | usaco.guide |
| Codeforces | codeforces.com |
| AtCoder | atcoder.jp |

### Contest checklist

Before every contest, verify:

- [ ] USACO account works (can log in)
- [ ] Computer is charged and plugged in
- [ ] Internet connection is stable
- [ ] IDE/editor works for your contest language
- [ ] Templates are ready (if you use them)
- [ ] 4+ uninterrupted hours are available
- [ ] Water, snacks, paper, pen are ready
- [ ] Phone is off or silenced

### Division quick reference

| Division | You need to know | This book's chapters |
|----------|-----------------|---------------------|
| Bronze | Complete search, simulation, sorting, ad hoc | Ch 7-13 (Part II) |
| Silver | Prefix sums, two pointers, binary search, greedy, BFS/DFS | Ch 14-22 (Part III) |
| Gold | DP, trees, shortest paths, Union-Find, MST | Ch 23-29 (Part IV) |
| Platinum | Segment trees, advanced DP, strings, geometry | Ch 30-34 (Part V) |

### Scoring quick reference

| Fact | Value |
|------|-------|
| Problems per contest | 3 |
| Test cases per problem | 10 |
| Points per test case | 100 |
| Points per problem | 1,000 |
| Maximum total score | 3,000 |
| Time limit | 4 hours |
| Resubmissions allowed | Unlimited |

---

## Closing Words

You now know everything you need to register for USACO, prepare for a contest, and build a long-term training plan. The only thing left is to actually do it.

Your first contest will feel intimidating. You might not solve anything. You might make silly mistakes. You might run out of time. All of that is normal, and all of it is part of the process.

Every Platinum competitor was once a nervous Bronze beginner who was not sure if they belonged. The difference is that they kept showing up, kept solving problems, and kept learning from their mistakes.

You have this book. You have a plan. Now go register at usaco.org and start your journey.

See also: [Appendix A: Contest Strategy & Time Management](contest-strategy.md) for detailed in-contest tactics, and [Appendix B: Patterns Cheatsheet](patterns-cheatsheet.md) for a quick reference of the algorithms and techniques covered in this book.
