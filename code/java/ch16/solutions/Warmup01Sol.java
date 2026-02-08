package ch16.solutions;

public class Warmup01Sol {
    public static int solve(int n) {
        if (n <= 0) return 0;
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (mid <= n / mid) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
