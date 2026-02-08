package ch11.solutions;

import java.util.*;

/**
 * Solution for Challenge 3: Repeating and Missing Number
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Use a HashMap (or array) to count frequencies.
 *           The number with frequency 2 is repeating.
 *           The number with frequency 0 is missing.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Challenge03Sol {
    public static int[] solve(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        int repeating = 0, missing = 0;
        for (int i = 1; i <= n; i++) {
            int count = freq.getOrDefault(i, 0);
            if (count == 2) repeating = i;
            if (count == 0) missing = i;
        }

        return new int[]{repeating, missing};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        int[] result = solve(nums);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
