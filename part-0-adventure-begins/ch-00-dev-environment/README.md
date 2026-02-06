# Setting Up Your Coding Workshop

Welcome to the very beginning. Before you can solve a single problem, write a single algorithm, or compete in a single contest, you need a place to work. Think of this chapter like setting up a woodworking shop: you need your tools organized and your workbench ready before you can build anything.

By the end of this chapter, your Mac will be a fully equipped coding machine, and you'll have written your first programs in three different programming languages.

Let's get started.

## Chapter Goals

- [ ] **Get comfortable with the Terminal** -- the command-line tool that every programmer uses daily
- [ ] **Install Python, Java, and C++** -- the three languages you'll use throughout this workbook
- [ ] **Set up VS Code** -- your code editor, customized with the right extensions
- [ ] **Write and run Hello World** in all three languages -- proof that everything works

---

## What You'll Need

Before we begin, make sure you have:

- A **Mac computer** (macOS Ventura 13 or later recommended)
- A **stable internet connection** (we'll be downloading several tools)
- About **1 hour** of uninterrupted time

That's it. Everything else, we'll install together.

---

## 0.1 Opening the Terminal

### What Is the Terminal?

The Terminal is a text-based way to talk to your computer. Instead of clicking icons and dragging windows, you type commands. It might feel strange at first -- like texting your computer instead of pointing at things -- but it's incredibly powerful. Every professional developer uses it daily, and you will too.

### How to Find It

1. Press **Cmd + Space** to open Spotlight Search
2. Type **Terminal**
3. Press **Enter**

A window will appear with a blinking cursor. That's your command line. You're in.

{% hint style="info" %}
**Pro tip:** Right-click the Terminal icon in your Dock and select **Options > Keep in Dock**. You'll be opening it a lot.
{% endhint %}

### Your First Commands

Let's try a few commands to get comfortable. Type each one and press **Enter**.

**`pwd` -- Print Working Directory** (Where am I?)

```bash
pwd
```

Expected output:

```
/Users/yourname
```

This shows you the folder you're currently in. When you first open Terminal, you start in your **home directory**.

**`ls` -- List** (What's in this folder?)

```bash
ls
```

Expected output (yours will vary):

```
Applications  Desktop  Documents  Downloads  Music  Pictures
```

**`mkdir` -- Make Directory** (Create a new folder)

```bash
mkdir Projects
```

No output means it worked. You just created a `Projects` folder.

**`cd` -- Change Directory** (Move into a folder)

```bash
cd Projects
```

Now type `pwd` again:

```bash
pwd
```

```
/Users/yourname/Projects
```

You've moved into the `Projects` folder. To go back up one level:

```bash
cd ..
```

{% hint style="info" %}
**The `..` trick:** Two dots (`..`) always means "the parent folder." So `cd ..` takes you up one level, no matter where you are.
{% endhint %}

{% hint style="warning" %}
**Spaces in commands matter.** `cd..` (no space) will NOT work. It must be `cd ..` with a space between the command and the argument.
{% endhint %}

### A Quick Summary

| Command | What It Does | Example |
|---------|-------------|---------|
| `pwd` | Shows your current folder | `pwd` |
| `ls` | Lists files and folders | `ls` |
| `cd` | Changes to a folder | `cd Documents` |
| `cd ..` | Goes up one folder | `cd ..` |
| `mkdir` | Creates a new folder | `mkdir my-project` |

You'll learn more commands as we go. For now, these five are enough to get started.

---

## 0.2 Installing Homebrew

### What Is Homebrew?

Homebrew is a **package manager** for macOS. It lets you install programming tools with a single Terminal command instead of hunting for download links on websites.

Think of it like an app store, but for developer tools -- and everything is free.

### Step 1: Install Homebrew

Copy and paste this entire command into your Terminal, then press **Enter**:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

{% hint style="info" %}
**This command is long.** Make sure you copy the whole thing. It starts with `/bin/bash` and ends with `install.sh)"`.
{% endhint %}

The installer will show you what it's going to do and ask for your **password**. This is your Mac login password. When you type it, you won't see any characters appear -- that's normal. Just type your password and press Enter.

The installation takes a few minutes. You'll see lots of text scrolling by. That's fine -- it's working.

### Step 2: Add Homebrew to Your PATH (Apple Silicon Macs)

If your Mac has an Apple Silicon chip (M1, M2, M3, or M4), you need to run two more commands. The installer will actually tell you this at the very end of its output -- look for the lines under **"Next steps"**.

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

{% hint style="info" %}
**How do I know if I have Apple Silicon?** Click the Apple menu in the top-left corner of your screen, then **About This Mac**. If it says "Apple M1" (or M2, M3, M4), you have Apple Silicon. If it says "Intel," you can skip this step.
{% endhint %}

### Step 3: Verify It Worked

```bash
brew --version
```

Expected output (version numbers may differ):

```
Homebrew 4.4.15
```

If you see a version number, you're good. If you see "command not found," close your Terminal completely (Cmd + Q), reopen it, and try again.

{% hint style="danger" %}
**"command not found" after installing?** This almost always means the PATH wasn't set up correctly. If you're on Apple Silicon, make sure you ran both commands from Step 2. Then close Terminal, reopen it, and try `brew --version` again.
{% endhint %}

---

## 0.3 Python Setup

Python is the friendliest of our three languages. It reads almost like English, and it's perfect for learning algorithms quickly. We'll install it using **pyenv**, a tool that lets you manage multiple Python versions cleanly.

### Step 1: Install pyenv

```bash
brew install pyenv
```

Expected output (abbreviated):

```
==> Fetching pyenv
==> Installing pyenv
...
==> Summary
🍺  /opt/homebrew/Cellar/pyenv/2.x.x: ... files, ...
```

### Step 2: Configure Your Shell

Run these commands to add pyenv to your shell configuration:

```bash
echo '' >> ~/.zshrc
echo '# pyenv (added by DSA workbook setup)' >> ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

Now reload your shell so the changes take effect:

```bash
source ~/.zshrc
```

### Step 3: Install Python 3.12

```bash
pyenv install 3.12.4
```

This takes a few minutes -- it's compiling Python from source. Be patient.

Expected output (last few lines):

```
Installing Python-3.12.4...
Installed Python-3.12.4 to /Users/yourname/.pyenv/versions/3.12.4
```

Now set it as your default:

```bash
pyenv global 3.12.4
```

### Step 4: Verify

```bash
python3 --version
```

Expected output:

```
Python 3.12.4
```

Let's also run a quick one-liner to make sure Python is really working:

```bash
python3 -c "print('Python is ready!')"
```

Expected output:

```
Python is ready!
```

{% hint style="warning" %}
**If you see an older Python version** (like 3.9), your shell might not be picking up pyenv. Try closing and reopening Terminal, then run `python3 --version` again.
{% endhint %}

---

## 0.4 Java Setup

Java is a more structured language than Python. It requires you to be explicit about types (like saying "this variable is a number" or "this variable is text"), which teaches discipline. Most USACO contestants use Java through the Gold division.

### Step 1: Install JDK 21

```bash
brew install openjdk@21
```

Expected output (abbreviated):

```
==> Fetching openjdk@21
==> Installing openjdk@21
...
==> Summary
🍺  /opt/homebrew/Cellar/openjdk@21/21.x/: ... files, ...
```

### Step 2: Make Java Available System-Wide

```bash
sudo ln -sfn "$(brew --prefix openjdk@21)/libexec/openjdk.jdk" /Library/Java/JavaVirtualMachines/openjdk-21.jdk
```

You'll be asked for your password again.

Also add it to your shell PATH:

```bash
echo 'export PATH="$(brew --prefix openjdk@21)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Step 3: Verify

```bash
java --version
```

Expected output:

```
openjdk 21.0.5 2024-10-15
OpenJDK Runtime Environment Homebrew (build 21.0.5)
OpenJDK 64-Bit Server VM Homebrew (build 21.0.5, mixed mode, sharing)
```

Also check the compiler:

```bash
javac --version
```

Expected output:

```
javac 21.0.5
```

{% hint style="info" %}
**What's the difference between `java` and `javac`?** `javac` is the Java **compiler** -- it translates your code into something the computer can run. `java` is the **runtime** -- it actually runs the compiled code. You need both.
{% endhint %}

{% hint style="danger" %}
**If `java --version` says "No Java runtime present":** Make sure you ran the `sudo ln` command from Step 2. If it still doesn't work, close and reopen Terminal.
{% endhint %}

---

## 0.5 C++ Setup

C++ is the fastest of our three languages and the go-to choice for competitive programming at the highest levels. The good news: if you installed Xcode Command Line Tools (which happened automatically during the Homebrew install), you already have a C++ compiler.

### Verify Your C++ Compiler

```bash
g++ --version
```

Expected output:

```
Apple clang version 16.0.0 (clang-1600.0.26.6)
Target: arm64-apple-darwin24.2.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
```

{% hint style="info" %}
**Wait, it says "clang," not "g++"!** On macOS, the `g++` command is actually an alias for **Clang**, Apple's C++ compiler. Clang is excellent -- it's fast, produces great error messages, and supports all the C++ features you'll need. For competitive programming, it works just as well as the "real" GCC. You don't need to do anything differently.
{% endhint %}

If you see "command not found" instead:

```bash
xcode-select --install
```

A dialog box will appear. Click **Install**, wait for it to finish, then try `g++ --version` again.

### Clang vs. GCC -- What's the Difference?

You might see people online talking about GCC (the GNU Compiler Collection) vs. Clang. Here's what you need to know:

| | Clang (what you have) | GCC |
|---|---|---|
| **Speed** | Very fast compilation | Slightly faster executables sometimes |
| **Error messages** | Excellent, beginner-friendly | Decent but more cryptic |
| **macOS support** | Built-in, just works | Requires extra installation |
| **For this workbook** | Perfect | Not needed |

**Bottom line:** Clang is great. You don't need to install GCC.

---

## 0.6 Installing VS Code

VS Code (Visual Studio Code) is a free code editor made by Microsoft. It's lightweight, fast, and has excellent support for Python, Java, and C++. It's what most developers and many competitive programmers use.

### Step 1: Download and Install

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click the big blue **Download** button
3. Open the downloaded `.zip` file -- it will extract an app called **Visual Studio Code**
4. Drag **Visual Studio Code** into your **Applications** folder

### Step 2: Enable the `code` Command in Terminal

Open VS Code from your Applications folder, then:

1. Press **Cmd + Shift + P** to open the Command Palette
2. Type **shell command**
3. Click **Shell Command: Install 'code' command in PATH**

Now you can open any folder in VS Code from Terminal:

```bash
code .
```

The `.` means "the current folder." Try it -- VS Code should open with your current directory.

### Step 3: Install Extensions

Extensions add language support to VS Code. We need three. Run these commands in Terminal:

```bash
code --install-extension ms-python.python
```

```bash
code --install-extension vscjava.vscode-java-pack
```

```bash
code --install-extension ms-vscode.cpptools
```

Each one will output something like:

```
Installing extension 'ms-python.python'...
Extension 'ms-python.python' v2024.x.x was successfully installed.
```

{% hint style="info" %}
**What do these extensions do?**
- **Python** (`ms-python.python`) -- syntax highlighting, linting, debugging, and IntelliSense for Python
- **Java Extension Pack** (`vscjava.vscode-java-pack`) -- everything you need for Java development, bundled together
- **C/C++** (`ms-vscode.cpptools`) -- syntax highlighting, debugging, and IntelliSense for C and C++
{% endhint %}

{% hint style="warning" %}
**If `code` command is not found:** Make sure you did Step 2 (installing the shell command). If you did and it still doesn't work, close and reopen Terminal.
{% endhint %}

---

## 0.7 Hello World -- Three Languages

This is the moment of truth. We're going to create a simple "Hello, World!" program in Python, Java, and C++. This is a tradition in programming -- the very first program you write in any language just prints a greeting to the screen.

### Set Up Your Workspace

First, let's create a folder for this exercise:

```bash
mkdir -p ~/Projects/dsa-a2z-workspace/hello
cd ~/Projects/dsa-a2z-workspace/hello
```

Now open it in VS Code:

```bash
code .
```

### Write the Code

Create three files. You can do this in VS Code (File > New File) or from the Terminal.

{% tabs %}
{% tab title="Python" %}

Create a file called `hello.py`:

```bash
touch hello.py
```

Open it in VS Code and type this code:

```python
print("Hello, World!")
```

That's it. One line. Python keeps things simple.

**Run it:**

```bash
python3 hello.py
```

**Expected output:**

```
Hello, World!
```

{% endtab %}

{% tab title="Java" %}

Create a file called `Hello.java`:

```bash
touch Hello.java
```

Open it in VS Code and type this code:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Java requires more structure: a class, a `main` method, and `System.out.println` to print.

**Compile it first, then run it:**

```bash
javac Hello.java
java Hello
```

**Expected output:**

```
Hello, World!
```

{% hint style="info" %}
**Two steps?** Yes. `javac` compiles your `.java` file into a `.class` file (bytecode). `java` then runs that bytecode. You'll notice a new file called `Hello.class` appeared -- that's the compiled version.
{% endhint %}

{% endtab %}

{% tab title="C++" %}

Create a file called `hello.cpp`:

```bash
touch hello.cpp
```

Open it in VS Code and type this code:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

C++ uses `#include` to load the input/output library, and `std::cout` with the `<<` operator to print.

**Compile it first, then run it:**

```bash
g++ -std=c++17 -o hello hello.cpp
./hello
```

**Expected output:**

```
Hello, World!
```

{% hint style="info" %}
**What does `-std=c++17` mean?** It tells the compiler to use the C++17 standard, which is the version we'll use throughout this workbook. The `-o hello` part names the output file `hello` (without it, you'd get a file called `a.out`).
{% endhint %}

{% endtab %}
{% endtabs %}

### Language Spotlight: How Each Language Prints

Take a moment to compare how each language handles the simple task of printing text:

| | Python | Java | C++ |
|---|---|---|---|
| **Print command** | `print(...)` | `System.out.println(...)` | `std::cout << ... << std::endl` |
| **File name** | `hello.py` | `Hello.java` (must match class name!) | `hello.cpp` |
| **To run** | `python3 hello.py` | `javac Hello.java` then `java Hello` | `g++ -std=c++17 -o hello hello.cpp` then `./hello` |
| **Steps** | 1 (just run) | 2 (compile, then run) | 2 (compile, then run) |
| **Boilerplate** | None | Class + main method | `#include` + main function |

**Notice the pattern:** Python is the quickest to write and run. Java and C++ both need a compilation step, but they catch certain errors earlier (before the program runs) because of it. Each language has tradeoffs -- and that's exactly why we learn all three.

{% hint style="info" %}
**Congratulations!** You just wrote and ran programs in three different programming languages. That's a real accomplishment. Most people never learn even one.
{% endhint %}

---

## 0.8 Installing pytest

### What Are Tests?

Tests are small programs that check whether your code works correctly. Instead of running your code and manually looking at the output every time, you write tests that do the checking for you automatically.

Here's a simple analogy: imagine you're building a calculator. Instead of punching in `2 + 2` yourself every time you make a change, you write a test that says "when I give this function 2 and 2, the answer should be 4." Then you can run that test with one command whenever you want.

Throughout this workbook, every chapter has tests you can run to check your solutions. The Python testing tool we use is called **pytest**.

### Install pytest

```bash
pip install pytest
```

Expected output:

```
Collecting pytest
  Downloading pytest-8.x.x-py3-none-any.whl (xxx kB)
...
Successfully installed pytest-8.x.x ...
```

### Verify It Works

```bash
python3 -m pytest --version
```

Expected output:

```
pytest 8.x.x
```

{% hint style="warning" %}
**If `pip` is not found:** Try `pip3 install pytest` instead. If that doesn't work either, make sure your pyenv Python is active by running `python3 --version` first -- it should show 3.12.x.
{% endhint %}

### A Quick Test Drive

Let's see pytest in action. Create a tiny test file:

```bash
cd ~/Projects/dsa-a2z-workspace/hello
```

Create a file called `test_hello.py` with this content:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
```

Run the tests:

```bash
python3 -m pytest test_hello.py -v
```

Expected output:

```
========================= test session starts ==========================
collected 1 item

test_hello.py::test_add PASSED                                  [100%]

========================== 1 passed in 0.01s ===========================
```

That green **PASSED** is one of the most satisfying things in programming. You'll be seeing it a lot.

---

## 0.9 The One-Command Setup

Already overwhelmed by all those steps? Don't worry -- if you run into trouble or want to start fresh, there's a script that automates everything above.

From the root of the workbook repository, run:

```bash
bash scripts/setup_mac.sh
```

This single script will:

1. Check for (and install if needed) Xcode Command Line Tools
2. Install Homebrew
3. Install Python 3.12 via pyenv
4. Install Java (JDK 21)
5. Verify your C++ compiler
6. Install VS Code extensions
7. Install pytest
8. Run a verification check on everything

{% hint style="info" %}
**When should I use this script?** Use it if you want to skip the manual steps above, or if something went wrong and you want to make sure everything is installed correctly. The script is safe to run multiple times -- it skips anything that's already installed.
{% endhint %}

{% hint style="warning" %}
**You still need to install VS Code manually** by downloading it from [code.visualstudio.com](https://code.visualstudio.com/). The script can install the extensions, but it can't install VS Code itself.
{% endhint %}

---

## Checkpoint

Time to make sure everything is working. Run each of these commands and confirm you get the expected result:

| # | Check | Command | Expected |
|---|-------|---------|----------|
| 1 | Python | `python3 --version` | `Python 3.12.x` |
| 2 | Java runtime | `java --version` | `openjdk 21.x.x` |
| 3 | Java compiler | `javac --version` | `javac 21.x.x` |
| 4 | C++ compiler | `g++ --version` | `Apple clang version 16.x.x` (or similar) |
| 5 | pytest | `python3 -m pytest --version` | `pytest 8.x.x` |
| 6 | VS Code | `code --version` | A version number (e.g., `1.96.x`) |
| 7 | Homebrew | `brew --version` | `Homebrew 4.x.x` |

{% hint style="danger" %}
**Don't move on until all seven checks pass.** If any of them fail, scroll back to the relevant section in this chapter and re-do those steps. If you're still stuck, run `bash scripts/setup_mac.sh` and see if it catches the problem.
{% endhint %}

You can also run the setup script in verification-only mode to check everything at once:

```bash
bash scripts/setup_mac.sh
```

Look for the **Verification** section at the end -- every line should say `[PASS]`.

---

## What's Next

Your workshop is set up. Your tools are sharp. You've written code in three languages.

In **Chapter 1: The Coder's Toolkit -- Git & Problem Solving**, you'll learn Git, the tool that lets you save your progress like checkpoints in a video game. You'll never lose your work again, and you'll learn the workflow that every professional developer and competitive programmer uses.

You've already taken the hardest step: getting started. Everything from here builds on what you just did.

Let's keep going.
