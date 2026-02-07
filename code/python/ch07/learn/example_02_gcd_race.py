"""
Example 02: The GCD Race
==============================
Chapter 7: Number Wizardry — Math for Programmers

Run with:
    python code/python/ch07/learn/example_02_gcd_race.py

This demo compares GCD algorithms, shows the sieve of Eratosthenes,
and demonstrates modular exponentiation.
"""

import time

# ============================================================
# PART 1: GCD by Subtraction (slow!)
# ============================================================
print("=== PART 1: GCD by Subtraction ===")

def gcd_subtract(a, b):
    steps = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        steps += 1
    return a, steps

for a, b in [(48, 18), (100, 75), (1000000, 1)]:
    result, steps = gcd_subtract(a, b)
    print(f"  GCD({a}, {b}) = {result}  (took {steps:,} steps)")
print()

# ============================================================
# PART 2: GCD by Euclidean Algorithm (fast!)
# ============================================================
print("=== PART 2: GCD by Euclidean Algorithm ===")

def gcd_euclidean(a, b):
    steps = 0
    while b != 0:
        a, b = b, a % b
        steps += 1
    return a, steps

for a, b in [(48, 18), (100, 75), (1000000000, 1), (1000000000, 999999999)]:
    result, steps = gcd_euclidean(a, b)
    print(f"  GCD({a}, {b}) = {result}  (took {steps} steps!)")
print()

# ============================================================
# PART 3: Timing Comparison
# ============================================================
print("=== PART 3: Speed Comparison ===")
a, b = 100000, 3

start = time.perf_counter()
r1, _ = gcd_subtract(a, b)
t_sub = time.perf_counter() - start

start = time.perf_counter()
for _ in range(10000):
    r2, _ = gcd_euclidean(a, b)
t_euc = time.perf_counter() - start

print(f"  Subtraction:  GCD({a}, {b}) = {r1}  time = {t_sub:.6f}s (1 run)")
print(f"  Euclidean:    GCD({a}, {b}) = {r2}  time = {t_euc:.6f}s (10,000 runs!)")
print(f"  Euclidean is MUCH faster, especially when one number is small.")
print()

# ============================================================
# PART 4: Sieve of Eratosthenes — Visual Demo
# ============================================================
print("=== PART 4: Sieve of Eratosthenes (primes up to 50) ===")
limit = 50
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

print(f"  Start: all numbers 2..{limit} marked as potential primes")
for i in range(2, int(limit**0.5) + 1):
    if is_prime[i]:
        crossed = []
        for j in range(i * i, limit + 1, i):
            if is_prime[j]:
                crossed.append(j)
            is_prime[j] = False
        if crossed:
            print(f"  Sieving {i}: crossed out {crossed}")

primes = [i for i in range(2, limit + 1) if is_prime[i]]
print(f"  Primes up to {limit}: {primes}")
print(f"  Count: {len(primes)} primes")
print()

# ============================================================
# PART 5: Binary Exponentiation
# ============================================================
print("=== PART 5: Binary Exponentiation ===")

def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    steps = 0
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
        steps += 1
    return result, steps

MOD = 10**9 + 7
for base, exp in [(2, 10), (2, 100), (2, 1000000)]:
    result, steps = power_mod(base, exp, MOD)
    print(f"  {base}^{exp} mod {MOD} = {result}  (took {steps} steps)")
print()
print(f"  Even 2^1000000 only takes ~20 steps with binary exponentiation!")
print(f"  A naive loop would need 1,000,000 multiplications.")
