# The Coder's Toolkit — Git & Problem Solving

## Chapter Goals

- [ ] Understand what Git is and why every programmer needs it
- [ ] Create your first repository, make commits, and explore your history
- [ ] Learn how to read and understand competitive programming problem statements
- [ ] Solve your very first coding problem in Python, Java, and C++

---

## The Story: "The Time Traveler's Notebook"

Maya had a science project due Friday: build a simulation of the solar system. By Tuesday she had Mercury, Venus, and Earth orbiting a glowing yellow sun. It was beautiful.

"What if I add gravity calculations?" she thought. She started rewriting the orbital math. Twenty minutes later, the screen was a mess. Earth was flying into the sun. Venus had disappeared entirely. And she couldn't remember what the working code looked like before she changed it.

"I wish I could go back in time," she muttered.

Her older brother Kai walked in, glanced at her screen, and grinned. "You can."

He showed her a tool called **Git**. With one command, she could take a "snapshot" of her entire project at any moment. She saved her working three-planet version. Then she experimented wildly — adding gravity, trying rings on Saturn, making comets fly across the screen. Some experiments broke everything. But it didn't matter. She could always jump back to any snapshot that worked.

By Thursday, Maya's simulation had all eight planets, realistic gravity, and a shooting star easter egg. She'd tried dozens of wild ideas because she was never afraid of breaking things.

That's Git. It's a time machine for your code.

---

## Johari Window: Before

Before diving in, take a moment to honestly assess where you are. Fill out the "Before" section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
**Be honest!** The Johari Window only helps if you're truthful about what you know and don't know. There's no shame in "I have no idea" — that's where the best learning happens.
{% endhint %}

---

## 1.1 What is Git?

Imagine you're playing a video game with no save points. Every time you mess up, you start over from the very beginning. Brutal, right?

Now imagine a game where you can save whenever you want. Before a tough boss fight? Save. About to try a risky move? Save first. If things go wrong, reload and try again.

**Git is a save system for your code.**

Every time you "save" (called a **commit** in Git), Git takes a snapshot of every file in your project. You can look back at any snapshot, compare what changed, or jump back in time if something breaks.

Here's what a project's history looks like in Git:

```
[commit 1] -----> [commit 2] -----> [commit 3] -----> [commit 4]
"started           "added             "fixed a           "added
 the project"       input/output"      bug"               colors"
```

Each circle is a **commit** — a saved snapshot of your code at a moment in time. Together, they form a **timeline** of your project.

### Key vocabulary

| Term | What it means | Video game equivalent |
|------|--------------|----------------------|
| **Repository (repo)** | A project folder tracked by Git | Your game's save folder |
| **Commit** | A saved snapshot of your code | A save point |
| **Commit message** | A note describing what changed | "Defeated the dragon" save label |
| **History / Log** | The list of all your commits | Your list of save files |

{% hint style="info" %}
**Why does this matter for competitive programming?** As you solve harder problems, you'll try many approaches. Git lets you experiment fearlessly. Try a brute-force solution, commit it, then try a clever optimization. If the optimization breaks things, you can always go back.
{% endhint %}

---

## 1.2 Your First Repository

Let's create your very first Git repository, step by step. Open your terminal and follow along.

### Step 1: Create a folder and initialize Git

```bash
mkdir my-first-repo
cd my-first-repo
git init
```

You'll see: `Initialized empty Git repository in .../my-first-repo/.git/`

Congratulations — you just created a repository! The `git init` command creates a hidden `.git` folder that stores all of Git's tracking data.

### Step 2: Create a file

```bash
echo "Hello, Git!" > hello.txt
```

### Step 3: Check the status

```bash
git status
```

Git will tell you that `hello.txt` is an **untracked file**. Git sees it, but isn't tracking it yet. Think of it like this: the file exists, but Git hasn't been told to care about it.

### Step 4: Stage and commit

```bash
git add hello.txt
git commit -m "Add hello.txt with a greeting"
```

Two things happened:

1. **`git add`** — This moves the file to the **staging area** (like putting items in a box before shipping). You're telling Git: "Include this file in my next save."
2. **`git commit -m "..."`** — This creates the actual save point. The `-m` flag lets you write a message describing what you did.

