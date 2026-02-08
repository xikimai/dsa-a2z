package ch20.solutions;

import java.util.*;

public class Challenge04Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};

        int lo = Math.max(grid[0][0], grid[n - 1][n - 1]);
        int hi = n * n - 1;

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (canReach(grid, n, mid, dr, dc))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo;
    }

    private static boolean canReach(int[][] grid, int n, int t, int[] dr, int[] dc) {
        if (grid[0][0] > t) return false;
        boolean[][] visited = new boolean[n][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        visited[0][0] = true;
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            if (cell[0] == n - 1 && cell[1] == n - 1) return true;
            for (int d = 0; d < 4; d++) {
                int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n
                        && !visited[nr][nc] && grid[nr][nc] <= t) {
                    visited[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        return false;
    }
}
