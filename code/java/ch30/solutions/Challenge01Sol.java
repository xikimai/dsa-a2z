package ch30.solutions;
import java.util.*;
public class Challenge01Sol {
    static long[] tree;
    static Long[] lazy;
    static void pushDown(int node, int s, int e) {
        if (lazy[node] != null) {
            long val = lazy[node]; int m = (s + e) / 2;
            tree[2*node] = val * (m - s + 1); tree[2*node+1] = val * (e - m);
            lazy[2*node] = val; lazy[2*node+1] = val;
            lazy[node] = null;
        }
    }
    static void rangeSet(int node, int s, int e, int l, int r, long val) {
        if (r < s || e < l) return;
        if (l <= s && e <= r) { tree[node] = val * (e - s + 1); lazy[node] = val; return; }
        pushDown(node, s, e); int m = (s + e) / 2;
        rangeSet(2*node, s, m, l, r, val); rangeSet(2*node+1, m+1, e, l, r, val);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    static long rangeQuery(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        pushDown(node, s, e); int m = (s + e) / 2;
        return rangeQuery(2*node, s, m, l, r) + rangeQuery(2*node+1, m+1, e, l, r);
    }
    public static long[] solve(int n, int[][] queries) {
        tree = new long[4*n]; lazy = new Long[4*n];
        List<Long> res = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) rangeSet(1, 0, n-1, q[1], q[2], q[3]);
            else res.add(rangeQuery(1, 0, n-1, q[1], q[2]));
        }
        return res.stream().mapToLong(Long::longValue).toArray();
    }
}
