package ch07.solutions;

import java.util.*;

/**
 * Solution for Warmup 04: Palindrome Number
 * =========================================
 * Chapter 7: Number Wizardry
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Negative numbers are not palindromes. For non-negatives, reverse the
 * number and compare with the original.
 *
 * TIME COMPLEXITY:  O(d) where d = number of digits
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup04Sol {

    public static boolean solve(long n) {
        if (n < 0) return false;
        long original = n;
        long reversed = 0;
        while (n > 0) {
            reversed = reversed * 10 + n % 10;
            n /= 10;
        }
        return original == reversed;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = Long.parseLong(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
