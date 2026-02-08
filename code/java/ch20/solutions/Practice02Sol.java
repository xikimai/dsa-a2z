package ch20.solutions;

import java.util.*;

public class Practice02Sol {
    public static int[][] solve(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        int[][] dist = new int[rows][cols];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        Queue<int[]> queue = new LinkedList<>();

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (mat[r][c] == 0) {
                    dist[r][c] = 0;
                    queue.add(new int[]{r, c});
                }

        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && dist[nr][nc] > dist[r][c] + 1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        return dist;
    }
}
