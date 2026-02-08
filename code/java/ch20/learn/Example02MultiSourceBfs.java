package ch20.learn;

import java.util.*;

/**
 * Example 2: Multi-Source BFS
 * Chapter 20: Graphs II — Real Problems
 *
 * Demonstrates rotten oranges and distance-to-nearest-zero via multi-source BFS.
 */
public class Example02MultiSourceBfs {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    // Rotten oranges: return minutes to rot all, or -1
    public static int rottenOranges(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int fresh = 0;

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) queue.add(new int[]{r, c});
                else if (grid[r][c] == 1) fresh++;
            }

        if (fresh == 0) return 0;

        int minutes = 0;
        while (!queue.isEmpty() && fresh > 0) {
            minutes++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int d = 0; d < 4; d++) {
                    int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols
                            && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        queue.add(new int[]{nr, nc});
                    }
                }
            }
        }
        return fresh == 0 ? minutes : -1;
    }

    public static void main(String[] args) {
        System.out.println("=== Rotten Oranges Demo ===");
        int[][] grid = {{2, 1, 1}, {1, 1, 0}, {0, 1, 1}};
        System.out.println("  Minutes: " + rottenOranges(grid)); // Expected: 4
    }
}
