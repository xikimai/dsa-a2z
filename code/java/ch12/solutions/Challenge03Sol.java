package ch12.solutions;

/**
 * Solution for Challenge 3: Minimum Bit Flips
 * TIME: O(k) where k = differing bits   SPACE: O(1)
 */
public class Challenge03Sol {
    public static int solve(int start, int goal) {
        int xor = start ^ goal;
        int count = 0;
        while (xor != 0) {
            xor &= (xor - 1);
            count++;
        }
        return count;
    }
}
