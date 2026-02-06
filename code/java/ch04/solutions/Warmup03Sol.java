package ch04.solutions;

import java.util.Scanner;

/**
 * Solution for Warmup 03: Min of Three (using Min of Two)
 * ========================================================
 * Chapter 4: Functions
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Write a minOfTwo helper, then call it twice:
 *   minOfTwo(a, minOfTwo(b, c))
 * This demonstrates function composition — building complex logic from
 * simple building blocks.
 *
 * TIME COMPLEXITY:  O(1) — two comparisons
 * SPACE COMPLEXITY: O(1)
 */
public class Warmup03Sol {

    public static int minOfTwo(int a, int b) {
        if (a <= b) return a;
        return b;
    }

    public static int solve(int a, int b, int c) {
        return minOfTwo(a, minOfTwo(b, c));
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.println(solve(a, b, c));
        sc.close();
    }
}
