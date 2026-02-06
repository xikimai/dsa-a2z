package ch05.practice;

import java.util.*;

/**
 * Warmup 05: Character Frequency
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given a string, return a map of each character to its frequency.
 *
 * INPUT FORMAT
 * ------------
 * A single line of text.
 *
 * OUTPUT FORMAT
 * -------------
 * Print sorted key:count pairs, one per line (sorted by character).
 *
 * CONSTRAINTS
 * -----------
 * 0 <= s.length() <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:  aab
 * Output:
 * a:2
 * b:1
 *
 * Input:  (empty)
 * Output: (nothing)
 *
 * Input:  aaa
 * Output:
 * a:3
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return new HashMap<>();" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup05CharFrequency {

    /**
     * Return a frequency map of characters in the string.
     *
     * @param s the input string
     * @return map from character to count
     */
    public static Map<Character, Integer> solve(String s) {
        // TODO: Replace this with your solution
        return new HashMap<>();
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
