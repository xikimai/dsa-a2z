package ch25.solutions;

import java.util.*;

public class Challenge04Sol {
    // Longest String Chain: sort by length, hash map DP
    public static int solve(String[] words) {
        Arrays.sort(words, (a, b) -> a.length() - b.length());
        Map<String, Integer> dp = new HashMap<>();
        int best = 1;
        for (String word : words) {
            dp.put(word, 1);
            for (int i = 0; i < word.length(); i++) {
                String pred = word.substring(0, i) + word.substring(i + 1);
                if (dp.containsKey(pred))
                    dp.put(word, Math.max(dp.get(word), dp.get(pred) + 1));
            }
            best = Math.max(best, dp.get(word));
        }
        return best;
    }
}
