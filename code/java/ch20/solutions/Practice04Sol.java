package ch20.solutions;

import java.util.*;

public class Practice04Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;
        if (n == 1) return 1;

        int[][] dirs = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1});
        grid[0][0] = 1;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1], dist = cell[2];
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    if (nr == n - 1 && nc == n - 1) return dist + 1;
                    grid[nr][nc] = 1;
                    queue.add(new int[]{nr, nc, dist + 1});
                }
            }
        }
        return -1;
    }
}
