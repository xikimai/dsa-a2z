package ch27.solutions;

import java.util.*;

public class Warmup04Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        if (n == 1) return 1;

        int[][] dirs = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0, 1});
        grid[0][0] = 1;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], len = cur[2];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    if (nr == n - 1 && nc == n - 1) return len + 1;
                    grid[nr][nc] = 1;
                    q.offer(new int[]{nr, nc, len + 1});
                }
            }
        }
        return -1;
    }
}
