package ch18.practice;

import java.util.*;

/**
 * Practice 2: Fractional Knapsack
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Max value with fractional items. Items are (weight, value).
 *
 * EXAMPLES:
 *   solve(50, [[10,60],[20,100],[30,120]]) -> 240.0
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice02FractionalKnapsack {
    public static double solve(int capacity, int[][] items) {
        // TODO: Replace this with your solution
        return 0.0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cap = Integer.parseInt(sc.nextLine().trim());
        int n = Integer.parseInt(sc.nextLine().trim());
        int[][] items = new int[n][2];
        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().trim().split(" ");
            items[i][0] = Integer.parseInt(parts[0]);
            items[i][1] = Integer.parseInt(parts[1]);
        }
        System.out.printf("%.4f%n", solve(cap, items));
        sc.close();
    }
}
