package ch28.solutions;

import java.util.*;

public class Warmup02Sol {
    // Course Schedule I: can all courses be finished?
    public static boolean solve(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDeg = new int[numCourses];
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] p : prerequisites) {
            adj.get(p[1]).add(p[0]);
            inDeg[p[0]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++)
            if (inDeg[i] == 0) queue.add(i);
        int count = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            count++;
            for (int v : adj.get(u))
                if (--inDeg[v] == 0) queue.add(v);
        }
        return count == numCourses;
    }
}
