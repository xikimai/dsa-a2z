package ch17.practice;

import java.util.*;

/**
 * Practice 4: Find Median from Data Stream
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Return list of medians after adding each number.
 * EXAMPLES:
 *   solve([5,15,1,3]) -> [5.0, 10.0, 5.0, 4.0]
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice04FindMedian {
    public static List<Double> solve(int[] nums) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) nums[i] = Integer.parseInt(parts[i]);
        System.out.println(solve(nums));
        sc.close();
    }
}
