package ch12.solutions;

/**
 * Solution for Warmup 3: Check Power of Two
 * TIME: O(1)   SPACE: O(1)
 */
public class Warmup03Sol {
    public static boolean solve(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
