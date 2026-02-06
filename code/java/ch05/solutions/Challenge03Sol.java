package ch05.solutions;

import java.util.*;

/**
 * Solution for Challenge 03: Rotate Array
 * =========================================
 * Chapter 5: Collections
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Three-reverse trick:
 *   1. Normalize k = k % n (handle k > length).
 *   2. Reverse the entire array.
 *   3. Reverse the first k elements.
 *   4. Reverse the remaining n-k elements.
 *
 * Example: [1,2,3,4,5,6,7], k=3
 *   After full reverse:  [7,6,5,4,3,2,1]
 *   After reverse [0,3): [5,6,7,4,3,2,1]
 *   After reverse [3,7): [5,6,7,1,2,3,4]
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) — in-place
 */
public class Challenge03Sol {

    private static void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }

    public static int[] solve(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) return nums;

        k = k % n;
        if (k == 0) return nums;

        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
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
        int k = Integer.parseInt(sc.nextLine().trim());
        int[] result = solve(nums, k);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(result[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
