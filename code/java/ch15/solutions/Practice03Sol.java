package ch15.solutions;

import java.util.*;

public class Practice03Sol {
    public static String solve(String s, String t) {
        if (s.isEmpty() || t.isEmpty()) return "";

        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray())
            need.put(c, need.getOrDefault(c, 0) + 1);

        int required = need.size();
        int formed = 0;
        Map<Character, Integer> window = new HashMap<>();
        int left = 0, bestLen = Integer.MAX_VALUE, bestStart = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            window.put(ch, window.getOrDefault(ch, 0) + 1);

            if (need.containsKey(ch) && window.get(ch).intValue() == need.get(ch).intValue())
                formed++;

            while (formed == required) {
                if (right - left + 1 < bestLen) {
                    bestLen = right - left + 1;
                    bestStart = left;
                }
                char out = s.charAt(left);
                window.put(out, window.get(out) - 1);
                if (need.containsKey(out) && window.get(out) < need.get(out))
                    formed--;
                left++;
            }
        }
        return bestLen == Integer.MAX_VALUE ? "" : s.substring(bestStart, bestStart + bestLen);
    }
}
