package ch23.solutions;

public class Practice02Sol {
    public static int solve(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        return Math.max(robLinear(nums, 0, n - 2), robLinear(nums, 1, n - 1));
    }

    private static int robLinear(int[] nums, int lo, int hi) {
        int prev2 = nums[lo];
        int prev1 = Math.max(nums[lo], nums[lo + 1]);
        for (int i = lo + 2; i <= hi; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
