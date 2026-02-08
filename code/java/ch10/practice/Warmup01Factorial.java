package ch10.practice;

import java.util.*;

/**
 * Warmup 01: Factorial
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given a non-negative integer n, return n! (n factorial).
 *          n! = n * (n-1) * ... * 1, with 0! = 1.
 *
 * ALGORITHM: Use recursion with base case n == 0.
 *
 * EXAMPLES:
 *   solve(0)  = 1
 *   solve(1)  = 1
 *   solve(5)  = 120
 *   solve(10) = 3628800
 *
 * CONSTRAINTS: 0 <= n <= 20 (result fits in long)
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01Factorial {
    public static long solve(int n) {
        // TODO: Replace this with your solution
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
