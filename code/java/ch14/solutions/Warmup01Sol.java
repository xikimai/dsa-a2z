package ch14.solutions;

import java.util.*;

public class Warmup01Sol {
    public static long[] solve(int[] arr) {
        int n = arr.length;
        long[] prefix = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + arr[i - 1];
        }
        return prefix;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine().trim();
        if (line.isEmpty()) {
            System.out.println(Arrays.toString(solve(new int[]{})));
        } else {
            int[] arr = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).toArray();
            System.out.println(Arrays.toString(solve(arr)));
        }
        sc.close();
    }
}
