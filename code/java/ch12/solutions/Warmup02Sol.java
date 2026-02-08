package ch12.solutions;

/**
 * Solution for Warmup 2: Count Set Bits (Brian Kernighan's)
 * TIME: O(k) where k = set bits   SPACE: O(1)
 */
public class Warmup02Sol {
    public static int solve(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
}
