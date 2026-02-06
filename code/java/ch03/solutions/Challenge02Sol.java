package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Challenge 02: Prime Check
 * ========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * A prime number is an integer greater than 1 whose only divisors are
 * 1 and itself.
 *
 * Optimization: Only check divisors from 2 to sqrt(n). If n has a
 * factor larger than sqrt(n), then the matching factor on the other
 * side must be smaller than sqrt(n), so we'd already have found it.
 *
 * Edge cases: n <= 1 is not prime. n == 2 is the smallest prime.
 *
 * TIME COMPLEXITY:  O(sqrt(n)) — we check at most sqrt(n) divisors
 * SPACE COMPLEXITY: O(1) — no extra space
 */
public class Challenge02Sol {

    public static boolean solve(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
