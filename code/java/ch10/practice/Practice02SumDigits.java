package ch10.practice;

import java.util.*;

/**
 * Practice 02: Sum of Digits
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given an integer n, return the sum of its digits.
 *          Use the absolute value of n (handle negatives).
 *
 * ALGORITHM: sumDigits(n) = n%10 + sumDigits(n/10), base case: n < 10.
 *
 * EXAMPLES:
 *   solve(12345) = 15
 *   solve(0)     = 0
 *   solve(999)   = 27
 *   solve(-123)  = 6
 *
 * CONSTRAINTS: -10^9 <= n <= 10^9
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02SumDigits {
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
