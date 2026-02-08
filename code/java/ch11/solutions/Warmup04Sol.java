package ch11.solutions;

import java.util.*;

/**
 * Solution for Warmup 4: Valid Anagram
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count character frequencies for both strings using a HashMap.
 *           If all counts match, they are anagrams.
 * TIME:  O(n) where n = max(s1.length, s2.length)
 * SPACE: O(1) — at most 26 entries for lowercase letters
 */
public class Warmup04Sol {
    public static boolean solve(String s1, String s2) {
        if (s1.length() != s2.length()) return false;

        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s1.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for (char c : s2.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) - 1);
        }

        for (int v : freq.values()) {
            if (v != 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        System.out.println(solve(s1, s2));
        sc.close();
    }
}
