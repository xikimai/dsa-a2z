package ch14.solutions;

import java.util.*;

public class Practice03Sol {
    public static long[] solve(int[] arr) {
        int n = arr.length;
        long[] result = new long[n];
        long left = 1;
        for (int i = 0; i < n; i++) {
            result[i] = left;
            left *= arr[i];
        }
        long right = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= right;
            right *= arr[i];
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(Arrays.toString(solve(arr)));
        sc.close();
    }
}
