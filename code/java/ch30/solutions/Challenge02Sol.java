package ch30.solutions;
import java.util.*;
public class Challenge02Sol {
    static int[] bit; static int n;
    static void update(int i, int d) { for (i++; i <= n; i += i & (-i)) bit[i] += d; }
    static int prefix(int i) { int s = 0; for (i++; i > 0; i -= i & (-i)) s += bit[i]; return s; }
    public static int[] solve(int[] arr, int[][] queries) {
        n = arr.length; bit = new int[n + 2];
        int[][] indexed = new int[queries.length][3];
        for (int i = 0; i < queries.length; i++) { indexed[i][0] = queries[i][0]; indexed[i][1] = queries[i][1]; indexed[i][2] = i; }
        Arrays.sort(indexed, (a, b) -> a[1] - b[1]);
        int[] results = new int[queries.length];
        Map<Integer,Integer> lastSeen = new HashMap<>();
        int j = 0;
        for (int[] q : indexed) {
            int l = q[0], r = q[1], origIdx = q[2];
            while (j <= r) {
                int val = arr[j];
                if (lastSeen.containsKey(val)) update(lastSeen.get(val), -1);
                lastSeen.put(val, j); update(j, 1); j++;
            }
            results[origIdx] = prefix(r) - (l > 0 ? prefix(l - 1) : 0);
        }
        return results;
    }
}
