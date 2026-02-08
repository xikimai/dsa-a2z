package ch16.solutions;

public class Practice01Sol {
    public static int solve(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(piles, mid, h)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    static boolean feasible(int[] piles, int k, int h) {
        int hours = 0;
        for (int p : piles) hours += (p + k - 1) / k;
        return hours <= h;
    }
}
