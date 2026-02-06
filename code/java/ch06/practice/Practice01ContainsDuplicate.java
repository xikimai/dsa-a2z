package ch06.practice;

import java.util.*;

/**
 * Practice 01: Contains Duplicate
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given an integer array nums, return true if any value appears at
 * least twice in the array, and return false if every element is distinct.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers (may be empty).
 *
 * OUTPUT FORMAT
 * -------------
 * Print true or false.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 *
 * EXAMPLES
 * --------
 * Input:  1 2 3 1       Output: true
 * Input:  1 2 3 4       Output: false
 * Input:                Output: false
 * Input:  1             Output: false
 *
 * HINT
 * ----
 * Think about what data structure lets you check "have I seen this before?"
 * in O(1) time. A HashSet is your friend here!
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return false;" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice01ContainsDuplicate {

    /**
     * Return true if any element appears more than once.
     *
     * @param nums the input array
     * @return true if duplicates exist
     */
    public static boolean solve(int[] nums) {
        // TODO: Replace this with your solution
        return false;
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
