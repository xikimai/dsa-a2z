package ch11.solutions;

import java.util.*;

/**
 * Solution for Warmup 3: First Non-Repeating Character
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count frequencies with HashMap, then scan string left to right
 *           for the first character with count == 1.
 * TIME:  O(n)
 * SPACE: O(1) — at most 26 entries for lowercase letters
 */
public class Warmup03Sol {
    public static String solve(String s) {
        if (s.isEmpty()) return "_";

        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        for (char c : s.toCharArray()) {
            if (freq.get(c) == 1) {
                return String.valueOf(c);
            }
        }

        return "_";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
