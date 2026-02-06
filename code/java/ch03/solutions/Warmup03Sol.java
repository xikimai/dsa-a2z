package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 03: Largest of Three
 * =========================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Start by assuming 'a' is the largest. Then compare with b and c,
 * updating our answer if we find something bigger.
 * This "running max" pattern is fundamental — you'll use it everywhere.
 *
 * TIME COMPLEXITY:  O(1) — two comparisons
 * SPACE COMPLEXITY: O(1) — one extra variable
 */
public class Warmup03Sol {

    public static int solve(int a, int b, int c) {
        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;
        return max;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        System.out.println(solve(a, b, c));
        scanner.close();
    }
}
