package ch15.solutions;

public class Practice05Sol {
    public static int[] solve(int[] arr) {
        if (arr.length <= 1) return arr;
        int low = 0, mid = 0, high = arr.length - 1;
        while (mid <= high) {
            if (arr[mid] == 0) {
                int temp = arr[low]; arr[low] = arr[mid]; arr[mid] = temp;
                low++; mid++;
            } else if (arr[mid] == 1) {
                mid++;
            } else {
                int temp = arr[mid]; arr[mid] = arr[high]; arr[high] = temp;
                high--;
            }
        }
        return arr;
    }
}
