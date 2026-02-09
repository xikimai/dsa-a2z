package ch30.solutions;
import java.util.*;
public class Warmup04Sol {
    public static int solve(int[] arr) {
        if (arr.length == 0) return 0;
        int[] sorted = arr.clone(); Arrays.sort(sorted);
        Map<Integer,Integer> rank = new HashMap<>();
        int r = 0;
        for (int v : sorted) if (!rank.containsKey(v)) rank.put(v, ++r);
        int maxR = r;
        int[] bit = new int[maxR + 1];
        int inv = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            int rk = rank.get(arr[i]);
            for (int j = rk - 1; j > 0; j -= j & (-j)) inv += bit[j];
            for (int j = rk; j <= maxR; j += j & (-j)) bit[j]++;
        }
        return inv;
    }
}