{% hint style="warning" %}
**Always write meaningful commit messages.** "Fixed stuff" tells future-you nothing. "Fix off-by-one error in binary search" tells future-you exactly what happened and why.
{% endhint %}

### Step 5: See your history

```bash
git log
```

You'll see something like:

```
commit a1b2c3d4... (HEAD -> main)
Author: Your Name <you@example.com>
Date:   Mon Jan 6 10:30:00 2025

    Add hello.txt with a greeting
```

That's your first entry in the timeline. Every commit has a unique ID (that long `a1b2c3d4...` string), the author, the date, and your message.

### Step 6: Make a change and see the diff

```bash
echo "This is my first Git project." >> hello.txt
git diff
```

`git diff` shows you exactly what changed since your last commit. Lines that were added show up with a `+` in front. Lines that were removed show up with a `-`. This is incredibly useful when you're debugging — "What did I actually change?"

### Step 7: Commit the change

```bash
git add hello.txt
git commit -m "Add project description to hello.txt"
```

Now run `git log` again — you'll see two commits in your history. You're building a timeline!

### The Git workflow in three commands

You'll use this cycle hundreds of times:

```
1. Edit your files
2. git add <files>       ← stage what you want to save
3. git commit -m "..."   ← create the save point
```

That's it. Those three steps are 90% of everything you'll do with Git.

---

## 1.3 Branching: Trying New Ideas Safely

Here's where Git gets really powerful. Let's say you have a working solution to a problem, but you want to try a completely different approach. You don't want to risk breaking what works.

**Branches** let you create a parallel timeline. You can experiment on the branch without affecting your main code. If the experiment works, you merge it back. If it fails, you just delete the branch. No harm done.

```
main:       [commit 1] --> [commit 2] --> [commit 3] -----------> [commit 5 — merged!]
                                  \                               /
experiment:                        --> [commit 4: try new idea] --
```

### Create a branch

```bash
git checkout -b experiment
```

This creates a new branch called `experiment` and switches to it. You're now on a parallel timeline.

### Make changes on the branch

```bash
echo "This is an experiment!" > experiment.txt
git add experiment.txt
git commit -m "Add experimental feature"
```

### Switch back to main

```bash
git checkout main
```

Look — `experiment.txt` doesn't exist here! Your main branch is completely untouched. That's the magic of branches.

### Merge the branch back

If you're happy with your experiment:

```bash
git merge experiment
```

Now `experiment.txt` appears on `main` too. The parallel timelines have merged back together.

### Delete the branch (optional cleanup)

```bash
git branch -d experiment
```

{% hint style="info" %}
**For competitive programming**, branches are great when you want to try a different algorithm for the same problem. Commit your brute-force solution on `main`, create a branch, try the optimized approach. If it works, merge it. If not, switch back to `main` — your brute-force solution is still safe.
{% endhint %}

---

## 1.4 How to Use This Workbook

This workbook is itself a Git repository. Here's the workflow you'll follow for every chapter.

### Step 1: Fork and clone (one-time setup)

If you haven't already, fork this repo on GitHub and clone it to your computer:

```bash
git clone https://github.com/YOUR-USERNAME/dsa-a2z.git
cd dsa-a2z
```

### Step 2: Create a branch for the chapter

```bash
git checkout -b ch01-solutions
```

### Step 3: Fill out the Johari Window "Before"

Open the chapter's `johari.md` file and fill in the "Before" section honestly.

### Step 4: Work through the chapter

Read the explanations, try the examples, and solve the practice problems. Your code goes in the `code/` directory:

```
code/
  python/ch01/practice/    ← Your Python solutions go here
  java/ch01/practice/      ← Your Java solutions go here
  cpp/ch01/practice/       ← Your C++ solutions go here
```

### Step 5: Run the tests

{% tabs %}
{% tab title="Python" %}
```bash
python -m pytest code/python/ch01/tests/ -v
```
{% endtab %}

{% tab title="Java" %}
```bash
cd code/java
javac ch01/practice/Warmup01Sum.java
java -cp . ch01.practice.Warmup01Sum
```
{% endtab %}

{% tab title="C++" %}
```bash
cd code/cpp
make test-ch01
```
{% endtab %}
{% endtabs %}

Or use the helper script:

```bash
./scripts/run_tests.sh ch01 python
./scripts/run_tests.sh ch01 java
./scripts/run_tests.sh ch01 cpp
```

