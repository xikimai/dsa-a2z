package ch05.practice;

import java.util.*;

/**
 * Warmup 06: Move Zeros
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of integers, move all zeros to the end while
 * maintaining the relative order of the non-zero elements.
 * Do this in place.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the resulting array as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:  0 1 0 3 12
 * Output: 1 3 12 0 0
 *
 * Input:  0 0 1
 * Output: 1 0 0
 *
 * Input:  1 2 3
 * Output: 1 2 3
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return nums;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup06MoveZeros {

    /**
     * Move all zeros to the end, maintaining order of non-zeros.
     *
     * @param nums the input array (modified in place)
     * @return the same array with zeros moved to end
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
