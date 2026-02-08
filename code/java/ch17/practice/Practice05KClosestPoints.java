package ch17.practice;

import java.util.*;

/**
 * Practice 5: K Closest Points to Origin
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM: Return k closest points to origin, sorted by distance.
 * EXAMPLES:
 *   solve([[1,3],[-2,2]], 1) -> [[-2,2]]
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
public class Practice05KClosestPoints {
    public static List<int[]> solve(int[][] points, int k) {
        // TODO: Replace this with your solution
        return new ArrayList<>();
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
