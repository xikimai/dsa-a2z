package ch34.solutions;

import java.util.*;

public class Practice01Sol {
    // Closest Pair of Points (Divide and Conquer)
    public static double solve(int[][] points) {
        int[][] pts = points.clone();
        Arrays.sort(pts, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        return rec(pts, 0, pts.length - 1);
    }

    static double dist(int[] a, int[] b) {
        return Math.sqrt((double)(a[0]-b[0])*(a[0]-b[0])
                       + (double)(a[1]-b[1])*(a[1]-b[1]));
    }

    static double rec(int[][] pts, int lo, int hi) {
        if (hi - lo < 3) {
            double best = Double.MAX_VALUE;
            for (int i = lo; i <= hi; i++)
                for (int j = i + 1; j <= hi; j++)
                    best = Math.min(best, dist(pts[i], pts[j]));
            return best;
        }
        int mid = (lo + hi) / 2;
        int midX = pts[mid][0];
        double d = Math.min(rec(pts, lo, mid), rec(pts, mid + 1, hi));

        List<int[]> strip = new ArrayList<>();
        for (int i = lo; i <= hi; i++)
            if (Math.abs(pts[i][0] - midX) < d) strip.add(pts[i]);
        strip.sort((a, b) -> a[1] - b[1]);

        for (int i = 0; i < strip.size(); i++)
            for (int j = i + 1; j < strip.size()
                 && strip.get(j)[1] - strip.get(i)[1] < d; j++)
                d = Math.min(d, dist(strip.get(i), strip.get(j)));
        return d;
    }
}
