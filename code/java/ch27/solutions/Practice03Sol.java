package ch27.solutions;

import java.util.*;

public class Practice03Sol {
    public static int solve(int n, int[][] edges, int threshold) {
        int INF = (int) 1e9;
        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, INF);
        for (int i = 0; i < n; i++) dist[i][i] = 0;
        for (int[] e : edges) {
            dist[e[0]][e[1]] = Math.min(dist[e[0]][e[1]], e[2]);
            dist[e[1]][e[0]] = Math.min(dist[e[1]][e[0]], e[2]);
        }

        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];

        int bestCity = -1, bestCount = n + 1;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++)
                if (j != i && dist[i][j] <= threshold) count++;
            if (count <= bestCount) {
                bestCount = count;
                bestCity = i;
            }
        }
        return bestCity;
    }
}
