package ch12.solutions;

/**
 * Solution for Warmup 1: Binary Representation
 * TIME: O(log n)   SPACE: O(log n)
 */
public class Warmup01Sol {
    public static String solve(int n) {
        if (n == 0) return "0";
        StringBuilder bits = new StringBuilder();
        while (n > 0) {
            bits.append(n % 2);
            n /= 2;
        }
        return bits.reverse().toString();
    }
}
