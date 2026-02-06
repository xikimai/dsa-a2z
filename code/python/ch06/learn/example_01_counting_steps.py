"""
Example 01: Counting Steps
==============================
Chapter 6: How Fast Is Your Code?

Run with:
    python code/python/ch06/learn/example_01_counting_steps.py

This demo shows how different algorithms take wildly different amounts
of time — even when they compute the same thing.  We'll time four
approaches to see the difference between O(1), O(n), O(n^2), and O(log n).
"""

import time

# ============================================================
# PART 1: O(1) — Constant time (formula)
# ============================================================
# The sum 1 + 2 + ... + n can be computed instantly with a formula.
# No matter how large n is, it takes the same amount of work.

print("=== PART 1: O(1) — Formula ===")
for n in [1_000, 1_000_000, 1_000_000_000]:
    start = time.perf_counter()
    result = n * (n + 1) // 2
    elapsed = time.perf_counter() - start
    print(f"  n = {n:>13,}  |  sum = {result:>20,}  |  time = {elapsed:.6f}s")
print()

# ============================================================
# PART 2: O(n) — Linear time (loop)
# ============================================================
# Adding numbers one by one takes time proportional to n.
# Double n, and the time roughly doubles.

print("=== PART 2: O(n) — Loop ===")
for n in [10_000, 100_000, 1_000_000]:
    start = time.perf_counter()
    total = 0
    for i in range(1, n + 1):
        total += i
    elapsed = time.perf_counter() - start
    print(f"  n = {n:>10,}  |  sum = {total:>15,}  |  time = {elapsed:.6f}s")
print()

# ============================================================
# PART 3: O(n^2) — Quadratic time (nested loops)
# ============================================================
# For each number i from 1 to n, we add 1 exactly i times using
# an inner loop.  This is intentionally slow to show the effect.
# Double n, and the time roughly quadruples.

print("=== PART 3: O(n^2) — Nested Loops ===")
for n in [1_000, 5_000, 10_000]:
    start = time.perf_counter()
    total = 0
    for i in range(1, n + 1):
        for _ in range(i):
            total += 1
    elapsed = time.perf_counter() - start
    print(f"  n = {n:>6,}  |  sum = {total:>12,}  |  time = {elapsed:.6f}s")
print()

# ============================================================
# PART 4: O(log n) — Logarithmic time (halving)
# ============================================================
# Repeatedly halving a number reaches 0 in about log2(n) steps.
# Even for n = 1 billion, that's only about 30 steps!

print("=== PART 4: O(log n) — Halving ===")
for n in [1_000, 1_000_000, 1_000_000_000]:
    start = time.perf_counter()
    steps = 0
    val = n
    while val > 0:
        val //= 2
        steps += 1
    elapsed = time.perf_counter() - start
    print(f"  n = {n:>13,}  |  steps = {steps:>3}  |  time = {elapsed:.6f}s")
print()

print("Notice how O(1) and O(log n) are nearly instant for ANY n,")
print("while O(n^2) gets painful fast.  That's why complexity matters!")
