package ch10.practice;

import java.util.*;

/**
 * Practice 01: Fibonacci Number
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given a non-negative integer n, return the nth Fibonacci number.
 *          fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).
 *
 * ALGORITHM: Use recursion (memoization recommended for larger n).
 *
 * EXAMPLES:
 *   solve(0)  = 0
 *   solve(1)  = 1
 *   solve(10) = 55
 *   solve(15) = 610
 *
 * CONSTRAINTS: 0 <= n <= 30
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01Fibonacci {
    public static int solve(int n) {
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
