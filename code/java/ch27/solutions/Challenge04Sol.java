package ch27.solutions;

import java.util.*;

public class Challenge04Sol {
    public static int solve(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dist = new int[m][n];
        for (int[] row : dist) Arrays.fill(row, -1);
        dist[0][0] = grid[0][0];
        // Max-heap: negate for PQ
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        pq.offer(new int[]{grid[0][0], 0, 0});
        int[][] dirs = {{0,1},{0,-1},{1,0},{-1,0}};

        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            int d = top[0], r = top[1], c = top[2];
            if (d < dist[r][c]) continue;
            if (r == m - 1 && c == n - 1) return d;
            for (int[] dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int nv = Math.min(d, grid[nr][nc]);
                    if (nv > dist[nr][nc]) {
                        dist[nr][nc] = nv;
                        pq.offer(new int[]{nv, nr, nc});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
}
