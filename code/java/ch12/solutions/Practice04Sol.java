package ch12.solutions;

import java.util.*;

/**
 * Solution for Practice 4: Power Set Using Bitmasks
 * TIME: O(n * 2^n)   SPACE: O(n * 2^n)
 */
public class Practice04Sol {
    public static List<List<Integer>> solve(int[] nums) {
        int n = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for (int mask = 0; mask < (1 << n); mask++) {
            List<Integer> subset = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    subset.add(nums[i]);
                }
            }
            result.add(subset);
        }
        return result;
    }
}
