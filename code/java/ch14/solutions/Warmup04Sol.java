package ch14.solutions;

import java.util.*;

public class Warmup04Sol {
    public static boolean solve(int[] arr1, int[] arr2) {
        if (arr1.length > arr2.length) return false;
        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line1 = sc.nextLine().trim();
        String line2 = sc.nextLine().trim();
        int[] arr1 = line1.isEmpty() ? new int[]{} : Arrays.stream(line1.split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] arr2 = line2.isEmpty() ? new int[]{} : Arrays.stream(line2.split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(solve(arr1, arr2));
        sc.close();
    }
}
