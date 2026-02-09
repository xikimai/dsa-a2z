package ch34.solutions;

public class Warmup03Sol {
    // Polygon Area (Shoelace Formula)
    public static double solve(int[][] polygon) {
        int n = polygon.length;
        long area = 0;
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            area += (long) polygon[i][0] * polygon[j][1];
            area -= (long) polygon[j][0] * polygon[i][1];
        }
        return Math.abs(area) / 2.0;
    }
}
