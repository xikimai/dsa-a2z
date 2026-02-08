package ch11.solutions;

import java.util.*;

/**
 * Solution for Practice 3: Longest Subarray with Sum K
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Prefix sum + HashMap. Store the earliest index of each prefix sum.
 *           At each index, check if (prefixSum - k) was seen before.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Practice03Sol {
    public static int solve(int[] arr, int k) {
        HashMap<Long, Integer> prefixIndex = new HashMap<>();
        prefixIndex.put(0L, -1); // prefix sum 0 at virtual index -1

        long prefixSum = 0;
        int maxLen = 0;

        for (int i = 0; i < arr.length; i++) {
            prefixSum += arr[i];
            long need = prefixSum - k;

            if (prefixIndex.containsKey(need)) {
                int len = i - prefixIndex.get(need);
                maxLen = Math.max(maxLen, len);
            }

            // Only store the first occurrence (earliest index gives longest subarray)
            if (!prefixIndex.containsKey(prefixSum)) {
                prefixIndex.put(prefixSum, i);
            }
        }

        return maxLen;
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
