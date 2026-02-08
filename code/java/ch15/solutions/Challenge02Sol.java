package ch15.solutions;

public class Challenge02Sol {
    public static int solve(int[] heights) {
        if (heights.length < 3) return 0;
        int left = 0, right = heights.length - 1;
        int leftMax = heights[left], rightMax = heights[right];
        int water = 0;

        while (left < right) {
            if (leftMax <= rightMax) {
                left++;
                leftMax = Math.max(leftMax, heights[left]);
                water += leftMax - heights[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, heights[right]);
                water += rightMax - heights[right];
            }
        }
        return water;
    }
}
