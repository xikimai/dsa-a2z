package ch30.solutions;
import java.util.*;
public class Practice03Sol {
    static List<int[]> tree;
    static void build(int[] arr, int node, int s, int e) {
        if (s == e) { tree.set(node, new int[]{arr[s]}); return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree.set(node, merge(tree.get(2*node), tree.get(2*node+1)));
    }
    static int[] merge(int[] a, int[] b) {
        int[] c = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        while (i < a.length && j < b.length) c[k++] = a[i] <= b[j] ? a[i++] : b[j++];
        while (i < a.length) c[k++] = a[i++];
        while (j < b.length) c[k++] = b[j++];
        return c;
    }
    static int countInRange(int[] sorted, int lo, int hi) {
        return upperBound(sorted, hi) - lowerBound(sorted, lo);
    }
    static int lowerBound(int[] a, int v) {
        int lo = 0, hi = a.length;
        while (lo < hi) { int m = (lo+hi)/2; if (a[m] < v) lo = m+1; else hi = m; }
        return lo;
    }
    static int upperBound(int[] a, int v) {
        int lo = 0, hi = a.length;
        while (lo < hi) { int m = (lo+hi)/2; if (a[m] <= v) lo = m+1; else hi = m; }
        return lo;
    }
    static int query(int node, int s, int e, int l, int r, int lo, int hi) {
        if (r < s || e < l) return 0;
        if (l <= s && e <= r) return countInRange(tree.get(node), lo, hi);
        int m = (s + e) / 2;
        return query(2*node, s, m, l, r, lo, hi) + query(2*node+1, m+1, e, l, r, lo, hi);
    }
    public static int[] solve(int[] arr, int[][] queries) {
        int n = arr.length;
        tree = new ArrayList<>(Collections.nCopies(4*n, new int[0]));
        build(arr, 1, 0, n-1);
        int[] res = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] q = queries[i];
            res[i] = query(1, 0, n-1, q[0], q[1], q[2], q[3]);
        }
        return res;
    }
}
