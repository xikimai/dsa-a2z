package ch15.solutions;

public class Practice01Sol {
    public static int solve(int[] heights) {
        int left = 0, right = heights.length - 1;
        int best = 0;
        while (left < right) {
            int w = right - left;
            int h = Math.min(heights[left], heights[right]);
            best = Math.max(best, w * h);
            if (heights[left] < heights[right]) left++;
            else right--;
        }
        return best;
    }
}
