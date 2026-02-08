package ch15.solutions;

import java.util.*;

public class Practice02Sol {
    public static int solve(String s) {
        Map<Character, Integer> charIndex = new HashMap<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            if (charIndex.containsKey(ch) && charIndex.get(ch) >= left) {
                left = charIndex.get(ch) + 1;
            }
            charIndex.put(ch, right);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
