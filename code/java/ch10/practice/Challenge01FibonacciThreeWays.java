package ch10.practice;

import java.util.*;

/**
 * Challenge 01: Fibonacci — Three Ways
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Implement Fibonacci three ways to compare approaches:
 *   1. solveNaive(n)  — pure recursion (exponential time)
 *   2. solveMemo(n)   — recursion with memoization (linear time)
 *   3. solveIter(n)   — iterative with two variables (linear time, O(1) space)
 *   4. solve(n)       — calls solveIter (the best approach)
 *
 * EXAMPLES:
 *   solveNaive(10) = 55
 *   solveMemo(30)  = 832040
 *   solveIter(30)  = 832040
 *
 * CONSTRAINTS: 0 <= n <= 45 for memo/iter, 0 <= n <= 30 for naive
 *
 * INSTRUCTIONS: Replace the bodies of all four methods with your solutions.
 */
public class Challenge01FibonacciThreeWays {
    public static long solveNaive(int n) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static long solveMemo(int n) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static long solveIter(int n) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static long solve(int n) {
        // TODO: Replace this with your solution (use solveIter)
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
