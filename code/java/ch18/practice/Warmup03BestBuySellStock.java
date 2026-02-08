package ch18.practice;

import java.util.*;

/**
 * Warmup 3: Best Time to Buy and Sell Stock
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Find max profit from one buy-sell. Return 0 if no profit.
 *
 * EXAMPLES:
 *   solve([7,1,5,3,6,4]) -> 5
 *   solve([7,6,4,3,1])   -> 0
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Warmup03BestBuySellStock {
    public static int solve(int[] prices) {
        // TODO: Replace this with your solution
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] prices = Arrays.stream(sc.nextLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(prices));
        sc.close();
    }
}
