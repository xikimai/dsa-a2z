package ch10.solutions;

import java.util.*;

/**
 * Solution for Warmup 03: Reverse String
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Peel off the first character and append it to the end
 *           of the reversed rest. Base case: length <= 1.
 *
 * TIME COMPLEXITY:  O(n^2) — substring creates new strings
 * SPACE COMPLEXITY: O(n) — call stack depth
 */
public class Warmup03Sol {

    public static String solve(String s) {
        if (s.length() <= 1) return s;
        return solve(s.substring(1)) + s.charAt(0);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
