package ch11.solutions;

import java.util.*;

/**
 * Solution for Challenge 2: Longest Consecutive Sequence
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Put all numbers in a HashSet. For each number, only start counting
 *           a sequence if (num - 1) is NOT in the set (sequence start).
 *           Then count consecutive elements forward.
 * TIME:  O(n) — each element visited at most twice
 * SPACE: O(n)
 */
public class Challenge02Sol {
    public static int solve(int[] nums) {
        if (nums.length == 0) return 0;

        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);

        int longest = 0;

        for (int num : set) {
            // Only start from the beginning of a sequence
            if (!set.contains(num - 1)) {
                int current = num;
                int length = 1;

                while (set.contains(current + 1)) {
                    current++;
                    length++;
                }

                longest = Math.max(longest, length);
            }
        }

        return longest;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        System.out.println(solve(nums));
        sc.close();
    }
}
