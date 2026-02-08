package ch10.solutions;

import java.util.*;

/**
 * Solution for Warmup 04: Check Palindrome
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Compare first and last characters. If they match,
 *           recurse on the inner substring. Base case: length <= 1.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) — call stack depth
 */
public class Warmup04Sol {

    public static boolean solve(String s) {
        if (s.length() <= 1) return true;
        if (s.charAt(0) != s.charAt(s.length() - 1)) return false;
        return solve(s.substring(1, s.length() - 1));
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
