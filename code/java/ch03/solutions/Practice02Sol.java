package ch03.solutions;

import java.util.Scanner;

/**
 * Solution for Practice 02: Digit Count
 * =======================================
 * Chapter 3: Decisions and Loops
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Handle n = 0 as a special case (1 digit). For other values,
 * take the absolute value and repeatedly divide by 10, counting
 * how many times until we reach 0.
 *
 * TIME COMPLEXITY:  O(d) — where d is the number of digits (at most 10 for int)
 * SPACE COMPLEXITY: O(1) — just a counter
 */
public class Practice02Sol {

    public static int solve(int n) {
        if (n == 0) return 1;
        int count = 0;
        // Handle negative by working with absolute value
        if (n < 0) n = -n;
        while (n > 0) {
            n /= 10;
            count++;
        }
        return count;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(solve(n));
        scanner.close();
    }
}
