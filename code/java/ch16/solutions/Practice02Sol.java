package ch16.solutions;

public class Practice02Sol {
    public static int solve(int[] weights, int d) {
        int lo = 0, hi = 0;
        for (int w : weights) { lo = Math.max(lo, w); hi += w; }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(weights, mid, d)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    static boolean feasible(int[] weights, int cap, int d) {
        int days = 1, load = 0;
        for (int w : weights) {
            if (load + w > cap) { days++; load = 0; }
            load += w;
        }
        return days <= d;
    }
}
