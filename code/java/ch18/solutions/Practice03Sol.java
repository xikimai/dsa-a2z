package ch18.solutions;

import java.util.*;

public class Practice03Sol {
    public static int[][] solve(int[][] intervals) {
        if (intervals.length == 0) return new int[0][];
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0].clone());
        for (int i = 1; i < intervals.length; i++) {
            int[] last = merged.get(merged.size() - 1);
            if (intervals[i][0] <= last[1]) {
                last[1] = Math.max(last[1], intervals[i][1]);
            } else {
                merged.add(intervals[i].clone());
            }
        }
        return merged.toArray(new int[0][]);
    }
}
