package ch11.solutions;

import java.util.*;

/**
 * Solution for Warmup 1: Frequency Count
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Use a HashMap to count frequencies, then convert to sorted list.
 * TIME:  O(n log n) — dominated by sorting the keys
 * SPACE: O(n) — for the hash map
 */
public class Warmup01Sol {
    public static List<int[]> solve(int[] arr) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        List<int[]> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            result.add(new int[]{entry.getKey(), entry.getValue()});
        }

        result.sort((a, b) -> Integer.compare(a[0], b[0]));
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        List<int[]> result = solve(arr);
        for (int[] pair : result) {
            System.out.println(pair[0] + " " + pair[1]);
        }
        sc.close();
    }
}
