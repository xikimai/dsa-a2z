package ch24.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(int[][] points) {
        int[] prev = points[0].clone();
        for (int i = 1; i < points.length; i++) {
            int[] curr = new int[3];
            for (int j = 0; j < 3; j++)
                for (int k = 0; k < 3; k++)
                    if (k != j)
                        curr[j] = Math.max(curr[j], prev[k] + points[i][j]);
            prev = curr;
        }
        return Math.max(prev[0], Math.max(prev[1], prev[2]));
    }
}
