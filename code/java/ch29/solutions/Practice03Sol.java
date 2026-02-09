package ch29.solutions;

import java.util.*;

public class Practice03Sol {
    // Most Stones Removed — Union-Find on row/col
    static Map<Integer, Integer> parent, rank;

    static int find(int x) {
        if (!parent.containsKey(x)) { parent.put(x, x); rank.put(x, 0); }
        if (parent.get(x) != x) parent.put(x, find(parent.get(x)));
        return parent.get(x);
    }

    static void union(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        int rrx = rank.get(rx), rry = rank.get(ry);
        if (rrx < rry) parent.put(rx, ry);
        else if (rrx > rry) parent.put(ry, rx);
        else { parent.put(ry, rx); rank.put(rx, rrx + 1); }
    }

    public static int solve(int[][] stones) {
        if (stones.length == 0) return 0;
        parent = new HashMap<>();
        rank = new HashMap<>();
        for (int[] s : stones)
            union(s[0], s[1] + 10001);
        Set<Integer> components = new HashSet<>();
        for (int[] s : stones)
            components.add(find(s[0]));
        return stones.length - components.size();
    }
}
