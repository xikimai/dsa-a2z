package ch10.solutions;

import java.util.*;

/**
 * Solution for Challenge 01: Fibonacci — Three Ways
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * Three approaches compared:
 *   1. Naive recursion:  O(2^n) time, O(n) space
 *   2. Memoized:         O(n) time, O(n) space
 *   3. Iterative:        O(n) time, O(1) space
 */
public class Challenge01Sol {

    // Approach 1: Naive recursion — exponential time
    public static long solveNaive(int n) {
        if (n <= 1) return n;
        return solveNaive(n - 1) + solveNaive(n - 2);
    }

    // Approach 2: Memoized recursion — linear time
    public static long solveMemo(int n) {
        return memoHelper(n, new HashMap<>());
    }

    private static long memoHelper(int n, HashMap<Integer, Long> memo) {
        if (n <= 1) return n;
        if (memo.containsKey(n)) return memo.get(n);
        long result = memoHelper(n - 1, memo) + memoHelper(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    // Approach 3: Iterative — linear time, constant space
    public static long solveIter(int n) {
        if (n <= 1) return n;
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    // Default: use the best approach
    public static long solve(int n) {
        return solveIter(n);
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
