"""
Example 01: Binary Search on Answers Basics
=============================================
Chapter 16: Binary Search Beyond Arrays — Searching on Answers

This example demonstrates:
  - Part 1: BS on answers to find integer square root
  - Part 2: BS on answers for Koko's bananas (min eating speed)
  - Part 3: Comparing brute force O(max*n) vs BS O(n*log(max)) timing
"""

import math
import time


# ── Part 1: Integer Square Root via BS on Answers ──────────────────

def part1_square_root():
    """Find floor(sqrt(n)) using binary search on the answer space."""
    print("=" * 60)
    print("PART 1: BS on Answers — Integer Square Root")
    print("=" * 60)

    n = 49
    print(f"  Finding floor(sqrt({n}))\n")
    print(f"  Search space: [0, {n}]")

    lo, hi = 0, n
    step = 0
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2  # round up for "find maximum"
        step += 1
        sq = mid * mid
        print(f"  Step {step}: mid={mid}, mid*mid={sq}", end="")
        if sq <= n:
            print(f" <= {n}  -> lo = {mid}")
            lo = mid
        else:
            print(f" > {n}  -> hi = {mid - 1}")
            hi = mid - 1

    print(f"\n  Answer: floor(sqrt({n})) = {lo}")
    print(f"  Found in {step} steps (vs {n} brute-force checks)")


# ── Part 2: Koko's Bananas ─────────────────────────────────────────

def part2_koko():
    """Find minimum eating speed using binary search on answers."""
    print("\n" + "=" * 60)
    print("PART 2: BS on Answers — Koko Eating Bananas")
    print("=" * 60)

    piles = [3, 6, 7, 11]
    h = 8
    print(f"  Piles: {piles}")
    print(f"  Hours available: {h}")
    print(f"  Search space: [1, {max(piles)}]\n")

    def hours_needed(piles, k):
        return sum(math.ceil(p / k) for p in piles)

    lo, hi = 1, max(piles)
    step = 0
    while lo < hi:
        mid = lo + (hi - lo) // 2
        step += 1
        hrs = hours_needed(piles, mid)
        print(f"  Step {step}: speed={mid}, hours={hrs}", end="")
        if hrs <= h:
            print(f" <= {h}  -> hi = {mid}")
            hi = mid
        else:
            print(f" > {h}  -> lo = {mid + 1}")
            lo = mid + 1

    print(f"\n  Minimum eating speed: {lo}")
    print(f"  Verification: hours at speed {lo} = {hours_needed(piles, lo)}")


# ── Part 3: Timing Comparison ──────────────────────────────────────

def part3_timing():
    """Compare brute-force vs BS on answers for Koko's Bananas."""
    print("\n" + "=" * 60)
    print("PART 3: Performance — Brute Force vs BS on Answers")
    print("=" * 60)

    print(f"\n  {'Piles':>15}  {'H':>5}  {'Brute (ms)':>12}  {'BS (ms)':>10}  {'Speedup':>10}")
    print(f"  {'-'*15}  {'-'*5}  {'-'*12}  {'-'*10}  {'-'*10}")

    import random
    random.seed(42)

    for n_piles, max_val in [(10, 100), (100, 1000), (1000, 10000)]:
        piles = [random.randint(1, max_val) for _ in range(n_piles)]
        h = n_piles * 2  # generous time limit

        def hours_needed(piles, k):
            return sum(-(-p // k) for p in piles)

        # Brute force: try k=1, 2, 3, ...
        start = time.perf_counter()
        for k in range(1, max(piles) + 1):
            if hours_needed(piles, k) <= h:
                brute_ans = k
                break
        brute_time = (time.perf_counter() - start) * 1000

        # Binary search
        start = time.perf_counter()
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if hours_needed(piles, mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        bs_ans = lo
        bs_time = (time.perf_counter() - start) * 1000

        assert brute_ans == bs_ans, f"Mismatch: {brute_ans} vs {bs_ans}"

        speedup = brute_time / bs_time if bs_time > 0 else float("inf")
        piles_str = f"{n_piles}x[1..{max_val}]"
        print(f"  {piles_str:>15}  {h:>5}  {brute_time:>12.4f}  {bs_time:>10.4f}  {speedup:>9.1f}x")

    print("\n  Takeaway: BS on answers is O(n*log(max)) — dramatically faster!")


# ── Main ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_square_root()
    part2_koko()
    part3_timing()
