package ch07.solutions;

import java.util.*;

/**
 * Solution for Warmup 03: Sum of Digits
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Take absolute value, then extract and sum each digit using mod-10.
 *
 * TIME COMPLEXITY:  O(d) where d = number of digits
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup03Sol {

    public static int solve(long n) {
        n = Math.abs(n);
        int sum = 0;
        while (n > 0) {
            sum += (int)(n % 10);
            n /= 10;
        }
        return sum;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
