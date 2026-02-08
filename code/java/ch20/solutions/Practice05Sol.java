package ch20.solutions;

import java.util.*;

public class Practice05Sol {
    public static int solve(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        Queue<int[]> queue = new LinkedList<>();

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if ((r == 0 || r == rows - 1 || c == 0 || c == cols - 1) && grid[r][c] == 1) {
                    queue.add(new int[]{r, c});
                    grid[r][c] = 0;
                }

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int d = 0; d < 4; d++) {
                int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                    grid[nr][nc] = 0;
                    queue.add(new int[]{nr, nc});
                }
            }
        }

        int count = 0;
        for (int[] row : grid)
            for (int v : row)
                if (v == 1) count++;
        return count;
    }
}
