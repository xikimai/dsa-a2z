package ch05.solutions;

import java.util.*;

/**
 * Solution for Warmup 06: Move Zeros
 * ====================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Write-pointer technique: maintain a write index that tracks where
 * the next non-zero should go. Scan through the array; when we find
 * a non-zero, write it at the write index and advance. After the scan,
 * fill the rest with zeros.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) — in-place
 */
public class Warmup06Sol {

    public static int[] solve(int[] nums) {
        int write = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[write] = nums[i];
                write++;
            }
        }
        while (write < nums.length) {
            nums[write] = 0;
            write++;
        }
        return nums;
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
