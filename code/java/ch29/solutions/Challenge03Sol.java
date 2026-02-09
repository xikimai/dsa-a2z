package ch29.solutions;

import java.util.*;

public class Challenge03Sol {
    // Number of Islands II — online Union-Find
    public static List<Integer> solve(int m, int n, int[][] positions) {
        int[] parent = new int[m * n];
        int[] rank = new int[m * n];
        Arrays.fill(parent, -1);
        int count = 0;
        List<Integer> result = new ArrayList<>();
        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};

        for (int[] pos : positions) {
            int r = pos[0], c = pos[1];
            int idx = r * n + c;
            if (parent[idx] != -1) { // duplicate
                result.add(count);
                continue;
            }
            parent[idx] = idx;
            count++;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                int nidx = nr * n + nc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && parent[nidx] != -1) {
                    int rx = find(parent, idx), ry = find(parent, nidx);
                    if (rx != ry) {
                        if (rank[rx] < rank[ry]) parent[rx] = ry;
                        else if (rank[rx] > rank[ry]) parent[ry] = rx;
                        else { parent[ry] = rx; rank[rx]++; }
                        count--;
                    }
                }
            }
            result.add(count);
        }
        return result;
    }

    static int find(int[] parent, int x) {
        if (parent[x] != x) parent[x] = find(parent, parent[x]);
        return parent[x];
    }
}
