package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Challenge 01: Diamond Pattern
 * ============================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * A diamond with parameter n has (2*n - 1) rows total.
 * Think of it as two halves:
 *
 * Top half (rows 1..n): row i has (n-i) leading spaces and (2*i-1) stars.
 * Bottom half (rows n+1..2n-1): mirror of the top half.
 *
 * We can unify both halves by computing a "distance from center":
 *   - For absolute row number r (1-indexed), the distance from the
 *     middle row is |r - n|. Call it d.
 *   - Leading spaces = d
 *   - Stars = (2*(n - d) - 1)
 *
 * No trailing spaces per line.
 *
 * TIME COMPLEXITY:  O(n^2) — total characters in the diamond
 * SPACE COMPLEXITY: O(n^2) — the output string
 */
public class Challenge01Sol {

    public static String solve(int n) {
        int totalRows = 2 * n - 1;
        StringBuilder sb = new StringBuilder();
        for (int r = 1; r <= totalRows; r++) {
            int dist = Math.abs(r - n);
            int spaces = dist;
            int stars = 2 * (n - dist) - 1;

            for (int s = 0; s < spaces; s++) {
                sb.append(' ');
            }
            for (int s = 0; s < stars; s++) {
                sb.append('*');
            }
            if (r < totalRows) {
                sb.append('\n');
            }
        }
        return sb.toString();
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
