package ch11.solutions;

import java.util.*;

/**
 * Solution for Practice 4: Count Subarrays with Sum K
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Prefix sum + frequency HashMap. Initialize with {0: 1}.
 *           At each index, count how many times (prefixSum - k) has appeared.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Practice04Sol {
    public static int solve(int[] arr, int k) {
        HashMap<Long, Integer> prefixCount = new HashMap<>();
        prefixCount.put(0L, 1);

        long prefixSum = 0;
        int count = 0;

        for (int x : arr) {
            prefixSum += x;
            long need = prefixSum - k;

            count += prefixCount.getOrDefault(need, 0);
            prefixCount.put(prefixSum, prefixCount.getOrDefault(prefixSum, 0) + 1);
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        System.out.println(solve(arr, k));
        sc.close();
    }
}
