package ch18.solutions;

public class Warmup03Sol {
    public static int solve(int[] prices) {
        if (prices.length < 2) return 0;
        int minPrice = prices[0], maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }
        return maxProfit;
    }
}
