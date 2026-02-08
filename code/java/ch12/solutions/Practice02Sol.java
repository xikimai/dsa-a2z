package ch12.solutions;

/**
 * Solution for Practice 2: Toggle i-th Bit
 * TIME: O(1)   SPACE: O(1)
 */
public class Practice02Sol {
    public static int solve(int n, int i) {
        return n ^ (1 << i);
    }
}
