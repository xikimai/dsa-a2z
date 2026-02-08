package ch14.solutions;

import java.util.*;

public class Challenge04Sol {
    public static long solve(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        if (n <= 1) return 0;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];
        long minCost = Long.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            long leftCost = (long) i * arr[i] - prefix[i];
            long rightCost = (prefix[n] - prefix[i + 1]) - (long)(n - i - 1) * arr[i];
            minCost = Math.min(minCost, leftCost + rightCost);
        }
        return minCost;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
