package ch05.practice;

import java.util.*;

/**
 * Warmup 04: Remove Duplicates
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given a sorted array of integers, remove duplicates and return
 * a new array containing only the unique elements, preserving order.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated sorted integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the unique elements as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 * The input array is sorted in non-decreasing order.
 *
 * EXAMPLES
 * --------
 * Input:  1 1 2
 * Output: 1 2
 *
 * Input:  1 1 1 2 2 3
 * Output: 1 2 3
 *
 * Input:  1
 * Output: 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return nums;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup04RemoveDuplicates {

    /**
     * Remove duplicates from a sorted array, returning a new array
     * of unique elements.
     *
     * @param nums sorted input array
     * @return new array with duplicates removed
     */
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution
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
