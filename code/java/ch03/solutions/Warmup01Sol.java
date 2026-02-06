package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 01: Even or Odd
 * ====================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use the modulo operator (%) to check if n is divisible by 2.
 * If n % 2 == 0, it's even; otherwise, it's odd.
 * Note: In Java, (-3) % 2 == -1 (not 1), but -1 != 0, so it still
 * correctly identifies odd numbers.
 *
 * TIME COMPLEXITY:  O(1) — one modulo operation
 * SPACE COMPLEXITY: O(1) — no extra space
 */
public class Warmup01Sol {

    public static String solve(int n) {
        return (n % 2 == 0) ? "Even" : "Odd";
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
