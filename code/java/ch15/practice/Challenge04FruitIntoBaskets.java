package ch15.practice;

import java.util.*;

/**
 * Challenge 4: Fruit Into Baskets (Max Two Distinct Types)
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Find the longest subarray with at most 2 distinct elements.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge04FruitIntoBaskets {
    public static int solve(int[] fruits) {
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
