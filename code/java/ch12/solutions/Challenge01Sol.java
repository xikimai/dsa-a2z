package ch12.solutions;

import java.util.*;

/**
 * Solution for Challenge 1: Single Number — Three Ways
 */
public class Challenge01Sol {
    public static int solveSort(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        for (int i = 0; i < sorted.length - 1; i += 2) {
            if (sorted[i] != sorted[i + 1]) return sorted[i];
        }
        return sorted[sorted.length - 1];
    }

    public static int solveHash(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.put(x, freq.getOrDefault(x, 0) + 1);
        for (var entry : freq.entrySet()) {
            if (entry.getValue() == 1) return entry.getKey();
        }
        return -1;
    }

    public static int solveXor(int[] nums) {
        int result = 0;
        for (int x : nums) result ^= x;
        return result;
    }
}
