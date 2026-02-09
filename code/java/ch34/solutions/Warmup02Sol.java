package ch34.solutions;

import java.util.*;

public class Warmup02Sol {
    // Convex Hull (Andrew's Monotone Chain)
    static long cross(int[] o, int[] a, int[] b) {
        return (long)(a[0] - o[0]) * (b[1] - o[1])
             - (long)(a[1] - o[1]) * (b[0] - o[0]);
    }

    public static int[][] solve(int[][] points) {
        int n = points.length;
        if (n <= 1) return points;
        Arrays.sort(points, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        // Remove duplicates
        int[][] unique = new int[n][];
        int u = 0;
        for (int[] p : points)
            if (u == 0 || p[0] != unique[u-1][0] || p[1] != unique[u-1][1])
                unique[u++] = p;
        if (u <= 1) return Arrays.copyOf(unique, u);

        int[][] hull = new int[2 * u][];
        int k = 0;

        // Lower hull
        for (int i = 0; i < u; i++) {
            while (k >= 2 && cross(hull[k-2], hull[k-1], unique[i]) <= 0) k--;
            hull[k++] = unique[i];
        }

        // Upper hull
        int lower = k + 1;
        for (int i = u - 2; i >= 0; i--) {
            while (k >= lower && cross(hull[k-2], hull[k-1], unique[i]) <= 0) k--;
            hull[k++] = unique[i];
        }

        return Arrays.copyOf(hull, k - 1);
    }
}
