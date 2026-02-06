package ch05.practice;

import java.util.*;

/**
 * Challenge 01: Find Duplicates (Three Ways)
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM
 * -------
 * Given an array of integers, find all elements that appear more
 * than once. Return them in sorted order.
 *
 * Implement THREE approaches:
 *   solveBrute — O(n^2) nested loops
 *   solveSort  — O(n log n) sort then scan
 *   solveSet   — O(n) using a HashSet
 *
 * The solve() method should call solveSet (the best approach).
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the sorted duplicates as space-separated integers.
 *
 * CONSTRAINTS
 * -----------
 * 0 <= nums.length <= 10^5
 *
 * EXAMPLES
 * --------
 * Input:  4 3 2 7 8 2 3 1
 * Output: 2 3
 *
 * Input:  1 2 3
 * Output: (empty)
 *
 * Input:  1 1 1 1
 * Output: 1
 *
 * INSTRUCTIONS
 * ------------
 * 1. Implement all three approaches.
 * 2. Use solveSet in solve() for best performance.
 * The main method handles input/output -- don't change it.
 */
public class Challenge01FindDuplicates {

    /**
     * Brute force: O(n^2) nested loops.
     *
     * @param nums the input array
     * @return sorted array of duplicate elements
     */
    public static int[] solveBrute(int[] nums) {
        // TODO: Implement
        return new int[0];
    }

    /**
     * Sort approach: O(n log n) sort then scan neighbors.
     *
     * @param nums the input array
     * @return sorted array of duplicate elements
     */
    public static int[] solveSort(int[] nums) {
        // TODO: Implement
        return new int[0];
    }

    /**
     * Set approach: O(n) using a HashSet.
     *
     * @param nums the input array
     * @return sorted array of duplicate elements
     */
    public static int[] solveSet(int[] nums) {
        // TODO: Implement
        return new int[0];
    }

    /**
     * Find all duplicate elements (uses the best approach).
     *
     * @param nums the input array
     * @return sorted array of duplicate elements
     */
    public static int[] solve(int[] nums) {
        // TODO: Replace this with your solution (call solveSet)
        return new int[0];
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
