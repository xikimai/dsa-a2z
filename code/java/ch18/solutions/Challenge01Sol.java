package ch18.solutions;

import java.util.*;

public class Challenge01Sol {
    public static int[] solve(int[][] jobs) {
        if (jobs.length == 0) return new int[]{0, 0};
        Arrays.sort(jobs, (a, b) -> Integer.compare(b[2], a[2]));
        int maxDeadline = 0;
        for (int[] j : jobs) maxDeadline = Math.max(maxDeadline, j[1]);
        boolean[] slots = new boolean[maxDeadline + 1];
        int count = 0, totalProfit = 0;
        for (int[] job : jobs) {
            for (int t = job[1]; t >= 1; t--) {
                if (!slots[t]) {
                    slots[t] = true;
                    count++;
                    totalProfit += job[2];
                    break;
                }
            }
        }
        return new int[]{count, totalProfit};
    }
}
