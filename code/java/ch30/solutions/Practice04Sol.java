package ch30.solutions;
import java.util.*;
public class Practice04Sol {
    static int[] tree;
    static final int MAX_VAL = 100001;
    static void update(int node, int s, int e, int idx, int d) {
        if (s == e) { tree[node] += d; return; }
        int m = (s + e) / 2;
        if (idx <= m) update(2*node, s, m, idx, d);
        else update(2*node+1, m+1, e, idx, d);
        tree[node] = tree[2*node] + tree[2*node+1];
    }
    static int kth(int node, int s, int e, int k) {
        if (s == e) return s;
        int m = (s + e) / 2;
        if (tree[2*node] >= k) return kth(2*node, s, m, k);
        return kth(2*node+1, m+1, e, k - tree[2*node]);
    }
    public static int[] solve(int[][] queries) {
        tree = new int[4 * MAX_VAL];
        List<Integer> res = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) update(1, 1, MAX_VAL-1, q[1], 1);
            else if (q[0] == 2) update(1, 1, MAX_VAL-1, q[1], -1);
            else res.add(kth(1, 1, MAX_VAL-1, q[1]));
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
