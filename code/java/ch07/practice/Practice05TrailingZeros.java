package ch07.practice;

import java.util.*;

/**
 * Practice 05: Trailing Zeros in n!
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given a non-negative integer n, return the number of
 *          trailing zeros in n! (n factorial).
 *
 * EXAMPLES:
 *   solve(5)   = 1    (5! = 120)
 *   solve(10)  = 2    (10! = 3628800)
 *   solve(25)  = 6    (25! has 6 trailing zeros)
 *   solve(100) = 24
 *   solve(0)   = 0
 *
 * CONSTRAINTS:
 *   0 <= n <= 10^9
 *
 * HINT: Trailing zeros come from factors of 10 = 2 * 5.
 *       There are always more 2s than 5s, so count factors of 5.
 *       Don't forget 25 contributes two 5s, 125 contributes three, etc.
 *       Formula: n/5 + n/25 + n/125 + ...
 *
 * INSTRUCTIONS: Replace "return 0;" in solve() with your solution.
 */
public class Practice05TrailingZeros {
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
