package ch18.solutions;

public class Practice05Sol {
    public static int solve(int[] nums) {
        if (nums.length <= 1) return 0;
        int jumps = 0, currentEnd = 0, farthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;
                if (currentEnd >= nums.length - 1) break;
            }
        }
        return jumps;
    }
}
