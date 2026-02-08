package ch15.learn;

import java.util.*;

/**
 * Example 02: Sliding Window Patterns
 * =====================================
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * Demonstrates fixed-size and variable-size sliding windows.
 */
public class Example02SlidingWindowPatterns {

    public static void main(String[] args) {
        // Part 1: Fixed-size window — max sum of k elements
        System.out.println("=== Part 1: Fixed-Size Window ===");
        int[] arr = {2, 1, 5, 1, 3, 2, 8, 1};
        int k = 3;
        System.out.println("Array: [2,1,5,1,3,2,8,1], k=" + k);

        int windowSum = 0;
        for (int i = 0; i < k; i++) windowSum += arr[i];
        int best = windowSum;

        for (int i = k; i < arr.length; i++) {
            windowSum += arr[i] - arr[i - k];
            best = Math.max(best, windowSum);
            System.out.printf("  Window [%d..%d] sum=%d%s%n",
                i - k + 1, i, windowSum, windowSum == best ? " <- best" : "");
        }
        System.out.println("Best sum: " + best);

        // Part 2: Variable-size window — longest substring without repeats
        System.out.println("\n=== Part 2: Variable Window + HashMap ===");
        String s = "abcabcbb";
        System.out.println("String: \"" + s + "\"");

        Map<Character, Integer> charIndex = new HashMap<>();
        int left = 0, bestLen = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (charIndex.containsKey(ch) && charIndex.get(ch) >= left) {
                left = charIndex.get(ch) + 1;
            }
            charIndex.put(ch, right);
            bestLen = Math.max(bestLen, right - left + 1);
            System.out.printf("  right=%d '%c' window=\"%s\" len=%d%n",
                right, ch, s.substring(left, right + 1), right - left + 1);
        }
        System.out.println("Longest substring without repeating: " + bestLen);
    }
}
