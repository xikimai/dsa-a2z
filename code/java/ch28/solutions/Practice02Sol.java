package ch28.solutions;

import java.util.*;

public class Practice02Sol {
    // Parallel Courses: min semesters (1-indexed)
    public static int solve(int n, int[][] relations) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDeg = new int[n + 1];
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] r : relations) {
            adj.get(r[0]).add(r[1]);
            inDeg[r[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= n; i++)
            if (inDeg[i] == 0) queue.add(i);
        int semesters = 0, count = 0;
        while (!queue.isEmpty()) {
            semesters++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int u = queue.poll();
                count++;
                for (int v : adj.get(u))
                    if (--inDeg[v] == 0) queue.add(v);
            }
        }
        return count == n ? semesters : -1;
    }
}
