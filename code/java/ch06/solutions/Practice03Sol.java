package ch06.solutions;

import java.util.*;

/**
 * Solution for Practice 03: Squares of a Sorted Array
 * =====================================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Two pointers from both ends. The largest square must come from either
 * the leftmost (most negative) or rightmost (most positive) element.
 * Compare absolute values and fill result from right to left.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(n) for the result array
 */
public class Practice03Sol {

    public static int[] solve(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int left = 0, right = n - 1;
        int pos = n - 1;

        while (left <= right) {
            int leftSq = nums[left] * nums[left];
            int rightSq = nums[right] * nums[right];
            if (leftSq > rightSq) {
                result[pos] = leftSq;
                left++;
            } else {
                result[pos] = rightSq;
                right--;
            }
            pos--;
        }
        return result;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println();
        } else {
            int[] nums = Arrays.stream(line.split("\\s+"))
                               .mapToInt(Integer::parseInt).toArray();
            int[] result = solve(nums);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb);
        }
        sc.close();
    }
}
