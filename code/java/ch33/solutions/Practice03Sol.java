package ch33.solutions;

import java.util.*;

public class Practice03Sol {
    static int timerVal;
    static int[] tin, tout;
    static List<Integer> order;

    public static int[] solve(int n, int[] values, int[][] edges, int[] queries) {
        if (n == 1) {
            int[] res = new int[queries.length];
            Arrays.fill(res, values[0]);
            return res;
        }
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        tin = new int[n]; tout = new int[n];
        order = new ArrayList<>(); timerVal = 0;
        dfs(0, -1, adj);

        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + values[order.get(i)];

        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int q = queries[i];
            result[i] = (int)(prefix[tout[q] + 1] - prefix[tin[q]]);
        }
        return result;
    }

    static void dfs(int node, int parent, List<List<Integer>> adj) {
        tin[node] = timerVal;
        order.add(node);
        timerVal++;
        for (int nb : adj.get(node))
            if (nb != parent) dfs(nb, node, adj);
        tout[node] = timerVal - 1;
    }
}
