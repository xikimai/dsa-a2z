package ch07.practice;

import java.util.*;

/**
 * Warmup 02: Reverse Number
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given integer n, return its digits reversed. Preserve the sign.
 *          Trailing zeros become leading zeros and disappear.
 *
 * EXAMPLES:
 *   solve(12345) = 54321
 *   solve(-123)  = -321
 *   solve(1200)  = 21
 *   solve(0)     = 0
 *
 * CONSTRAINTS:
 *   -10^18 <= n <= 10^18
 *
 * INSTRUCTIONS: Replace "return 0;" in solve() with your solution.
 * Do NOT convert to String!
 */
public class Warmup02ReverseNumber {
    public static long solve(long n) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
