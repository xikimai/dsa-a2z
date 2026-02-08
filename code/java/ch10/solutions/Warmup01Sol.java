package ch10.solutions;

import java.util.*;

/**
 * Solution for Warmup 01: Factorial
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Simple recursion. Base case: 0! = 1.
 *           Recursive case: n! = n * (n-1)!
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) — call stack depth
 */
public class Warmup01Sol {

    public static long solve(int n) {
        if (n == 0) return 1;
        return (long) n * solve(n - 1);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
