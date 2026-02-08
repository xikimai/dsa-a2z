package ch12.solutions;

/**
 * Solution for Practice 3: Set and Clear Bits
 * TIME: O(1)   SPACE: O(1)
 */
public class Practice03Sol {
    public static int solveSet(int n, int i) {
        return n | (1 << i);
    }

    public static int solveClear(int n, int i) {
        return n & ~(1 << i);
    }
}
