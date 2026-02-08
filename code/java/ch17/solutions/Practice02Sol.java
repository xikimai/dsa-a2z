package ch17.solutions;

import java.util.*;

/**
 * Solution for Practice 2: Merge K Sorted Arrays
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Min-heap of (value, arrayIdx, elemIdx).
 * TIME:  O(N log K)
 * SPACE: O(K) + O(N)
 */
public class Practice02Sol {
    public static List<Integer> solve(int[][] arrays) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(
                (a, b) -> Integer.compare(a[0], b[0])
        );
        for (int i = 0; i < arrays.length; i++) {
            if (arrays[i].length > 0) {
                pq.add(new int[]{arrays[i][0], i, 0});
            }
        }
        List<Integer> result = new ArrayList<>();
        while (!pq.isEmpty()) {
            int[] top = pq.poll();
            result.add(top[0]);
            int arrIdx = top[1], elemIdx = top[2];
            if (elemIdx + 1 < arrays[arrIdx].length) {
                pq.add(new int[]{arrays[arrIdx][elemIdx + 1], arrIdx, elemIdx + 1});
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int[][] arrays = new int[k][];
        for (int i = 0; i < k; i++) {
            int n = sc.nextInt();
            arrays[i] = new int[n];
            for (int j = 0; j < n; j++) arrays[i][j] = sc.nextInt();
        }
        System.out.println(solve(arrays));
        sc.close();
    }
}
