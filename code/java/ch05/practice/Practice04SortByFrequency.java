package ch05.practice;

import java.util.*;

/**
 * Practice 04: Sort by Frequency
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of integers, sort the elements by their frequency
 * in descending order. If two elements have the same frequency,
 * the smaller element comes first.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the sorted array as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= nums.length <= 10^5
 * -10^5 <= nums[i] <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:  2 3 1 3 2
 * Output: 2 2 3 3 1
 *
 * Input:  1
 * Output: 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return nums;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice04SortByFrequency {

    /**
     * Sort elements by frequency (descending), ties broken by value (ascending).
     *
     * @param nums the input array
     * @return sorted array
     */
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution
        return nums;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                           .mapToInt(Integer::parseInt).toArray();
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
