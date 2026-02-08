package ch20.solutions;

import java.util.*;

public class Challenge02Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        Queue<int[]> queue = new LinkedList<>();

        // Find first island via BFS
        boolean found = false;
        for (int r = 0; r < n && !found; r++)
            for (int c = 0; c < n && !found; c++)
                if (grid[r][c] == 1) {
                    Queue<int[]> bfs = new LinkedList<>();
                    bfs.add(new int[]{r, c});
                    grid[r][c] = 2;
                    while (!bfs.isEmpty()) {
                        int[] cell = bfs.poll();
                        queue.add(new int[]{cell[0], cell[1], 0});
                        for (int d = 0; d < 4; d++) {
                            int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                            if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                                grid[nr][nc] = 2;
                                bfs.add(new int[]{nr, nc});
                            }
                        }
                    }
                    found = true;
                }

        // Multi-source BFS from island 1
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1], dist = cell[2];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
                    if (grid[nr][nc] == 1) return dist;
                    if (grid[nr][nc] == 0) {
                        grid[nr][nc] = 2;
                        queue.add(new int[]{nr, nc, dist + 1});
                    }
                }
            }
        }
        return -1;
    }
}
