package ch14.solutions;

import java.util.*;

public class Practice04Sol {
    public static long[] solve(int n, int[][] updates) {
        long[] diff = new long[n + 1];
        for (int[] u : updates) {
            int l = u[0], r = u[1], val = u[2];
            diff[l] += val;
            if (r + 1 <= n) diff[r + 1] -= val;
        }
        long[] result = new long[n];
        long running = 0;
        for (int i = 0; i < n; i++) {
            running += diff[i];
            result[i] = running;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        int q = Integer.parseInt(sc.nextLine().trim());
        int[][] updates = new int[q][3];
        for (int i = 0; i < q; i++) {
            String[] parts = sc.nextLine().split(" ");
            updates[i][0] = Integer.parseInt(parts[0]);
            updates[i][1] = Integer.parseInt(parts[1]);
            updates[i][2] = Integer.parseInt(parts[2]);
        }
        System.out.println(Arrays.toString(solve(n, updates)));
        sc.close();
    }
}
