package ch20.learn;

import java.util.*;

/**
 * Example 1: Grid BFS Basics
 * Chapter 20: Graphs II — Real Problems
 *
 * Demonstrates grid BFS, flood fill, and counting islands.
 */
public class Example01GridBfsBasics {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    // Flood fill starting from (sr, sc) with new color
    public static int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int rows = image.length, cols = image[0].length;
        int original = image[sr][sc];
        if (original == color) return image;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{sr, sc});
        image[sr][sc] = color;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int d = 0; d < 4; d++) {
                int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                        && image[nr][nc] == original) {
                    image[nr][nc] = color;
                    queue.add(new int[]{nr, nc});
                }
            }
        }
        return image;
    }

    // Count number of islands (connected components of 1's)
    public static int countIslands(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1 && !visited[r][c]) {
                    count++;
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[]{r, c});
                    visited[r][c] = true;
                    while (!queue.isEmpty()) {
                        int[] cell = queue.poll();
                        for (int d = 0; d < 4; d++) {
                            int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                                    && !visited[nr][nc] && grid[nr][nc] == 1) {
                                visited[nr][nc] = true;
                                queue.add(new int[]{nr, nc});
                            }
                        }
                    }
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println("=== Flood Fill Demo ===");
        int[][] image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
        floodFill(image, 1, 1, 2);
        for (int[] row : image)
            System.out.println("  " + Arrays.toString(row));

        System.out.println("\n=== Count Islands Demo ===");
        int[][] grid = {{1, 1, 0, 0, 0}, {1, 1, 0, 0, 0}, {0, 0, 1, 0, 0}, {0, 0, 0, 1, 1}};
        System.out.println("  Islands: " + countIslands(grid));
    }
}
