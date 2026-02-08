package ch23.learn;

/**
 * Example 02: Stock DP — State Machine Thinking
 * ================================================
 * Chapter 23: Dynamic Programming I — The Foundation
 *
 * Demonstrates: Stock I, II, III, Cooldown, Fee
 */
public class Example02StockDp {

    static int stockOne(int[] prices) {
        int minPrice = prices[0], maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }
        return maxProfit;
    }

    static int stockUnlimited(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++)
            if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
        return profit;
    }

    static int stockTwoTxn(int[] prices) {
        int buy1 = -prices[0], sell1 = 0, buy2 = -prices[0], sell2 = 0;
        for (int i = 1; i < prices.length; i++) {
            buy1 = Math.max(buy1, -prices[i]);
            sell1 = Math.max(sell1, buy1 + prices[i]);
            buy2 = Math.max(buy2, sell1 - prices[i]);
            sell2 = Math.max(sell2, buy2 + prices[i]);
        }
        return sell2;
    }

    static int stockCooldown(int[] prices) {
        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int prevHeld = held;
            held = Math.max(held, rest - prices[i]);
            rest = Math.max(rest, sold);
            sold = prevHeld + prices[i];
        }
        return Math.max(sold, rest);
    }

    static int stockFee(int[] prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            cash = Math.max(cash, hold + prices[i] - fee);
            hold = Math.max(hold, cash - prices[i]);
        }
        return cash;
    }

    public static void main(String[] args) {
        int[] p1 = {7, 1, 5, 3, 6, 4};
        System.out.println("Prices: [7,1,5,3,6,4]");
        System.out.printf("  Stock I:   %d%n", stockOne(p1));
        System.out.printf("  Stock II:  %d%n", stockUnlimited(p1));

        int[] p2 = {3, 3, 5, 0, 0, 3, 1, 4};
        System.out.println("Prices: [3,3,5,0,0,3,1,4]");
        System.out.printf("  Stock III: %d%n", stockTwoTxn(p2));

        int[] p3 = {1, 2, 3, 0, 2};
        System.out.println("Prices: [1,2,3,0,2]");
        System.out.printf("  Cooldown:  %d%n", stockCooldown(p3));

        int[] p4 = {1, 3, 2, 8, 4, 9};
        System.out.println("Prices: [1,3,2,8,4,9], Fee: 2");
        System.out.printf("  With Fee:  %d%n", stockFee(p4, 2));
    }
}
