"""
Example 1: Recursion Basics — Visual Walkthrough
=================================================
Chapter 10: The Magic of Recursion

This example shows HOW recursion works step by step.
Run it and watch the calls unfold!
"""


# ── Part 1: Factorial Step-by-Step Trace ─────────────────────────────

def factorial_traced(n, depth=0):
    """Compute n! while printing each call and return with indentation."""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    if n == 0:
        print(f"{indent}factorial(0) returns 1  (base case)")
        return 1
    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returns {result}")
    return result


def part1_factorial_trace():
    """Show factorial recursion with call/return trace."""
    print("=" * 60)
    print("PART 1: Factorial — Step-by-Step Trace")
    print("=" * 60)
    print()
    print("  Computing factorial(5):")
    print()
    result = factorial_traced(5)
    print()
    print(f"  Final answer: 5! = {result}")
    print()
    print("  Notice how the calls go DOWN (deeper) before coming back UP.")
    print("  Each level waits for the one below to finish — that's recursion!")
    print()


# ── Part 2: Fibonacci Call Tree ──────────────────────────────────────

def fibonacci_counted(n, counter):
    """Compute fib(n) while counting total calls."""
    counter[0] += 1
    if n <= 1:
        return n
    return fibonacci_counted(n - 1, counter) + fibonacci_counted(n - 2, counter)


def part2_fibonacci_call_tree():
    """Show how Fibonacci makes redundant calls."""
    print("=" * 60)
    print("PART 2: Fibonacci — Redundant Calls Exposed")
    print("=" * 60)
    print()

    for n in range(2, 11):
        counter = [0]
        result = fibonacci_counted(n, counter)
        print(f"  fib({n:>2}) = {result:>4}   total calls: {counter[0]:>5}")

    print()
    print("  Look how fast the call count grows!")
    print("  fib(10) needs 177 calls, but only 11 unique values (fib(0)..fib(10)).")
    print("  All those extra calls are REDUNDANT. We'll fix this with memoization!")
    print()


# ── Part 3: Reverse String Recursion Trace ───────────────────────────

def reverse_traced(s, depth=0):
    """Reverse a string recursively with a trace."""
    indent = "  " * depth
    print(f"{indent}reverse(\"{s}\")")
    if len(s) <= 1:
        print(f"{indent}→ base case, return \"{s}\"")
        return s
    result = reverse_traced(s[1:], depth + 1) + s[0]
    print(f"{indent}→ reverse(\"{s[1:]}\") + \"{s[0]}\" = \"{result}\"")
    return result


def part3_reverse_string():
    """Trace how reversing a string works recursively."""
    print("=" * 60)
    print("PART 3: Reverse String — Recursion Trace")
    print("=" * 60)
    print()
    print("  Reversing \"hello\":")
    print()
    result = reverse_traced("hello")
    print()
    print(f"  Final answer: \"{result}\"")
    print()
    print("  Each call peels off the first character and appends it at the end.")
    print("  The string shrinks by 1 each time until we hit the base case.")
    print()


# ── Part 4: Recursion vs Iteration Comparison ───────────────────────

def factorial_recursive(n):
    """Factorial using recursion."""
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Factorial using a loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def part4_recursion_vs_iteration():
    """Compare recursive and iterative factorial."""
    print("=" * 60)
    print("PART 4: Recursion vs Iteration — Factorial Comparison")
    print("=" * 60)
    print()

    print("  Recursive code:")
    print("    def factorial(n):")
    print("        if n == 0: return 1")
    print("        return n * factorial(n - 1)")
    print()
    print("  Iterative code:")
    print("    def factorial(n):")
    print("        result = 1")
    print("        for i in range(2, n + 1):")
    print("            result *= i")
    print("        return result")
    print()

    print(f"  {'n':>4}  {'Recursive':>12}  {'Iterative':>12}  {'Match?':>8}")
    print(f"  {'─' * 4}  {'─' * 12}  {'─' * 12}  {'─' * 8}")

    for n in [0, 1, 5, 10, 15, 20]:
        r = factorial_recursive(n)
        i = factorial_iterative(n)
        match = "Yes" if r == i else "NO!"
        print(f"  {n:>4}  {r:>12}  {i:>12}  {match:>8}")

    print()
    print("  Both give the same answer! Recursion is elegant,")
    print("  but iteration can be faster (no function-call overhead).")
    print("  Choose what makes your code clearest.")
    print()


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_factorial_trace()
    part2_fibonacci_call_tree()
    part3_reverse_string()
    part4_recursion_vs_iteration()
