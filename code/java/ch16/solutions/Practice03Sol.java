package ch16.solutions;

public class Practice03Sol {
    public static int[] solve(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return new int[]{-1, -1};
        int rows = matrix.length, cols = matrix[0].length;
        int lo = 0, hi = rows * cols - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int val = matrix[mid / cols][mid % cols];
            if (val == target) return new int[]{mid / cols, mid % cols};
            else if (val < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return new int[]{-1, -1};
    }
}
