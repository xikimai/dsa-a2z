package ch23.solutions;

public class Warmup03Sol {
    public static int solve(int[] cost) {
        int n = cost.length;
        int prev2 = 0, prev1 = 0;
        for (int i = 2; i <= n; i++) {
            int current = Math.min(prev1 + cost[i - 1], prev2 + cost[i - 2]);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
