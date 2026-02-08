package ch10.solutions;

import java.util.*;

/**
 * Solution for Practice 02: Sum of Digits
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Take absolute value first, then recurse:
 *           sumDigits(n) = n%10 + sumDigits(n/10).
 *           Base case: single digit (n < 10).
 *
 * TIME COMPLEXITY:  O(d) where d = number of digits
 * SPACE COMPLEXITY: O(d) — call stack depth
 */
public class Practice02Sol {

    public static int solve(int n) {
        n = Math.abs(n);
        if (n < 10) return n;
        return n % 10 + solve(n / 10);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
