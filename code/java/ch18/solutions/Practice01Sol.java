package ch18.solutions;

import java.util.*;

public class Practice01Sol {
    public static int solve(int[][] activities) {
        if (activities.length == 0) return 0;
        Arrays.sort(activities, (a, b) -> Integer.compare(a[1], b[1]));
        int count = 0, lastEnd = 0;
        for (int[] act : activities) {
            if (act[0] >= lastEnd) { count++; lastEnd = act[1]; }
        }
        return count;
    }
}
