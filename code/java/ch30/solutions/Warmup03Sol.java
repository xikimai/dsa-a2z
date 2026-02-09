package ch30.solutions;
import java.util.*;
public class Warmup03Sol {
    static int[] bit;
    static int n;
    static void update(int i, int d) { for (i++; i <= n; i += i & (-i)) bit[i] += d; }
    static int prefix(int i) { int s = 0; for (i++; i > 0; i -= i & (-i)) s += bit[i]; return s; }
    public static int[] solve(int[] arr, int[][] queries) {
        n = arr.length; bit = new int[n + 1];
        for (int i = 0; i < n; i++) update(i, arr[i]);
        List<Integer> res = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) res.add(prefix(q[1]));
            else update(q[1], q[2]);
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
