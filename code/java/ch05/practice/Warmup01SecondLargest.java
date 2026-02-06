package ch05.practice;

import java.util.*;

/**
 * Warmup 01: Second Largest
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of integers, return the second largest element.
 * If there is no second largest (all elements are the same, or
 * the array has fewer than 2 elements), return -1.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the second largest element, or -1.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:  3 1 4 1 5
 * Output: 4
 *
 * Input:  7 7 7
 * Output: -1
 *
 * Input:  1 2
 * Output: 1
 *
 * Input:  10
 * Output: -1
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return -1;" in the solve() method with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Warmup01SecondLargest {

    /**
     * Return the second largest element, or -1 if none exists.
     *
     * @param nums the input array
     * @return second largest, or -1
     */
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return -1;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(solve(new int[0]));
        } else {
            int[] nums = Arrays.stream(line.split("\\s+"))
                               .mapToInt(Integer::parseInt).toArray();
            System.out.println(solve(nums));
        }
        sc.close();
    }
}
