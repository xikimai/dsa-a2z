package ch15.solutions;

import java.util.*;

public class Warmup02Sol {
    public static int[] solve(int[] arr) {
        if (arr.length <= 1) return arr.clone();
        int slow = 0;
        for (int fast = 1; fast < arr.length; fast++) {
            if (arr[fast] != arr[slow]) {
                slow++;
                arr[slow] = arr[fast];
            }
        }
        return Arrays.copyOf(arr, slow + 1);
    }
}
