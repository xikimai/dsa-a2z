package ch14.solutions;

import java.util.*;

public class Practice01Sol {
    public static int solve(int[] arr) {
        int n = arr.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];
        long total = prefix[n];
        for (int i = 0; i < n; i++) {
            long leftSum = prefix[i];
            long rightSum = total - prefix[i + 1];
            if (leftSum == rightSum) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr));
        sc.close();
    }
}
