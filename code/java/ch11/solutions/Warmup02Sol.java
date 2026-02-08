package ch11.solutions;

import java.util.*;

/**
 * Solution for Warmup 2: Highest and Lowest Frequency
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count frequencies with HashMap, then scan for max and min frequency.
 * TIME:  O(n)
 * SPACE: O(n)
 */
public class Warmup02Sol {
    public static int[] solve(int[] arr) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        int maxFreq = Integer.MIN_VALUE, minFreq = Integer.MAX_VALUE;
        int maxElem = 0, minElem = 0;

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int val = entry.getKey();
            int cnt = entry.getValue();
            if (cnt > maxFreq) {
                maxFreq = cnt;
                maxElem = val;
            }
            if (cnt < minFreq) {
                minFreq = cnt;
                minElem = val;
            }
        }

        return new int[]{maxElem, minElem};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int[] result = solve(arr);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
