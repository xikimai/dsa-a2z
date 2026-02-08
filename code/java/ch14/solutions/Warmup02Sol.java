package ch14.solutions;

import java.util.*;

public class Warmup02Sol {
    public static long[] solve(int[] arr, int[][] queries) {
        int n = arr.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];

        long[] result = new long[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int l = queries[q][0], r = queries[q][1];
            result[q] = prefix[r + 1] - prefix[l];
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int q = Integer.parseInt(sc.nextLine().trim());
        int[][] queries = new int[q][2];
        for (int i = 0; i < q; i++) {
            String[] parts = sc.nextLine().split(" ");
            queries[i][0] = Integer.parseInt(parts[0]);
            queries[i][1] = Integer.parseInt(parts[1]);
        }
        System.out.println(Arrays.toString(solve(arr, queries)));
        sc.close();
    }
}
