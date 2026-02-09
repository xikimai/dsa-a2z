package ch28.solutions;

import java.util.*;

public class Challenge03Sol {
    // Largest Color Value: Kahn's BFS + DP
    public static int solve(String colors, int[][] edges) {
        int n = colors.length();
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDeg = new int[n];
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            inDeg[e[1]]++;
        }

        int[][] dp = new int[n][26];
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++)
            if (inDeg[i] == 0) queue.add(i);

        int count = 0, result = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            count++;
            dp[u][colors.charAt(u) - 'a']++;
            for (int c = 0; c < 26; c++)
                result = Math.max(result, dp[u][c]);
            for (int v : adj.get(u)) {
                for (int c = 0; c < 26; c++)
                    dp[v][c] = Math.max(dp[v][c], dp[u][c]);
                if (--inDeg[v] == 0) queue.add(v);
            }
        }
        return count == n ? result : -1;
    }
}
