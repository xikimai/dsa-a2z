package ch14.solutions;

import java.util.*;

public class Practice05Sol {
    public static long solve(int[] arr) {
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
        System.out.println(solve(arr));
        sc.close();
    }
}
