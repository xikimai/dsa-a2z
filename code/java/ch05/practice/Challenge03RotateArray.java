package ch05.practice;

import java.util.*;

/**
 * Challenge 03: Rotate Array
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array and an integer k, rotate the array to the right
 * by k steps. Handle the case where k is greater than the array length.
 *
 * INPUT FORMAT
 * ------------
 * First line: space-separated integers (the array).
 * Second line: a single integer k.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the rotated array as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 * 0 <= k <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:
 * 1 2 3 4 5 6 7
 * 3
 * Output: 5 6 7 1 2 3 4
 *
 * Input:
 * 1 2
 * 3
 * Output: 2 1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return nums;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Challenge03RotateArray {

    /**
     * Rotate the array to the right by k steps.
     *
     * @param nums the input array
     * @param k    number of steps to rotate right
     * @return the rotated array
     */
    public static int[] solve(int[] nums, int k) {
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
