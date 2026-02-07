package ch07.solutions;

import java.util.*;

/**
 * Solution for Warmup 05: Armstrong Number
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Count the digits (k), then sum each digit raised to the power k.
 * Compare the sum with the original number.
 *
 * TIME COMPLEXITY:  O(d) where d = number of digits
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup05Sol {

    public static boolean solve(long n) {
        if (n < 0) return false;
        int numDigits = String.valueOf(n).length();
        long temp = n;
        long sum = 0;
        while (temp > 0) {
            long d = temp % 10;
            sum += (long) Math.pow(d, numDigits);
            temp /= 10;
        }
        return sum == n;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
