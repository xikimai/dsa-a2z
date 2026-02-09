package ch30.solutions;
import java.util.*;
public class Challenge04Sol {
    public static int solve(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int count = 1, lastEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= lastEnd) { count++; lastEnd = intervals[i][1]; }
        }
        return count;
    }
}
