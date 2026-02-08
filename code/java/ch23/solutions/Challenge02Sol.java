package ch23.solutions;

public class Challenge02Sol {
    public static int solve(int[] prices) {
        if (prices.length == 0) return 0;
        int held = -prices[0], sold = 0, rest = 0;
        for (int i = 1; i < prices.length; i++) {
            int prevHeld = held;
            held = Math.max(held, rest - prices[i]);
            rest = Math.max(rest, sold);
            sold = prevHeld + prices[i];
        }
        return Math.max(sold, rest);
    }
}
