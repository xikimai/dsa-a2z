package ch16.solutions;

public class Warmup04Sol {
    public static int solve(int[] arr) {
        if (arr.length == 0) return -1;
        if (arr.length == 1) return 0;
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < arr[mid + 1]) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
