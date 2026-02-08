package ch15.solutions;

public class Practice04Sol {
    public static int solve(int[] arr, int k) {
        int left = 0, currentSum = 0, count = 0;
        for (int right = 0; right < arr.length; right++) {
            currentSum += arr[right];
            while (currentSum > k && left <= right) {
                currentSum -= arr[left];
                left++;
            }
            if (currentSum == k) count++;
        }
        return count;
    }
}
