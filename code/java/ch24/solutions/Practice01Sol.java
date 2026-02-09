package ch24.solutions;

import java.util.*;

public class Practice01Sol {
    static int result;

    public static int solve(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int startR = 0, startC = 0, empty = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) { startR = i; startC = j; empty++; }
                else if (grid[i][j] == 0) empty++;
            }
        result = 0;
        dfs(grid, startR, startC, empty, m, n);
        return result;
    }

    static void dfs(int[][] grid, int r, int c, int remaining, int m, int n) {
        if (grid[r][c] == 2) { if (remaining == 0) result++; return; }
        int temp = grid[r][c];
        grid[r][c] = -2;
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != -1 && grid[nr][nc] != -2)
                dfs(grid, nr, nc, remaining - 1, m, n);
        }
        grid[r][c] = temp;
    }
}
