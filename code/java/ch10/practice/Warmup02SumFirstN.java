package ch10.practice;

import java.util.*;

/**
 * Warmup 02: Sum of First N Natural Numbers
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given a non-negative integer n, return the sum 1 + 2 + ... + n.
 *          When n == 0, the sum is 0.
 *
 * ALGORITHM: Use recursion with base case n == 0.
 *
 * EXAMPLES:
 *   solve(0)   = 0
 *   solve(1)   = 1
 *   solve(5)   = 15
 *   solve(100) = 5050
 *
 * CONSTRAINTS: 0 <= n <= 10^5
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02SumFirstN {
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
