package ch02.solutions;

import java.util.Scanner;

/**
 * Solution for Challenge 01: Extract Digits
 * ============================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use integer division and modulo to peel off each digit:
 *   hundreds = n / 100        (e.g., 507 / 100 = 5)
 *   tens     = (n / 10) % 10  (e.g., 507 / 10 = 50, 50 % 10 = 0)
 *   ones     = n % 10         (e.g., 507 % 10 = 7)
 *
 * This is a fundamental pattern you'll use often: dividing strips the
 * rightmost digits, modulo keeps only the rightmost digit.
 *
 * TIME COMPLEXITY:  O(1) — just arithmetic
 * SPACE COMPLEXITY: O(1) — a three-element array
 */
public class Challenge01Sol {

    /**
     * Extract the hundreds, tens, and ones digits of a 3-digit number.
     *
     * @param n a 3-digit integer (100-999)
     * @return an int array {hundreds, tens, ones}
     */
    public static int[] solve(int n) {
        int hundreds = n / 100;
        int tens = (n / 10) % 10;
        int ones = n % 10;
        return new int[]{hundreds, tens, ones};
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] result = solve(n);
        System.out.println(result[0] + " " + result[1] + " " + result[2]);
        scanner.close();
    }
}
