package ch16.solutions;

import java.util.Arrays;

public class Challenge01Sol {
    public static int solve(int[] stalls, int cows) {
        Arrays.sort(stalls);
        int lo = 1, hi = stalls[stalls.length - 1] - stalls[0];
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (feasible(stalls, cows, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    static boolean feasible(int[] stalls, int cows, int minDist) {
        int count = 1, last = stalls[0];
        for (int i = 1; i < stalls.length; i++) {
            if (stalls[i] - last >= minDist) {
                count++;
                last = stalls[i];
                if (count >= cows) return true;
            }
        }
        return false;
    }
}
