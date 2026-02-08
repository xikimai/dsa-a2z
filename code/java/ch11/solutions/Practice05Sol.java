package ch11.solutions;

import java.util.*;

/**
 * Solution for Practice 5: Sort Characters by Frequency
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count frequencies, then sort characters by (-freq, char).
 *           Build the result string by repeating each char by its frequency.
 * TIME:  O(n + k log k) where k = number of distinct characters
 * SPACE: O(n)
 */
public class Practice05Sol {
    public static String solve(String s) {
        if (s.isEmpty()) return "";

        HashMap<Character, Integer> freq = new HashMap<>();
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        // Sort by frequency descending, then alphabetically ascending for ties
        List<Character> chars = new ArrayList<>(freq.keySet());
        chars.sort((a, b) -> {
            int cmp = Integer.compare(freq.get(b), freq.get(a)); // desc by freq
            if (cmp != 0) return cmp;
            return Character.compare(a, b); // asc by char
        });

        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            int count = freq.get(c);
            for (int i = 0; i < count; i++) {
                sb.append(c);
            }
        }

        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println(solve(s));
        sc.close();
    }
}
