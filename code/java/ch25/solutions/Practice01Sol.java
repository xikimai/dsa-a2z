package ch25.solutions;

public class Practice01Sol {
    // Partition Equal Subset Sum: reduce to Subset Sum with target = total/2
    public static boolean solve(int[] nums) {
        int total = 0;
        for (int n : nums) total += n;
        if (total % 2 != 0) return false;
        int target = total / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums)
            for (int s = target; s >= num; s--)
                if (dp[s - num]) dp[s] = true;
        return dp[target];
    }
}
