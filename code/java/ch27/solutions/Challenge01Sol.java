package ch27.solutions;

import java.util.*;

public class Challenge01Sol {
    public static int solve(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int INF = (int) 1e9;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, INF);
        dist[0][0] = 0;
        Deque<int[]> dq = new ArrayDeque<>();
        dq.addFirst(new int[]{0, 0});
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!dq.isEmpty()) {
            int[] cur = dq.pollFirst();
            int r = cur[0], c = cur[1];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int cost = grid[nr][nc];
                    if (dist[r][c] + cost < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + cost;
                        if (cost == 0) dq.addFirst(new int[]{nr, nc});
                        else dq.addLast(new int[]{nr, nc});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
}
