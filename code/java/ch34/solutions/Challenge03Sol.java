package ch34.solutions;

import java.util.*;

public class Challenge03Sol {
    // Rectangle Union Area (Sweep Line)
    public static int solve(int[][] rectangles) {
        if (rectangles.length == 0) return 0;

        // Collect y-coordinates
        TreeSet<Integer> ySet = new TreeSet<>();
        List<int[]> events = new ArrayList<>();
        for (int[] r : rectangles) {
            ySet.add(r[1]);
            ySet.add(r[3]);
            events.add(new int[]{r[0], 0, r[1], r[3]}); // open
            events.add(new int[]{r[2], 1, r[1], r[3]}); // close
        }

        events.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        // Compress y
        int[] ys = new int[ySet.size()];
        Map<Integer, Integer> yIndex = new HashMap<>();
        int idx = 0;
        for (int y : ySet) {
            ys[idx] = y;
            yIndex.put(y, idx);
            idx++;
        }

        int m = ys.length - 1;
        if (m <= 0) return 0;
        int[] count = new int[m];

        long area = 0;
        int prevX = events.get(0)[0];

        for (int[] ev : events) {
            int x = ev[0];
            // Add area contribution
            long activeY = 0;
            for (int i = 0; i < m; i++)
                if (count[i] > 0) activeY += ys[i + 1] - ys[i];
            area += (long)(x - prevX) * activeY;
            prevX = x;

            int i1 = yIndex.get(ev[2]);
            int i2 = yIndex.get(ev[3]);
            int delta = (ev[1] == 0) ? 1 : -1;
            for (int i = i1; i < i2; i++)
                count[i] += delta;
        }

        return (int) area;
    }
}
