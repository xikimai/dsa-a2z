package ch30.solutions;
import java.util.*;
public class Challenge03Sol {
    static long[][] tree; // [total, prefix, suffix, best]
    static long[] makeLeaf(int v) { return new long[]{v, v, v, v}; }
    static long[] merge(long[] a, long[] b) {
        return new long[]{
            a[0] + b[0],
            Math.max(a[1], a[0] + b[1]),
            Math.max(b[2], b[0] + a[2]),
            Math.max(Math.max(a[3], b[3]), a[2] + b[1])
        };
    }
    static void build(int[] arr, int node, int s, int e) {
        if (s == e) { tree[node] = makeLeaf(arr[s]); return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = merge(tree[2*node], tree[2*node+1]);
    }
    static final long NEG_INF = Long.MIN_VALUE / 2;
    static long[] IDENTITY = {0, NEG_INF, NEG_INF, NEG_INF};
    static long[] query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return IDENTITY;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        long[] left = query(2*node, s, m, l, r), right = query(2*node+1, m+1, e, l, r);
        if (left[3] == NEG_INF) return right;
        if (right[3] == NEG_INF) return left;
        return merge(left, right);
    }
    public static int[] solve(int[] arr, int[][] queries) {
        int n = arr.length; tree = new long[4*n][];
        build(arr, 1, 0, n-1);
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long[] r = query(1, 0, n-1, queries[i][0], queries[i][1]);
            res[i] = (int) r[3];
        }
        return res;
    }
}
