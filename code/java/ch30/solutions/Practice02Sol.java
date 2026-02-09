package ch30.solutions;
import java.util.*;
public class Practice02Sol {
    static int[] tree;
    static final int NEG_INF = Integer.MIN_VALUE;
    static void build(int[] arr, int node, int s, int e) {
        if (s == e) { tree[node] = arr[s]; return; }
        int m = (s + e) / 2;
        build(arr, 2*node, s, m); build(arr, 2*node+1, m+1, e);
        tree[node] = Math.max(tree[2*node], tree[2*node+1]);
    }
    static void update(int node, int s, int e, int idx, int val) {
        if (s == e) { tree[node] = val; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, val);
        else update(2*node+1, m+1, e, idx, val);
        tree[node] = Math.max(tree[2*node], tree[2*node+1]);
    }
    static int query(int node, int s, int e, int l, int r) {
        if (r < s || e < l) return NEG_INF;
        if (l <= s && e <= r) return tree[node];
        int m = (s + e) / 2;
        return Math.max(query(2*node, s, m, l, r), query(2*node+1, m+1, e, l, r));
    }
    public static int[] solve(int[] arr, int[][] queries) {
        int n = arr.length; tree = new int[4*n]; Arrays.fill(tree, NEG_INF);
        build(arr, 1, 0, n-1);
        List<Integer> res = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) res.add(query(1, 0, n-1, q[1], q[2]));
            else update(1, 0, n-1, q[1], q[2]);
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
