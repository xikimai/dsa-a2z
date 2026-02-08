package ch15.practice;

import java.util.*;

/**
 * Challenge 1: Three Sum
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Find all unique triplets that sum to zero.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge01ThreeSum {
    public static List<List<Integer>> solve(int[] nums) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] nums = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(nums));
        sc.close();
    }
}
