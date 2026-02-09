package ch30.solutions;
import java.util.*;
public class Practice01Sol {
    static long[] tree, lazy;
    static void pushDown(int node, int s, int e) {
        if (lazy[node] != 0) {
            int m = (s + e) / 2;
            tree[2*node] += lazy[node] * (m - s + 1);
            tree[2*node+1] += lazy[node] * (e - m);
            lazy[2*node] += lazy[node]; lazy[2*node+1] += lazy[node];
            lazy[node] = 0;
        }
    }
    static void rangeUpdate(int node, int s, int e, int l, int r, long val) {
        if (r < s || e < l) return;
        if (l <= s && e <= r) { tree[node] += val * (e - s + 1); lazy[node] += val; return; }
        pushDown(node, s, e); int m = (s + e) / 2;
        rangeUpdate(2*node, s, m, l, r, val); rangeUpdate(2*node+1, m+1, e, l, r, val);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    static long rangeQuery(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        pushDown(node, s, e); int m = (s + e) / 2;
        return rangeQuery(2*node, s, m, l, r) + rangeQuery(2*node+1, m+1, e, l, r);
    }
    public static long[] solve(int n, int[][] queries) {
        tree = new long[4*n]; lazy = new long[4*n];
        List<Long> res = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) rangeUpdate(1, 0, n-1, q[1], q[2], q[3]);
            else res.add(rangeQuery(1, 0, n-1, q[1], q[2]));
        }
        return res.stream().mapToLong(Long::longValue).toArray();
    }
}
