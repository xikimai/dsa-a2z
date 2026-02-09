package ch29.solutions;

import java.util.*;

public class Challenge04Sol {
    // Smallest String With Swaps
    static int[] parent, rank;

    static int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    static void union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
    }

    public static String solve(String s, List<int[]> pairs) {
        int n = s.length();
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] p : pairs) union(p[0], p[1]);

        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int i = 0; i < n; i++)
            groups.computeIfAbsent(find(i), k -> new ArrayList<>()).add(i);

        char[] result = new char[n];
        for (List<Integer> indices : groups.values()) {
            List<Character> chars = new ArrayList<>();
            for (int i : indices) chars.add(s.charAt(i));
            Collections.sort(chars);
            Collections.sort(indices);
            for (int k = 0; k < indices.size(); k++)
                result[indices.get(k)] = chars.get(k);
        }
        return new String(result);
    }
}
