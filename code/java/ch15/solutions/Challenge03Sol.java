package ch15.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(String s, int k) {
        Map<Character, Integer> freq = new HashMap<>();
        int left = 0, maxFreq = 0, best = 0;

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);
            freq.put(ch, freq.getOrDefault(ch, 0) + 1);
            maxFreq = Math.max(maxFreq, freq.get(ch));

            while ((right - left + 1) - maxFreq > k) {
                char out = s.charAt(left);
                freq.put(out, freq.get(out) - 1);
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
