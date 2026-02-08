package ch15.solutions;

public class Warmup03Sol {
    public static int solve(int[] arr, int k) {
        if (arr.length < k) return 0;
        int windowSum = 0;
        for (int i = 0; i < k; i++) windowSum += arr[i];
        int best = windowSum;
        for (int i = k; i < arr.length; i++) {
            windowSum += arr[i] - arr[i - k];
            best = Math.max(best, windowSum);
        }
        return best;
    }
}
