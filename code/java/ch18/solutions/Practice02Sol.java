package ch18.solutions;

import java.util.*;

public class Practice02Sol {
    public static double solve(int capacity, int[][] items) {
        if (capacity == 0 || items.length == 0) return 0.0;
        Arrays.sort(items, (a, b) -> Double.compare(
            (double) b[1] / b[0], (double) a[1] / a[0]));
        double totalValue = 0.0;
        int remaining = capacity;
        for (int[] item : items) {
            if (remaining <= 0) break;
            int take = Math.min(item[0], remaining);
            totalValue += take * ((double) item[1] / item[0]);
            remaining -= take;
        }
        return totalValue;
    }
}
