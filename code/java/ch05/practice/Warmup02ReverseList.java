package ch05.practice;

import java.util.*;

/**
 * Warmup 02: Reverse List
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of integers, reverse it in place without using
 * any built-in reverse function. Return the reversed array.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the reversed array as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:  1 2 3 4 5
 * Output: 5 4 3 2 1
 *
 * Input:  1
 * Output: 1
 *
 * Input:  (empty)
 * Output: (empty)
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return nums;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup02ReverseList {

    /**
     * Reverse the array in place and return it.
     *
     * @param nums the input array
     * @return the reversed array (same reference)
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
