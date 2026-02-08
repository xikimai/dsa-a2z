package ch17.solutions;

import java.util.*;

/**
 * Solution for Practice 5: K Closest Points to Origin
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Max-heap of size k by distance.
 * TIME:  O(n log k)
 * SPACE: O(k)
 */
public class Practice05Sol {
    public static List<int[]> solve(int[][] points, int k) {
        // Max-heap by distance (negate for max behavior, or use reverse comparator)
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
                (a, b) -> (b[0]*b[0] + b[1]*b[1]) - (a[0]*a[0] + a[1]*a[1])
        );
        for (int[] p : points) {
            maxHeap.add(p);
            if (maxHeap.size() > k) maxHeap.poll();
        }
        List<int[]> result = new ArrayList<>(maxHeap);
        result.sort((a, b) -> (a[0]*a[0]+a[1]*a[1]) - (b[0]*b[0]+b[1]*b[1]));
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }
        List<int[]> result = solve(points, k);
        for (int[] p : result) System.out.println(p[0] + " " + p[1]);
        sc.close();
    }
}
