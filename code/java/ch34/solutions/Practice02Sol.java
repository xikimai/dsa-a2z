package ch34.solutions;

public class Practice02Sol {
    // Line Segment Intersection
    static long cross(int[] o, int[] a, int[] b) {
        return (long)(a[0] - o[0]) * (b[1] - o[1])
             - (long)(a[1] - o[1]) * (b[0] - o[0]);
    }

    static int orientation(int[] a, int[] b, int[] c) {
        long cp = cross(a, b, c);
        if (cp > 0) return 1;
        if (cp < 0) return -1;
        return 0;
    }

    static boolean onSegment(int[] p, int[] q, int[] r) {
        return q[0] >= Math.min(p[0], r[0]) && q[0] <= Math.max(p[0], r[0])
            && q[1] >= Math.min(p[1], r[1]) && q[1] <= Math.max(p[1], r[1]);
    }

    static boolean intersects(int[] a, int[] b, int[] c, int[] d) {
        int d1 = orientation(c, d, a), d2 = orientation(c, d, b);
        int d3 = orientation(a, b, c), d4 = orientation(a, b, d);
        if (d1 * d2 < 0 && d3 * d4 < 0) return true;
        if (d1 == 0 && onSegment(c, a, d)) return true;
        if (d2 == 0 && onSegment(c, b, d)) return true;
        if (d3 == 0 && onSegment(a, c, b)) return true;
        if (d4 == 0 && onSegment(a, d, b)) return true;
        return false;
    }

    public static boolean[] solve(int[][][] segments) {
        boolean[] result = new boolean[segments.length];
        for (int i = 0; i < segments.length; i++) {
            result[i] = intersects(segments[i][0], segments[i][1],
                                   segments[i][2], segments[i][3]);
        }
        return result;
    }
}
