package ch07.solutions;

import java.util.*;

/**
 * Solution for Warmup 02: Reverse Number
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Preserve the sign, take absolute value, then build the reversed number
 * digit by digit: reversed = reversed * 10 + lastDigit.
 *
 * TIME COMPLEXITY:  O(d) where d = number of digits
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup02Sol {

    public static long solve(long n) {
        long sign = n < 0 ? -1 : 1;
        n = Math.abs(n);
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return sign * reversed;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
