package ch14.solutions;

import java.util.*;

public class Practice02Sol {
    public static int solve(int[] arr, int k) {
        Map<Long, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0L, 1);
        long currentSum = 0;
        int count = 0;
        for (int x : arr) {
            currentSum += x;
            long complement = currentSum - k;
            count += prefixCount.getOrDefault(complement, 0);
            prefixCount.put(currentSum, prefixCount.getOrDefault(currentSum, 0) + 1);
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(arr, k));
        sc.close();
    }
}
