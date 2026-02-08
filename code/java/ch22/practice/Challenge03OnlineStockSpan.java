package ch22.practice;

import java.util.*;

/**
 * Challenge 3: Online Stock Span
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: For each day's price, return the span (consecutive days with
 *          price <= today's price, counting backward from today).
 *
 * EXAMPLES:
 *   solve([100,80,60,70,60,75,85]) -> [1,1,1,2,1,4,6]
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Challenge03OnlineStockSpan {
    public static int[] solve(int[] prices) {
        // TODO: Replace this with your solution
        return new int[prices.length];
    }

    public static void main(String[] args) {
        int[] prices = {100, 80, 60, 70, 60, 75, 85};
        System.out.println(Arrays.toString(solve(prices)));
    }
}
