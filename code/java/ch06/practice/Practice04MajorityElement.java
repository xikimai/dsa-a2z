package ch06.practice;

import java.util.*;

/**
 * Practice 04: Majority Element
 * ==============================
 * Chapter 6: How Fast Is Your Code?
 *
 * PROBLEM
 * -------
 * Given an array nums of size n, return the majority element.
 * The majority element is the element that appears more than n/2 times.
 * You may assume the majority element always exists.
 *
 * Use the Boyer-Moore Voting Algorithm for O(n) time and O(1) space.
 *
 * INPUT FORMAT
 * ------------
 * A single line of space-separated integers.
 *
 * OUTPUT FORMAT
 * -------------
 * Print the majority element.
 *
 * CONSTRAINTS
 * -----------
 * 1 <= nums.length <= 10^5
 * The majority element always exists.
 *
 * EXAMPLES
 * --------
 * Input:  3 2 3            Output: 3
 * Input:  2 2 1 1 1 2 2    Output: 2
 * Input:  1                Output: 1
 *
 * HINT
 * ----
 * Boyer-Moore Voting: maintain a candidate and a count. When count
 * reaches 0, pick the current element as the new candidate. Increment
 * count when you see the candidate, decrement otherwise.
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return 0;" in solve() with your solution.
 * The main method handles input/output -- don't change it.
 */
public class Practice04MajorityElement {

    /**
     * Find the majority element using Boyer-Moore Voting.
     *
     * @param nums the input array
     * @return the majority element
     */
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = Arrays.stream(sc.nextLine().trim().split("\\s+"))
                           .mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(nums));
        sc.close();
    }
}
