package ch15.practice;

import java.util.*;

/**
 * Practice 1: Container With Most Water
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Find two lines forming a container holding the most water.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice01ContainerMostWater {
    public static int solve(int[] heights) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        int[] arr = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
