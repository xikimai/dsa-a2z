package ch23.solutions;

public class Warmup05Sol {
    public static int solve(int[] nums) {
        int current = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            current = Math.max(current + nums[i], nums[i]);
            best = Math.max(best, current);
        }
        return best;
    }
}
