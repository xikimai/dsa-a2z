package ch29.solutions;

import java.util.*;

public class Challenge02Sol {
    // Making a Large Island
    static int[] parent, rank, size;

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    static void union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rank[rx] < rank[ry]) { parent[rx] = ry; size[ry] += size[rx]; }
        else if (rank[rx] > rank[ry]) { parent[ry] = rx; size[rx] += size[ry]; }
        else { parent[ry] = rx; size[rx] += size[ry]; rank[rx]++; }
    }

    public static int solve(int[][] grid) {
        int n = grid.length;
        parent = new int[n * n];
        rank = new int[n * n];
        size = new int[n * n];
        for (int i = 0; i < n * n; i++) { parent[i] = i; size[i] = 1; }

        int[][] dirs = {{0,1},{1,0}};
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1)
                    for (int[] d : dirs) {
                        int nr = r + d[0], nc = c + d[1];
                        if (nr < n && nc < n && grid[nr][nc] == 1)
                            union(r * n + c, nr * n + nc);
                    }

        int best = 0;
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1)
                    best = Math.max(best, size[find(r * n + c)]);

        int[][] dirs4 = {{-1,0},{1,0},{0,-1},{0,1}};
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 0) {
                    Set<Integer> seen = new HashSet<>();
                    int total = 1;
                    for (int[] d : dirs4) {
                        int nr = r + d[0], nc = c + d[1];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                            int root = find(nr * n + nc);
                            if (seen.add(root)) total += size[root];
                        }
                    }
                    best = Math.max(best, total);
                }
        return best;
    }
}
