package ch14.solutions;

import java.util.*;

public class Challenge03Sol {
    public static int solve(int[] arr, int k) {
        Map<Integer, Integer> remainderCount = new HashMap<>();
        remainderCount.put(0, 1);
        long currentSum = 0;
        int count = 0;
        for (int x : arr) {
            currentSum += x;
            // Handle negative mod: ((a % k) + k) % k ensures non-negative remainder
            int rem = (int)(((currentSum % k) + k) % k);
            count += remainderCount.getOrDefault(rem, 0);
            remainderCount.put(rem, remainderCount.getOrDefault(rem, 0) + 1);
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int k = Integer.parseInt(sc.nextLine().trim());
        System.out.println(solve(arr, k));
        sc.close();
    }
}
