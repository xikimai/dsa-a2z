package ch10.solutions;

import java.util.*;

/**
 * Solution for Practice 01: Fibonacci Number
 * =========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Recursion with memoization using a HashMap.
 *           Stores already-computed values to avoid redundant work.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) — memo table + call stack
 */
public class Practice01Sol {

    public static int solve(int n) {
        return helper(n, new HashMap<>());
    }

    private static int helper(int n, HashMap<Integer, Integer> memo) {
        if (n <= 1) return n;
        if (memo.containsKey(n)) return memo.get(n);
        int result = helper(n - 1, memo) + helper(n - 2, memo);
        memo.put(n, result);
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(n));
        sc.close();
    }
}
