package ch12.practice;

import java.util.*;

/**
 * Practice 4: Power Set Using Bitmasks
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * PROBLEM: Return all subsets of nums using bitmask iteration.
 * EXAMPLES:
 *   solve([1,2,3]) -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * CONSTRAINTS: 0 <= nums.length <= 10
 */
public class Practice04PowerSetBitmask {
    public static List<List<Integer>> solve(int[] nums) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        List<List<Integer>> result = solve(nums);
        for (List<Integer> subset : result) {
            System.out.println(subset);
        }
        sc.close();
    }
}
