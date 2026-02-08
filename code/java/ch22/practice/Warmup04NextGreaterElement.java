package ch22.practice;

import java.util.*;

/**
 * Warmup 4: Next Greater Element
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: For each element, find the next greater element to its right.
 *          If none exists, use -1.
 *
 * EXAMPLES:
 *   solve([4,5,2,10,8]) -> [5,10,10,-1,-1]
 *   solve([3,2,1])      -> [-1,-1,-1]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup04NextGreaterElement {
    public static int[] solve(int[] arr) {
        // TODO: Replace this with your solution
        return new int[arr.length];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().trim().split("\\s+");
        int[] arr = new int[parts.length];
        for (int i = 0; i < parts.length; i++) arr[i] = Integer.parseInt(parts[i]);
        System.out.println(Arrays.toString(solve(arr)));
        sc.close();
    }
}
