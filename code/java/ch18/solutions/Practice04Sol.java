package ch18.solutions;

import java.util.*;

public class Practice04Sol {
    public static int solve(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int keep = 0, lastEnd = Integer.MIN_VALUE;
        for (int[] iv : intervals) {
            if (iv[0] >= lastEnd) { keep++; lastEnd = iv[1]; }
        }
        return intervals.length - keep;
    }
}
