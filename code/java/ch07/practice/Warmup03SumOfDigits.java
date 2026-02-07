package ch07.practice;

import java.util.*;

/**
 * Warmup 03: Sum of Digits
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given integer n, return the sum of its digits. Use abs(n).
 *
 * EXAMPLES:
 *   solve(12345) = 15   (1+2+3+4+5)
 *   solve(0)     = 0
 *   solve(-456)  = 15   (4+5+6)
 *   solve(999)   = 27
 *
 * CONSTRAINTS:
 *   -10^18 <= n <= 10^18
 *
 * INSTRUCTIONS: Replace "return 0;" in solve() with your solution.
 * Do NOT convert to String!
 */
public class Warmup03SumOfDigits {
    public static int solve(long n) {
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
