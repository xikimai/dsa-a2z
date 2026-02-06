package ch05.solutions;

import java.util.*;

/**
 * Solution for Warmup 05: Character Frequency
 * =============================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Iterate through the string, using a HashMap to count each character's
 * occurrences with getOrDefault.
 *
 * TIME COMPLEXITY:  O(n) where n is the string length
 * SPACE COMPLEXITY: O(k) where k is the number of unique characters
 */
public class Warmup05Sol {

    public static Map<Character, Integer> solve(String s) {
        Map<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        return freq;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        Map<Character, Integer> freq = solve(line);
        TreeMap<Character, Integer> sorted = new TreeMap<>(freq);
        for (Map.Entry<Character, Integer> entry : sorted.entrySet()) {
            System.out.println(entry.getKey() + ":" + entry.getValue());
        }
        sc.close();
    }
}
