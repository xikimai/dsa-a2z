package ch15.solutions;

import java.util.*;

public class Warmup01Sol {
    public static int[] solve(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == target) return new int[]{arr[left], arr[right]};
            else if (sum < target) left++;
            else right--;
        }
        return new int[]{-1, -1};
    }
}