### Step 6: Commit your work

```bash
git add code/python/ch01/practice/warmup_01_sum.py
git commit -m "Solve ch01 warmup: Sum of Two Numbers (Python)"
```

### Step 7: Fill out the Johari Window "After"

Go back to `johari.md` and fill in the "After" section. Compare with your "Before" — notice what changed?

### Step 8: Push your work

```bash
git push origin ch01-solutions
```

---

## 1.5 Reading Problem Statements

Competitive programming problems follow a very specific format. Learning to read them carefully is a skill — and it's one that separates good competitors from great ones.

Here's a sample problem statement. Read it, and then we'll break it down piece by piece.

---

> ### Sum of Two Numbers
>
> **Problem:** Given two integers, find their sum.
>
> **Input format:**
> A single line containing two space-separated integers `a` and `b`.
>
> **Output format:**
> Print a single integer — the sum of `a` and `b`.
>
> **Constraints:**
> `-10^6 <= a, b <= 10^6`
>
> **Examples:**
>
> | Input | Output |
> |-------|--------|
> | `1 2` | `3` |
> | `0 0` | `0` |
> | `-5 5` | `0` |

---

### Breaking it down

**1. The problem description** tells you *what* to do. Read it carefully — sometimes a single word changes the whole approach.

**2. Input format** tells you *exactly* what your program will receive. Here, it's two integers on one line, separated by a space. Pay attention to:
- How many lines of input?
- What type of data? (integers, strings, floating point?)
- What separator? (spaces, newlines, commas?)

**3. Output format** tells you *exactly* what to print. Match this precisely. If it says "print a single integer," don't print `The answer is 3` — just print `3`.

**4. Constraints** tell you how big the input can be. This matters a lot for choosing your algorithm:
- Numbers up to 10^6? A regular `int` in any language can handle that.
- Numbers up to 10^18? You might need `long` in Java or `long long` in C++.
- Array of size up to 10^5? You can probably try an O(n^2) approach.
- Array of size up to 10^6? You need O(n log n) or better.

{% hint style="warning" %}
**The #1 mistake beginners make:** Not reading the constraints. Your solution might be correct but too slow. Always check the limits!
{% endhint %}

**5. Examples** give you concrete test cases. Use them to:
- Verify you understand the problem correctly
- Test your solution before submitting
- Look for edge cases (notice how `0 0` and `-5 5` are included — both produce `0` but for different reasons)

### A reading checklist

Every time you see a new problem, ask yourself:

1. What are the **inputs**? (type, count, range)
2. What is the **output**? (type, format)
3. What are the **constraints**? (how big can things get?)
4. Are there **edge cases** in the examples? (zeros, negatives, maximums)
5. Can I explain the problem in **my own words**?

---

## 1.6 Your First Problem: "Sum of Two Numbers"

Time to write actual code! This is deliberately simple so you can focus on the workflow: read the problem, write the code, run the tests, commit your work.

> **Problem:** Given two integers, print their sum.
>
> **Input:** A single line with two space-separated integers `a` and `b`.
>
> **Output:** A single integer — the sum of `a` and `b`.
>
> **Constraints:** `-10^6 <= a, b <= 10^6`

### The solution in all three languages

{% tabs %}
{% tab title="Python" %}
```python
# Read two integers from input (they're on the same line, separated by a space)
a, b = map(int, input().split())

# Print their sum
print(a + b)
```

**How it works:**
- `input()` reads a line of text from the user
- `.split()` breaks it into pieces at each space: `"1 2"` becomes `["1", "2"]`
- `map(int, ...)` converts each piece to an integer
- `a, b = ...` assigns them to two variables
{% endtab %}

{% tab title="Java" %}
```java
import java.util.Scanner;

public class Warmup01Sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read two integers
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        // Print their sum
        System.out.println(a + b);

        scanner.close();
    }
}
```

**How it works:**
- `Scanner` reads input from the user
- `scanner.nextInt()` reads the next integer from the input
- `System.out.println()` prints a line of output
{% endtab %}

{% tab title="C++" %}
```cpp
#include <iostream>
using namespace std;

int main() {
    // Read two integers
    int a, b;
    cin >> a >> b;

    // Print their sum
    cout << a + b << endl;

    return 0;
}
```

