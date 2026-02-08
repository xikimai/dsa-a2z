package ch15.practice;

import java.util.*;

/**
 * Challenge 2: Trapping Rain Water
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Compute how much water can be trapped after raining.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge02TrappingRainWater {
    public static int solve(int[] heights) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = line.isEmpty() ? new int[]{} :
            Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
