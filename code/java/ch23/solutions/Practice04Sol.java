package ch23.solutions;

public class Practice04Sol {
    public static int solve(int[] prices) {
        if (prices.length == 0) return 0;
        int minPrice = prices[0], maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }
        return maxProfit;
    }
}
