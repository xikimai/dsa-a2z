package ch05.solutions;

import java.util.*;

/**
 * Solution for Warmup 04: Remove Duplicates
 * ==========================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Two-pointer technique on a sorted array: a write pointer and a read pointer.
 * Since the array is sorted, duplicates are adjacent. Only write when we
 * see a new value different from the previous.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) for the result array (O(1) if counting only)
 */
public class Warmup04Sol {

    public static int[] solve(int[] nums) {
        if (nums.length == 0) return nums;

        // Count unique elements first
        int unique = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                unique++;
            }
        }

        // Build result
        int[] result = new int[unique];
        result[0] = nums[0];
        int write = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                result[write] = nums[i];
                write++;
            }
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] nums;
        if (line.isEmpty()) {
            nums = new int[0];
        } else {
            nums = Arrays.stream(line.split("\\s+"))
                         .mapToInt(Integer::parseInt).toArray();
        }
        int[] result = solve(nums);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
