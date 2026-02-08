package ch14.solutions;

import java.util.*;

public class Challenge02Sol {
    public static long solveBrute(int[] arr) {
        if (arr.length == 0) return 0;
        long maxSum = arr[0];
        int n = arr.length;
        for (int l = 0; l < n; l++) {
            for (int r = l; r < n; r++) {
                long total = 0;
                for (int k = l; k <= r; k++) total += arr[k];
                maxSum = Math.max(maxSum, total);
            }
        }
        return maxSum;
    }

    public static long solvePrefix(int[] arr) {
        if (arr.length == 0) return 0;
        int n = arr.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];
        long maxSum = arr[0];
        for (int l = 0; l < n; l++) {
            for (int r = l; r < n; r++) {
                long total = prefix[r + 1] - prefix[l];
                maxSum = Math.max(maxSum, total);
            }
        }
        return maxSum;
    }

    public static long solveKadane(int[] arr) {
        if (arr.length == 0) return 0;
        long currentSum = arr[0];
        long maxSum = arr[0];
        for (int i = 1; i < arr.length; i++) {
            currentSum = Math.max(currentSum + arr[i], arr[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println("brute=" + solveBrute(arr) + " prefix=" + solvePrefix(arr)
            + " kadane=" + solveKadane(arr));
        sc.close();
    }
}
