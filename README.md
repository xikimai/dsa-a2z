# The DSA Olympiad Workbook

**A step-by-step guide to mastering Data Structures & Algorithms — from beginner to USACO Platinum.**

Built for a teenager who already knows a little Python and Java, and is ready to become a competitive programming champion.

---

## Who Is This Book For?

You. A student who:

- Knows the basics of programming (variables, loops, if/else, simple functions)
- Wants to learn **Python, Java, AND C++** — because real competitors speak all three
- Is aiming for **USACO** (USA Computing Olympiad) and beyond
- Likes learning by *doing*, not just reading

## What Makes This Book Different?

This isn't a textbook that dumps theory on you. It's a **workbook** — you learn by solving problems.

Every chapter follows the same pattern:

1. **A Story** — a real-world scenario that makes the concept click
2. **Discovery** — try problems *before* the explanation (yes, really!)
3. **The Big Idea** — now the concept, explained clearly
4. **Multiple Solutions** — the same problem solved 2-3 different ways, each one better than the last (inspired by the Art of Problem Solving books)
5. **Gotchas** — the traps that catch everyone, so they won't catch you
6. **Practice** — warm-up, practice, and challenge problems in all three languages
7. **Johari Window** — a self-reflection tool to honestly track what you know, what surprised you, and what you still need to work on

## The Journey

| Part | What You'll Learn | USACO Level | Time |
|------|------------------|-------------|------|
| **0. The Adventure Begins** | Dev setup, Git, your first problem | Getting ready | 1-2 weeks |
| **I. Learning to Speak Code** | Programming in Python, Java & C++ | Pre-Bronze | 6-8 weeks |
| **II. The Bronze Forge** | Sorting, searching, recursion, hashing | **Bronze** | 8-10 weeks |
| **III. The Silver Arena** | Prefix sums, graphs, binary search on answers | **Silver** | 10-12 weeks |
| **IV. The Gold Crucible** | Dynamic programming, trees, shortest paths | **Gold** | 12-14 weeks |
| **V. The Platinum Summit** | Segment trees, advanced DP, geometry | **Platinum** | 10-12 weeks |

**Total: 35 chapters over ~2 years at a steady pace.**

## How to Use This Book

### Step 0: Get the Code

```bash
git clone https://github.com/xikimai/dsa-a2z.git
cd dsa-a2z
```

### Step 1: Set Up Your Environment
Start with [Chapter 0: Setting Up Your Coding Workshop](part-0-adventure-begins/ch-00-dev-environment/README.md). You'll install Python, Java, C++, and VS Code on your Mac.

### Step 2: Learn Git
[Chapter 1: The Coder's Toolkit](part-0-adventure-begins/ch-01-coders-toolkit/README.md) teaches you Git — the tool that lets you save your progress like checkpoints in a video game.

### Step 3: Work Through Chapters In Order
Each chapter builds on the previous one. Don't skip ahead (even if you think you know it — you might be surprised!).

### Step 4: For Each Chapter
1. Fill out the **Johari Window: Before** — be honest about what you know
2. Try the **Discovery problems** before reading the explanation
3. Read **The Big Idea** and study the **Multiple Solutions**
4. Read the **Gotchas** carefully
5. Solve all **Practice Problems** (warm-up → practice → challenge)
6. Run the tests to check your work: `./scripts/run_tests.sh ch01 python`
7. Fill out the **Johari Window: After** — what changed?
8. Commit your work with Git!

### Step 5: Track Your Progress
Use [PROGRESS.md](PROGRESS.md) to check off completed chapters and problems.

## Running the Code

All runnable code lives in the `code/` directory, organized by language:

{% tabs %}
{% tab title="Python" %}
```bash
# Run tests for a specific chapter
python -m pytest code/python/ch01/tests/ -v

# Run a specific test file
python -m pytest code/python/ch01/tests/test_warmup_01.py -v
```
{% endtab %}

{% tab title="Java" %}
```bash
# Compile and run
cd code/java
javac ch01/practice/Warmup01.java
java -cp . ch01.practice.Warmup01

# Run tests (JUnit)
cd code/java
javac -cp .:lib/junit-platform-console-standalone.jar ch01/tests/TestWarmup01.java
java -cp .:lib/junit-platform-console-standalone.jar org.junit.platform.console.ConsoleLauncher --select-class ch01.tests.TestWarmup01
```
{% endtab %}

{% tab title="C++" %}
```bash
# Compile and run
cd code/cpp
g++ -std=c++17 -o warmup01 ch01/practice/warmup_01.cpp
./warmup01

# Run tests
cd code/cpp
make test-ch01
```
{% endtab %}
{% endtabs %}

Or use the helper script:
```bash
./scripts/run_tests.sh ch01 python   # Run Python tests for Chapter 1
./scripts/run_tests.sh ch01 java     # Run Java tests for Chapter 1
./scripts/run_tests.sh ch01 cpp      # Run C++ tests for Chapter 1
./scripts/run_tests.sh ch01 all      # Run all languages for Chapter 1
```

## Three Languages, One Idea

Every concept in this book is shown in **Python, Java, and C++** side by side. Why three?

- **Python** — the easiest to read and write; great for learning ideas quickly
- **Java** — teaches you discipline with types and structure; works well through USACO Gold
- **C++** — the language of champions; fastest execution, essential for USACO Gold and Platinum

You'll start comfortable in Python/Java and gradually build C++ fluency alongside them.

## What is USACO?

The **USA Computing Olympiad** is *the* competitive programming contest for US students. It has four divisions:

- **Bronze** — fundamentals: arrays, sorting, brute force
- **Silver** — algorithms: graphs, prefix sums, binary search
- **Gold** — advanced: dynamic programming, shortest paths, trees
- **Platinum** — expert: segment trees, advanced DP, geometry

Contests happen in **December, January, February, and March** each year. You can register for free at [usaco.org](http://usaco.org). This workbook prepares you for all four divisions.

---

*Built with love, powered by curiosity. Let's begin.*
