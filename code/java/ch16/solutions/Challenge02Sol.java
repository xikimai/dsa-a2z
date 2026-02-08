package ch16.solutions;

public class Challenge02Sol {
    public static int solve(int[] boards, int k) {
        int lo = 0, hi = 0;
        for (int b : boards) { lo = Math.max(lo, b); hi += b; }
        if (k > boards.length) return lo;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(boards, k, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    static boolean feasible(int[] boards, int k, int maxLen) {
        int painters = 1, current = 0;
        for (int b : boards) {
            if (current + b > maxLen) { painters++; current = 0; }
            current += b;
        }
        return painters <= k;
    }
}
