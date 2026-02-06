package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 04: Right-Aligned Triangle
 * ==================================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * For each row i (1-indexed from 1 to n):
 *   - Print (n - i) spaces
 *   - Print i stars
 *   - Add a newline (except after the last row)
 *
 * Example for n=3:
 *   Row 1: 2 spaces + 1 star  -> "  *"
 *   Row 2: 1 space  + 2 stars -> " **"
 *   Row 3: 0 spaces + 3 stars -> "***"
 *
 * TIME COMPLEXITY:  O(n^2) — nested loops for spaces and stars
 * SPACE COMPLEXITY: O(n^2) — the output string
 */
public class Practice04Sol {

    public static String solve(int n) {
        StringBuilder sb = new StringBuilder();
        for (int row = 1; row <= n; row++) {
            // Leading spaces
            for (int s = 0; s < n - row; s++) {
                sb.append(' ');
            }
            // Stars
            for (int s = 0; s < row; s++) {
                sb.append('*');
            }
            // Newline between rows (not after last row)
            if (row < n) {
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
