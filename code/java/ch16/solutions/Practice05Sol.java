package ch16.solutions;

public class Practice05Sol {
    public static int solve(int[] pages, int students) {
        if (students > pages.length) return -1;
        int lo = 0, hi = 0;
        for (int p : pages) { lo = Math.max(lo, p); hi += p; }
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (feasible(pages, students, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    static boolean feasible(int[] pages, int students, int maxPages) {
        int count = 1, current = 0;
        for (int p : pages) {
            if (current + p > maxPages) { count++; current = 0; }
            current += p;
        }
        return count <= students;
    }
}
