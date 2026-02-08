package ch20.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(int[][] grid) {
        int n = grid.length;
        int[][] islandId = new int[n][n];
        Map<Integer, Integer> islandSize = new HashMap<>();
        int[] dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1};
        int currentId = 2;

        // Label islands
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 1 && islandId[r][c] == 0) {
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[]{r, c});
                    islandId[r][c] = currentId;
                    int size = 0;
                    while (!queue.isEmpty()) {
                        int[] cell = queue.poll();
                        size++;
                        for (int d = 0; d < 4; d++) {
                            int nr = cell[0] + dr[d], nc = cell[1] + dc[d];
                            if (nr >= 0 && nr < n && nc >= 0 && nc < n
                                    && grid[nr][nc] == 1 && islandId[nr][nc] == 0) {
                                islandId[nr][nc] = currentId;
                                queue.add(new int[]{nr, nc});
                            }
                        }
                    }
                    islandSize.put(currentId, size);
                    currentId++;
                }

        if (islandSize.isEmpty()) return 1;

        int maxSize = 0;
        for (int v : islandSize.values()) maxSize = Math.max(maxSize, v);

        // Check each 0-cell
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++)
                if (grid[r][c] == 0) {
                    Set<Integer> neighborIds = new HashSet<>();
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d], nc = c + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && islandId[nr][nc] != 0)
                            neighborIds.add(islandId[nr][nc]);
                    }
                    int total = 1;
                    for (int id : neighborIds) total += islandSize.get(id);
                    maxSize = Math.max(maxSize, total);
                }
        return maxSize;
    }
}
