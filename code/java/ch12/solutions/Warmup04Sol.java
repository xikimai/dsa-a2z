package ch12.solutions;

/**
 * Solution for Warmup 4: Check if i-th Bit Is Set
 * TIME: O(1)   SPACE: O(1)
 */
public class Warmup04Sol {
    public static boolean solve(int n, int i) {
        return ((n >> i) & 1) == 1;
    }
}
