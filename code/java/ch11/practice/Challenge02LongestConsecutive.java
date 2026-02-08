package ch11.practice;

import java.util.*;

/**
 * Challenge 2: Longest Consecutive Sequence
 * ==============================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM: Given an unsorted array of integers, find the length of the longest
 *          consecutive elements sequence. Your algorithm should run in O(n) time.
 *
 *          Use a HashSet. For each number, only start counting a sequence if
 *          (num - 1) is NOT in the set (this means num is the start of a sequence).
 *
 * EXAMPLES:
 *   solve([100,4,200,1,3,2])             -> 4    (sequence: 1,2,3,4)
 *   solve([0,3,7,2,5,8,4,6,0,1])        -> 9    (sequence: 0,1,2,3,4,5,6,7,8)
 *   solve([])                            -> 0
 *   solve([1])                           -> 1
 *   solve([1,1,1])                       -> 1
 *   solve([9,1,4,7,3,-1,0,5,8,2,6])     -> 11   (sequence: -1,0,1,...,9)
 *
 * CONSTRAINTS:
 *   - 0 <= nums.length <= 10^5
 *   - -10^9 <= nums[i] <= 10^9
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02LongestConsecutive {
    public static int solve(int[] nums) {
        // TODO: Replace this with your solution
        return 0;
    }

    // ── Do not change anything below this line ──────────────────────
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        System.out.println(solve(nums));
        sc.close();
    }
}
