package ch34.solutions;

import java.util.*;

public class Practice04Sol {
    // Maximum Points on a Line
    public static int solve(int[][] points) {
        int n = points.length;
        if (n <= 2) return n;

        int best = 1;
        for (int i = 0; i < n; i++) {
            Map<String, Integer> slopes = new HashMap<>();
            int dup = 1; // count point i itself
            for (int j = i + 1; j < n; j++) {
                int dx = points[j][0] - points[i][0];
                int dy = points[j][1] - points[i][1];

                if (dx == 0 && dy == 0) {
                    dup++;
                    continue;
                }

                // Normalize
                int g = gcd(Math.abs(dx), Math.abs(dy));
                dx /= g;
                dy /= g;
                if (dx < 0 || (dx == 0 && dy < 0)) {
                    dx = -dx;
                    dy = -dy;
                }

                String key = dx + "," + dy;
                slopes.merge(key, 1, Integer::sum);
            }

            int localMax = dup;
            for (int count : slopes.values()) {
                localMax = Math.max(localMax, count + dup);
            }
            best = Math.max(best, localMax);
        }
        return best;
    }

    static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
