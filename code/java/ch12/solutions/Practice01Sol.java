package ch12.solutions;

/**
 * Solution for Practice 1: Single Number (XOR)
 * TIME: O(n)   SPACE: O(1)
 */
public class Practice01Sol {
    public static int solve(int[] nums) {
        int result = 0;
        for (int x : nums) result ^= x;
        return result;
    }
}
