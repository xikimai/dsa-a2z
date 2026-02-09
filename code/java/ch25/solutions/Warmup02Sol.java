package ch25.solutions;

public class Warmup02Sol {
    // Subset Sum: 1D boolean DP, iterate backwards
    public static boolean solve(int[] nums, int target) {
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums)
            for (int s = target; s >= num; s--)
                if (dp[s - num]) dp[s] = true;
        return dp[target];
    }
}
