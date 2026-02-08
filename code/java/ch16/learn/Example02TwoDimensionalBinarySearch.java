package ch16.learn;

/**
 * Example 02: 2D Binary Search — Searching in Matrices
 * ======================================================
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * Demonstrates searching in a fully sorted matrix and finding the row
 * with the maximum number of 1s in a binary matrix.
 */
public class Example02TwoDimensionalBinarySearch {

    public static void main(String[] args) {
        // Part 1: Search in Sorted Matrix
        System.out.println("=== Part 1: Search in Sorted Matrix ===");
        int[][] matrix = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60},
            {61, 62, 67, 70}
        };

        System.out.println("Matrix:");
        for (int[] row : matrix) {
            System.out.print("  [");
            for (int j = 0; j < row.length; j++) {
                System.out.printf("%3d%s", row[j], j < row.length - 1 ? "," : "");
            }
            System.out.println("]");
        }

        int target = 30;
        int rows = matrix.length, cols = matrix[0].length;
        System.out.println("\nSearching for " + target + ":");

        int lo = 0, hi = rows * cols - 1;
        int step = 0;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int r = mid / cols, c = mid % cols;
            int val = matrix[r][c];
            step++;
            System.out.printf("  Step %d: idx=%d -> [%d][%d] = %d", step, mid, r, c, val);
            if (val == target) {
                System.out.println("  FOUND!");
                break;
            } else if (val < target) {
                System.out.println("  < " + target + " -> search right");
                lo = mid + 1;
            } else {
                System.out.println("  > " + target + " -> search left");
                hi = mid - 1;
            }
        }

        // Part 2: Row with Maximum 1s
        System.out.println("\n=== Part 2: Row with Maximum 1s ===");
        int[][] binMatrix = {
            {0, 0, 0, 1, 1},
            {0, 0, 1, 1, 1},
            {0, 0, 0, 0, 1},
            {0, 1, 1, 1, 1},
            {0, 0, 0, 0, 0}
        };

        int binCols = binMatrix[0].length;
        int bestRow = -1, bestCount = 0;
        for (int i = 0; i < binMatrix.length; i++) {
            int blo = 0, bhi = binCols;
            while (blo < bhi) {
                int mid = blo + (bhi - blo) / 2;
                if (binMatrix[i][mid] == 1) bhi = mid;
                else blo = mid + 1;
            }
            int count = binCols - blo;
            String marker = count > bestCount ? " <-- BEST" : "";
            System.out.println("  Row " + i + ": first 1 at idx " + blo + ", count=" + count + marker);
            if (count > bestCount) { bestCount = count; bestRow = i; }
        }
        System.out.println("Row with max 1s: " + bestRow + " (" + bestCount + " ones)");
    }
}
