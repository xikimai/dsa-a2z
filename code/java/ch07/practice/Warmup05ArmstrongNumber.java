package ch07.practice;

import java.util.*;

/**
 * Warmup 05: Armstrong Number
 * ==============================
 * Chapter 7: Number Wizardry
 *
 * PROBLEM: Given integer n, return true if it is an Armstrong number.
 *          A k-digit number is Armstrong if the sum of each digit raised
 *          to the power k equals the number itself.
 *          Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
 *          Negative numbers are NOT Armstrong numbers.
 *
 * EXAMPLES:
 *   solve(153)  = true   (1^3 + 5^3 + 3^3 = 153)
 *   solve(370)  = true   (3^3 + 7^3 + 0^3 = 370)
 *   solve(9474) = true   (9^4 + 4^4 + 7^4 + 4^4 = 9474)
 *   solve(100)  = false  (1^3 + 0^3 + 0^3 = 1 != 100)
 *   solve(1)    = true   (1^1 = 1)
 *   solve(0)    = true   (0^1 = 0)
 *
 * CONSTRAINTS:
 *   -10^18 <= n <= 10^18
 *
 * INSTRUCTIONS: Replace "return false;" in solve() with your solution.
 */
public class Warmup05ArmstrongNumber {
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
