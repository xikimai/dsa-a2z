package ch07.practice;

import java.util.*;

/**
 * Warmup 04: Palindrome Number
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given integer n, return true if it is a palindrome (reads
 *          the same forwards and backwards). Negative numbers are NOT
 *          palindromes.
 *
 * EXAMPLES:
 *   solve(121)  = true
 *   solve(-121) = false
 *   solve(10)   = false
 *   solve(0)    = true
 *   solve(1001) = true
 *
 * CONSTRAINTS:
 *   -10^18 <= n <= 10^18
 *
 * INSTRUCTIONS: Replace "return false;" in solve() with your solution.
 * Do NOT convert to String!
 */
public class Warmup04PalindromeNumber {
    public static boolean solve(long n) {
        // TODO: Replace this with your solution
        return false;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
