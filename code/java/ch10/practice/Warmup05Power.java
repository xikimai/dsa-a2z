package ch10.practice;

import java.util.*;

/**
 * Warmup 05: Power (Exponentiation)
 * ==============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM: Given non-negative integers base and exp, return base^exp.
 *          Use simple recursion (not fast exponentiation).
 *
 * ALGORITHM: base^exp = base * base^(exp-1), base case: exp == 0 -> 1.
 *
 * EXAMPLES:
 *   solve(2, 0)  = 1
 *   solve(2, 10) = 1024
 *   solve(3, 4)  = 81
 *
 * CONSTRAINTS: 0 <= base, exp <= 30 (result fits in long)
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup05Power {
    public static long solve(int base, int exp) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int base = Integer.parseInt(sc.nextLine().trim());
        int exp = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(base, exp));
        sc.close();
    }
}
