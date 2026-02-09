package ch34.solutions;

public class Practice03Sol {
    // Point in Polygon (Ray Casting + Boundary Check)
    public static boolean[] solve(int[][] polygon, int[][] queries) {
        boolean[] result = new boolean[queries.length];
        for (int q = 0; q < queries.length; q++) {
            result[q] = pointInPoly(polygon, queries[q][0], queries[q][1]);
        }
        return result;
    }

    static boolean pointInPoly(int[][] poly, int px, int py) {
        int n = poly.length;

        // Check boundary
        for (int i = 0; i < n; i++) {
            int j = (i + 1) % n;
            long cp = (long)(poly[j][0] - poly[i][0]) * (py - poly[i][1])
                    - (long)(poly[j][1] - poly[i][1]) * (px - poly[i][0]);
            if (cp == 0
                && px >= Math.min(poly[i][0], poly[j][0])
                && px <= Math.max(poly[i][0], poly[j][0])
                && py >= Math.min(poly[i][1], poly[j][1])
                && py <= Math.max(poly[i][1], poly[j][1]))
                return true;
        }

        // Ray casting
        boolean inside = false;
        for (int i = 0, j2 = n - 1; i < n; j2 = i++) {
            int yi = poly[i][1], yj = poly[j2][1];
            int xi = poly[i][0], xj = poly[j2][0];
            if ((yi > py) != (yj > py)) {
                double xIntersect = (double)(xj - xi) * (py - yi) / (yj - yi) + xi;
                if (px < xIntersect) inside = !inside;
            }
        }
        return inside;
    }
}
