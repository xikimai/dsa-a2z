package ch16.solutions;

public class Practice04Sol {
    public static int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return -1;
        int bestRow = -1, bestCount = 0;
        int cols = matrix[0].length;
        for (int i = 0; i < matrix.length; i++) {
            int lo = 0, hi = cols;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (matrix[i][mid] == 1) hi = mid;
                else lo = mid + 1;
            }
            int count = cols - lo;
            if (count > bestCount) { bestCount = count; bestRow = i; }
        }
        return bestRow;
    }
}
