package ch18.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(int[] arrivals, int[] departures) {
        if (arrivals.length == 0) return 0;
        Arrays.sort(arrivals);
        Arrays.sort(departures);
        int platforms = 0, maxPlatforms = 0;
        int i = 0, j = 0, n = arrivals.length;
        while (i < n) {
            if (arrivals[i] <= departures[j]) {
                platforms++;
                maxPlatforms = Math.max(maxPlatforms, platforms);
                i++;
            } else {
                platforms--;
                j++;
            }
        }
        return maxPlatforms;
    }
}
