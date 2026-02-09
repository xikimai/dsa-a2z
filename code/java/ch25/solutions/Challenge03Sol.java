package ch25.solutions;

public class Challenge03Sol {
    // Target Sum: reduce to subset sum count
    public static int solve(int[] nums, int target) {
        int total = 0;
        for (int n : nums) total += n;
        if ((total + target) % 2 != 0 || total + target < 0) return 0;
        int p = (total + target) / 2;
        if (p < 0) return 0;
        int[] dp = new int[p + 1];
        dp[0] = 1;
        for (int num : nums)
            for (int s = p; s >= num; s--)
                dp[s] += dp[s - num];
        return dp[p];
    }
}
