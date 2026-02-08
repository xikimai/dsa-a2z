package ch20.solutions;

import java.util.*;

public class Warmup03Sol {
    public static int solve(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int maxArea = 0;
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 1) {
                    int area = 0;
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[]{r, c});
                    grid[r][c] = 0;
                    while (!queue.isEmpty()) {
                        int[] cell = queue.poll();
                        area++;
                        for (int d = 0; d < 4; d++) {
                            int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                                grid[nr][nc] = 0;
                                queue.add(new int[]{nr, nc});
                            }
                        }
                    }
                    maxArea = Math.max(maxArea, area);
                }
        return maxArea;
    }
}
