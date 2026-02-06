package ch05.solutions;

import java.util.*;

/**
 * Solution for Practice 02: Anagram Check
 * =========================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Convert both strings to lowercase, then build a frequency map for each.
 * If the maps are equal, the strings are anagrams.
 * (Alternative: sort both and compare. This approach avoids sorting.)
 *
 * TIME COMPLEXITY:  O(n + m) where n and m are the string lengths
 * SPACE COMPLEXITY: O(k) where k is the number of unique characters
 */
public class Practice02Sol {

    public static boolean solve(String s1, String s2) {
        String a = s1.toLowerCase();
        String b = s2.toLowerCase();
        if (a.length() != b.length()) return false;

        Map<Character, Integer> freq = new HashMap<>();
        for (char c : a.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for (char c : b.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) - 1);
        }
        for (int count : freq.values()) {
            if (count != 0) return false;
        }
        return true;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        System.out.println(solve(s1, s2));
        sc.close();
    }
}
