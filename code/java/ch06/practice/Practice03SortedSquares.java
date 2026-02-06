package ch06.practice;

import java.util.*;

/**
 * Practice 03: Squares of a Sorted Array
 * ========================================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given an integer array nums sorted in non-decreasing order, return
 * an array of the squares of each number sorted in non-decreasing order.
 *
 * Can you do it in O(n) time using a two-pointer technique?
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated sorted integers (may be empty).
 *
 * OUTPUT FORMAT
 * -------------
 * Print the sorted squares, space-separated.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^4
 * -10^4 <= nums[i] <= 10^4
 * nums is sorted in non-decreasing order.
 *
 * EXAMPLES
 * --------
 * Input:  -4 -1 0 3 10     Output: 0 1 9 16 100
 * Input:  -3 -2 -1         Output: 1 4 9
 * Input:  0 1 2 3           Output: 0 1 4 9
 *
 * HINT
 * ----
 * The largest square must come from either the leftmost (most negative)
 * or rightmost (most positive) element. Use two pointers starting from
 * both ends and fill the result array from right to left.
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return new int[0];" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice03SortedSquares {

    /**
     * Return sorted squares of a sorted array in O(n) time.
     *
     * @param nums sorted input array
     * @return sorted array of squares
     */
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution
        return new int[0];
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
