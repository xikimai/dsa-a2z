package ch16.practice;

import java.util.*;

/**
 * Warmup 2: First and Last Position
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Given sorted array and target, return [first, last] indices
 *          of target. Return [-1, -1] if not found.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup02FirstLastPosition {
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
