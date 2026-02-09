package ch34.solutions;

import java.util.*;

public class Challenge01Sol {
    // Convex Hull Perimeter
    static long cross(int[] o, int[] a, int[] b) {
        return (long)(a[0] - o[0]) * (b[1] - o[1])
             - (long)(a[1] - o[1]) * (b[0] - o[0]);
    }

    public static double solve(int[][] points) {
        int n = points.length;
        if (n <= 1) return 0.0;
        Arrays.sort(points, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        int[][] unique = new int[n][];
        int u = 0;
        for (int[] p : points)
            if (u == 0 || p[0] != unique[u-1][0] || p[1] != unique[u-1][1])
                unique[u++] = p;

        if (u <= 1) return 0.0;
        if (u == 2) {
            return 2.0 * Math.sqrt((double)(unique[0][0]-unique[1][0])*(unique[0][0]-unique[1][0])
                                 + (double)(unique[0][1]-unique[1][1])*(unique[0][1]-unique[1][1]));
        }

        int[][] hull = new int[2 * u][];
        int k = 0;

        for (int i = 0; i < u; i++) {
            while (k >= 2 && cross(hull[k-2], hull[k-1], unique[i]) <= 0) k--;
            hull[k++] = unique[i];
        }

        int lower = k + 1;
        for (int i = u - 2; i >= 0; i--) {
            while (k >= lower && cross(hull[k-2], hull[k-1], unique[i]) <= 0) k--;
            hull[k++] = unique[i];
        }
        k--; // remove duplicate

        double perimeter = 0.0;
        for (int i = 0; i < k; i++) {
            int j = (i + 1) % k;
            double dx = hull[i][0] - hull[j][0];
            double dy = hull[i][1] - hull[j][1];
            perimeter += Math.sqrt(dx * dx + dy * dy);
        }
        return perimeter;
    }
}
