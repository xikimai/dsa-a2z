package ch07.practice;

import java.util.*;

/**
 * Warmup 01: Count Digits
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given integer n, return number of digits. Use abs(n). 0 has 1 digit.
 * EXAMPLES: solve(12345)=5, solve(0)=1, solve(-42)=2
 * INSTRUCTIONS: Replace "return 0;" in solve() with your solution.
 * Do NOT convert to String!
 */
public class Warmup01CountDigits {
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
