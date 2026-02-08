package ch20.solutions;

import java.util.*;

public class Practice03Sol {
    static int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};

    public static List<int[]> solve(int[][] heights) {
        int rows = heights.length, cols = heights[0].length;
        boolean[][] pacific = new boolean[rows][cols];
        boolean[][] atlantic = new boolean[rows][cols];

        Queue<int[]> pq = new LinkedList<>(), aq = new LinkedList<>();

        for (int c = 0; c < cols; c++) {
            pacific[0][c] = true; pq.add(new int[]{0, c});
            atlantic[rows - 1][c] = true; aq.add(new int[]{rows - 1, c});
        }
        for (int r = 0; r < rows; r++) {
            pacific[r][0] = true; pq.add(new int[]{r, 0});
            atlantic[r][cols - 1] = true; aq.add(new int[]{r, cols - 1});
        }

        bfs(heights, pq, pacific, rows, cols);
        bfs(heights, aq, atlantic, rows, cols);

        List<int[]> result = new ArrayList<>();
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (pacific[r][c] && atlantic[r][c])
                    result.add(new int[]{r, c});
        return result;
    }

    private static void bfs(int[][] heights, Queue<int[]> queue, boolean[][] visited, int rows, int cols) {
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                        && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    visited[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
    }
}
