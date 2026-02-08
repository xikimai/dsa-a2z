package ch11.solutions;

import java.util.*;

/**
 * Solution for Practice 2: Missing Number
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Add all numbers to a HashSet, then check 0..n for the missing one.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Practice02Sol {
    public static int solve(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);

        for (int i = 0; i <= nums.length; i++) {
            if (!set.contains(i)) return i;
        }

        return -1; // unreachable
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