**How it works:**
- `#include <iostream>` gives us input/output tools
- `cin >> a >> b` reads two integers from input
- `cout << ... << endl` prints the result followed by a newline
{% endtab %}
{% endtabs %}

### Try it yourself

The skeleton files are waiting for you in the `code/` directory. Open them up, write your solution, and run the tests:

| Language | Skeleton file | Solution (don't peek!) |
|----------|-------------|----------------------|
| Python | `code/python/ch01/practice/warmup_01_sum.py` | `code/python/ch01/solutions/warmup_01_sol.py` |
| Java | `code/java/ch01/practice/Warmup01Sum.java` | `code/java/ch01/solutions/Warmup01Sol.java` |
| C++ | `code/cpp/ch01/practice/warmup_01_sum.cpp` | `code/cpp/ch01/solutions/warmup_01_sol.cpp` |

### Running the tests

{% tabs %}
{% tab title="Python" %}
```bash
python -m pytest code/python/ch01/tests/test_warmup_01.py -v
```

You should see output like:
```
test_warmup_01.py::test_sum_positive PASSED
test_warmup_01.py::test_sum_zeros PASSED
test_warmup_01.py::test_sum_negative_positive PASSED
test_warmup_01.py::test_sum_large PASSED
test_warmup_01.py::test_sum_negatives PASSED
```
{% endtab %}

{% tab title="Java" %}
```bash
cd code/java
javac ch01/practice/Warmup01Sum.java
echo "1 2" | java -cp . ch01.practice.Warmup01Sum
```

You should see: `3`
{% endtab %}

{% tab title="C++" %}
```bash
cd code/cpp
make test-ch01
```

You should see: `test_warmup_01... PASS`
{% endtab %}
{% endtabs %}

### Commit your work!

Once all tests pass:

```bash
git add code/python/ch01/practice/warmup_01_sum.py
git add code/java/ch01/practice/Warmup01Sum.java
git add code/cpp/ch01/practice/warmup_01_sum.cpp
git commit -m "Solve ch01: Sum of Two Numbers in all 3 languages"
```

{% hint style="success" %}
**You just completed your first full competitive programming workflow!** Read the problem, write the code, test it, commit it. Every chapter from here on follows this same pattern. It becomes second nature fast.
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Gotcha #1: Forgetting to `git add` before committing**

```bash
# You edit warmup_01_sum.py, then run:
git commit -m "Solve the problem"
# Nothing happens! Your changes aren't staged.

# Fix: Always add first
git add warmup_01_sum.py
git commit -m "Solve the problem"
```

Think of it this way: `git add` puts items in the shipping box. `git commit` ships the box. If you don't put anything in the box, there's nothing to ship.
{% endhint %}

{% hint style="danger" %}
**Gotcha #2: Committing to the wrong branch**

You meant to work on `ch01-solutions` but you're on `main`. Oops!

**Prevention:** Always check which branch you're on before working:
```bash
git status    # Shows the current branch at the top
git branch    # Lists all branches, with * next to the current one
```

**Fix:** If you already committed to the wrong branch, don't panic. Ask your mentor or look up `git cherry-pick` — it lets you move commits between branches.
{% endhint %}

{% hint style="danger" %}
**Gotcha #3: "Detached HEAD" — the scariest Git message**

You might see this:
```
You are in 'detached HEAD' state...
```

Don't panic! This usually happens when you `git checkout` a specific commit ID instead of a branch name. You're looking at a snapshot in time, but you're not on any branch.

**Fix:** Just switch back to a branch:
```bash
git checkout main
```

If you made changes you want to keep while in detached HEAD, create a branch first:
```bash
git checkout -b save-my-work
```
{% endhint %}

{% hint style="danger" %}
**Gotcha #4: Misreading the input format**

When a problem says "two space-separated integers," it means `1 2` on one line — not `1` on one line and `2` on the next. Read the input format very carefully and compare with the examples.
{% endhint %}

---

## Johari Window: After

Now fill out the "After" section of your [Johari Window worksheet](johari.md). Compare it with your "Before" — what changed? What surprised you?

---

## What's Next

In **Chapter 2: Your First Programs — Speaking Three Languages**, you'll write real programs in Python, Java, and C++ side by side. You'll learn how each language handles variables, input/output, and basic operations — and start to see why competitive programmers choose different languages for different situations.

You've got your toolkit ready. Now it's time to build something with it.
