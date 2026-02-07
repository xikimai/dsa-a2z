package ch07.solutions;

import java.util.*;

/**
 * Solution for Warmup 01: Count Digits
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Take absolute value, then repeatedly divide by 10, counting iterations.
 * Special case: 0 has 1 digit.
 *
 * TIME COMPLEXITY:  O(d) where d = number of digits
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup01Sol {

    public static int solve(long n) {
        n = Math.abs(n);
        if (n == 0) return 1;
        int count = 0;
        while (n > 0) {
            count++;
            n /= 10;
        }
        return count;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
