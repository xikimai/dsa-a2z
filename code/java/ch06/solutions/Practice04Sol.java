package ch06.solutions;

import java.util.*;

/**
 * Solution for Practice 04: Majority Element
 * ============================================
 * Chapter 6: How Fast Is Your Code?
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Boyer-Moore Voting Algorithm:
 *   1. Maintain a candidate and a count (starting at 0).
 *   2. For each element:
 *      - If count == 0, set candidate = current element
 *      - If current == candidate, increment count
 *      - Otherwise, decrement count
 *   3. The candidate at the end is the majority element.
 *
 * This works because the majority element appears > n/2 times, so it
 * can never be fully "voted out."
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1)
 */
public class Practice04Sol {

    public static int solve(int[] nums) {
        int candidate = 0;
        int count = 0;
        for (int n : nums) {
            if (count == 0) {
                candidate = n;
            }
            count += (n == candidate) ? 1 : -1;
        }
        return candidate;
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
