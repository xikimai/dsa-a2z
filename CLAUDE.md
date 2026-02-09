# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A trilingual (Python/Java/C++) DSA workbook for a teenager targeting USACO Platinum over 2-3 years. Published via **GitBook.com** (synced from this GitHub repo). Uses AOPS-style pedagogy: discovery-first, multiple solutions per problem, stories, Johari Windows, gotchas.

- **Audience**: 14-year-old with basic Python/Java experience, C++ is new
- **Curriculum source**: `striver-a2z.md` (Striver's A2Z DSA guide)
- **Master plan**: `.claude/plans/wobbly-greeting-hedgehog.md`

## Architecture

Two parallel trees in one repo:

1. **Book content** (`part-*/ch-*/README.md`) — GitBook renders these as the published website
2. **Runnable code** (`code/{python,java,cpp}/chXX/`) — student clones and runs locally with tests

GitBook uses `SUMMARY.md` for sidebar navigation and `.gitbook.yaml` for config.

## Directory Layout

```
part-{0..5}-*/ch-XX-*/README.md   # Chapter textbook content (GitBook)
part-{0..5}-*/ch-XX-*/johari.md   # Johari Window worksheet
code/python/chXX/{learn,practice,tests,solutions}/
code/java/chXX/{learn,practice,tests,solutions}/
code/cpp/chXX/{learn,practice,tests,solutions}/
scripts/                          # setup_mac.sh, run_tests.sh, etc.
templates/                        # Chapter scaffolding templates
appendices/                       # Contest strategy, cheatsheet, USACO guide
```

## Commands

```bash
# Run tests for a chapter
./scripts/run_tests.sh ch01 python
./scripts/run_tests.sh ch01 java
./scripts/run_tests.sh ch01 cpp
./scripts/run_tests.sh ch01 all

# Run Python tests directly
python -m pytest code/python/ch01/tests/ -v

# Compile and run C++
g++ -std=c++17 -o out code/cpp/ch01/practice/warmup_01_sum.cpp && ./out

# Scaffold a new chapter
./scripts/new_chapter.sh part-2-the-bronze-forge ch-07-number-wizardry "Number Wizardry"

# Check overall progress
./scripts/check_progress.sh
```

## Chapter Template Structure

Each chapter README.md follows this exact order:
1. Chapter Goals
2. Story (narrative hook)
3. Johari Window: Before (link to johari.md)
4. Discovery (problems before theory — AOPS style)
5. The Big Idea (formal explanation)
6. Multiple Solutions Showcase (same problem, 2-3 approaches, progressive improvement)
7. Language Spotlight (comparison table after each tabbed code block)
8. Gotchas (common mistakes)
9. Practice Problems (warmup/practice/challenge tiers)
10. Language Idioms
11. Johari Window: After
12. What's Next

## GitBook Formatting

Use these GitBook-specific constructs in chapter README.md files:

- **Language tabs**: Wrap code in `tabs/endtabs` blocks with `tab title="Python"/endtab` for each language
- **Hints**: Use `hint style="info|warning|danger"` / `endhint` blocks for callouts
- **Expandable**: `<details><summary>Click to reveal</summary>...</details>`

## Conventions

- **Problem skeleton files**: Include docstring with problem statement, examples, constraints, and a `pass` / empty body
- **Test files**: Always visible to student; use pytest (Python), assert-based (C++), JUnit (Java)
- **Solutions**: In `solutions/` dirs — these are reference implementations, not shown to student
- **Chapter numbering**: ch00-ch30, code dirs use `chXX` (no dash)
- **Tone**: Friendly mentor talking to a teenager, not a textbook. Conversational, encouraging.
- **USACO mapping**: Part 0-1 = Pre-Bronze, Part 2 = Bronze, Part 3 = Silver, Part 4 = Gold, Part 5 = Platinum
