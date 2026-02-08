package ch15.solutions;

import java.util.*;

public class Challenge04Sol {
    public static int solve(int[] fruits) {
        Map<Integer, Integer> freq = new HashMap<>();
        int left = 0, best = 0;

        for (int right = 0; right < fruits.length; right++) {
            freq.put(fruits[right], freq.getOrDefault(fruits[right], 0) + 1);

            while (freq.size() > 2) {
                int leftFruit = fruits[left];
                freq.put(leftFruit, freq.get(leftFruit) - 1);
                if (freq.get(leftFruit) == 0) freq.remove(leftFruit);
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
