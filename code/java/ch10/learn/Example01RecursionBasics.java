package ch10.learn;

/**
 * Example 01: Recursion Basics — See It in Action
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * This file demonstrates how recursion works with visual traces
 * so you can see the call stack building up and unwinding.
 *
 * Build and run:
 *   cd code/java
 *   javac ch10/learn/Example01RecursionBasics.java
 *   java ch10.learn.Example01RecursionBasics
 */
public class Example01RecursionBasics {

    // ── 1. Factorial with Indentation Trace ─────────────────────────

    static long factorialTrace(int n, int depth) {
        String indent = "  ".repeat(depth + 1);
        System.out.println(indent + "factorial(" + n + ") called");
        if (n == 0) {
            System.out.println(indent + "  base case! returning 1");
            return 1;
        }
        long result = n * factorialTrace(n - 1, depth + 1);
        System.out.println(indent + "  returning " + n + " * factorial(" + (n - 1) + ") = " + result);
        return result;
    }

    static void demoFactorial() {
        System.out.println("=== Part 1: Factorial with Call Trace ===");
        System.out.println("Formula: n! = n * (n-1) * ... * 1, with 0! = 1\n");

        long result = factorialTrace(5, 0);
        System.out.println("\n  Final answer: 5! = " + result);
        System.out.println("\n  Notice how the calls go DOWN (building the stack),");
        System.out.println("  then come back UP (unwinding with results).\n");
    }

    // ── 2. Fibonacci with Call Count ────────────────────────────────

    static int fibCallCount;

    static int fibNaive(int n) {
        fibCallCount++;
        if (n <= 1) return n;
        return fibNaive(n - 1) + fibNaive(n - 2);
    }

    static void demoFibonacci() {
        System.out.println("=== Part 2: Fibonacci Call Count ===");
        System.out.println("Formula: fib(n) = fib(n-1) + fib(n-2), fib(0)=0, fib(1)=1\n");

        int[] testValues = {5, 10, 15, 20, 25};
        System.out.printf("  %-6s  %-10s  %-12s%n", "n", "fib(n)", "# calls");
        System.out.println("  " + "-".repeat(32));

        for (int n : testValues) {
            fibCallCount = 0;
            int result = fibNaive(n);
            System.out.printf("  %-6d  %-10d  %-12d%n", n, result, fibCallCount);
        }

        System.out.println();
        System.out.println("  The call count EXPLODES! fib(25) needs over 240,000 calls.");
        System.out.println("  That's because the same sub-problems are solved over and over.");
        System.out.println("  We'll fix this with memoization in the Challenge problems.\n");
    }

    // ── 3. Reverse String Trace ─────────────────────────────────────

    static String reverseTrace(String s, int depth) {
        String indent = "  ".repeat(depth + 1);
        System.out.println(indent + "reverse(\"" + s + "\") called");
        if (s.length() <= 1) {
            System.out.println(indent + "  base case! returning \"" + s + "\"");
            return s;
        }
        String rest = reverseTrace(s.substring(1), depth + 1);
        String result = rest + s.charAt(0);
        System.out.println(indent + "  returning \"" + rest + "\" + '" + s.charAt(0) + "' = \"" + result + "\"");
        return result;
    }

    static void demoReverseString() {
        System.out.println("=== Part 3: Reverse String Trace ===");
        System.out.println("Idea: reverse(s) = reverse(s[1:]) + s[0]\n");

        String result = reverseTrace("cat", 0);
        System.out.println("\n  Final answer: reverse(\"cat\") = \"" + result + "\"");
        System.out.println("\n  Each call peels off the first character,");
        System.out.println("  then appends it to the END of the reversed rest.\n");
    }

    // ── 4. Iteration vs Recursion Comparison ────────────────────────

    static long factorialIter(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    static long factorialRecur(int n) {
        if (n == 0) return 1;
        return n * factorialRecur(n - 1);
    }

    static void demoComparison() {
        System.out.println("=== Part 4: Iteration vs Recursion ===\n");

        System.out.println("  Both compute the same result:");
        System.out.printf("  %-6s  %-14s  %-14s%n", "n", "Iterative", "Recursive");
        System.out.println("  " + "-".repeat(36));

        int[] testValues = {0, 1, 5, 10, 15, 20};
        for (int n : testValues) {
            System.out.printf("  %-6d  %-14d  %-14d%n", n, factorialIter(n), factorialRecur(n));
        }

        System.out.println();
        System.out.println("  When to use iteration:");
        System.out.println("    - Simple loops (factorial, sum, etc.)");
        System.out.println("    - Performance matters and recursion is deep");
        System.out.println();
        System.out.println("  When to use recursion:");
        System.out.println("    - Tree-like structures (subsets, permutations)");
        System.out.println("    - Divide-and-conquer (merge sort, binary search)");
        System.out.println("    - Backtracking (N-Queens, Sudoku)");
        System.out.println();
    }

    // ── Main ────────────────────────────────────────────────────────

    public static void main(String[] args) {
        System.out.println("Chapter 10: Recursion Basics");
        System.out.println("============================\n");

        demoFactorial();
        demoFibonacci();
        demoReverseString();
        demoComparison();

        System.out.println("KEY TAKEAWAYS:");
        System.out.println("  1. Every recursion needs a BASE CASE (when to stop)");
        System.out.println("  2. Each call must make progress TOWARD the base case");
        System.out.println("  3. The call stack builds up, then unwinds with results");
        System.out.println("  4. Naive recursion can be slow — memoization helps!");
    }
}
