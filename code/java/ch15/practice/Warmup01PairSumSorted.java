package ch15.practice;

import java.util.*;

/**
 * Warmup 1: Pair Sum in Sorted Array
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Given a sorted array and target, find two numbers summing to target.
 *          Return [a, b] with a <= b, smallest first element. Return [-1,-1] if none.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup01PairSumSorted {
    public static int[] solve(int[] arr, int target) {
        // TODO: Replace this with your solution
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        int target = sc.nextInt();
        System.out.println(Arrays.toString(solve(arr, target)));
        sc.close();
    }
}
