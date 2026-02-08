package ch14.solutions;

import java.util.*;

public class Warmup03Sol {
    public static long[] solve(int[] arr) {
        if (arr.length == 0) return new long[0];
        long[] result = new long[arr.length];
        result[0] = arr[0];
        for (int i = 1; i < arr.length; i++) {
            result[i] = result[i - 1] + arr[i];
        }
        return result;
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
