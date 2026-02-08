package ch17.practice;

import java.util.*;

/**
 * Practice 1: Top K Frequent Elements
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Return the k most frequent elements, sorted ascending.
 * EXAMPLES:
 *   solve([1,1,1,2,2,3], 2) -> [1,2]
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01TopKFrequent {
    public static List<Integer> solve(int[] nums, int k) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(nums, k));
        sc.close();
    }
}
