package ch10.solutions;

import java.util.*;

/**
 * Solution for Warmup 02: Sum of First N Natural Numbers
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Simple recursion. Base case: sum(0) = 0.
 *           Recursive case: sum(n) = n + sum(n-1).
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) — call stack depth
 */
public class Warmup02Sol {

    public static int solve(int n) {
        if (n == 0) return 0;
        return n + solve(n - 1);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
